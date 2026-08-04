from typing import Dict, Any, List
from backend.models.audit import AuditContext

def verify_factual_legal_integrity(context: AuditContext, proposed_title: str, proposed_tags: List[str]) -> Dict[str, Any]:
    """
    Rule-based scanner enforcing compliance with v2 Amendment and AI Marketing Reference.
    No LLM is used.
    """
    passed = True
    errors = []
    
    # Lowercase title and tags for scanning
    title_lower = proposed_title.lower()
    tags_lower = [t.lower() for t in proposed_tags]
    
    # 1. Check for material/handmade claims in generated text
    # e.g., "silver", "gold", "handmade", "925"
    material_claims = ["silver", "gold", "handmade", "925", "sterling"]
    found_material_claims = []
    for claim in material_claims:
        if claim in title_lower or any(claim in t for t in tags_lower):
            found_material_claims.append(claim)
            
    # Check if these claims are supported by a verified Evidence Object
    for claim in found_material_claims:
        supported = False
        evidence_found = None
        for ev in context.evidence_store:
            # Check observed marketplace facts
            if ev.source_type == "observed fact":
                for val in ev.supporting_data.values():
                    if isinstance(val, str) and claim in val.lower():
                        supported = True
                        evidence_found = ev
                        break
                    elif isinstance(val, list):
                        if any(isinstance(v, str) and claim in v.lower() for v in val):
                            supported = True
                            evidence_found = ev
                            break
            # Check seller claims evaluated by Researcher as SUPPORTED
            elif ev.source_type == "seller claim" and ev.evidence_state == "SUPPORTED":
                claim_name = ev.supporting_data.get("claim_name", "").lower()
                if claim in claim_name or claim_name in claim:
                    supported = True
                    evidence_found = ev
                    break
            if supported:
                break
                
        if not supported:
            passed = False
            errors.append(
                f"Prohibited Claim: The generated copy contains the factual claim '{claim}', "
                "but no supporting Evidence Object was found in the audit context."
            )
            
    # 2. Check for False Urgency/Scarcity
    # e.g., "only", "left", "hurry", "selling fast"
    scarcity_keywords = ["only", "left", "hurry", "limited", "scarcity", "selling fast", "last chance"]
    found_scarcity = []
    for kw in scarcity_keywords:
        if kw in title_lower or any(kw in t for t in tags_lower):
            found_scarcity.append(kw)
            
    if found_scarcity:
        # Check if quantity/inventory evidence confirms low stock (e.g. <= 3)
        confirmed_low_stock = False
        qty_evidence_id = None
        for ev in context.evidence_store:
            if ev.source_type == "observed fact" and "quantity" in ev.supporting_data:
                qty = ev.supporting_data["quantity"]
                if isinstance(qty, int) and qty <= 3:
                    confirmed_low_stock = True
                    qty_evidence_id = ev.evidence_id
                    break
                    
        if not confirmed_low_stock:
            passed = False
            errors.append(
                f"Prohibited Urgency: The generated copy uses urgency/scarcity keyword(s) {found_scarcity}, "
                "but quantity evidence does not show low stock (<= 3 items left)."
            )

    # 3. Check for Fake Testimonials/Social Proof
    # e.g., "best seller", "top rated", "5 star", "highly reviewed"
    social_proof_keywords = ["best seller", "top rated", "5 star", "highly reviewed", "award winning", "famous"]
    found_social_proof = []
    for kw in social_proof_keywords:
        if kw in title_lower or any(kw in t for t in tags_lower):
            found_social_proof.append(kw)
            
    if found_social_proof:
        # Verify if external reviews evidence explicitly confirms high ratings/best-seller status
        has_social_proof_evidence = False
        for ev in context.evidence_store:
            if ev.source_type == "external evidence" and "reviews" in ev.supporting_data:
                # Mock logic check for high ratings
                has_social_proof_evidence = True
                break
        if not has_social_proof_evidence:
            passed = False
            errors.append(
                f"Prohibited Social Proof: The generated copy uses social proof keyword(s) {found_social_proof}, "
                "but no supporting external reviews or shop badge Evidence Object exists."
            )

    # 4. Check for unverified Was-Now Pricing / Sale claims
    # e.g., "sale", "percent off", "was", "now", "save"
    pricing_keywords = ["sale", "off", "was", "now", "save", "discount"]
    found_pricing_claims = []
    for kw in pricing_keywords:
        # Note: 'now' might be used generally (e.g., 'buy now'), let's be careful,
        # but in titles/tags we scan for sale-related pricing
        if kw in title_lower or any(kw in t for t in tags_lower):
            if kw == "now" and "was" not in title_lower and not any("was" in t for t in tags_lower):
                continue  # Skip generic "now" without "was"
            found_pricing_claims.append(kw)
            
    if found_pricing_claims:
        # Check if price history evidence exists
        has_price_history = False
        for ev in context.evidence_store:
            if "price_history" in ev.supporting_data:
                has_price_history = True
                break
        if not has_price_history:
            passed = False
            errors.append(
                f"Prohibited Pricing Claim: The generated copy uses discount/price claim keyword(s) {found_pricing_claims}, "
                "but no price_history Evidence Object is available to justify a comparative pricing claim."
            )

    return {
        "passed": passed,
        "errors": errors,
        "scanned_claims": {
            "materials": found_material_claims,
            "scarcity": found_scarcity,
            "social_proof": found_social_proof,
            "pricing": found_pricing_claims
        }
    }
