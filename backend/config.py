import os

# Config definitions for MerchSage
PROJECT_ID = os.getenv("GCP_PROJECT", None)
LOCATION = os.getenv("GCP_LOCATION", "us-central1")

# The confirmed runtime model for MerchSage's own LLM tasks
# CLAUDE IS FORBIDDEN as a runtime model or fallback.
GEMINI_MODEL_ID = os.getenv("GEMINI_MODEL_ID", "gemini-2.5-flash")

# Etsy API to Gemini production gating flag
# True = Gated (use mock/fixture data only); False = Allowed (only if written permission is confirmed)
# NOTE: this now actually gates MarketplaceEvidenceProvider (previously
# defined here but unused anywhere in the codebase).
ETSY_API_GATING = os.getenv("ETSY_API_GATING", "True").lower() in ("true", "1", "yes")

# Required only when ETSY_API_GATING=False
ETSY_API_KEY = os.getenv("ETSY_API_KEY", None)
ETSY_SHARED_SECRET = os.getenv("ETSY_SHARED_SECRET", None)

# Which concrete LLMProvider to instantiate: "vertex" | "ai_studio"
# Defaulting to ai_studio while GCP Billing is blocked. Flip back to
# "vertex" once Google Cloud Billing is restored -- no other code
# change should be required (see get_llm_provider() factory in
# backend/providers/llm_provider.py).
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ai_studio").lower()

# Required only when LLM_PROVIDER=ai_studio
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", None)

# Local storage path for JSON files
AUDIT_STORE_DIR = os.getenv("AUDIT_STORE_DIR", os.path.join(os.path.dirname(os.path.dirname(__file__)), "data"))
os.makedirs(AUDIT_STORE_DIR, exist_ok=True)

# Maximum retries for internal verification loop
MAX_INTERNAL_RETRIES = 2

