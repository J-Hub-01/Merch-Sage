import json
import logging
from datetime import datetime
from backend.models.audit import AuditContext
from backend.models.evidence import EvidenceObject
from backend.providers.llm_provider import LLMProvider

logger = logging.getLogger("MerchSage.Classifier")

class ClassifierAgent:
    def __init__(self, llm_provider: LLMProvider):
        self.llm_provider = llm_provider

    def execute(self, context: AuditContext) -> None:
        logger.info("Executing Classification Stage...")
        
        # Extract title and description from evidence store
        title = ""
        description = ""
        for ev in context.evidence_store:
            if "title" in ev.supporting_data:
                title = ev.supporting_data["title"]
            if "description" in ev.supporting_data:
                description = ev.supporting_data["description"]
        
        system_instruction = (
            "You are a Classification Agent for MerchSage, an Etsy listing audit system. "
            "Your task is to identify the product category of the listing based on its title and description. "
            "You must return a valid JSON object matching this schema:\n"
            "{\n"
            "  \"category\": \"string description of the listing category\",\n"
            "  \"confidence\": \"HIGH or MEDIUM or LOW\",\n"
            "  \"reasoning\": \"brief reasoning text\"\n"
            "}"
        )
        
        prompt = (
            f"Please classify the following listing:\n"
            f"Title: {title}\n"
            f"Description: {description}\n"
        )
        
        response_text = self.llm_provider.generate_text(
            prompt=prompt,
            system_instruction=system_instruction,
            response_schema={
                "type": "OBJECT",
                "properties": {
                    "category": {"type": "STRING"},
                    "confidence": {"type": "STRING"},
                    "reasoning": {"type": "STRING"}
                },
                "required": ["category", "confidence", "reasoning"]
            }
        )
        
        try:
            res = json.loads(response_text)
            context.classification = res.get("category", "unknown")
            
            # Create classification evidence object
            now_str = datetime.utcnow().isoformat() + "Z"
            classification_ev = EvidenceObject(
                source_type="inference",
                origin="ClassifierAgent",
                timestamp=now_str,
                confidence=res.get("confidence", "MEDIUM"),
                evidence_state="SUPPORTED",
                provenance=["Marketplace Evidence -> ClassifierAgent"],
                supporting_data={
                    "classified_category": context.classification,
                    "reasoning": res.get("reasoning", "")
                },
                downstream_consumers=["DiagnosisRouterAgent", "EntrepreneurAgent"]
            )
            context.evidence_store.append(classification_ev)
            context.status = "classified"
            logger.info(f"Listing classified as: {context.classification}")
        except Exception as e:
            logger.error(f"Failed to parse classification response: {response_text}. Error: {e}")
            context.errors.append(f"Classification failed: {e}")
            context.status = "error"
