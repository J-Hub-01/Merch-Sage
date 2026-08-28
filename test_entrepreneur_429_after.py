"""
Regression test for 0017: Entrepreneur 429 -> honest abort.

Mirrors test_classifier_429_before_after.py's methodology and
assertion style, applied to EntrepreneurAgent. Proves the fix:
raise_on_quota_exhaustion=True on Entrepreneur's Gemini call now
causes a 429 to propagate as GeminiQuotaExhaustedError -- caught only
by the orchestrator's existing top-level handler (added in 0016) --
instead of silently falling back to unrelated developer-mock
hypotheses (the bug demonstrated by test_entrepreneur_429_before.py).

Companion / "after" counterpart to test_entrepreneur_429_before.py,
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


def _fake_tote_evidence(_self, listing_url):
    return [EvidenceObject(
        source_type="observed fact", origin="Etsy API Listings Endpoint (live)",
        timestamp="2026-08-29T00:00:00Z", confidence="HIGH", evidence_state="SUPPORTED",
        provenance=["Etsy Listings API"],
        supporting_data={"title": REAL_TOTE_TITLE, "description": "A boho tote bag.",
                          "tags": REAL_TOTE_TAGS_13, "quantity": 56, "listing_state": "active",
                          "price": "35.71", "creation_tsz": "2026-06-01T12:00:00Z"},
        downstream_consumers=["ClassifierAgent", "EntrepreneurAgent"],
    )]


def _valid(stage):
    """Only used for classifier here -- every stage after Entrepreneur
    must NOT run, so no valid response is defined for researcher/
    triage/seo/business_verifier. If any of them get called, the fake
    client raises, which will surface as a test failure."""
    resp = MagicMock()
    if stage == "classifier":
        resp.text = json.dumps({
            "category": "Bags & Purses / Tote Bags", "confidence": "HIGH",
            "reasoning": "Title and description describe a fabric tote bag.",
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


class FakeClientEntrepreneurAlways429:
    """ONLY the Entrepreneur-stage call fails, with a 429, on every
    attempt. Classification (which runs before Entrepreneur) succeeds
    normally with a real, category-correct response, so the failure
    under test is isolated to Entrepreneur specifically. No stage
    after Entrepreneur (Researcher/Triage/SEO/BusinessVerifier) is
    given a valid response -- if the fix fails and the pipeline
    continues past Entrepreneur, the fake client raises immediately,
    proving no downstream stage should have been reached."""
    def __init__(self):
        self.call_log = []
        self.models = self

    def generate_content(self, model, contents, config=None):
        sys_inst = (getattr(config, "system_instruction", "") or "") if config else ""
        stage = _identify(sys_inst)
        self.call_log.append(stage)

        if stage == "entrepreneur":
            raise Exception(
                "429 RESOURCE_EXHAUSTED. Quota exceeded for metric: "
                "generativelanguage.googleapis.com/generate_content_free_tier_requests, "
                "limit: 20, model: gemini-3.5-flash"
            )
        if stage == "classifier":
            return _valid(stage)

        raise AssertionError(
            f"Stage '{stage}' was called, but the pipeline should have aborted "
            f"at Entrepreneur's 429 before reaching any stage after it. "
            f"system_instruction={sys_inst!r}"
        )


def _run():
    fake_client = FakeClientEntrepreneurAlways429()
    provider = AIStudioGeminiProvider.__new__(AIStudioGeminiProvider)
    provider.initialized = True
    provider.client = fake_client

    captured = []
    intake = SellerIntakePayload(
        listing_url="https://www.etsy.com/in-en/listing/1716154949/boho-embroidered-floral-tote-bag-in-sage"
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

    entrepreneur_calls = fake_client.call_log.count("entrepreneur")
    assert entrepreneur_calls == 1, f"expected exactly 1 Gemini call for Entrepreneur (no wasted retry on quota), got {entrepreneur_calls}"
    print("[1/7] PASS: exactly 1 Gemini call for Entrepreneur (no retry).")

    # No stage after Entrepreneur was called at all -- the fake client
    # would have raised AssertionError if researcher/triage/seo/
    # business_verifier had been reached, and that assertion did not fire.
    downstream_calls = [s for s in fake_client.call_log if s in ("researcher", "triage", "seo", "business_verifier")]
    assert downstream_calls == [], f"expected zero downstream-stage calls, got {downstream_calls}"
    print("[2/7] PASS: zero downstream Gemini calls (Researcher/Triage/SEO/BusinessVerifier never ran).")

    assert report.get("pipeline_status") == "failed", report.get("pipeline_status")
    print("[3/7] PASS: pipeline_status == 'failed'.")

    assert report.get("failure_type") == "gemini_quota_exhausted_error", report.get("failure_type")
    print("[4/7] PASS: failure_type == 'gemini_quota_exhausted_error'.")

    error_msg = report.get("error", "")
    assert "quota" in error_msg.lower()
    assert "try again" in error_msg.lower()
    print(f"[5/7] PASS: clear customer-facing message: {error_msg!r}")

    # No developer-mock content (the jewelry-specific fallback text from
    # llm_mock.py's entrepreneur branch) reached Entrepreneur or the report.
    known_mock_markers = ["custom name necklace", "premium silver", "tarnishing", "keyword mismatch with buyer search intent"]
    report_str = json.dumps(report).lower()
    found_in_report = [m for m in known_mock_markers if m in report_str]
    assert found_in_report == [], f"mock content leaked into report: {found_in_report}"
    print("[6/7] PASS: no developer-mock content anywhere in the final report.")

    assert len(captured) == 1
    ctx = captured[0]
    # Classification (the stage before Entrepreneur) DID complete --
    # this proves the abort is specific to Entrepreneur, not a pipeline
    # that failed before even reaching it.
    assert ctx.classification is not None, "Classification should have completed before Entrepreneur's 429"
    # Entrepreneur itself never wrote anything -- no fabricated
    # hypotheses in context.hypothesis_map, and no EntrepreneurAgent
    # evidence objects (mock or otherwise) in the evidence store.
    assert ctx.hypothesis_map == [], f"expected empty hypothesis_map, got {ctx.hypothesis_map}"
    entrepreneur_evidence = [ev for ev in ctx.evidence_store if ev.origin == "EntrepreneurAgent"]
    assert entrepreneur_evidence == [], f"expected zero EntrepreneurAgent evidence objects, got {len(entrepreneur_evidence)}"
    ctx_str = json.dumps([ev.supporting_data for ev in ctx.evidence_store]).lower()
    found_in_ctx = [m for m in known_mock_markers if m in ctx_str]
    assert found_in_ctx == [], f"mock content leaked into evidence_store: {found_in_ctx}"
    assert ctx.status == "infrastructure_error", ctx.status
    print("[7/7] PASS: internal context confirms Classification completed, Entrepreneur wrote "
          "nothing (no fabricated hypothesis_map, no EntrepreneurAgent evidence, no mock "
          "content anywhere in context), status='infrastructure_error'.")

    print("\n=== ALL 7 CHECKS PASSED: Entrepreneur 429 -> no retry -> GeminiQuotaExhaustedError "
          "-> clean 'failed' audit, zero downstream execution, zero mock contamination. ===")
