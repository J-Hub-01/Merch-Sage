from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional
from datetime import datetime
import uuid

class EvidenceObject(BaseModel):
    evidence_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    source_type: str  # "observed fact", "seller claim", "external evidence", "inference"
    origin: str  # e.g., "Etsy API Listings Endpoint", "Seller CSV Upload", "Researcher Agent"
    timestamp: str  # ISO-8601 string when observed/collected
    confidence: str  # e.g., "HIGH", "MEDIUM", "LOW", "CONFIRMED", "LIKELY", "INCONCLUSIVE", "REFUTED", "UNKNOWN"
    evidence_state: str  # "SUPPORTED", "CONTRADICTED", "MIXED", "UNKNOWN", "INSUFFICIENT EVIDENCE"
    provenance: List[str] = Field(default_factory=list)  # Chain back to origin
    supporting_data: Dict[str, Any] = Field(default_factory=dict)  # Underlying text, field value, etc.
    downstream_consumers: List[str] = Field(default_factory=list)  # Citing agents/solutions
