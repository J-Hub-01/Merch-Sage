import json
import logging
from datetime import datetime
from backend.models.audit import AuditContext
from backend.models.evidence import EvidenceObject
from backend.providers.llm_provider import LLMProvider
from backend.providers.exceptions import GeminiQuotaExhaustedError

logger = logging.getLogger("MerchSage.Triage")

class TriageAgent:
    def __init__(self, llm_provider: LLMProvider):
        self.llm_provider = llm_provider

    def execute(self, context: AuditContext) -> None:
        logger.info("Executing Triage Stage (Problem Prioritization & Dependency Mapping)...")
        
        # Gather all confirmed or likely hypotheses from evidence store
        confirmed_evidence = []
        for ev in context.evidence_store:
            if ev.origin == "EntrepreneurAgent" and ev.evidence_state in ("CONFIRMED", "LIKELY"):
                confirmed_evidence.append({
                    "evidence_id": ev.evidence_id,
                    "hypothesis_title": ev.supporting_data.get("hypothesis", {}).get("title"),
                    "hypothesis_description": ev.supporting_data.get("hypothesis", {}).get("description"),
                    "state": ev.evidence_state,
                    "details": ev.supporting_data.get("evaluation_details")
                })
        
        if not confirmed_evidence:
            logger.info("No confirmed discoverability problems found. Registering empty triage result.")
            context.triage_results = {"problems": []}
            context.status = "triaged"
            return

        system_instruction = (
            "You are the Triage Agent for MerchSage, an Etsy listings multi-agent audit system. "
            "Your task is to merge duplicate findings, separate root causes from symptoms, "
            "and priority-order all confirmed problems. "
            "CRITICAL RULES:\n"
            "1. You must discard NOTHING that was verified. Every confirmed or likely problem in the input must be accounted for.\n"
            "2. Map dependencies clearly. A problem is a dependency if solving it is required before solving the other.\n"
            "3. Assign a severity to each (CRITICAL, HIGH, MEDIUM, LOW).\n"
            "Return a valid JSON object matching this schema:\n"
            "{\n"
            "  \"problems\": [\n"
            "    {\n"
            "      \"problem_id\": \"string ID, e.g. P1, P2\",\n"
            "      \"title\": \"short name of problem\",\n"
            "      \"severity\": \"CRITICAL or HIGH or MEDIUM or LOW\",\n"
            "      \"is_root_cause\": true or false,\n"
            "      \"dependencies\": [\"list of problem_ids this problem depends on, if any\"],\n"
            "      \"description\": \"brief description of the problem\",\n"
            "      \"associated_evidence_ids\": [\"list of evidence IDs from the input that prove this problem\"]\n"
            "    }\n"
            "  ]\n"
            "}"
        )
        
        prompt = (
            f"Please prioritize and map dependencies for these confirmed problems:\n"
            f"{json.dumps(confirmed_evidence, indent=2)}\n"
        )
        
        try:
            response_text = self.llm_provider.generate_text(
                prompt=prompt,
                system_instruction=system_instruction,
                response_schema={
                    "type": "OBJECT",
                    "properties": {
                        "problems": {
                            "type": "ARRAY",
                            "items": {
                                "type": "OBJECT",
                                "properties": {
                                    "problem_id": {"type": "STRING"},
                                    "title": {"type": "STRING"},
                                    "severity": {"type": "STRING"},
                                    "is_root_cause": {"type": "BOOLEAN"},
                                    "dependencies": {
                                        "type": "ARRAY",
                                        "items": {"type": "STRING"}
                                    },
                                    "description": {"type": "STRING"},
                                    "associated_evidence_ids": {
                                        "type": "ARRAY",
                                        "items": {"type": "STRING"}
                                    }
                                },
                                "required": ["problem_id", "title", "severity", "is_root_cause", "dependencies", "description", "associated_evidence_ids"]
                            }
                        }
                    },
                    "required": ["problems"]
                },
                raise_on_quota_exhaustion=True,
            )
        except GeminiQuotaExhaustedError as e:
            # Unlike Classification/Entrepreneur/Researcher, Triage already
            # has a truthful, non-fabricated "nothing to report" output
            # built in above (lines 29-33) for the structurally identical
            # case of having no confirmed evidence to triage. A live-call
            # failure is evidence-wise indistinguishable from that case --
            # there is nothing safely establishable either way -- so reuse
            # the exact same truthful payload instead of falling through to
            # the developer mock's fabricated, listing-unrelated problems.
            # Marked degraded via the same mechanism SEO Specialist (0011)
            # uses, so the failure is not silently identical to a genuine
            # empty-triage result internally, even though the report-level
            # gap (degraded flag not surfaced in the customer report,
            # found in 0012) remains separate, deferred scope.
            logger.warning(
                f"Gemini quota exhausted during Triage stage: {e}. "
                f"Falling back to the same truthful empty result already used "
                f"when there is no confirmed evidence, instead of developer mock."
            )
            context.triage_results = {"problems": []}

            now_str = datetime.utcnow().isoformat() + "Z"
            triage_ev = EvidenceObject(
                source_type="inference",
                origin="TriageAgent",
                timestamp=now_str,
                confidence="LOW",
                evidence_state="SUPPORTED",
                provenance=["TriageAgent (degraded: quota exhausted)"],
                supporting_data={
                    "problem_graph": context.triage_results,
                    "degraded": True,
                    "degradation_reason": "gemini_quota_exhausted",
                },
                downstream_consumers=["DiscoverabilitySeoCopySpecialist"]
            )
            context.evidence_store.append(triage_ev)
            context.status = "triaged"
            return
        
        try:
            res = json.loads(response_text)
            if "problems" not in res:
                raise ValueError("Triage response missing required field 'problems'.")
            context.triage_results = res
            
            # Create a triage inference evidence object
            now_str = datetime.utcnow().isoformat() + "Z"
            triage_ev = EvidenceObject(
                source_type="inference",
                origin="TriageAgent",
                timestamp=now_str,
                confidence="HIGH",
                evidence_state="SUPPORTED",
                provenance=[f"Evidence ID: {item['evidence_id']} -> TriageAgent" for item in confirmed_evidence],
                supporting_data={
                    "problem_graph": context.triage_results
                },
                downstream_consumers=["DiscoverabilitySeoCopySpecialist"]
            )
            context.evidence_store.append(triage_ev)
            context.status = "triaged"
            logger.info("Successfully triaged and mapped dependencies.")
        except Exception as e:
            logger.error(f"Failed to parse triage result: {response_text}. Error: {e}")
            context.errors.append(f"Triage prioritization failed: {e}")
            context.status = "error"
