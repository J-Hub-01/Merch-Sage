"""
Regression test for the Triage 429 fix (degraded fallback, not abort).

Unlike the Classification/Entrepreneur/Researcher fixes, Triage does
NOT abort on quota exhaustion -- it catches GeminiQuotaExhaustedError
locally and returns the same truthful {"problems": []} result it
already uses when there is no confirmed evidence to triage, marked
degraded via the same mechanism SEO Specialist (0011) uses. The
pipeline continues to downstream stages.

Two scenarios in this file:
  A) 429 at Triage -- proves the degraded fallback (checks 1-6, 8).
  B) Normal happy path -- proves Triage's live-call behavior is
     unchanged when there is no failure (check 7).

Companion / "after" counterpart to test_triage_429_before.py, which
is preserved unmodified as the permanent before-state record.
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
    elif stage == "researcher":
        resp.text = json.dumps({
            "hypothesis_evaluations": [
                {"hypothesis_id": "H1", "state": "CONFIRMED", "confidence": "HIGH",
                 "details": "The current 13 tags do not include common boho-tote search terms."},
            ],
            "seller_claim_evaluations": [],
        })
    elif stage == "triage":
        # Real (non-mock) Triage response, used ONLY in the happy-path
        # scenario, to prove the live-call code path is unaffected.
        resp.text = json.dumps({
            "problems": [
                {"problem_id": "P1", "title": "Tag coverage gap", "severity": "HIGH",
                 "is_root_cause": True, "dependencies": [],
                 "description": "Tags do not cover common buyer search terms.",
                 "associated_evidence_ids": ["real-evidence-id"]},
            ]
        })
    elif stage == "business_verifier":
        resp.text = json.dumps({"is_compatible": True, "conflicts": [], "evaluations": []})
    elif stage == "seo":
        resp.text = json.dumps({
            "specialist": "DiscoverabilitySeoCopySpecialist",
            "proposed_title": REAL_TOTE_TITLE, "proposed_tags": REAL_TOTE_TAGS_13,
            "justification": "Retained current title/tags; insufficient evidence to justify changes.",
            "claims_made": [],
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


class FakeClient:
    """If triage_fails_429 is True, the Triage-stage call always raises
    a 429. Every other stage (including Triage in the happy-path case)
    gets a valid, real response. Also records the prompt 'contents'
    sent to the SEO-stage call, so contamination reaching downstream
    can be checked directly."""
    def __init__(self, triage_fails_429: bool):
        self.triage_fails_429 = triage_fails_429
        self.call_log = []
        self.seo_contents = None
        self.models = self

    def generate_content(self, model, contents, config=None):
        sys_inst = (getattr(config, "system_instruction", "") or "") if config else ""
        stage = _identify(sys_inst)
        self.call_log.append(stage)

        if stage == "triage" and self.triage_fails_429:
            raise Exception(
                "429 RESOURCE_EXHAUSTED. Quota exceeded for metric: "
                "generativelanguage.googleapis.com/generate_content_free_tier_requests, "
                "limit: 20, model: gemini-3.5-flash"
            )
        if stage == "seo":
            self.seo_contents = contents
        if stage == "unknown":
            raise AssertionError(f"Unrecognized stage. system_instruction={sys_inst!r}")
        return _valid(stage)


def _run(triage_fails_429: bool):
    fake_client = FakeClient(triage_fails_429)
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


KNOWN_MOCK_MARKERS = ["keyword mismatch in tags and titles", "slow delivery performance"]


if __name__ == "__main__":
    # ── Scenario A: 429 at Triage -> degraded fallback ──
    print("=" * 20 + " SCENARIO A: 429 at Triage " + "=" * 20)
    report, fake_client, captured = _run(triage_fails_429=True)
    print(f"call log: {fake_client.call_log}")
    print(f"report: {json.dumps(report, indent=2)}")

    triage_calls = fake_client.call_log.count("triage")
    assert triage_calls == 1, f"expected exactly 1 Gemini call for Triage, got {triage_calls}"
    print("[1/8] PASS: exactly 1 Gemini call for Triage.")

    # [2/8] No retry: same call count as [1] confirms it (no separate
    # retry-count mechanism exists to check independently here beyond
    # call count, since the quota short-circuit is unconditional and
    # already covered by [1]).
    print("[2/8] PASS: no retry occurred (call count == 1, consistent with the unconditional quota short-circuit).")

    # Downstream stages (SEO/BusinessVerifier) WERE reached this time --
    # different from the hard-abort stages -- so mock markers must be
    # absent from everything they touched.
    assert fake_client.seo_contents is not None, "SEO should have been called (degraded fallback continues the pipeline)"
    seo_prompt_str = str(fake_client.seo_contents).lower()
    seo_contamination = [m for m in KNOWN_MOCK_MARKERS if m in seo_prompt_str]
    assert seo_contamination == [], f"mock content leaked into SEO's prompt: {seo_contamination}"
    print("[3/8] PASS: developer mock content never entered SEO's prompt (or anywhere else -- confirmed below).")

    assert len(captured) == 1
    ctx = captured[0]
    assert ctx.triage_results == {"problems": []}, ctx.triage_results
    print("[4/8] PASS: triage_results == {'problems': []} (the exact truthful empty result).")

    downstream_calls = [s for s in fake_client.call_log if s in ("seo", "business_verifier")]
    assert downstream_calls == ["seo", "business_verifier"], downstream_calls
    print("[5/8] PASS: downstream stages (SEO, BusinessVerifier) were reached and ran.")

    report_str = json.dumps(report).lower()
    report_contamination = [m for m in KNOWN_MOCK_MARKERS if m in report_str]
    assert report_contamination == [], f"mock content leaked into report: {report_contamination}"
    assert report.get("problem_dependency_graph") == [], report.get("problem_dependency_graph")
    print("[6/8] PASS: final report contains no fabricated mock problems; "
          "problem_dependency_graph == [].")

    # [8/8] Verify exactly how the degraded state is represented internally.
    triage_evidence = [ev for ev in ctx.evidence_store if ev.origin == "TriageAgent"]
    assert len(triage_evidence) == 1, f"expected exactly 1 TriageAgent evidence object, got {len(triage_evidence)}"
    ev = triage_evidence[0]
    assert ev.supporting_data.get("degraded") is True, ev.supporting_data
    assert ev.supporting_data.get("degradation_reason") == "gemini_quota_exhausted", ev.supporting_data
    assert ev.supporting_data.get("problem_graph") == {"problems": []}, ev.supporting_data
    assert ev.confidence == "LOW", ev.confidence
    assert "degraded: quota exhausted" in ev.provenance[0], ev.provenance
    assert ctx.status != "error" and ctx.status != "infrastructure_error", ctx.status
    print(f"[8/8] PASS: degraded state represented internally as a TriageAgent evidence object with "
          f"supporting_data.degraded=True, degradation_reason='gemini_quota_exhausted', "
          f"confidence='LOW', provenance noting '(degraded: quota exhausted)'; "
          f"final ctx.status == {ctx.status!r} (pipeline continued normally to completion, per design).")

    print(f"\n[note] report.pipeline_status = {report.get('pipeline_status')!r} "
          f"-- unchanged/undistinguished by this patch, per instructions "
          f"(ReportFormatterAgent/pipeline_status not touched here).")

    # ── Scenario B: normal happy path -- Triage's live-call behavior unchanged ──
    print("\n" + "=" * 20 + " SCENARIO B: happy path (no failure) " + "=" * 20)
    report_b, fake_client_b, captured_b = _run(triage_fails_429=False)
    print(f"call log: {fake_client_b.call_log}")
    print(f"report: {json.dumps(report_b, indent=2)}")

    assert fake_client_b.call_log.count("triage") == 1
    ctx_b = captured_b[0]
    assert ctx_b.triage_results == {
        "problems": [
            {"problem_id": "P1", "title": "Tag coverage gap", "severity": "HIGH",
             "is_root_cause": True, "dependencies": [],
             "description": "Tags do not cover common buyer search terms.",
             "associated_evidence_ids": ["real-evidence-id"]},
        ]
    }, ctx_b.triage_results
    triage_evidence_b = [ev for ev in ctx_b.evidence_store if ev.origin == "TriageAgent"]
    assert len(triage_evidence_b) == 1
    assert triage_evidence_b[0].confidence == "HIGH", triage_evidence_b[0].confidence
    assert "degraded" not in triage_evidence_b[0].supporting_data, triage_evidence_b[0].supporting_data
    assert report_b.get("pipeline_status") == "success", report_b.get("pipeline_status")
    print("[7/8] PASS: normal happy path unchanged -- real Triage output (confidence='HIGH', "
          "no degraded marker), pipeline_status == 'success'.")

    print("\n=== ALL CHECKS PASSED (8/8, including happy-path check 7): Triage 429 -> no retry -> "
          "degraded {'problems': []} fallback -> pipeline continues -> zero mock contamination "
          "anywhere; live-call happy path unaffected. ===")
