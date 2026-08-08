from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from backend.models.evidence import EvidenceObject
from backend.models.intake import SellerIntakePayload
import uuid

class AuditContext(BaseModel):
    audit_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    intake_payload: SellerIntakePayload
    evidence_store: List[EvidenceObject] = Field(default_factory=list)
    classification: Optional[str] = None
    diagnosed_branch: Optional[str] = None  # e.g., "Discoverability"
    hypothesis_map: List[Dict[str, Any]] = Field(default_factory=list)  # Set by Entrepreneur Agent
    triage_results: Optional[Dict[str, Any]] = None  # Set by Triage Agent
    specialist_solutions: List[Dict[str, Any]] = Field(default_factory=list)  # Set by SEO Specialist
    verification_results: Optional[Dict[str, Any]] = None  # Domain-Specific Verification
    business_verification_results: Optional[Dict[str, Any]] = None  # Business Verifier
    formatter_report: Optional[Dict[str, Any]] = None  # Final output
    status: str = "intake"
    errors: List[str] = Field(default_factory=list)
    active_llm_provider: Optional[str] = None  # e.g. "AIStudioGeminiProvider (live)" or "VertexAIGeminiProvider (mock fallback)"
