import logging
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional
from backend.models.intake import SellerIntakePayload
from backend.pipeline.orchestrator import run_audit

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s] %(levelname)s: %(message)s")

app = FastAPI(
    title="MerchSage Audit API",
    description="Discoverability branch vertical slice — fixture-backed pipeline.",
    version="0.1.0",
)


class AuditRequest(BaseModel):
    listing_url: str
    seller_differentiators: List[str] = Field(default_factory=list)
    other_differentiator_details: Optional[str] = None
    historical_stats_ref: Optional[str] = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/audit")
def create_audit(request: AuditRequest):
    """
    Runs the full Discoverability audit pipeline and returns
    the structured JSON report.
    """
    intake = SellerIntakePayload(
        listing_url=request.listing_url,
        seller_differentiators=request.seller_differentiators,
        other_differentiator_details=request.other_differentiator_details,
        historical_stats_ref=request.historical_stats_ref,
    )
    report = run_audit(intake)
    return report
