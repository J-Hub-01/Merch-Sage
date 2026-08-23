"""
Focused regression test for the pipeline_status derivation fix
(_derive_final_status in report_formatter.py).

Covers the 5 required cases:
  1. normal successful audit -> "success"
  2. verification failure + successful BusinessVerifier -> "degraded"
  3. Gemini quota fallback (degraded=True) + passed verification -> "degraded"
  4. Gemini auth/generation infrastructure failure -> "failed"
  5. generic existing report generation behavior remains intact
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
    if stage == "classifier":
        resp.text = json.dumps({"category": "Bags & Purses / Tote Bags", "confidence": "HIGH", "reasoning": "tote"})
    elif stage == "entrepreneur":
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


def _identify(sys_inst):
    s = sys_inst.lower()
    if "discoverability/seo specialist" in s: return "seo"
    if "classification agent" in s: return "classifier"
    if "entrepreneur agent" in s: return "entrepreneur"
    if "researcher agent" in s: return "researcher"
    if "triage agent" in s: return "triage"
    if "business verifier agent" in s: return "business_verifier"
    return "unknown"


def _run(fake_client):
    provider = AIStudioGeminiProvider.__new__(AIStudioGeminiProvider)
    provider.initialized = True
    provider.client = fake_client
    intake = SellerIntakePayload(listing_url="https://www.etsy.com/in-en/listing/1716154949/boho-embroidered-floral-tote-bag-in-sage")
    with patch("backend.pipeline.orchestrator.get_llm_provider", return_value=provider), \
         patch("backend.pipeline.orchestrator.MarketplaceEvidenceProvider.get_listing_evidence", new=_fake_tote_evidence), \
         patch("backend.pipeline.orchestrator.LocalJsonAuditStore.save_context", new=lambda self, ctx: None):
        from backend.pipeline.orchestrator import run_audit
        return run_audit(intake)


class Client:
    def __init__(self, fail_seo_with=None):
        self.fail_seo_with = fail_seo_with
        self.models = self

    def generate_content(self, model, contents, config=None):
        s = _identify((getattr(config, "system_instruction", "") or "") if config else "")
        if s == "seo" and self.fail_seo_with:
            if self.fail_seo_with == "bad_claim":
                resp = MagicMock()
                resp.text = json.dumps({"specialist": "DiscoverabilitySeoCopySpecialist",
                    "proposed_title": REAL_TOTE_TITLE + " - Premium Handmade",
                    "proposed_tags": REAL_TOTE_TAGS_13, "justification": "j", "claims_made": ["handmade"]})
                return resp
            raise self.fail_seo_with
        return _valid(s)


all_passed = True

def check(label, cond):
    global all_passed
    status = "PASS" if cond else "FAIL"
    if not cond:
        all_passed = False
    print(f"[{status}] {label}")


print("### 1. Normal successful audit -> 'success' ###")
r1 = _run(Client())
check("pipeline_status == 'success'", r1.get("pipeline_status") == "success")
check("verification_results preserved and all passed", all(v.get("passed") for v in r1["verification_results"].values()))
check("errors == []", r1.get("errors") == [])
check("classification preserved", r1.get("classification") == "Bags & Purses / Tote Bags")
print()

print("### 2. Verification failure + successful BusinessVerifier -> 'degraded' ###")
r2 = _run(Client(fail_seo_with="bad_claim"))
check("pipeline_status == 'degraded'", r2.get("pipeline_status") == "degraded")
check("verification_results.factual_legal.passed == False (preserved)", r2["verification_results"]["factual_legal"]["passed"] is False)
check("errors non-empty (preserved)", len(r2.get("errors", [])) > 0)
check("business_verification still present (proves BusinessVerifier DID succeed independently)",
      r2.get("business_verification") is not None)
print()

print("### 3. Gemini quota fallback (degraded=True) + passed verification -> 'degraded' ###")
r3 = _run(Client(fail_seo_with=Exception("429 RESOURCE_EXHAUSTED. Quota exceeded.")))
check("pipeline_status == 'degraded'", r3.get("pipeline_status") == "degraded")
check("verification_results all passed (preserved -- degraded status is NOT from a failed check here)",
      all(v.get("passed") for v in r3["verification_results"].values()))
check("proposed_title is the real tote listing, not necklace mock",
      r3["proposed_solutions"][0]["solution"]["proposed_title"] == REAL_TOTE_TITLE)
print()

print("### 4. Gemini auth/generation infrastructure failure -> 'failed' ###")
r4a = _run(Client(fail_seo_with=Exception("401 UNAUTHENTICATED. API key not valid.")))
check("auth failure: pipeline_status == 'failed'", r4a.get("pipeline_status") == "failed")
check("auth failure: failure_type == 'gemini_authentication_error'", r4a.get("failure_type") == "gemini_authentication_error")
r4b = _run(Client(fail_seo_with=Exception("500 Internal Server Error. Unexpected.")))
check("generation failure: pipeline_status == 'failed'", r4b.get("pipeline_status") == "failed")
check("generation failure: failure_type == 'gemini_generation_error'", r4b.get("failure_type") == "gemini_generation_error")
print()

print("### 5. Generic existing report generation behavior remains intact ###")
check("proposed_solutions still has provenance chain shape", "addressed_problems" in r1["proposed_solutions"][0])
check("problem_dependency_graph preserved", len(r1.get("problem_dependency_graph", [])) == 1)
check("seller_claim_evaluations key present", "seller_claim_evaluations" in r1)
check("total_evidence_objects present and > 0", r1.get("total_evidence_objects", 0) > 0)
check("audit_id present", bool(r1.get("audit_id")))
check("timestamp present", bool(r1.get("timestamp")))
print()

print("=" * 70)
print("ALL CHECKS PASSED" if all_passed else "SOME CHECKS FAILED")
sys.exit(0 if all_passed else 1)
