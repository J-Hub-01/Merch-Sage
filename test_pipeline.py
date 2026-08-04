import json
import logging
from backend.models.intake import SellerIntakePayload
from backend.pipeline.orchestrator import run_audit

logging.basicConfig(level=logging.INFO)

def main():
    print("Executing End-to-End Vertical Slice Test...")
    
    intake = SellerIntakePayload(
        listing_url="https://www.etsy.com/listing/123456789/custom-name-necklace",
        seller_differentiators=["handmade craftsmanship", "quality"],
        other_differentiator_details="Fast shipping within 24 hours",
        historical_stats_ref="fixture_low_views_csv"
    )
    
    report = run_audit(intake)
    
    print("\n================ FINAL AUDIT REPORT ================")
    print(json.dumps(report, indent=2))
    print("====================================================\n")

if __name__ == "__main__":
    main()
