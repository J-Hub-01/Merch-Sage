import logging
from backend.config import GEMINI_MODEL_ID, GEMINI_API_KEY
from backend.providers.llm_provider import LLMProvider
from backend.providers.llm_mock import get_mock_response

logger = logging.getLogger("MerchSage.LLMProvider.AIStudio")


class AIStudioGeminiProvider(LLMProvider):
    """
    Gemini API via Google AI Studio (google-genai SDK), authenticated
    with a plain API key -- no GCP billing account, no ADC, no Vertex
    project/location required.

    Implements the exact same LLMProvider interface as
    VertexAIGeminiProvider so the rest of the backend (orchestrator,
    all agents) never needs to know which concrete provider is active.
    """

    def __init__(self):
        self.initialized = False
        self.client = None
        try:
            if not GEMINI_API_KEY:
                raise ValueError(
                    "GEMINI_API_KEY is not set. Required when LLM_PROVIDER=ai_studio."
                )
            from google import genai
            self.client = genai.Client(api_key=GEMINI_API_KEY)
            self.initialized = True
            logger.info(
                f"AI Studio Gemini Provider initialized successfully with model {GEMINI_MODEL_ID}."
            )
        except Exception as e:
            logger.warning(
                f"Failed to initialize AI Studio (google-genai) client: {e}. "
                f"Falling back to developer-mock mode."
            )

    def generate_text(self, prompt: str, system_instruction: str = None, response_schema: dict = None) -> str:
        if self.initialized:
            try:
                from google.genai import types

                config_args = {}
                if system_instruction:
                    config_args["system_instruction"] = system_instruction

                if response_schema:
                    config_args["response_mime_type"] = "application/json"
                    config_args["response_schema"] = response_schema
                else:
                    # Look for clues in the prompt to see if JSON is expected
                    # (mirrors VertexAIGeminiProvider's heuristic exactly)
                    if "json" in prompt.lower():
                        config_args["response_mime_type"] = "application/json"

                generate_config = types.GenerateContentConfig(**config_args) if config_args else None

                response = self.client.models.generate_content(
                    model=GEMINI_MODEL_ID,
                    contents=prompt,
                    config=generate_config,
                )
                return response.text
            except Exception as e:
                logger.error(
                    f"AI Studio Gemini call failed: {e}. Attempting developer-mock fallback."
                )

        # Developer-mock fallback mode (shared across all LLMProvider implementations)
        return get_mock_response(prompt, system_instruction)
