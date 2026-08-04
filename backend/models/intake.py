from pydantic import BaseModel, Field
from typing import List, Optional

class SellerIntakePayload(BaseModel):
    listing_url: str
    seller_differentiators: List[str] = Field(default_factory=list)  # selections like "handmade", "customization", "quality", "price"
    other_differentiator_details: Optional[str] = None  # Free-text "Other" field
    historical_stats_ref: Optional[str] = None  # Reference to CSV stats / fixture identifier
