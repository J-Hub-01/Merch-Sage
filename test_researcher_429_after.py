"""
Regression test for 0018: Researcher 429 -> honest abort.

Mirrors test_entrepreneur_429_after.py's methodology, applied to
ResearcherAgent. Proves the fix: raise_on_quota_exhaustion=True on
Researcher's Gemini call now causes a 429 to propagate as
GeminiQuotaExhaustedError -- caught only by the orchestrator's
existing top-level handler (0016) -- instead of silently falling back
to unrelated developer-mock content that (per the before-state
investigation, test_researcher_429_before.py) both overwrote real
hypothesis evidence AND fabricated seller-claim evidence that reached
the final customer-facing report directly.

Companion / "after" counterpart to test_researcher_429_before.py,
which is preserved unmodified as the permanent before-state record.
"""
import json
import sys
from unittest.mock import patch, MagicMock

sys.path.insert(0, ".")

from backend.models.intake import SellerIntakePayload
from backend.models.evidence import EvidenceObject
from backend.providers.llm_provider_aistudio import AIStudioGeminiProvider

REAL_TOTE_TITLE = "Boho Embroidered Floral Tote Bag | Sage Green Linen, Zippered"
REAL_TOTE_TAGS_13 = [
    "boho tote bag", "floral tote", "linen tote bag", "zippered tote",
    "market tote", "beach bag", "shopping bag", "canvas tote",
    "embroidered bag", "sage green bag", "boho bag gift", "tote for her",
    "eco tote bag",
]

# Deliberately different from llm_mock.py's hardcoded Researcher
# seller-claim mock text ("handmade craftsmanship", "fast shipping") --
# if the fix is correct, NONE of this ever gets evaluated.
REAL_SELLER_DIFFERENTIATORS = ["eco-friendly packaging", "locally sourced linen"]


def _fake_tote_evidence(_self, listing_url):
    return [EvidenceObject(
        source_type="observed fact", origin="Etsy API Listings Endpoint (live)",
        timestamp="2026-08-29T00:00:00Z", confidence="HIGH", evidence_state="SUPPORTED",
        provenance=["Etsy Listings API"],
        supporting_data={"title": REAL_TOTE_TITLE, "description": "A boho tote bag.",
                          "tags": REAL_TOTE_TAGS_13, "quantity": 56, "listing_state": "active",
                          "price": "35.71", "creation_tsz": "2026-06-01T12:00:00Z"},
        downstream_consumers=["ClassifierAgent", "EntrepreneurAgent", "ResearcherAgent"],
    )]


def _valid(stage):
    """Only classifier/entrepreneur (the stages BEFORE Researcher) get
    valid responses. No stage after Researcher should ever run -- if
    the fix fails and the pipeline continues past it, the fake client
    raises immediately, proving no downstream stage should have been
    reached."""
    resp = MagicMock()
    if stage == "classifier":
        resp.text = json.dumps({
            "category": "Bags & Purses / Tote Bags", "confidence": "HIGH",
            "reasoning": "Title and description describe a fabric tote bag.",
        })
    elif stage == "entrepreneur":
        resp.text = json.dumps({
            "hypotheses": [
                {"hypothesis_id": "H1", "title": "Tag coverage gap",
                 "description": "Tags may not cover common buyer search terms for boho tote bags.",
                 "assumptions": ["Buyers search using terms not present in current tags"]},
            ]
        })
    return resp


def _identify(sys_inst: str) -> str:
    s = sys_inst.lower()
    if "classification agent" in s:
        return "classifier"
    if "entrepreneur agent" in s:
        return "entrepreneur"
    if "researcher agent" in s:
        return "researcher"
    if "triage agent" in s:
        return "triage"
    if "discoverability/seo specialist" in s:
        return "seo"
    if "business verifier agent" in s:
        return "business_verifier"
    return "unknown"


class FakeClientResearcherAlways429:
    """ONLY the Researcher-stage call fails, with a 429, on every
    attempt. Classification and Entrepreneur (before it) succeed with
    real, listing-specific responses. No stage after Researcher
    (Triage/SEO/BusinessVerifier) is given a valid response."""
    def __init__(self):
        self.call_log = []
        self.models = self

    def generate_content(self, model, contents, config=None):
        sys_inst = (getattr(config, "system_instruction", "") or "") if config else ""
        stage = _identify(sys_inst)
        self.call_log.append(stage)

        if stage == "researcher":
            raise Exception(
                "429 RESOURCE_EXHAUSTED. Quota exceeded for metric: "
                "generativelanguage.googleapis.com/generate_content_free_tier_requests, "
                "limit: 20, model: gemini-3.5-flash"
            )
        if stage in ("classifier", "entrepreneur"):
            return _valid(stage)

        raise AssertionError(
            f"Stage '{stage}' was called, but the pipeline should have aborted "
            f"at Researcher's 429 before reaching any stage after it. "
            f"system_instruction={sys_inst!r}"
        )


