"""
Controlled unknown/generic Gemini failure integration test.

Companion to test_429_integration.py and test_401_403_integration.py,
covering the failure class demonstrated as a real bug before this fix:

    Gemini 500 / ConnectionResetError / TimeoutError (or any other
    unclassified exception, or a 503 that never recovers) -> provider
    retries with the existing bounded policy -> retries exhausted ->
    GeminiGenerationError -> orchestrator surfaces a clear
    infrastructure-failure response -> NO necklace/mock content enters
    the report -> pipeline_status is NEVER "verified" for this case.

Runs the REAL orchestrator and REAL provider retry logic via a fake
genai client -- nothing under test is re-implemented here. Consumes
zero real Gemini quota, requires no live Etsy access.
"""
import json
import sys
from unittest.mock import patch, MagicMock

sys.path.insert(0, ".")

from backend.models.intake import SellerIntakePayload
from backend.models.evidence import EvidenceObject
from backend.providers.llm_provider_aistudio import AIStudioGeminiProvider

REAL_TOTE_TITLE = "Boho Embroidered Floral Tote Bag | Sage Green Linen, Zippered"
REAL_TOTE_TAGS = ["boho tote bag", "floral tote", "linen tote bag", "zippered tote"]


def _fake_tote_evidence(_self, listing_url):
    return [
        EvidenceObject(
            source_type="observed fact", origin="Etsy API Listings Endpoint (live)",
            timestamp="2026-08-23T00:00:00Z", confidence="HIGH", evidence_state="SUPPORTED",
            provenance=["Etsy Listings API"],
            supporting_data={
                "title": REAL_TOTE_TITLE, "description": "A boho tote bag.",
                "tags": REAL_TOTE_TAGS, "quantity": 56, "listing_state": "active",
                "price": "35.71", "creation_tsz": "2026-06-01T12:00:00Z",
            },
            downstream_consumers=["ClassifierAgent"],
        )
    ]


class FakeGenAIClient:
    """Every stage before SEO succeeds live; SEO fails every attempt
    with an unclassified 500 -- not 429, not 401/403."""
    def __init__(self):
        self.call_log = []
        self.models = self

    def generate_content(self, model, contents, config=None):
        sys_inst = (getattr(config, "system_instruction", "") or "") if config else ""
        s = sys_inst.lower()
        if "discoverability/seo specialist" in s:
            self.call_log.append("seo")
            raise Exception("500 Internal Server Error. An unexpected error occurred.")

        stage = "other"
        if "classification agent" in s: stage = "classifier"
        elif "entrepreneur agent" in s: stage = "entrepreneur"
        elif "researcher agent" in s: stage = "researcher"
        elif "triage agent" in s: stage = "triage"
        self.call_log.append(stage)

        resp = MagicMock()
        if stage == "classifier":
            resp.text = json.dumps({"category": "Bags & Purses / Tote Bags", "confidence": "HIGH", "reasoning": "tote"})
        elif stage == "entrepreneur":
            resp.text = json.dumps({"hypotheses": [
                {"hypothesis_id": "H1", "title": "Low visibility", "description": "d", "assumptions": ["a"]}]})
        elif stage == "researcher":
            resp.text = json.dumps({"hypothesis_evaluations": [
                {"hypothesis_id": "H1", "state": "CONFIRMED", "confidence": "HIGH", "details": "d"}],
                "seller_claim_evaluations": []})
        elif stage == "triage":
            resp.text = json.dumps({"problems": [
                {"problem_id": "P1", "title": "Low visibility", "severity": "HIGH", "is_root_cause": True,
                 "dependencies": [], "description": "d", "associated_evidence_ids": []}]})
        else:
            raise AssertionError(f"unexpected stage {stage} -- business_verifier should never be reached")
        return resp


