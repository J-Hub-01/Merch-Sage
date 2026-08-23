import json
import logging
from datetime import datetime
from backend.models.audit import AuditContext
from backend.models.evidence import EvidenceObject
from backend.providers.llm_provider import LLMProvider
from backend.providers.exceptions import GeminiQuotaExhaustedError

logger = logging.getLogger("MerchSage.SeoSpecialist")

class DiscoverabilitySeoCopySpecialist:
    def __init__(self, llm_provider: LLMProvider):
        self.llm_provider = llm_provider

    def execute(self, context: AuditContext) -> None:
        logger.info("Executing Discoverability/SEO Specialist Stage...")
        
        # Gather context data
        problems = context.triage_results.get("problems", []) if context.triage_results else []
        classification = context.classification or "unknown"
        
        original_listing = {}
        for ev in context.evidence_store:
            if ev.source_type == "observed fact" and ev.origin.startswith("Etsy API Listings Endpoint"):
                original_listing.update(ev.supporting_data)
        
        evidence_summary = []
        for ev in context.evidence_store:
            evidence_summary.append({
                "evidence_id": ev.evidence_id,
                "source_type": ev.source_type,
                "origin": ev.origin,
                "supporting_data": ev.supporting_data,
                "evidence_state": ev.evidence_state
            })

        system_instruction = (
            "You are the Discoverability/SEO Specialist Agent for MerchSage, an Etsy listings multi-agent audit system. "
            "Your task is to write an optimized title and exactly 13 search tags targeting the root causes identified "
            "in the prioritized problems list. "
            "CRITICAL CONSTRAINTS (v2 Amendment & AI Marketing Legal Compliance):\n"
            "1. You must not include any unsupported factual claims (e.g. claiming 'sterling silver 925' or 'handmade' unless there is an Evidence Object confirming it).\n"
            "2. You must not invent false urgency/scarcity or fake reviews/pricing references.\n"
            "3. Every claim embedded in your proposed copy must be traced back to a specific evidence ID in the input.\n"
            "4. Return exactly 13 tags in the tags array.\n"
            "Return a valid JSON object matching this schema:\n"
            "{\n"
            "  \"proposed_title\": \"string, optimized listing title (<= 140 chars)\",\n"
            "  \"proposed_tags\": [\"exactly 13 tag strings, each <= 20 chars\"],\n"
            "  \"justification\": \"brief explanation of how these resolve the primary problems\",\n"
            "  \"claims_made\": [\n"
            "    \"Factual claim: [description] -> Traced to Evidence ID: [ID]\"\n"
            "  ]\n"
            "}"
        )
        
        prompt = (
            f"Optimizing for Category: {classification}\n"
            f"Prioritized Problems: {json.dumps(problems, indent=2)}\n"
            f"Original Listing Details:\nTitle: {original_listing.get('title')}\nTags: {original_listing.get('tags')}\nDescription: {original_listing.get('description')}\n\n"
            f"Full Evidence Objects List:\n{json.dumps(evidence_summary, indent=2)}\n"
        )
        
        try:
            response_text = self.llm_provider.generate_text(
                prompt=prompt,
                system_instruction=system_instruction,
                response_schema={
                    "type": "OBJECT",
                    "properties": {
                        "proposed_title": {"type": "STRING"},
                        "proposed_tags": {
                            "type": "ARRAY",
                            "items": {"type": "STRING"}
                        },
                        "justification": {"type": "STRING"},
                        "claims_made": {
                            "type": "ARRAY",
                            "items": {"type": "STRING"}
                        }
                    },
                    "required": ["proposed_title", "proposed_tags", "justification", "claims_made"]
                },
                raise_on_quota_exhaustion=True,
            )
        except GeminiQuotaExhaustedError as e:
            # Non-transient failure: live Gemini is unavailable for this
            # request because the quota ceiling has been hit. Rather than
            # fall through to a static, listing-unrelated developer mock
            # (which would silently describe a different product), return
            # the seller's own real, current title/tags unchanged. This is
            # honest and trivially evidence-grounded -- every "claim" in it
            # is already backed by the observed-fact Evidence Object it was
            # read from -- at the cost of not being AI-optimized this run.
            logger.warning(
                f"Gemini quota exhausted during SEO Specialist stage: {e}. "
                f"Falling back to the listing's own current title/tags "
                f"(no AI-generated claims) instead of developer mock."
            )
            solution_data = {
                "specialist": "DiscoverabilitySeoCopySpecialist",
                "proposed_title": original_listing.get("title") or "",
                "proposed_tags": list(original_listing.get("tags") or []),
                "justification": (
                    "AI-generated SEO recommendations were unavailable for this run "
                    "because the Gemini API quota was exhausted. The listing's current, "
                    "unmodified title and tags are shown as a safe fallback -- no new "
                    "claims were generated, so nothing here goes beyond what Etsy already "
                    "reports for this listing."
                ),
                "claims_made": [],
                "degraded": True,
                "degradation_reason": "gemini_quota_exhausted",
            }
            context.specialist_solutions.append(solution_data)

            now_str = datetime.utcnow().isoformat() + "Z"
            solution_ev = EvidenceObject(
                source_type="inference",
                origin="DiscoverabilitySeoCopySpecialist",
                timestamp=now_str,
                confidence="LOW",
                evidence_state="SUPPORTED",
                provenance=["Triage Results & Evidence -> DiscoverabilitySeoCopySpecialist (degraded: quota exhausted)"],
                supporting_data=solution_data,
                downstream_consumers=["Verification", "BusinessVerifierAgent"]
            )
            context.evidence_store.append(solution_ev)
            context.status = "solved"
            return

        try:
            res = json.loads(response_text)
            
            # Map solutions back to context
            solution_data = {
                "specialist": "DiscoverabilitySeoCopySpecialist",
                "proposed_title": res.get("proposed_title"),
                "proposed_tags": res.get("proposed_tags"),
                "justification": res.get("justification"),
                "claims_made": res.get("claims_made")
            }
            context.specialist_solutions.append(solution_data)
            
            # Write solution evidence object
            now_str = datetime.utcnow().isoformat() + "Z"
            solution_ev = EvidenceObject(
                source_type="inference",
                origin="DiscoverabilitySeoCopySpecialist",
                timestamp=now_str,
                confidence="HIGH",
                evidence_state="SUPPORTED",
                provenance=["Triage Results & Evidence -> DiscoverabilitySeoCopySpecialist"],
                supporting_data=solution_data,
                downstream_consumers=["Verification", "BusinessVerifierAgent"]
            )
            context.evidence_store.append(solution_ev)
            context.status = "solved"
            logger.info("Successfully generated SEO solution.")
        except Exception as e:
            logger.error(f"Failed to parse SEO solution: {response_text}. Error: {e}")
            context.errors.append(f"SEO Specialist solution generation failed: {e}")
            context.status = "error"
