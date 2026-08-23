"""
Controlled 429 RESOURCE_EXHAUSTED integration test.

Purpose (per "MerchSage -- Remaining Building Phase.md", P0 #1):

    "0011 is deployed" and "0011 works under the exact production
    failure" are two different claims. This test closes that gap
    deterministically, without waiting for Google to produce a real
    429 and without consuming any real Gemini quota.

It runs the REAL orchestrator (backend.pipeline.orchestrator.run_audit)
end-to-end, using a fake genai client that:
  - returns valid, schema-correct responses for every LLM-calling stage
    EXCEPT SEO Specialist,
  - raises a 429 RESOURCE_EXHAUSTED-shaped exception (identical string
    signature to what real Render logs showed) only for the SEO call.

This exercises the REAL AIStudioGeminiProvider.generate_text() retry/
quota-detection logic and the REAL SeoSpecialist fallback path -- not a
re-implementation of them -- so a regression in either would show up
here.

Verifies the complete chain:
    429 -> NO retry -> GeminiQuotaExhaustedError -> SEO does NOT use
    necklace mock -> listing-specific degraded output -> verification
    passes -> pipeline completes honestly.

Does not touch production code. Read-only exercise of the existing
0011 behavior.
"""
import json
import logging
import sys
from unittest.mock import patch, MagicMock

sys.path.insert(0, ".")

from backend.models.intake import SellerIntakePayload
from backend.models.evidence import EvidenceObject
from backend.providers.llm_provider_aistudio import AIStudioGeminiProvider


# ─── Log capture, so we can assert on WHICH log lines fired, not just
#     on final data -- this is what proves "no retry" actually happened
#     inside the real provider, not just that the end result looks ok. ───
class ListHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.records = []

    def emit(self, record):
        self.records.append(record.getMessage())


log_capture = ListHandler()
logging.getLogger("MerchSage.LLMProvider.AIStudio").addHandler(log_capture)
logging.getLogger("MerchSage.SeoSpecialist").addHandler(log_capture)
logging.getLogger("MerchSage.LLMProvider.AIStudio").setLevel(logging.DEBUG)
logging.getLogger("MerchSage.SeoSpecialist").setLevel(logging.DEBUG)


# ─── The exact real tote listing evidence from the proven production
#     run, given 13 tags so the degraded fallback can pass verification
#     cleanly on the first attempt (no fabricated/padded tags -- this is
#     what a real, fully-tagged Etsy listing looks like). ───
REAL_TOTE_TITLE = "Boho Embroidered Floral Tote Bag | Sage Green Linen, Zippered"
REAL_TOTE_TAGS = [
    "boho tote bag", "floral tote", "linen tote bag", "zippered tote",
    "market tote", "beach bag", "shopping bag", "canvas tote",
    "embroidered bag", "sage green bag", "boho bag gift", "tote for her",
    "eco tote bag",
]
assert len(REAL_TOTE_TAGS) == 13 and len(set(REAL_TOTE_TAGS)) == 13


def _fake_tote_evidence(_self, listing_url):
    now_str = "2026-08-23T00:00:00Z"
    return [
        EvidenceObject(
            source_type="observed fact",
            origin="Etsy API Listings Endpoint (live)",
            timestamp=now_str,
            confidence="HIGH",
            evidence_state="SUPPORTED",
            provenance=["Etsy Listings API"],
            supporting_data={
                "title": REAL_TOTE_TITLE,
                "description": "A handwoven boho tote bag in sage green linen with a zippered closure.",
                "tags": REAL_TOTE_TAGS,
                "quantity": 56,
                "listing_state": "active",
                "price": "35.71",
                "creation_tsz": "2026-06-01T12:00:00Z",
            },
            downstream_consumers=["ClassifierAgent", "EntrepreneurAgent", "DiscoverabilitySeoCopySpecialist"],
        )
    ]


