import json
import logging
from datetime import datetime
from backend.models.audit import AuditContext
from backend.models.evidence import EvidenceObject
from backend.providers.llm_provider import LLMProvider

logger = logging.getLogger("MerchSage.Researcher")

class ResearcherAgent:
    def __init__(self, llm_provider: LLMProvider):
        self.llm_provider = llm_provider

    def execute(self, context: AuditContext) -> None:
        logger.info("Executing Researcher Stage (Hypothesis & Seller Claim Evaluation)...")
        
        # Collect all existing evidence for context
        available_evidence = []
        for ev in context.evidence_store:
            available_evidence.append({
                "evidence_id": ev.evidence_id,
                "source_type": ev.source_type,
                "origin": ev.origin,
                "supporting_data": ev.supporting_data
            })
            
        hypotheses = context.hypothesis_map
        
        # Get seller claims from intake
        seller_claims = list(context.intake_payload.seller_differentiators)
        if context.intake_payload.other_differentiator_details:
            seller_claims.append(f"other: {context.intake_payload.other_differentiator_details}")

        system_instruction = (
            "You are the Researcher Agent for MerchSage, an Etsy listings multi-agent audit system. "
            "Your task is to test every Entrepreneur-mandated hypothesis and evaluate the seller's differentiator claims "
            "strictly against the provided list of available Evidence Objects. "
            "CRITICAL RULES:\n"
            "1. You must never fabricate evidence to fill a gap. If there is no evidence to support a claim or hypothesis, "
            "you must classify it as UNKNOWN (for claims) or UNKNOWN-INSUFFICIENT EVIDENCE (for hypotheses).\n"
            "2. For each hypothesis, output the state as one of: CONFIRMED, LIKELY, INCONCLUSIVE, REFUTED, or UNKNOWN.\n"
            "3. For each seller claim, output the state as one of: SUPPORTED, CONTRADICTED, MIXED, or UNKNOWN.\n"
            "Return a valid JSON object matching this schema:\n"
            "{\n"
            "  \"hypothesis_evaluations\": [\n"
            "    {\n"
            "      \"hypothesis_id\": \"string ID\",\n"
            "      \"state\": \"CONFIRMED or LIKELY or INCONCLUSIVE or REFUTED or UNKNOWN\",\n"
            "      \"confidence\": \"HIGH or MEDIUM or LOW\",\n"
            "      \"details\": \"reasoning detailing supporting evidence IDs\"\n"
            "    }\n"
            "  ],\n"
            "  \"seller_claim_evaluations\": [\n"
            "    {\n"
            "      \"claim\": \"string description of the claim\",\n"
            "      \"state\": \"SUPPORTED or CONTRADICTED or MIXED or UNKNOWN\",\n"
            "      \"confidence\": \"HIGH or MEDIUM or LOW\",\n"
            "      \"details\": \"reasoning detailing supporting evidence IDs\"\n"
            "    }\n"
            "  ]\n"
            "}"
        )

        prompt = (
            f"Please test the hypotheses and evaluate the seller claims based on available evidence.\n"
            f"Available Evidence Objects:\n{json.dumps(available_evidence, indent=2)}\n\n"
            f"Hypotheses to Test:\n{json.dumps(hypotheses, indent=2)}\n\n"
            f"Seller Claims to Evaluate:\n{json.dumps(seller_claims, indent=2)}\n"
        )
        
        response_text = self.llm_provider.generate_text(
            prompt=prompt,
            system_instruction=system_instruction,
            response_schema={
                "type": "OBJECT",
                "properties": {
                    "hypothesis_evaluations": {
                        "type": "ARRAY",
                        "items": {
                            "type": "OBJECT",
                            "properties": {
                                "hypothesis_id": {"type": "STRING"},
                                "state": {"type": "STRING"},
                                "confidence": {"type": "STRING"},
                                "details": {"type": "STRING"}
                            },
                            "required": ["hypothesis_id", "state", "confidence", "details"]
                        }
                    },
                    "seller_claim_evaluations": {
                        "type": "ARRAY",
                        "items": {
                            "type": "OBJECT",
                            "properties": {
                                "claim": {"type": "STRING"},
                                "state": {"type": "STRING"},
                                "confidence": {"type": "STRING"},
                                "details": {"type": "STRING"}
                            },
                            "required": ["claim", "state", "confidence", "details"]
                        }
                    }
                },
                "required": ["hypothesis_evaluations", "seller_claim_evaluations"]
            }
        )
        
        try:
            res = json.loads(response_text)
            if "hypothesis_evaluations" not in res or "seller_claim_evaluations" not in res:
                raise ValueError("Researcher response missing required fields ('hypothesis_evaluations' or 'seller_claim_evaluations').")
            
            # Map hypothesis results back to context and update existing evidence objects
            now_str = datetime.utcnow().isoformat() + "Z"
            
            evals_by_id = {item["hypothesis_id"]: item for item in res.get("hypothesis_evaluations", [])}

            # --- DIAGNOSTIC LOGGING ONLY (temporary) ---
            # Purpose: confirm whether live Researcher responses return
            # hypothesis_id values matching what Entrepreneur (possibly
            # via mock fallback) actually generated. Does not alter
            # fallback behavior, ID matching, or success logic in any way.
            expected_ids = [
                ev.supporting_data["hypothesis"].get("hypothesis_id")
                for ev in context.evidence_store
                if ev.origin == "EntrepreneurAgent" and "hypothesis" in ev.supporting_data
            ]
            logger.info(f"[DIAGNOSTIC] Expected hypothesis IDs (from EntrepreneurAgent evidence): {expected_ids}")
            logger.info(f"[DIAGNOSTIC] Researcher evals_by_id keys (from live/mock response): {list(evals_by_id.keys())}")
            # --- END DIAGNOSTIC LOGGING ---

            # Update the untested hypotheses in evidence store
            matched_count = 0
            for ev in context.evidence_store:
                if ev.origin == "EntrepreneurAgent" and "hypothesis" in ev.supporting_data:
                    hyp_id = ev.supporting_data["hypothesis"].get("hypothesis_id")
                    if hyp_id in evals_by_id:
                        evaluation = evals_by_id[hyp_id]
                        ev.confidence = evaluation.get("confidence", "MEDIUM")
                        ev.evidence_state = evaluation.get("state", "UNKNOWN")
                        ev.supporting_data["evaluation_details"] = evaluation.get("details", "")
                        ev.provenance.append("ResearcherAgent Evaluation")
                        ev.timestamp = now_str
                        matched_count += 1

            # --- DIAGNOSTIC LOGGING ONLY (temporary) ---
            logger.info(f"[DIAGNOSTIC] Hypotheses matched and updated: {matched_count} / {len(expected_ids)}")
            # --- END DIAGNOSTIC LOGGING ---
            
            # Create new Evidence Objects for evaluated seller claims
            for claim_eval in res.get("seller_claim_evaluations", []):
                claim_ev = EvidenceObject(
                    source_type="seller claim",
                    origin="ResearcherAgent",
                    timestamp=now_str,
                    confidence=claim_eval.get("confidence", "MEDIUM"),
                    evidence_state=claim_eval.get("state", "UNKNOWN"),
                    provenance=["Seller Intake -> ResearcherAgent"],
                    supporting_data={
                        "claim_name": claim_eval.get("claim"),
                        "evaluation_details": claim_eval.get("details")
                    },
                    downstream_consumers=["BusinessVerifierAgent"]
                )
                context.evidence_store.append(claim_ev)
                
            context.status = "researched"
            logger.info("Successfully completed research and claim evaluation.")
        except Exception as e:
            logger.error(f"Failed to parse research evaluations: {response_text}. Error: {e}")
            context.errors.append(f"Researcher evaluation failed: {e}")
            context.status = "error"
