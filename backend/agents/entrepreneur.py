import json
import logging
from datetime import datetime
from backend.models.audit import AuditContext
from backend.models.evidence import EvidenceObject
from backend.providers.llm_provider import LLMProvider

logger = logging.getLogger("MerchSage.Entrepreneur")

class EntrepreneurAgent:
    def __init__(self, llm_provider: LLMProvider):
        self.llm_provider = llm_provider

    def execute(self, context: AuditContext) -> None:
        logger.info("Executing Entrepreneur Stage (Hypothesis Generation)...")
        
        # Extract classification & context
        classification = context.classification or "Etsy listing"
        branch = context.diagnosed_branch or "Discoverability"
        
        title = ""
        description = ""
        for ev in context.evidence_store:
            if "title" in ev.supporting_data:
                title = ev.supporting_data["title"]
            if "description" in ev.supporting_data:
                description = ev.supporting_data["description"]

        system_instruction = (
            "You are the Entrepreneur Agent for MerchSage, an Etsy listings multi-agent audit system. "
            "Your sole responsibility is to think like a business operator and generate a product-specific "
            "Investigation / Hypothesis Map outlining potential discoverability failure modes. "
            "You MUST ONLY generate hypotheses and list assumptions to be tested by the Researcher. "
            "Do NOT draw any conclusions about whether these hypotheses are true. "
            "Return a valid JSON object matching this schema:\n"
            "{\n"
            "  \"hypotheses\": [\n"
            "    {\n"
            "      \"hypothesis_id\": \"string ID, e.g. H1, H2\",\n"
            "      \"title\": \"short name of hypothesis\",\n"
            "      \"description\": \"why this could be causing underperformance for this category\",\n"
            "      \"assumptions\": [\"list of assumptions to be verified\"]\n"
            "    }\n"
            "  ]\n"
            "}"
        )
        
        prompt = (
            f"Generate a hypothesis map for the following listing:\n"
            f"Category: {classification}\n"
            f"Performance Branch: {branch}\n"
            f"Title: {title}\n"
            f"Description: {description}\n"
        )
        
        response_text = self.llm_provider.generate_text(
            prompt=prompt,
            system_instruction=system_instruction,
            response_schema={
                "type": "OBJECT",
                "properties": {
                    "hypotheses": {
                        "type": "ARRAY",
                        "items": {
                            "type": "OBJECT",
                            "properties": {
                                "hypothesis_id": {"type": "STRING"},
                                "title": {"type": "STRING"},
                                "description": {"type": "STRING"},
                                "assumptions": {
                                    "type": "ARRAY",
                                    "items": {"type": "STRING"}
                                }
                            },
                            "required": ["hypothesis_id", "title", "description", "assumptions"]
                        }
                    }
                },
                "required": ["hypotheses"]
            }
        )
        
        try:
            res = json.loads(response_text)
            context.hypothesis_map = res.get("hypotheses", [])
            
            # Write hypotheses into evidence store
            now_str = datetime.utcnow().isoformat() + "Z"
            for hyp in context.hypothesis_map:
                ev = EvidenceObject(
                    source_type="inference",
                    origin="EntrepreneurAgent",
                    timestamp=now_str,
                    confidence="MEDIUM",
                    evidence_state="UNKNOWN",  # Initially untested
                    provenance=["Diagnosis Context -> EntrepreneurAgent"],
                    supporting_data={
                        "hypothesis": hyp
                    },
                    downstream_consumers=["ResearcherAgent"]
                )
                context.evidence_store.append(ev)
                
            context.status = "hypothesized"
            logger.info(f"Generated {len(context.hypothesis_map)} hypotheses for investigation.")
        except Exception as e:
            logger.error(f"Failed to parse hypothesis map: {response_text}. Error: {e}")
            context.errors.append(f"Entrepreneur hypothesis generation failed: {e}")
            context.status = "error"
