from typing import List
from datetime import datetime
from backend.models.evidence import EvidenceObject

class MarketplaceEvidenceProvider:
    """
    Simulates fetching listing data from Etsy API.
    Strictly restricted to Matrix-confirmed fields.
    Does NOT contain views, visits, or traffic history.
    """
    def __init__(self):
        pass

    def get_listing_evidence(self, listing_url: str) -> List[EvidenceObject]:
        # Returns mock/fixture data matching the matrix-confirmed fields
        now_str = datetime.utcnow().isoformat() + "Z"
        
        # Supporting data restricted strictly to:
        # title, description, tags, price, quantity, taxonomy_id, images, creation_tsz, listing state, shop info
        data_payload = {
            "title": "Shiny custom name necklace for mother day",
            "description": "Beautiful premium 925 sterling silver custom nameplate necklace. Handmade craftsmanship with care.",
            "tags": ["necklace", "gift", "mother day", "jewelry", "silver", "nameplate"],

            "price": "29.99",
            "quantity": 10,
            "taxonomy_id": 1234,
            "images": ["https://img.etsy.com/mock-necklace-1.jpg"],
            "creation_tsz": "2026-07-01T12:00:00Z",
            "listing_state": "active",
            "shop_info": {
                "shop_name": "JayHandmadeJewelry",
                "total_active_listings": 45
            }
        }

        # Build evidence objects for each confirmed field
        evidence_list = []
        for field, value in data_payload.items():
            ev = EvidenceObject(
                source_type="observed fact",
                origin="Etsy API Listings Endpoint",
                timestamp=now_str,
                confidence="CONFIRMED",
                evidence_state="SUPPORTED",
                provenance=["Etsy API -> MarketplaceEvidenceProvider"],
                supporting_data={field: value},
                downstream_consumers=[]
            )
            evidence_list.append(ev)

        return evidence_list
