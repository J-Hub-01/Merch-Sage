from typing import List
from datetime import datetime
from backend.models.evidence import EvidenceObject

class HistoricalStatsProvider:
    """
    Simulates parsing and returning seller-provided Etsy Stats CSV metrics.
    Source type is always 'seller_provided_stats'.
    Used exclusively for traffic and discoverability statistics.
    """
    def __init__(self):
        pass

    def get_historical_stats_evidence(self, stats_ref: str) -> List[EvidenceObject]:
        # Returns mock statistics representing low/declining views
        now_str = datetime.utcnow().isoformat() + "Z"

        # Simulates parsed rows of Etsy Stats CSV
        stats_payload = {
            "views_time_series": [
                {"date": "2026-07-01", "views": 10},
                {"date": "2026-07-15", "views": 5},
                {"date": "2026-08-01", "views": 2}
            ],
            "total_views": 17,
            "total_visits": 5,
            "traffic_sources": {
                "etsy_search": 1,
                "direct": 3,
                "social_media": 1
            }
        }

        evidence_list = []
        for metric, value in stats_payload.items():
            ev = EvidenceObject(
                source_type="seller_provided_stats",
                origin="Seller Uploaded Etsy Stats CSV",
                timestamp=now_str,
                confidence="CONFIRMED",
                evidence_state="SUPPORTED",
                provenance=["Seller CSV Upload -> HistoricalStatsProvider"],
                supporting_data={metric: value},
                downstream_consumers=[]
            )
            evidence_list.append(ev)

        return evidence_list