def _run():
    fake_client = FakeClientResearcherAlways429()
    provider = AIStudioGeminiProvider.__new__(AIStudioGeminiProvider)
    provider.initialized = True
    provider.client = fake_client

    captured = []
    intake = SellerIntakePayload(
        listing_url="https://www.etsy.com/in-en/listing/1716154949/boho-embroidered-floral-tote-bag-in-sage",
        seller_differentiators=REAL_SELLER_DIFFERENTIATORS,
    )
    with patch("backend.pipeline.orchestrator.get_llm_provider", return_value=provider), \
         patch("backend.pipeline.orchestrator.MarketplaceEvidenceProvider.get_listing_evidence",
               new=_fake_tote_evidence), \
         patch("backend.pipeline.orchestrator.LocalJsonAuditStore.save_context",
               new=lambda self, ctx: captured.append(ctx)):
        from backend.pipeline.orchestrator import run_audit
        report = run_audit(intake)
    return report, fake_client, captured


if __name__ == "__main__":
    report, fake_client, captured = _run()

    print(f"call log: {fake_client.call_log}")
    print(f"report: {json.dumps(report, indent=2)}")

    researcher_calls = fake_client.call_log.count("researcher")
    assert researcher_calls == 1, f"expected exactly 1 Gemini call for Researcher (no wasted retry on quota), got {researcher_calls}"
    print("[1/8] PASS: exactly 1 Gemini call for Researcher (no retry).")

    downstream_calls = [s for s in fake_client.call_log if s in ("triage", "seo", "business_verifier")]
    assert downstream_calls == [], f"expected zero downstream-stage calls, got {downstream_calls}"
    print("[2/8] PASS: zero downstream Gemini calls (Triage/SEO/BusinessVerifier never ran).")

    assert report.get("pipeline_status") == "failed", report.get("pipeline_status")
    print("[3/8] PASS: pipeline_status == 'failed'.")

    assert report.get("failure_type") == "gemini_quota_exhausted_error", report.get("failure_type")
    print("[4/8] PASS: failure_type == 'gemini_quota_exhausted_error'.")

    error_msg = report.get("error", "")
    assert "quota" in error_msg.lower()
    assert "try again" in error_msg.lower()
    print(f"[5/8] PASS: clear customer-facing message: {error_msg!r}")

    known_mock_markers = [
        "handmade craftsmanship", "fast shipping", "tarnishing",
        "listing tags do not contain primary search keywords",
        "keyword mismatch with buyer search intent",
    ]
    report_str = json.dumps(report).lower()
    found_in_report = [m for m in known_mock_markers if m in report_str]
    assert found_in_report == [], f"mock content leaked into report: {found_in_report}"
    assert "seller_claim_evaluations" not in report, report
    print("[6/8] PASS: no developer-mock content anywhere in the final report; "
          "no seller_claim_evaluations field at all (nothing was evaluated).")

    assert len(captured) == 1
    ctx = captured[0]
    # Entrepreneur (the stage before Researcher) DID complete -- our real
    # H1 "Tag coverage gap" hypothesis exists, proving the abort is
    # specific to Researcher, not a pipeline that failed earlier.
    assert ctx.hypothesis_map and ctx.hypothesis_map[0]["hypothesis_id"] == "H1", ctx.hypothesis_map
    entrepreneur_evidence = [ev for ev in ctx.evidence_store if ev.origin == "EntrepreneurAgent"]
    assert len(entrepreneur_evidence) == 1, entrepreneur_evidence
    # Researcher must NOT have mutated it -- still exactly as Entrepreneur left it:
    # evidence_state="UNKNOWN" (initial/untested), confidence="MEDIUM" (Entrepreneur's
    # default), no evaluation_details, no "ResearcherAgent Evaluation" provenance entry.
    ev = entrepreneur_evidence[0]
    assert ev.evidence_state == "UNKNOWN", f"expected untouched evidence_state='UNKNOWN', got {ev.evidence_state!r}"
    assert ev.confidence == "MEDIUM", f"expected untouched confidence='MEDIUM', got {ev.confidence!r}"
    assert "evaluation_details" not in ev.supporting_data, ev.supporting_data
    assert "ResearcherAgent Evaluation" not in ev.provenance, ev.provenance
    print("[7/8] PASS: EntrepreneurAgent hypothesis evidence completely untouched by Researcher "
          "(evidence_state/confidence/provenance all still exactly as Entrepreneur left them).")

    # No fabricated ResearcherAgent seller-claim evidence was created at all.
    researcher_evidence = [ev for ev in ctx.evidence_store if ev.origin == "ResearcherAgent"]
    assert researcher_evidence == [], f"expected zero ResearcherAgent evidence objects, got {len(researcher_evidence)}"
    ctx_str = json.dumps([ev.supporting_data for ev in ctx.evidence_store]).lower()
    found_in_ctx = [m for m in known_mock_markers if m in ctx_str]
    assert found_in_ctx == [], f"mock content leaked into evidence_store: {found_in_ctx}"
    assert ctx.status == "infrastructure_error", ctx.status
    print("[8/8] PASS: zero ResearcherAgent evidence objects created (no fabricated seller-claim "
          "evidence); zero mock content anywhere in context; status='infrastructure_error'.")

    print("\n=== ALL 8 CHECKS PASSED: Researcher 429 -> no retry -> GeminiQuotaExhaustedError "
          "-> clean 'failed' audit, zero downstream execution, zero mutation, zero fabrication. ===")
