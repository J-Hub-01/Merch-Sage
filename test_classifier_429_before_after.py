"""
Controlled test: demonstrates the current (pre-fix) 429 ->
mock-contamination bug specifically for ClassifierAgent.

Run this BEFORE any code change to confirm the problem exists, and
again AFTER the fix to confirm it's closed. Companion to
test_mock_contamination_audit.py (the broader 5-agent audit), but
packaged as a dedicated regression test since Classification is the
first agent being fixed.
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
        timestamp="2026-08-23T00:00:00Z", confidence="HIGH", evidence_state="SUPPORTED",
        provenance=["Etsy Listings API"],
        supporting_data={"title": REAL_TOTE_TITLE, "description": "A boho tote bag.",
                          "tags": REAL_TOTE_TAGS_13, "quantity": 56, "listing_state": "active",
                          "price": "35.71", "creation_tsz": "2026-06-01T12:00:00Z"},
        downstream_consumers=["ClassifierAgent"],
    )]


def _valid(stage):
    resp = MagicMock()
    if stage == "entrepreneur":
        resp.text = json.dumps({"hypotheses": [{"hypothesis_id": "H1", "title": "t", "description": "d", "assumptions": ["a"]}]})
    elif stage == "researcher":
        resp.text = json.dumps({"hypothesis_evaluations": [{"hypothesis_id": "H1", "state": "CONFIRMED", "confidence": "HIGH", "details": "d"}], "seller_claim_evaluations": []})
    elif stage == "triage":
        resp.text = json.dumps({"problems": [{"problem_id": "P1", "title": "t", "severity": "HIGH", "is_root_cause": True, "dependencies": [], "description": "d", "associated_evidence_ids": []}]})
    elif stage == "business_verifier":
        resp.text = json.dumps({"is_compatible": True, "conflicts": [], "evaluations": []})
    elif stage == "seo":
        resp.text = json.dumps({"specialist": "DiscoverabilitySeoCopySpecialist",
            "proposed_title": REAL_TOTE_TITLE, "proposed_tags": REAL_TOTE_TAGS_13,
            "justification": "Improve keyword coverage.", "claims_made": []})
    return resp


class FakeClientClassifierAlways429:
    """ONLY Classification fails with a 429, on every attempt. Every
    other stage gets a valid, correct response -- isolating the true
    Classification-specific contamination signal instead of letting a
    separately-correct SEO degraded-fallback (0011) mask it."""
    def __init__(self):
        self.call_log = []
        self.models = self

    def generate_content(self, model, contents, config=None):
        sys_inst = (getattr(config, "system_instruction", "") or "") if config else ""
        s = sys_inst.lower()
        if "classification agent" in s:
            self.call_log.append("classifier")
            raise Exception("429 RESOURCE_EXHAUSTED. Quota exceeded for metric: "
                             "generativelanguage.googleapis.com/generate_content_free_tier_requests")
        stage = "other"
        if "entrepreneur agent" in s: stage = "entrepreneur"
        elif "researcher agent" in s: stage = "researcher"
        elif "triage agent" in s: stage = "triage"
        elif "discoverability/seo specialist" in s: stage = "seo"
        elif "business verifier agent" in s: stage = "business_verifier"
        self.call_log.append(stage)
        return _valid(stage)


def _run():
    fake_client = FakeClientClassifierAlways429()
    provider = AIStudioGeminiProvider.__new__(AIStudioGeminiProvider)
    provider.initialized = True
    provider.client = fake_client

    captured = []
    intake = SellerIntakePayload(listing_url="https://www.etsy.com/in-en/listing/1716154949/boho-embroidered-floral-tote-bag-in-sage")
    with patch("backend.pipeline.orchestrator.get_llm_provider", return_value=provider), \
         patch("backend.pipeline.orchestrator.MarketplaceEvidenceProvider.get_listing_evidence", new=_fake_tote_evidence), \
         patch("backend.pipeline.orchestrator.LocalJsonAuditStore.save_context", new=lambda self, ctx: captured.append(ctx)):
        from backend.pipeline.orchestrator import run_audit
        report = run_audit(intake)
    return report, fake_client, captured


if __name__ == "__main__":
    report, fake_client, captured = _run()

    calls = fake_client.call_log.count("classifier")
    print(f"classifier calls made: {calls}")
    print(f"report: {json.dumps(report, indent=2)}")

    assert calls == 1, f"expected exactly 1 call (no wasted retry on quota), got {calls}"
    print("[1/6] PASS: exactly 1 Gemini call for Classification (no retry).")

    assert report.get("pipeline_status") == "failed", report.get("pipeline_status")
    print("[2/6] PASS: pipeline_status == 'failed'.")

    assert report.get("failure_type") == "gemini_quota_exhausted_error", report.get("failure_type")
    print("[3/6] PASS: failure_type == 'gemini_quota_exhausted_error' "
          "(distinct from gemini_authentication_error and gemini_generation_error).")

    report_str = json.dumps(report).lower()
    assert "personalized handmade jewelry" not in report_str, report
    assert "classification" not in report, report
    assert "proposed_solutions" not in report, report
    print("[4/6] PASS: zero mock content, zero fabricated audit fields anywhere in the report.")

    error_msg = report.get("error", "")
    assert "quota" in error_msg.lower()
    assert "try again" in error_msg.lower()
    print(f"[5/6] PASS: clear customer-facing message: {error_msg!r}")

    assert len(captured) == 1
    ctx = captured[0]
    assert ctx.classification is None, "no downstream stage should have run"
    assert ctx.status == "infrastructure_error"
    print("[6/6] PASS: internal context confirms no downstream stage ran; "
          "status='infrastructure_error'.")

    print("\n=== ALL 6 CHECKS PASSED: Classification 429 -> no retry -> "
          "GeminiQuotaExhaustedError -> clean 'failed' audit, zero mock contamination. ===")
