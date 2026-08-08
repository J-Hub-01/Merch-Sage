import logging
from abc import ABC, abstractmethod
from backend.config import GEMINI_MODEL_ID, PROJECT_ID, LOCATION
from backend.providers.llm_mock import get_mock_response

logger = logging.getLogger("MerchSage.LLMProvider")

class LLMProvider(ABC):
    @abstractmethod
    def generate_text(self, prompt: str, system_instruction: str = None, response_schema: dict = None) -> str:
        """
        Generates text using the configured Gemini model.
        Claude is strictly prohibited from being used here.
        """
        pass

class VertexAIGeminiProvider(LLMProvider):
    def __init__(self):
        self.initialized = False
        try:
            import vertexai
            # Initialize Vertex AI. If PROJECT_ID is None, it relies on application default credentials
            vertexai.init(project=PROJECT_ID, location=LOCATION)
            from vertexai.generative_models import GenerativeModel
            self.model = GenerativeModel(
                model_name=GEMINI_MODEL_ID,
                system_instruction=None  # Can be overridden per-call
            )
            self.initialized = True
            logger.info(f"Vertex AI Gemini Provider initialized successfully with model {GEMINI_MODEL_ID}.")
        except Exception as e:
            logger.warning(f"Failed to initialize Vertex AI SDK: {e}. Falling back to developer-mock mode.")

    def generate_text(self, prompt: str, system_instruction: str = None, response_schema: dict = None) -> str:
        if self.initialized:
            try:
                from vertexai.generative_models import GenerativeModel, GenerationConfig
                # If custom system_instruction is provided, we instantiate a temporary model with it
                model_instance = self.model
                if system_instruction:
                    model_instance = GenerativeModel(
                        model_name=GEMINI_MODEL_ID,
                        system_instruction=system_instruction
                    )
                
                config_args = {}
                if response_schema:
                    config_args["response_mime_type"] = "application/json"
                    config_args["response_schema"] = response_schema
                else:
                    # Look for clues in the prompt to see if JSON is expected
                    if "json" in prompt.lower():
                        config_args["response_mime_type"] = "application/json"
                
                generation_config = GenerationConfig(**config_args) if config_args else None
                
                response = model_instance.generate_content(
                    prompt,
                    generation_config=generation_config
                )
                return response.text
            except Exception as e:
                logger.error(f"Vertex AI model call failed: {e}. Attempting developer-mock fallback.")
        
        # Developer-mock fallback mode (shared across all LLMProvider implementations)
        return get_mock_response(prompt, system_instruction)


def get_llm_provider() -> "LLMProvider":
    """
    Factory: returns the active LLMProvider implementation based on
    config.LLM_PROVIDER. This is the ONLY place provider selection
    logic should live -- callers (orchestrator, etc.) should always
    go through this function rather than instantiating a concrete
    provider class directly, so that switching backends (e.g. once
    GCP Billing is restored) is a single config change.
    """
    from backend.config import LLM_PROVIDER

    if LLM_PROVIDER == "ai_studio":
        from backend.providers.llm_provider_aistudio import AIStudioGeminiProvider
        return AIStudioGeminiProvider()
    elif LLM_PROVIDER == "vertex":
        return VertexAIGeminiProvider()
    else:
        logger.warning(
            f"Unrecognized LLM_PROVIDER='{LLM_PROVIDER}'. Defaulting to AI Studio."
        )
        from backend.providers.llm_provider_aistudio import AIStudioGeminiProvider
        return AIStudioGeminiProvider()


