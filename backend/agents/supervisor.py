import logging
from datetime import datetime
from backend.models.audit import AuditContext
from backend.models.evidence import EvidenceObject

logger = logging.getLogger("MerchSage.Supervisor")

class SupervisorAgent:
    """
    Supervisor / QC Agent checks pipeline execution integrity:
    - Verifies all required stages ran and recorded schema-valid outputs.
    - Verifies Evidence Object structures and ID references.
    - Verifies that mandatory Domain-Specific Verifications executed.
    Does not evaluate business strategy or output quality (left to Business Verifier).
    """
    def __init__(self):
        pass

    def execute(self, context: AuditContext) -> None:
        logger.info("Executing Supervisor/QC Stage...")
        
        passed = True
        errors = []
        
        # 1. Check classification
        if not context.classification:
            passed = False
            errors.append("Supervisor Error: Classification is missing.")
            
        # 2. Check diagnosed branch
        if not context.diagnosed_branch:
            passed = False
            errors.append("Supervisor Error: Diagnosed branch is missing.")
            
        # 3. Check hypothesis map
        if not context.hypothesis_map:
            passed = False
            errors.append("Supervisor Error: Hypothesis map is empty/missing.")
            
        # 4. Check that Researcher evaluated hypotheses
        hyp_evidences = [ev for ev in context.evidence_store if ev.origin == "EntrepreneurAgent"]
        if not hyp_evidences:
            passed = False
            errors.append("Supervisor Error: No hypotheses found in evidence store.")
        else:
            unevaluated = [ev for ev in hyp_evidences if ev.evidence_state == "UNKNOWN"]
            if len(unevaluated) == len(hyp_evidences):
                passed = False
                errors.append("Supervisor Error: All hypotheses remain unevaluated by Researcher.")
                
        # 5. Check Triage results exist
        if context.triage_results is None:
            passed = False
            errors.append("Supervisor Error: Triage results are missing.")
            
        # 6. Check that Specialist Solutions exist and are valid
        if not context.specialist_solutions:
            passed = False
            errors.append("Supervisor Error: SEO Specialist solutions are missing.")
        else:
            latest_solution = context.specialist_solutions[-1]
            title = latest_solution.get("proposed_title", "")
            tags = latest_solution.get("proposed_tags", [])
            
            if not title:
                passed = False
                errors.append("Supervisor Error: Proposed title is empty.")
            if len(tags) != 13:
                passed = False
                errors.append(f"Supervisor Error: Proposed tag count is {len(tags)}, must be exactly 13.")
                
        # 7. Check Domain Verification checks executed
        if not context.verification_results:
            passed = False
            errors.append("Supervisor Error: Domain verification results are missing.")
        else:
            structural = context.verification_results.get("structural", {})
            factual_legal = context.verification_results.get("factual_legal", {})
            
            if not structural or "passed" not in structural:
                passed = False
                errors.append("Supervisor Error: Structural domain verification did not execute correctly.")
            if not factual_legal or "passed" not in factual_legal:
                passed = False
                errors.append("Supervisor Error: Factual/Legal domain verification did not execute correctly.")
                
        # 8. Check schema integrity of all Evidence Objects
        for ev in context.evidence_store:
            if not ev.evidence_id or not ev.source_type or not ev.origin:
                passed = False
                errors.append(f"Supervisor Error: Malformed Evidence Object (ID: {ev.evidence_id}).")
                
        if passed:
            context.status = "qc_verified"
            qc_state = "SUPPORTED"
            logger.info("Supervisor/QC passed all integrity checks.")
        else:
            context.status = "error"
            context.errors.extend(errors)
            qc_state = "CONTRADICTED"
            logger.error(f"Supervisor/QC failed: {errors}")
            
        # Append QC Evidence Object
        now_str = datetime.utcnow().isoformat() + "Z"
        qc_ev = EvidenceObject(
            source_type="inference",
            origin="SupervisorAgent",
            timestamp=now_str,
            confidence="HIGH",
            evidence_state=qc_state,
            provenance=["Pipeline Context -> SupervisorAgent"],
            supporting_data={
                "qc_passed": passed,
                "qc_errors": errors
            },
            downstream_consumers=["BusinessVerifierAgent"]
        )
        context.evidence_store.append(qc_ev)
