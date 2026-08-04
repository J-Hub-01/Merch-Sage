from typing import Dict, Any, List

def verify_structure(proposed_title: str, proposed_tags: List[str]) -> Dict[str, Any]:
    """
    Deterministic structural validation for SEO Specialist outputs.
    No LLM is used.
    """
    passed = True
    errors = []
    
    # 1. Title length check (Etsy title length limit is 140 chars)
    if len(proposed_title) > 140:
        passed = False
        errors.append(f"Title exceeds 140 characters (actual length: {len(proposed_title)}).")
        
    # 2. Tag count check (Etsy allows up to 13 tags)
    if len(proposed_tags) > 13:
        passed = False
        errors.append(f"Tag count exceeds 13 tags limit (actual count: {len(proposed_tags)}).")
    elif len(proposed_tags) < 13:
        # A warning or failure depending on strictness - let's flag as a warning/failure
        passed = False
        errors.append(f"Tag count is less than 13 tags (actual count: {len(proposed_tags)}).")

    # 3. Duplicate tags check
    seen = set()
    duplicates = []
    for tag in proposed_tags:
        normalized_tag = tag.strip().lower()
        if normalized_tag in seen:
            duplicates.append(tag)
        else:
            seen.add(normalized_tag)
            
    if duplicates:
        passed = False
        errors.append(f"Duplicate tags detected: {list(set(duplicates))}.")
        
    # 4. Individual tag length check (Etsy tags limit is 20 chars)
    for tag in proposed_tags:
        if len(tag) > 20:
            passed = False
            errors.append(f"Tag '{tag}' exceeds 20 characters limit.")

    return {
        "passed": passed,
        "errors": errors,
        "metadata": {
            "title_length": len(proposed_title),
            "tag_count": len(proposed_tags),
            "unique_tag_count": len(seen)
        }
    }
