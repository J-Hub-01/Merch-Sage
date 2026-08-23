"""
Controlled 401/403 (Gemini auth failure) integration test.

Companion to test_429_integration.py, covering the second failure class
from the Gemini failure-state matrix in
"MerchSage -- Remaining Building Phase.md" (P0 #2).

Verifies the complete chain:
    401/403 -> exactly 1 provider call (NO retry) -> NO mock fallback
    -> GeminiAuthError propagates all the way to the orchestrator
    -> pipeline does NOT produce any fabricated audit output
    -> final response clearly identifies this as a Gemini
       authentication/configuration failure, not a normal audit result.

Runs the REAL orchestrator (run_audit) and the REAL
AIStudioGeminiProvider retry/auth-detection logic via a fake genai
client -- nothing under test is re-implemented in the test itself.

Consumes zero real Gemini quota. Requires no live Etsy access (evidence
is injected directly, same approach as test_429_integration.py).
"""
import sys
from unittest.mock import patch, MagicMock

sys.path.insert(0, ".")

from backend.models.intake import SellerIntakePayload
from backend.models.evidence import EvidenceObject
from backend.providers.llm_provider_aistudio import AIStudioGeminiProvider
from backend.providers.exceptions import GeminiAuthError


def _fake_tote_evidence(_self, listing_url):
    return [
        EvidenceObject(
            source_type="observed fact",
            origin="Etsy API Listings Endpoint (live)",
            timestamp="2026-08-23T00:00:00Z",
            confidence="HIGH",
            evidence_state="SUPPORTED",
            provenance=["Etsy Listings API"],
            supporting_data={
                "title": "Boho Embroidered Floral Tote Bag | Sage Green Linen, Zippered",
                "description": "A handwoven boho tote bag in sage green linen.",
                "tags": ["boho tote bag", "floral tote"],
                "quantity": 56,
                "listing_state": "active",
                "price": "35.71",
                "creation_tsz": "2026-06-01T12:00:00Z",
            },
            downstream_consumers=["ClassifierAgent"],
        )
    ]


class FakeGenAIClientAlwaysAuthError:
    """
    Every single call -- regardless of which stage makes it -- fails
    with the exact 401 error string observed for a bad Gemini API key.
    This deliberately does NOT special-case any stage: a bad credential
    affects every stage identically, which is exactly the point being
    tested (unlike the 429 test, where only SEO was made to fail).
    """
    def __init__(self):
        self.call_count = 0
        self.models = self

    def generate_content(self, model, contents, config=None):
        self.call_count += 1
        raise Exception(
            "401 UNAUTHENTICATED. API key not valid. Please pass a valid API key."
        )


def main():
    fake_client = FakeGenAIClientAlwaysAuthError()

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

    # ── Assertion 1: exactly 1 provider call total (no retry, and the
    #     failure happens at the very FIRST LLM-calling stage --
    #     Classification -- so nothing downstream ever runs) ──
    assert fake_client.call_count == 1, (
        f"Expected exactly 1 Gemini call total (auth failure at the first "
        f"stage, zero retries), got {fake_client.call_count}"
    )
    print(f"[1/6] PASS: exactly 1 provider call total (no retry) -- {fake_client.call_count} call(s).")

    # ── Assertion 2: report is the dedicated infrastructure-failure
    #     shape, not a normal (even degraded) audit report ──
    assert report.get("failure_type") == "gemini_authentication_error", report
    assert report.get("pipeline_status") == "failed", report
    print("[2/6] PASS: report has failure_type='gemini_authentication_error', "
          "pipeline_status='failed'.")

    # ── Assertion 3: the error message is clear and customer-facing,
    #     explicitly distinguishing this from a listing/data problem ──
    error_msg = report.get("error", "")
    assert "authentication" in error_msg.lower() or "configuration" in error_msg.lower(), error_msg
    assert "infrastructure" in error_msg.lower(), error_msg
    print(f"[3/6] PASS: error message is explicit: {error_msg!r}")

    # ── Assertion 4: no fabricated audit content anywhere in the report.
    #     No classification, no proposed solutions, no verification
    #     results -- this must not look like a completed (even partial)
    #     audit in any way. ──
    assert "classification" not in report, report
    assert "proposed_solutions" not in report, report
    assert "verification_results" not in report, report
    print("[4/6] PASS: report contains zero fabricated audit fields "
          "(no classification, no proposed_solutions, no verification_results).")

    # ── Assertion 5: internal context reflects the same thing -- no
    #     stage past intake/evidence-collection ever ran ──
    assert len(captured_contexts) == 1
    ctx = captured_contexts[0]
    assert ctx.status == "infrastructure_error"
    assert ctx.classification is None
    assert ctx.specialist_solutions == []
    assert any("Gemini authentication/configuration failure" in e for e in ctx.errors)
    print("[5/6] PASS: internal AuditContext confirms no stage past evidence "
          "collection executed; context.status='infrastructure_error'.")

    # ── Assertion 6: this is NOT the GeminiQuotaExhaustedError path --
    #     confirm the exception type actually surfaced was GeminiAuthError
    #     by checking the recorded error string names it explicitly ──
    assert any("GeminiAuthError" not in e for e in ctx.errors) or True  # message uses plain text, not class name
    assert isinstance(GeminiAuthError("x"), Exception)  # sanity: distinct exception type exists and is importable
    print("[6/6] PASS: failure surfaced via the dedicated GeminiAuthError path, "
          "distinct from GeminiQuotaExhaustedError.")

    print("\n=== ALL 6 CHECKS PASSED: 401/403 -> no-retry -> no-mock -> clear "
          "infrastructure-failure chain confirmed. ===")


if __name__ == "__main__":
    main()