# ─── Fake Gemini client: valid responses for every stage except SEO,
#     which gets the real 429 error string observed in production. ───
class FakeGenAIClient:
    def __init__(self):
        self.call_log = []  # list of (stage, ) for assertions
        self.models = self._Models(self)

    class _Models:
        def __init__(self, outer):
            self.outer = outer

        def generate_content(self, model, contents, config=None):
            sys_inst = (getattr(config, "system_instruction", "") or "") if config else ""
            stage = self.outer._identify_stage(sys_inst)
            self.outer.call_log.append(stage)

            if stage == "seo":
                # Exact error-string signature observed in real Render
                # logs for audit 29e516d0-e1d7-4696-9d57-72a4f1cdce93.
                raise Exception(
                    "429 RESOURCE_EXHAUSTED. Quota exceeded for metric: "
                    "generativelanguage.googleapis.com/generate_content_free_tier_requests, "
                    "limit: 20, model: gemini-3.5-flash"
                )

            return self.outer._valid_response_for(stage)

    def _identify_stage(self, sys_inst: str) -> str:
        s = sys_inst.lower()
        if "discoverability/seo specialist" in s:
            return "seo"
        if "classification agent" in s:
            return "classifier"
        if "entrepreneur agent" in s:
            return "entrepreneur"
        if "researcher agent" in s:
            return "researcher"
        if "triage agent" in s:
            return "triage"
        if "business verifier agent" in s:
            return "business_verifier"
        return "unknown"

    def _valid_response_for(self, stage: str):
        resp = MagicMock()
        if stage == "classifier":
            resp.text = json.dumps({
                "category": "Bags & Purses / Tote Bags",
                "confidence": "HIGH",
                "reasoning": "Title and description describe a fabric tote bag.",
            })
        elif stage == "entrepreneur":
            resp.text = json.dumps({
                "hypotheses": [
                    {"hypothesis_id": "H1", "title": "Low search visibility",
                     "description": "Tags may not match common buyer search terms.",
                     "assumptions": ["Buyers search using generic tote-bag terms"]},
                    {"hypothesis_id": "H2", "title": "Weak title keyword coverage",
                     "description": "Title may under-use high-traffic keywords.",
                     "assumptions": ["Title keyword density affects search rank"]},
                    {"hypothesis_id": "H3", "title": "Category mismatch",
                     "description": "Listing may be filed under a low-traffic subcategory.",
                     "assumptions": ["Taxonomy placement affects discoverability"]},
                ]
            })
        elif stage == "researcher":
            resp.text = json.dumps({
                "hypothesis_evaluations": [
                    {"hypothesis_id": "H1", "state": "CONFIRMED", "confidence": "HIGH",
                     "details": "Current tags omit common buyer search phrases."},
                    {"hypothesis_id": "H2", "state": "UNKNOWN", "confidence": "LOW",
                     "details": "Insufficient evidence to evaluate title keyword coverage."},
                    {"hypothesis_id": "H3", "state": "UNKNOWN", "confidence": "LOW",
                     "details": "Taxonomy placement not observable from available evidence."},
                ],
                "seller_claim_evaluations": [],
            })
        elif stage == "triage":
            resp.text = json.dumps({
                "problems": [
                    {"problem_id": "P1", "title": "Low search visibility",
                     "severity": "HIGH", "is_root_cause": True, "dependencies": [],
                     "description": "Tags omit common buyer search phrases.",
                     "associated_evidence_ids": []},
                ]
            })
        elif stage == "business_verifier":
            resp.text = json.dumps({
                "is_compatible": True,
                "conflicts": [],
                "evaluations": [
                    {"solution_ref": REAL_TOTE_TITLE, "status": "APPROVED",
                     "justification": "Degraded fallback reuses only the listing's own "
                                       "already-verified evidence; nothing to conflict with."},
                ],
            })
        else:
            raise AssertionError(f"Unexpected/unrecognized stage in fake client: {stage!r}")
        return resp


