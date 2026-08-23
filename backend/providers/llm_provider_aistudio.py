import logging
import time
from backend.config import GEMINI_MODEL_ID, GEMINI_API_KEY
from backend.providers.llm_provider import LLMProvider
from backend.providers.llm_mock import get_mock_response
from backend.providers.exceptions import GeminiQuotaExhaustedError, GeminiAuthError

logger = logging.getLogger("MerchSage.LLMProvider.AIStudio")

# Retry tuning for transient failures (e.g. HTTP 503 "high demand").
# Kept small and local to this provider only -- not a general retry
# framework, not shared with VertexAIGeminiProvider.
MAX_RETRIES = 2
RETRY_DELAY_SECONDS = 1.5


def _is_quota_exhausted(exc: Exception) -> bool:
    """
    Detects HTTP 429 RESOURCE_EXHAUSTED (daily/per-minute free-tier quota
    ceiling) as distinct from transient failures like 503 UNAVAILABLE.

    A quota ceiling will not clear in 1.5s, so retrying against it is a
    guaranteed-wasted call -- unlike a genuine transient overload, where
    a short retry can plausibly succeed.
    """
    msg = str(exc)
    return "RESOURCE_EXHAUSTED" in msg or "429" in msg


def _is_auth_error(exc: Exception) -> bool:
    """
    Detects HTTP 401 UNAUTHENTICATED / 403 PERMISSION_DENIED -- a
    missing, invalid, revoked, or insufficiently-scoped API key.

    Retrying against a bad credential is exactly as pointless as
    retrying against exhausted quota (it will never succeed), but the
    correct response is different: this is a configuration/
    infrastructure failure affecting every stage identically, not a
    single-stage degraded case, so it is always raised rather than
    routed through any per-stage fallback.
    """
    msg = str(exc)
    return (
        "401" in msg
        or "403" in msg
        or "UNAUTHENTICATED" in msg
        or "PERMISSION_DENIED" in msg
    )


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

    def generate_text(
        self,
        prompt: str,
        system_instruction: str = None,
        response_schema: dict = None,
        raise_on_quota_exhaustion: bool = False,
    ) -> str:
        if self.initialized:
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

            last_error = None
            quota_exhausted = False
            for attempt in range(1, MAX_RETRIES + 2):  # initial attempt + up to MAX_RETRIES retries
                try:
                    response = self.client.models.generate_content(
                        model=GEMINI_MODEL_ID,
                        contents=prompt,
                        config=generate_config,
                    )
                    return response.text
                except Exception as e:
                    last_error = e

                    if _is_auth_error(e):
                        # Always raised, never opt-in, never retried, never
                        # routed through mock: a bad credential means every
                        # remaining stage in the pipeline is about to fail
                        # identically, so there is nothing a per-stage
                        # fallback could meaningfully do here.
                        logger.error(
                            f"AI Studio Gemini call failed (attempt {attempt}/{MAX_RETRIES + 1}): {e}. "
                            f"Authentication/authorization failure is non-retryable and non-degradable "
                            f"-- raising immediately, no mock fallback."
                        )
                        raise GeminiAuthError(str(e))

                    if _is_quota_exhausted(e):
                        quota_exhausted = True
                        logger.error(
                            f"AI Studio Gemini call failed (attempt {attempt}/{MAX_RETRIES + 1}): {e}. "
                            f"Quota exhaustion is non-transient -- skipping remaining retries."
                        )
                        break

                    if attempt <= MAX_RETRIES:
                        logger.warning(
                            f"AI Studio Gemini call failed (attempt {attempt}/{MAX_RETRIES + 1}): {e}. "
                            f"Retrying in {RETRY_DELAY_SECONDS}s..."
                        )
                        time.sleep(RETRY_DELAY_SECONDS)
                    else:
                        logger.error(
                            f"AI Studio Gemini call failed after {MAX_RETRIES + 1} attempts: {last_error}. "
                            f"Attempting developer-mock fallback."
                        )

            if quota_exhausted and raise_on_quota_exhaustion:
                raise GeminiQuotaExhaustedError(str(last_error))

            if quota_exhausted:
                logger.warning(
                    "Quota exhausted and caller did not opt into raise_on_quota_exhaustion "
                    "-- attempting developer-mock fallback (legacy behavior)."
                )

        # Developer-mock fallback mode (shared across all LLMProvider implementations)
        return get_mock_response(prompt, system_instruction)
