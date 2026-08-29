import logging
from datetime import datetime
from backend.models.audit import AuditContext

logger = logging.getLogger("MerchSage.ReportFormatter")


def _derive_final_status(context: AuditContext) -> str:
    """
    Derives the customer-facing pipeline_status independently of
    context.status's internal per-stage bookkeeping value.

    context.status is used elsewhere purely as a per-stage progress/
    abort marker ("intake_complete", "evidence_collected", "error", the
    upstream-agent-specific "qc_verified"/"verified" values) -- it was
    never designed to answer "was the final audit result actually a
    full, non-degraded, verification-clean success?" BusinessVerifier's
    own context.status = "verified" reflects only whether ITS OWN
    independent business-compatibility call parsed successfully; it has
    no visibility into verification_results or any specialist solution's
    degraded flag, so it cannot answer that question either.

    This function is the single, deterministic place that combines all
    four signals actually needed:

      - context.status == "error"      -> a mandatory stage failed
                                           outright (e.g. BusinessVerifier
                                           itself couldn't parse a
                                           response) -> "failed"
      - any specialist solution has
        degraded=True                  -> a safe fallback was used
                                           (e.g. the 0011 Gemini-quota
                                           fallback) instead of a live
                                           AI-generated result -> "degraded"
      - any evidence_store entry has
        supporting_data.degraded=True  -> a safe fallback was used by
                                           a stage whose degraded marker
                                           lives on its own evidence
                                           object rather than on
                                           specialist_solutions (e.g.
                                           Triage's 0019 fallback, or
                                           BusinessVerifier's own quota-
                                           exhaustion fallback, which
                                           leaves business_verification_
                                           results unset and cannot be
                                           detected any other way) ->
                                           "degraded". This is the same
                                           degraded/degradation_reason
                                           marker convention SEO (0011)
                                           already writes into its own
                                           evidence object alongside
                                           specialist_solutions -- this
                                           check generalizes detection to
                                           that shared convention rather
                                           than adding a stage-specific
                                           special case.
      - any verification_results entry
        has passed=False               -> the generated content did not
                                           cleanly pass domain
                                           verification, even though the
                                           pipeline proceeded with
                                           flagged issues -> "degraded"
      - none of the above              -> "success"

    Deliberately conservative: if verification_results is missing
    entirely in a case that isn't already caught by context.status ==
    "error" (not expected to occur given current orchestrator control
    flow, but not assumed here), this treats that as "degraded" rather
    than silently defaulting to "success".
    """
    if context.status == "error":
        return "failed"

    any_degraded = any(
        isinstance(sol, dict) and sol.get("degraded") is True
        for sol in (context.specialist_solutions or [])
    )
    if any_degraded:
        return "degraded"

    any_degraded_evidence = any(
        isinstance(ev.supporting_data, dict) and ev.supporting_data.get("degraded") is True
        for ev in (context.evidence_store or [])
    )
    if any_degraded_evidence:
        return "degraded"

    vr = context.verification_results
    if not vr:
        return "degraded"

    any_failed_check = any(
        isinstance(check, dict) and check.get("passed") is False
        for check in vr.values()
    )
    if any_failed_check:
        return "degraded"

    return "success"


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
            "pipeline_status": _derive_final_status(context),
            "errors": context.errors,
        }

        context.formatter_report = report
        context.status = "complete"
        logger.info(f"Report formatted successfully for audit {context.audit_id}.")