def main():
    fake_client = FakeGenAIClient()
    provider = AIStudioGeminiProvider.__new__(AIStudioGeminiProvider)
    provider.initialized = True
    provider.client = fake_client

    captured_contexts = []

    def _capturing_save_context(self, context):
        captured_contexts.append(context)

    intake = SellerIntakePayload(
        listing_url="https://www.etsy.com/in-en/listing/1716154949/boho-embroidered-floral-tote-bag-in-sage"
    )

    with patch("backend.pipeline.orchestrator.get_llm_provider", return_value=provider), \
         patch("backend.pipeline.orchestrator.MarketplaceEvidenceProvider.get_listing_evidence",
               new=_fake_tote_evidence), \
         patch("backend.pipeline.orchestrator.LocalJsonAuditStore.save_context",
               new=_capturing_save_context):
        from backend.pipeline.orchestrator import run_audit
        report = run_audit(intake)

    # ── Assertion 1: bounded retries preserved, THEN raise (3 total
    #     calls for SEO -- 1 initial + 2 retries -- NOT 9 as it was
    #     before this fix, since the orchestrator's own SEO-retry-loop
    #     never gets a chance to re-invoke SEO: GeminiGenerationError
    #     propagates straight past it to the pipeline-level handler) ──
    seo_calls = fake_client.call_log.count("seo")
    assert seo_calls == 3, f"Expected exactly 3 SEO-stage calls (bounded retries preserved), got {seo_calls}"
    print(f"[1/6] PASS: SEO stage made exactly 3 calls (bounded retries preserved, then raised) -- "
          f"not 9, confirming the orchestrator's own retry loop never re-invoked a failing live call.")

    # ── Assertion 2: pipeline_status is NEVER "verified" for this case ──
    assert report.get("pipeline_status") == "failed", report
    print("[2/6] PASS: pipeline_status='failed', never 'verified'.")

    # ── Assertion 3: dedicated failure shape, distinct from the auth-error one ──
    assert report.get("failure_type") == "gemini_generation_error", report
    print("[3/6] PASS: failure_type='gemini_generation_error' (distinct from "
          "gemini_authentication_error).")

    # ── Assertion 4: zero necklace/mock content anywhere in the report ──
    report_str = json.dumps(report).lower()
    for term in ["necklace", "sterling", "925", "custom name"]:
        assert term not in report_str, f"Found mock term {term!r} in report: {report}"
    assert "classification" not in report
    assert "proposed_solutions" not in report
    assert "verification_results" not in report
    print("[4/6] PASS: zero necklace/mock content, zero fabricated audit fields anywhere in the report.")

    # ── Assertion 5: error message is clear and distinguishes this from
    #     a listing/data problem, and from an auth/config problem ──
    error_msg = report.get("error", "")
    assert "gemini" in error_msg.lower()
    assert "not a problem with the listing" in error_msg.lower()
    print(f"[5/6] PASS: clear customer-facing message: {error_msg!r}")

    # ── Assertion 6: internal context confirms real upstream stages DID
    #     succeed live (classification actually happened) before the
    #     failure -- proving this isn't masking an unrelated problem ──
    assert len(captured_contexts) == 1
    ctx = captured_contexts[0]
    assert ctx.classification == "Bags & Purses / Tote Bags", (
        "Expected earlier live stages to have genuinely succeeded before SEO failed -- "
        "this proves the failure is isolated to the SEO stage's live call, not a "
        "broader problem with the fake client setup."
    )
    assert ctx.specialist_solutions == [], "SEO must not have produced any solution_data"
    assert ctx.status == "infrastructure_error"
    print("[6/6] PASS: internal context confirms earlier stages genuinely succeeded live, "
          "SEO produced zero solution_data, status='infrastructure_error'.")

    print("\n=== ALL 6 CHECKS PASSED: unclassified Gemini failure -> bounded retries -> "
          "GeminiGenerationError -> clear failure, zero mock contamination. ===")


if __name__ == "__main__":
    main()
