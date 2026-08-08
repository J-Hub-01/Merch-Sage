import logging
from backend.models.audit import AuditContext
from backend.models.intake import SellerIntakePayload
from backend.providers.llm_provider import LLMProvider, get_llm_provider
from backend.providers.marketplace import MarketplaceEvidenceProvider
from backend.providers.historical_stats import HistoricalStatsProvider
from backend.providers.audit_store import AuditStore, LocalJsonAuditStore
from backend.agents.classifier import ClassifierAgent
from backend.agents.diagnosis_router import DiagnosisRouterAgent
from backend.agents.entrepreneur import EntrepreneurAgent
from backend.agents.researcher import ResearcherAgent
from backend.agents.triage import TriageAgent
from backend.agents.seo_specialist import DiscoverabilitySeoCopySpecialist
from backend.agents.business_verifier import BusinessVerifierAgent
from backend.agents.report_formatter import ReportFormatterAgent
from backend.verification.structural import verify_structure
from backend.verification.factual_legal import verify_factual_legal_integrity
from backend.config import MAX_INTERNAL_RETRIES

logger = logging.getLogger("MerchSage.Orchestrator")

# Retry cap for internal corrections per MERCHSAGE_FINAL_WORKING_PIPELINE §10
MAX_RETRIES = 2


