import os

# Config definitions for MerchSage
PROJECT_ID = os.getenv("GCP_PROJECT", None)
LOCATION = os.getenv("GCP_LOCATION", "us-central1")

# The confirmed runtime model for MerchSage's own LLM tasks
# CLAUDE IS FORBIDDEN as a runtime model or fallback.
GEMINI_MODEL_ID = os.getenv("GEMINI_MODEL_ID", "gemini-3.5-flash")

# Etsy API to Gemini production gating flag
# True = Gated (use mock/CSV uploads only); False = Allowed (only if written permission is confirmed)
ETSY_API_GATING = os.getenv("ETSY_API_GATING", "True").lower() in ("true", "1", "yes")

# Local storage path for JSON files
AUDIT_STORE_DIR = os.getenv("AUDIT_STORE_DIR", os.path.join(os.path.dirname(os.path.dirname(__file__)), "data"))
os.makedirs(AUDIT_STORE_DIR, exist_ok=True)

# Maximum retries for internal verification loop
MAX_INTERNAL_RETRIES = 2

