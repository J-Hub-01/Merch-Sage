import logging
from datetime import datetime
from backend.models.audit import AuditContext

logger = logging.getLogger("MerchSage.ReportFormatter")

class ReportFormatterAgent:
    """
    Deterministic report assembly — no LLM calls.
    Produces the structured JSON audit report containing:
    - Problem dependency graph
    - Proposed solutions with evidence provenance chains
    - Seller claim evaluation states
    - Verification results
    - Business verification results
    """

    def execute(self, context: AuditContext) -> None:
        logger.info("Executing Report Formatter Stage...")

        # Build provenance chains: Solution -> Problem -> Evidence -> Hypothesis
        provenance_chains = []
        solutions = context.specialist_solutions or []
        problems = (context.triage_results or {}).get("problems", [])

        for solution in solutions:
            chain = {
                "solution": {
                    "specialist": solution.get("specialist"),
                    "proposed_title": solution.get("proposed_title"),
                    "proposed_tags": solution.get("proposed_tags"),
                    "justification": solution.get("justification"),
                    "claims_made": solution.get("claims_made", []),
                },
                "addressed_problems": [],
            }
            # Link each problem to supporting evidence
            for problem in problems:
                problem_entry = {
                    "problem_id": problem.get("problem_id"),
                    "title": problem.get("title"),
                    "severity": problem.get("severity"),
                    "is_root_cause": problem.get("is_root_cause"),
                    "dependencies": problem.get("dependencies", []),
                    "associated_evidence_ids": problem.get("associated_evidence_ids", []),
                }
                chain["addressed_problems"].append(problem_entry)
            provenance_chains.append(chain)

        # Collect seller claim evaluations from evidence store
        seller_claim_states = []
        for ev in context.evidence_store:
            if ev.origin == "ResearcherAgent" and ev.source_type == "seller claim":
                seller_claim_states.append({
                    "claim": ev.supporting_data.get("claim_name"),
                    "evaluated_state": ev.evidence_state,
                    "confidence": ev.confidence,
                    "details": ev.supporting_data.get("evaluation_details"),
                    "evidence_id": ev.evidence_id,
                })

        # Assemble the final report
        report = {
            "audit_id": context.audit_id,
            "diagnosed_branch": context.diagnosed_branch,
            "classification": context.classification,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "problem_dependency_graph": problems,
            "proposed_solutions": provenance_chains,
            "seller_claim_evaluations": seller_claim_states,
            "verification_results": context.verification_results,
            "business_verification": context.business_verification_results,
            "total_evidence_objects": len(context.evidence_store),
            "pipeline_status": context.status,
            "errors": context.errors,
        }

        context.formatter_report = report
        context.status = "complete"
        logger.info(f"Report formatted successfully for audit {context.audit_id}.")
