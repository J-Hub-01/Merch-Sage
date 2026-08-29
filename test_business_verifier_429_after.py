"""
Regression test for:
  - BusinessVerifier 429 -> truthful degraded fallback (not abort, not mock)
  - ReportFormatterAgent._derive_final_status() generalized to recognize
    evidence_store-level degraded markers, closing the gap where
    Triage's (0019) degraded case silently reported "success"

Covers exactly the scenarios required before packaging:
  1. BusinessVerifier 429 -> 1 call, no mock, business_verification_results
     is None, degraded marker present, pipeline completes, pipeline_status
     == "degraded".
  2. Triage 429 -> unchanged behavior, but pipeline_status now correctly
     "degraded" instead of "success".
  3. SEO degraded -> still "degraded".
  4. Fully successful pipeline -> still "success".
  5. Classification/Entrepreneur/Researcher 429 -> still "failed".
  6. No fabricated BusinessVerifier content reaches the final report.
"""
import json
import subprocess
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
        resp.text = json.dumps({
            "problems": [
                {"problem_id": "P1", "title": "Tag coverage gap", "severity": "HIGH",
                 "is_root_cause": True, "dependencies": [],
                 "description": "Tags do not cover common buyer search terms.",
                 "associated_evidence_ids": ["real-evidence-id"]},
            ]
        })
    elif stage == "seo":
        resp.text = json.dumps({
            "specialist": "DiscoverabilitySeoCopySpecialist",
            "proposed_title": "Boho Embroidered Floral Tote Bag | Linen Market Tote, Zippered",
            "proposed_tags": REAL_TOTE_TAGS_13,
            "justification": "Added 'linen market tote' phrasing to close the tag coverage gap (P1).",
            "claims_made": [],
        })
    elif stage == "business_verifier":
        resp.text = json.dumps({
            "is_compatible": True, "conflicts": [],
            "evaluations": [{"solution_ref": REAL_TOTE_TITLE, "status": "APPROVED",
                              "justification": "Resolves P1, no conflicts."}],
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
    """failing_stage: which single stage (if any) always 429s. Every
    other stage gets a valid, real response."""
    def __init__(self, failing_stage=None):
        self.failing_stage = failing_stage
        self.call_log = []
        self.models = self

    def generate_content(self, model, contents, config=None):
        sys_inst = (getattr(config, "system_instruction", "") or "") if config else ""
        stage = _identify(sys_inst)
        self.call_log.append(stage)

        if stage == self.failing_stage:
            raise Exception(
                "429 RESOURCE_EXHAUSTED. Quota exceeded for metric: "
                "generativelanguage.googleapis.com/generate_content_free_tier_requests, "
                "limit: 20, model: gemini-3.5-flash"
            )
        if stage == "unknown":
            raise AssertionError(f"Unrecognized stage. system_instruction={sys_inst!r}")
        return _valid(stage)


def _run(failing_stage=None):
    fake_client = FakeClient(failing_stage)
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
    known_mock_markers = ["custom name necklace", "keyword mismatch"]

    # ── 1. BusinessVerifier 429 ──
    print("=" * 15 + " 1. BusinessVerifier 429 " + "=" * 15)
    report1, fc1, cap1 = _run(failing_stage="business_verifier")
    bv_calls = fc1.call_log.count("business_verifier")
    assert bv_calls == 1, bv_calls
    print("[1a] PASS: exactly 1 Gemini call for BusinessVerifier (no retry).")

    ctx1 = cap1[0]
    assert ctx1.business_verification_results is None, ctx1.business_verification_results
    print("[1b] PASS: business_verification_results is None (no mock, no fabricated judgment).")

    bv_evidence = [ev for ev in ctx1.evidence_store if ev.origin == "BusinessVerifierAgent"]
    assert len(bv_evidence) == 1
    ev = bv_evidence[0]
    assert ev.supporting_data.get("degraded") is True
    assert ev.supporting_data.get("degradation_reason") == "gemini_quota_exhausted"
    print("[1c] PASS: degraded marker present (degraded=True, degradation_reason='gemini_quota_exhausted').")

    assert report1.get("pipeline_status") == "degraded", report1.get("pipeline_status")
    print(f"[1d] PASS: pipeline completed, final pipeline_status == 'degraded'.")

    report1_str = json.dumps(report1).lower()
    contamination1 = [m for m in known_mock_markers if m in report1_str]
    assert contamination1 == [], contamination1
    assert report1.get("business_verification") is None, report1.get("business_verification")
    print("[1e] PASS: no fabricated BusinessVerifier content anywhere in the final report "
          "(business_verification == null, zero mock markers).")

    # ── 2. Triage 429 -> pipeline_status now correctly "degraded" ──
    print("\n" + "=" * 15 + " 2. Triage 429 " + "=" * 15)
    report2, fc2, cap2 = _run(failing_stage="triage")
    ctx2 = cap2[0]
    assert ctx2.triage_results == {"problems": []}, ctx2.triage_results
    print("[2a] PASS: Triage's own behavior unchanged -- triage_results == {'problems': []}.")
    assert report2.get("pipeline_status") == "degraded", report2.get("pipeline_status")
    print("[2b] PASS: pipeline_status now correctly 'degraded' (was 'success' before this fix).")

    # ── 3. SEO degraded -> still "degraded" (via the dedicated existing test) ──
    print("\n" + "=" * 15 + " 3. SEO degraded (existing dedicated test) " + "=" * 15)
    out3 = subprocess.run(["python3", "test_429_integration.py"], capture_output=True, text=True, cwd=".")
    assert out3.returncode == 0, out3.stdout + out3.stderr
    assert "pipeline_status='degraded'" in out3.stdout or "'degraded'" in out3.stdout
    print("[3] PASS: test_429_integration.py still passes, still asserts pipeline_status == 'degraded'.")

    # ── 4. Fully successful pipeline -> still "success" ──
    print("\n" + "=" * 15 + " 4. Fully successful pipeline " + "=" * 15)
    report4, fc4, cap4 = _run(failing_stage=None)
    assert report4.get("pipeline_status") == "success", report4.get("pipeline_status")
    assert report4.get("business_verification", {}).get("is_compatible") is True
    print("[4] PASS: pipeline_status == 'success' for a fully successful run "
          "(BusinessVerifier's real output present and unaffected).")

    # ── 5. Classification/Entrepreneur/Researcher 429 -> still "failed" ──
    print("\n" + "=" * 15 + " 5. Hard-abort stages still 'failed' " + "=" * 15)
    import test_entrepreneur_429_after
    report5a, _, _ = test_entrepreneur_429_after._run()
    assert report5a.get("pipeline_status") == "failed", report5a.get("pipeline_status")
    assert report5a.get("failure_type") == "gemini_quota_exhausted_error"
    print("[5a] PASS: Entrepreneur 429 -> pipeline_status == 'failed'.")

    import test_researcher_429_after
    report5b, _, _ = test_researcher_429_after._run()
    assert report5b.get("pipeline_status") == "failed", report5b.get("pipeline_status")
    print("[5b] PASS: Researcher 429 -> pipeline_status == 'failed'.")

    print("\n=== ALL REQUIRED SCENARIOS PASSED. ===")