def run_audit(intake: SellerIntakePayload) -> dict:
    """
    Executes the full Discoverability vertical slice pipeline sequentially.
    Returns the final structured JSON report.
    """
    logger.info("=== MerchSage Audit Pipeline Started ===")

    # Initialize providers
    llm = get_llm_provider()
    marketplace = MarketplaceEvidenceProvider()
    historical_stats = HistoricalStatsProvider()
    store = LocalJsonAuditStore()

    # Initialize audit context
    context = AuditContext(intake_payload=intake)
    logger.info(f"Audit ID: {context.audit_id}")

    # ── Stage 1: Intake ──────────────────────────────────────────────
    # Seller differentiators are stored as seller-claim evidence,
    # NOT promoted to facts.
    from backend.models.evidence import EvidenceObject
    from datetime import datetime

    now_str = datetime.utcnow().isoformat() + "Z"
    for diff in intake.seller_differentiators:
        ev = EvidenceObject(
            source_type="seller claim",
            origin="Seller Intake Form",
            timestamp=now_str,
            confidence="MEDIUM",
            evidence_state="UNKNOWN",  # Untested until Researcher evaluates
            provenance=["Seller Intake -> Orchestrator"],
            supporting_data={"claimed_differentiator": diff},
            downstream_consumers=["ResearcherAgent"],
        )
        context.evidence_store.append(ev)
    if intake.other_differentiator_details:
        ev = EvidenceObject(
            source_type="seller claim",
            origin="Seller Intake Form",
            timestamp=now_str,
            confidence="MEDIUM",
            evidence_state="UNKNOWN",
            provenance=["Seller Intake -> Orchestrator"],
            supporting_data={"claimed_differentiator": intake.other_differentiator_details},
            downstream_consumers=["ResearcherAgent"],
        )
        context.evidence_store.append(ev)
    context.status = "intake_complete"

    # ── Stage 2: Evidence Collection ─────────────────────────────────
    # Two separate providers with distinct source boundaries.
    marketplace_evidence = marketplace.get_listing_evidence(intake.listing_url)
    context.evidence_store.extend(marketplace_evidence)

    stats_ref = intake.historical_stats_ref or "default_fixture"
    stats_evidence = historical_stats.get_historical_stats_evidence(stats_ref)
    context.evidence_store.extend(stats_evidence)
    context.status = "evidence_collected"
    logger.info(f"Collected {len(context.evidence_store)} evidence objects.")

    # ── Stage 3: Classification ──────────────────────────────────────
    classifier = ClassifierAgent(llm)
    classifier.execute(context)
    if context.status == "error":
        logger.error("Pipeline aborted at Classification.")
        store.save_context(context)
        return context.formatter_report or {"error": "Classification failed", "errors": context.errors}

    # ── Stage 4: Diagnosis Routing ───────────────────────────────────
    # Consumes HistoricalStatsProvider Evidence Objects, NOT a raw int.
    router = DiagnosisRouterAgent()
    router.execute(context)
    if context.status == "error":
        logger.error("Pipeline aborted at Diagnosis Routing.")
        store.save_context(context)
        return context.formatter_report or {"error": "Diagnosis routing failed", "errors": context.errors}

    # ── Stage 5: Entrepreneur ────────────────────────────────────────
    entrepreneur = EntrepreneurAgent(llm)
    entrepreneur.execute(context)
    if context.status == "error":
        logger.error("Pipeline aborted at Entrepreneur.")
        store.save_context(context)
        return context.formatter_report or {"error": "Entrepreneur failed", "errors": context.errors}

    # ── Stage 6: Researcher ──────────────────────────────────────────
    researcher = ResearcherAgent(llm)
    researcher.execute(context)
    if context.status == "error":
        logger.error("Pipeline aborted at Researcher.")
        store.save_context(context)
        return context.formatter_report or {"error": "Researcher failed", "errors": context.errors}

    # ── Stage 7: Triage ──────────────────────────────────────────────
    triage = TriageAgent(llm)
    triage.execute(context)
    if context.status == "error":
        logger.error("Pipeline aborted at Triage.")
        store.save_context(context)
        return context.formatter_report or {"error": "Triage failed", "errors": context.errors}

    # ── Stage 8+9: SEO Specialist + Verification (with retry loop) ──
    seo = DiscoverabilitySeoCopySpecialist(llm)

    for attempt in range(1 + MAX_RETRIES):
        logger.info(f"SEO Specialist attempt {attempt + 1}/{1 + MAX_RETRIES}")

        # Clear previous attempt's solutions and verification if retrying
        if attempt > 0:
            context.specialist_solutions = []
            context.verification_results = None

        seo.execute(context)
        if context.status == "error":
            logger.error("Pipeline aborted at SEO Specialist.")
            break

        # Run deterministic verification
        proposed_title = ""
        proposed_tags = []
        if context.specialist_solutions:
            latest = context.specialist_solutions[-1]
            proposed_title = latest.get("proposed_title", "")
            proposed_tags = latest.get("proposed_tags", [])

        structural_result = verify_structure(proposed_title, proposed_tags)
        legal_result = verify_factual_legal_integrity(context, proposed_title, proposed_tags)

        context.verification_results = {
            "structural": structural_result,
            "factual_legal": legal_result,
        }

        all_passed = structural_result["passed"] and legal_result["passed"]

        if all_passed:
            logger.info("Verification passed on all checks.")
            break
        else:
            all_errors = structural_result.get("errors", []) + legal_result.get("errors", [])
            logger.warning(
                f"Verification failed (attempt {attempt + 1}): {all_errors}"
            )
            if attempt < MAX_RETRIES:
                # Feed failure context back for the next specialist attempt
                context.errors.append(
                    f"Verification attempt {attempt + 1} failed: {all_errors}"
                )
            else:
                logger.warning("Max retries exhausted. Proceeding with flagged issues.")

    # ── Stage 9.5: Supervisor/QC ──────────────────────────────────────
    from backend.agents.supervisor import SupervisorAgent
    supervisor = SupervisorAgent()
    supervisor.execute(context)
    if context.status == "error":
        logger.error("Pipeline aborted at Supervisor/QC Stage.")
        store.save_context(context)
        return context.formatter_report or {"error": "Supervisor QC failed", "errors": context.errors}

    # ── Stage 10: Business Verifier ──────────────────────────────────
    verifier = BusinessVerifierAgent(llm)
    verifier.execute(context)

    # ── Stage 11: Report Formatter ───────────────────────────────────
    formatter = ReportFormatterAgent()
    formatter.execute(context)

    # Persist to local JSON store
    store.save_context(context)

    logger.info("=== MerchSage Audit Pipeline Complete ===")
    return context.formatter_report
