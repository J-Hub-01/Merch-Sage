import re
import logging
from typing import List, Optional
from datetime import datetime
import requests
from backend.models.evidence import EvidenceObject
from backend.config import ETSY_API_GATING, ETSY_API_KEY

logger = logging.getLogger("MerchSage.MarketplaceEvidenceProvider")

ETSY_LISTING_URL_PATTERN = re.compile(r"etsy\.com/listing/(\d+)")
ETSY_API_BASE = "https://openapi.etsy.com/v3/application"


class MarketplaceEvidenceProvider:
    """
    Fetches seller own-listing data from Etsy's public-auth getListing
    endpoint (API key only, no OAuth required for active listings --
    confirmed HIGH confidence per ETSY_EVIDENCE_CAPABILITY_MATRIX.md).

    Scope is deliberately restricted to seller own-listing retrieval.
    Does NOT contain views history, competitor data, or any traffic
    time-series -- none of that is exposed by the Etsy API at any tier.

    Mapped fields: title, description, tags, quantity, listing_state,
    price, creation_tsz. taxonomy_id, images, and shop_info remain
    deferred:
      TODO(taxonomy_id): add once a taxonomy-name-resolution lookup
        (Etsy's getSellerTaxonomyNodes) is implemented -- a raw
        integer ID has no semantic value to the LLM on its own.
      TODO(images): add once a multimodal step exists to consume it --
        generate_text() is currently text-only, so an image URL string
        is unusable context.
      TODO(shop_info): add once getShop is implemented -- the prior
        fixture fabricated a shop name/listing count with no backing
        API call, which is worse than omitting the field.

    Gated by config.ETSY_API_GATING (default True == fixture-only),
    consistent with the AI/ML-content compliance concern documented in
    the project's own Evidence Capability Matrix: real Etsy content
    should not reach Gemini until Etsy's written authorization
    question is resolved.
    """

    def __init__(self):
        pass

    def get_listing_evidence(self, listing_url: str) -> List[EvidenceObject]:
        if ETSY_API_GATING:
            return self._get_fixture_evidence(listing_url)
        return self._get_live_evidence(listing_url)

    # ------------------------------------------------------------------
    # Live path
    # ------------------------------------------------------------------

    def _get_live_evidence(self, listing_url: str) -> List[EvidenceObject]:
        listing_id = self._parse_listing_id(listing_url)
        if listing_id is None:
            logger.error(f"Could not parse a listing ID from URL: {listing_url}")
            return self._get_fixture_evidence(listing_url)

        if not ETSY_API_KEY:
            logger.error("ETSY_API_GATING is False but ETSY_API_KEY is not set. Falling back to fixture data.")
            return self._get_fixture_evidence(listing_url)

        try:
            resp = requests.get(
                f"{ETSY_API_BASE}/listings/{listing_id}",
                headers={"x-api-key": ETSY_API_KEY},
                timeout=10,
            )
            resp.raise_for_status()
            listing = resp.json()
        except requests.exceptions.HTTPError as e:
            status = e.response.status_code if e.response is not None else None
            logger.error(f"Etsy getListing HTTP error for listing_id={listing_id}: status={status}. Falling back to fixture data.")
            return self._get_fixture_evidence(listing_url)
        except requests.exceptions.Timeout:
            logger.error(f"Etsy getListing timed out for listing_id={listing_id}. Falling back to fixture data.")
            return self._get_fixture_evidence(listing_url)
        except Exception as e:
            logger.error(f"Etsy getListing call failed for listing_id={listing_id}: {e}. Falling back to fixture data.")
            return self._get_fixture_evidence(listing_url)

        # Response validation: don't build EvidenceObjects from a response
        # missing fields the pipeline actually depends on. Fail safe to
        # fixture rather than propagate partial/malformed evidence.
        if not listing.get("title") or not listing.get("description"):
            logger.error(
                f"Etsy getListing response for listing_id={listing_id} is missing required "
                f"fields (title/description). Falling back to fixture data."
            )
            return self._get_fixture_evidence(listing_url)

        data_payload = {
            "title": listing.get("title"),
            "description": listing.get("description"),
            "tags": listing.get("tags", []),
            "quantity": listing.get("quantity"),
            "listing_state": listing.get("state"),
            "price": self._format_price(listing.get("price")),
            "creation_tsz": listing.get("created_timestamp"),
        }

        return self._build_evidence_list(data_payload, origin="Etsy API Listings Endpoint (live)")

    # ------------------------------------------------------------------
    # Fixture path (unchanged behavior from prior implementation)
    # ------------------------------------------------------------------

    def _get_fixture_evidence(self, listing_url: str) -> List[EvidenceObject]:
        data_payload = {
            "title": "Shiny custom name necklace for mother day",
            "description": "Beautiful premium 925 sterling silver custom nameplate necklace. Handmade craftsmanship with care.",
            "tags": ["necklace", "gift", "mother day", "jewelry", "silver", "nameplate"],
            "quantity": 10,
            "listing_state": "active",
            "price": "29.99",
            "creation_tsz": "2026-07-01T12:00:00Z",
        }
        return self._build_evidence_list(data_payload, origin="Etsy API Listings Endpoint")

    # ------------------------------------------------------------------
    # Shared helpers
    # ------------------------------------------------------------------

    def _parse_listing_id(self, listing_url: str) -> Optional[str]:
        match = ETSY_LISTING_URL_PATTERN.search(listing_url)
        return match.group(1) if match else None

    def _format_price(self, price_obj: Optional[dict]) -> Optional[str]:
        """
        Etsy's price field is a Money object: {amount, divisor, currency_code}.
        Formats it into a plain decimal string (e.g. "29.99") to match the
        fixture's shape, so downstream consumers see one consistent format
        regardless of live vs. fixture source.
        """
        if not price_obj:
            return None
        try:
            amount = price_obj.get("amount")
            divisor = price_obj.get("divisor", 100)
            if amount is None or not divisor:
                return None
            return f"{amount / divisor:.2f}"
        except (TypeError, ZeroDivisionError):
            return None

    def _build_evidence_list(self, data_payload: dict, origin: str) -> List[EvidenceObject]:
        now_str = datetime.utcnow().isoformat() + "Z"
        evidence_list = []
        for field, value in data_payload.items():
            ev = EvidenceObject(
                source_type="observed fact",
                origin=origin,
                timestamp=now_str,
                confidence="CONFIRMED",
                evidence_state="SUPPORTED",
                provenance=["Etsy API -> MarketplaceEvidenceProvider"],
                supporting_data={field: value},
                downstream_consumers=[]
            )
            evidence_list.append(ev)
        return evidence_list
