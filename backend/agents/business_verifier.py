import json
import logging
from datetime import datetime
from backend.models.audit import AuditContext
from backend.models.evidence import EvidenceObject
from backend.providers.llm_provider import LLMProvider

logger = logging.getLogger("MerchSage.BusinessVerifier")

class BusinessVerifierAgent:
    def __init__(self, llm_provider: LLMProvider):
        self.llm_provider = llm_provider

    def execute(self, context: AuditContext) -> None:
        logger.info("Executing Business Verifier Stage...")
        
        # Gather solutions, triage problems, and Researcher claim states
        solutions = context.specialist_solutions
        problems = context.triage_results.get("problems", []) if context.triage_results else []
        
        claims_states = []
        for ev in context.evidence_store:
            if ev.origin == "ResearcherAgent" and ev.source_type == "seller claim":
                claims_states.append({
                    "claim_name": ev.supporting_data.get("claim_name"),
                    "state": ev.evidence_state,
                    "details": ev.supporting_data.get("evaluation_details")
                })
                
        evidence_summary = []
        for ev in context.evidence_store:
            evidence_summary.append({
                "evidence_id": ev.evidence_id,
                "source_type": ev.source_type,
                "origin": ev.origin,
                "evidence_state": ev.evidence_state,
                "supporting_data": ev.supporting_data
            })

        system_instruction = (
            "You are the Business Verifier Agent for MerchSage, an Etsy listings multi-agent audit system. "
            "Your task is to perform strategic and compatibility checks on all proposed solutions: \n"
            "1. Trace verification: Ensure every solution traces back: Solution -> Confirmed Problem -> Evidence Object -> Hypothesis.\n"
            "2. Compatibility check: Ensure solutions do not contradict each other or degrade the listing's business strategy.\n"
            "3. Claim state enforcement: Validate that seller differentiator claims are ONLY cited at their Researcher-evaluated state "
            "(SUPPORTED, CONTRADICTED, MIXED, UNKNOWN). You must NEVER treat an unverified or refuted seller claim as a verified fact.\n"
            "Return a valid JSON object matching this schema:\n"
            "{\n"
            "  \"is_compatible\": true or false,\n"
            "  \"conflicts\": [\"list of conflict descriptions, if any\"],\n"
            "  \"evaluations\": [\n"
            "    {\n"
            "      \"solution_ref\": \"reference to the title/tag solution\",\n"
            "      \"status\": \"APPROVED or REJECTED\",\n"
            "      \"justification\": \"detailed reasoning referencing evidence IDs and claim states\"\n"
            "    }\n"
            "  ]\n"
            "}"
        )
        
        prompt = (
            f"Please verify business logic and compatibility for these solutions:\n"
            f"Proposed Solutions: {json.dumps(solutions, indent=2)}\n\n"
            f"Triage Problems: {json.dumps(problems, indent=2)}\n\n"
            f"Researcher Evaluated Claims: {json.dumps(claims_states, indent=2)}\n\n"
            f"Full Evidence List:\n{json.dumps(evidence_summary, indent=2)}\n"
        )
        
        response_text = self.llm_provider.generate_text(
            prompt=prompt,
            system_instruction=system_instruction,
            response_schema={
                "type": "OBJECT",
                "properties": {
                    "is_compatible": {"type": "BOOLEAN"},
                    "conflicts": {
                        "type": "ARRAY",
                        "items": {"type": "STRING"}
                    },
                    "evaluations": {
                        "type": "ARRAY",
                        "items": {
                            "type": "OBJECT",
                            "properties": {
                                "solution_ref": {"type": "STRING"},
                                "status": {"type": "STRING"},
                                "justification": {"type": "STRING"}
                            },
                            "required": ["solution_ref", "status", "justification"]
                        }
                    }
                },
                "required": ["is_compatible", "conflicts", "evaluations"]
            }
        )
        
        try:
            res = json.loads(response_text)
            context.business_verification_results = res
            
            # Write a business verifier evidence object
            now_str = datetime.utcnow().isoformat() + "Z"
            verifier_ev = EvidenceObject(
                source_type="inference",
                origin="BusinessVerifierAgent",
                timestamp=now_str,
                confidence="HIGH",
                evidence_state="SUPPORTED",
                provenance=["Specialist Solutions & Claims -> BusinessVerifierAgent"],
                supporting_data={
                    "business_verification": context.business_verification_results
                },
                downstream_consumers=["ReportFormatterAgent"]
            )
            context.evidence_store.append(verifier_ev)
            context.status = "verified"
            logger.info("Successfully completed business verification.")
        except Exception as e:
            logger.error(f"Failed to parse business verification: {response_text}. Error: {e}")
            context.errors.append(f"Business Verifier check failed: {e}")
            context.status = "error"
