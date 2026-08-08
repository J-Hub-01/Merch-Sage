import json

"""
Shared developer-mock response logic for LLMProvider implementations.

Extracted from VertexAIGeminiProvider so that every concrete provider
(Vertex AI, AI Studio, or any future backend) falls back to the same
mock behavior on init/call failure, instead of maintaining separate
copies that can silently drift apart.

This module contains NO live model calls. It is pure, deterministic
mock data selection based on agent-identifying text in the prompt or
system instruction.
"""


def get_mock_response(prompt: str, system_instruction: str = None) -> str:
    """
    Provides structured mock responses for development/sandbox mode
    when a provider's live credentials are not active or a call fails.

    Behavior is byte-identical to the original
    VertexAIGeminiProvider._get_mock_response implementation.
    """
    sys_inst = (system_instruction or "").lower()
    combined_text = (prompt + " " + sys_inst).lower()

    # 1. Determine agent type deterministically using system instruction signatures
    if "classification agent" in sys_inst:
        agent_type = "classifier"
    elif "entrepreneur agent" in sys_inst:
        agent_type = "entrepreneur"
    elif "researcher agent" in sys_inst:
        agent_type = "researcher"
    elif "triage agent" in sys_inst:
        agent_type = "triage"
    elif "seo specialist agent" in sys_inst:
        agent_type = "seo_specialist"
    elif "business verifier agent" in sys_inst:
        agent_type = "business_verifier"
    else:
        # Fallback to substring heuristic matching on combined text
        if "classification agent" in combined_text or "classification" in combined_text:
            agent_type = "classifier"
        elif "entrepreneur agent" in combined_text:
            agent_type = "entrepreneur"
        elif "researcher agent" in combined_text:
            agent_type = "researcher"
        elif "triage agent" in combined_text:
            agent_type = "triage"
        elif "seo specialist agent" in combined_text or "seo specialist" in combined_text:
            agent_type = "seo_specialist"
        elif "business verifier agent" in combined_text or "verifier" in combined_text:
            agent_type = "business_verifier"
        elif "classify" in combined_text:
            agent_type = "classifier"
        else:
            agent_type = "unknown"

    # Classifier Agent Mock Response
    if agent_type == "classifier":
        return json.dumps({
            "category": "personalized handmade jewelry",
            "confidence": "HIGH",
            "reasoning": "Mock classification based on listing title and description."
        })

    # Entrepreneur Agent Mock Response
    if agent_type == "entrepreneur":
        return json.dumps({
            "hypotheses": [
                {
                    "hypothesis_id": "H1",
                    "title": "Keyword mismatch with buyer search intent",
                    "description": "The listing uses generic tags like 'gift' rather than specific search queries like 'custom name necklace'.",
                    "assumptions": ["Buyers are searching for specific customized products", "Listing ranks poorly for personalized terms"]
                },
                {
                    "hypothesis_id": "H2",
                    "title": "Unverified seller quality claim",
                    "description": "Seller claims 'highest quality premium silver' but customer reviews indicate tarnishing issues.",
                    "assumptions": ["Customer reviews exist", "Reviews criticize material quality"]
                }
            ]
        })

    # Researcher Agent Mock Response
    if agent_type == "researcher":
        return json.dumps({
            "hypothesis_evaluations": [
                {
                    "hypothesis_id": "H1",
                    "state": "CONFIRMED",
                    "confidence": "HIGH",
                    "details": "Listing tags do not contain primary search keywords found in search intent data."
                },
                {
                    "hypothesis_id": "H2",
                    "state": "REFUTED",
                    "confidence": "MEDIUM",
                    "details": "Customer reviews show 95% praise for material quality and durability. Tarnishing is not a cluster."
                }
            ],
            "seller_claim_evaluations": [
                {
                    "claim": "handmade craftsmanship",
                    "state": "SUPPORTED",
                    "confidence": "HIGH",
                    "details": "Listing description details production process; customer reviews confirm authentic handmade quality."
                },
                {
                    "claim": "fast shipping",
                    "state": "CONTRADICTED",
                    "confidence": "MEDIUM",
                    "details": "Etsy stats show average shipping delay of 4 days; 3 reviews complain about delivery speed."
                }
            ]
        })

    # Triage Agent Mock Response
    if agent_type == "triage":
        return json.dumps({
            "problems": [
                {
                    "problem_id": "P1",
                    "title": "Keyword mismatch in tags and titles",
                    "severity": "CRITICAL",
                    "is_root_cause": True,
                    "dependencies": [],
                    "description": "The search terms do not match user intent, leading to zero discoverability.",
                    "associated_evidence_ids": ["E1"]
                },
                {
                    "problem_id": "P2",
                    "title": "Slow delivery performance",
                    "severity": "MEDIUM",
                    "is_root_cause": False,
                    "dependencies": ["P1"],
                    "description": "Low customer retention due to delivery delays, though discoverability is the primary barrier.",
                    "associated_evidence_ids": ["E2"]
                }
            ]
        })

    # SEO Specialist Mock Response
    if agent_type == "seo_specialist":
        return json.dumps({
            "proposed_title": "Custom Name Necklace - Handmade Personalized Silver Jewelry - Mother's Day Gift",
            "proposed_tags": [
                "custom name necklace", "handmade necklace", "personalized jewelry", "silver nameplate",
                "mothers day gift", "custom name jewelry", "engraved necklace", "gift for her",
                "sterling silver 925", "dainty nameplate", "personalized gift", "custom jewelry", "monogram necklace"
            ],
            "justification": "Optimized to target primary search queries with high intent.",
            "claims_made": [
                "Sterling silver 925 composition confirmed by description evidence",
                "Handmade craftsmanship verified by supported seller claims"
            ]
        })

    # Business Verifier Mock Response
    if agent_type == "business_verifier":
        return json.dumps({
            "is_compatible": True,
            "conflicts": [],
            "evaluations": [
                {
                    "solution_ref": "custom name necklace",
                    "status": "APPROVED",
                    "justification": "Directly resolves P1 (keyword mismatch) and aligns with supported seller claims."
                }
            ]
        })

    return json.dumps({"response": "Mock default response."})
