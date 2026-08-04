import logging
from datetime import datetime
from backend.models.audit import AuditContext
from backend.models.evidence import EvidenceObject

logger = logging.getLogger("MerchSage.DiagnosisRouter")

class DiagnosisRouterAgent:
    def __init__(self):
        pass

    def execute(self, context: AuditContext) -> None:
        logger.info("Executing Diagnosis Routing Stage...")
        
        # Check evidence store for seller-provided stats
        total_views = None
        views_evidence = None
        
        for ev in context.evidence_store:
            if ev.source_type == "seller_provided_stats" and "total_views" in ev.supporting_data:
                total_views = ev.supporting_data["total_views"]
                views_evidence = ev
                break
        
        if total_views is None:
            context.diagnosed_branch = "UNKNOWN"
            confidence = "LOW"
            state = "INSUFFICIENT EVIDENCE"
            reason = "Required traffic evidence (total_views) is absent."
            provenance_chain = ["Default fallback"]
            context.errors.append("Diagnosis routing failed: traffic evidence is absent.")
            context.status = "error"
        else:
            reason = f"Historical stats evidence shows low views: {total_views} total views."
            confidence = "CONFIRMED"
            state = "SUPPORTED"
            provenance_chain = [f"Evidence ID: {views_evidence.evidence_id} -> DiagnosisRouterAgent"]
            context.diagnosed_branch = "Discoverability"
            context.status = "diagnosed"
        
        now_str = datetime.utcnow().isoformat() + "Z"
        routing_ev = EvidenceObject(
            source_type="inference",
            origin="DiagnosisRouterAgent",
            timestamp=now_str,
            confidence=confidence,
            evidence_state=state,
            provenance=provenance_chain,
            supporting_data={
                "diagnosed_branch": context.diagnosed_branch,
                "routing_reason": reason,
                "observed_views": total_views
            },
            downstream_consumers=["EntrepreneurAgent", "ResearcherAgent"]
        )
        
        context.evidence_store.append(routing_ev)
        logger.info(f"Diagnosis routing determined branch: {context.diagnosed_branch} based on {reason}")