def main():
    fake_client = FakeGenAIClient()

    # Real provider, real retry/quota logic -- only its underlying
    # genai.Client is faked, exactly as done to validate 0011 itself.
    provider = AIStudioGeminiProvider.__new__(AIStudioGeminiProvider)
    provider.initialized = True
    provider.client = fake_client

    captured_contexts = []

    def _capturing_save_context(self, context):
        # Non-invasive: capture the real AuditContext object for
        # internal assertions (e.g. the `degraded` flag on
        # specialist_solutions) without needing new production hooks.
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

    # ── Assertion 1: pipeline completed all the way through, no abort ──
    assert "error" not in report or report.get("pipeline_status") not in (None,), \
        f"Pipeline aborted early: {report}"
    assert report.get("classification") == "Bags & Purses / Tote Bags"
    print("[1/7] PASS: pipeline completed end-to-end, correct tote classification.")

    # ── Assertion 2: SEO's Gemini call happened exactly ONCE (no retry) ──
    seo_calls = fake_client.call_log.count("seo")
    assert seo_calls == 1, (
        f"Expected exactly 1 SEO-stage Gemini call (no retry against a "
        f"non-transient 429), got {seo_calls}. Call log: {fake_client.call_log}"
    )
    print(f"[2/7] PASS: SEO stage called Gemini exactly once (call log: {fake_client.call_log}).")

    # ── Assertion 3: no retry-delay log line fired for the 429 ──
    retry_logs = [m for m in log_capture.records if "Retrying in" in m]
    assert not retry_logs, f"Expected zero retry-delay log lines for a 429, found: {retry_logs}"
    quota_shortcircuit_logs = [
        m for m in log_capture.records
        if "Quota exhaustion is non-transient" in m
    ]
    assert len(quota_shortcircuit_logs) == 1, (
        f"Expected exactly 1 quota short-circuit log line, got {len(quota_shortcircuit_logs)}: "
        f"{quota_shortcircuit_logs}"
    )
    print("[3/7] PASS: provider logged the non-transient short-circuit, zero retry-delay lines.")

    # ── Assertion 4: GeminiQuotaExhaustedError was actually raised and
    #     caught in SeoSpecialist (not swallowed somewhere else) ──
    seo_caught_logs = [
        m for m in log_capture.records
        if "Gemini quota exhausted during SEO Specialist stage" in m
    ]
    assert len(seo_caught_logs) == 1, (
        f"Expected SeoSpecialist to log exactly 1 caught GeminiQuotaExhaustedError, "
        f"got {len(seo_caught_logs)}: {seo_caught_logs}"
    )
    print("[4/7] PASS: GeminiQuotaExhaustedError raised by provider, caught by SeoSpecialist.")

    # ── Assertion 5: SEO output is the REAL tote listing, not necklace mock ──
    solutions = report.get("proposed_solutions", [])
    assert len(solutions) == 1
    sol = solutions[0]["solution"]
    assert sol["proposed_title"] == REAL_TOTE_TITLE, sol["proposed_title"]
    assert sol["proposed_tags"] == REAL_TOTE_TAGS, sol["proposed_tags"]
    banned = ["necklace", "silver", "925", "sterling", "handmade", "mother"]
    joined = (sol["proposed_title"] + " " + " ".join(sol["proposed_tags"])).lower()
    for term in banned:
        assert term not in joined, f"Found banned mock term {term!r} in SEO output: {sol}"
    print("[5/7] PASS: SEO output is the real tote listing's own data -- zero necklace-mock content.")

    # ── Assertion 6: the degraded flag is present internally on the
    #     AuditContext (proves SeoSpecialist marked it honestly), even
    #     though we separately confirm below it does NOT survive into
    #     the customer-facing report -- a real gap, not this test's bug. ──
    assert len(captured_contexts) == 1
    ctx = captured_contexts[0]
    internal_solution = ctx.specialist_solutions[-1]
    assert internal_solution.get("degraded") is True
    assert internal_solution.get("degradation_reason") == "gemini_quota_exhausted"
    assert internal_solution.get("claims_made") == []
    report_solution_keys = set(solutions[0]["solution"].keys())
    assert "degraded" not in report_solution_keys, (
        "NOTE: report_formatter.py's provenance chain construction only copies "
        "specialist/proposed_title/proposed_tags/justification/claims_made -- "
        "the internal 'degraded'/'degradation_reason' flags exist on the "
        "AuditContext but are silently dropped before reaching the customer-"
        "facing report. This matches the ambiguity flagged in the Remaining "
        "Building Phase doc item #3 (pipeline_status semantics) -- NOT fixed "
        "here, since this task is validating 0011, not report_formatter."
    )
    print("[6/7] PASS (with finding): 'degraded' flag set internally, confirmed absent from "
          "customer-facing report -- pre-existing gap, not caused by this test, not fixed here.")

    # ── Assertion 7: verification passes cleanly, pipeline completes honestly ──
    # NOTE: updated after the pipeline_status semantics fix (see
    # backend/agents/report_formatter.py::_derive_final_status). This
    # exact scenario -- a quota-exhausted degraded fallback that still
    # cleanly passes verification -- is precisely the case that fix
    # exists to correct: it is now "degraded" (a safe fallback was used,
    # not a live AI-generated result), never "verified"/"success". The
    # previous version of this assertion (`== "verified"`) was written
    # before that fix existed and encoded the exact bug it closes.
    vr = report.get("verification_results") or {}
    assert vr.get("factual_legal", {}).get("passed") is True, vr.get("factual_legal")
    assert vr.get("structural", {}).get("passed") is True, vr.get("structural")
    assert report.get("pipeline_status") == "degraded", report.get("pipeline_status")
    assert report.get("errors") == []
    print("[7/7] PASS: both structural and factual/legal verification passed cleanly on the "
          "first attempt (13 real tags => no padding needed); pipeline_status='degraded' "
          "(correctly distinct from 'success' -- this was a safe fallback, not a live AI "
          "result), errors=[] -- the full chain completed honestly with zero fabricated content.")

    print("\n=== ALL 7 CHECKS PASSED: full 429 -> degraded-fallback chain confirmed. ===")
    print(f"Total Gemini calls across whole pipeline: {len(fake_client.call_log)} "
          f"({fake_client.call_log})")


if __name__ == "__main__":
    main()
