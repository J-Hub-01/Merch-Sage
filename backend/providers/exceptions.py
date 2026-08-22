class GeminiQuotaExhaustedError(Exception):
    """
    Raised when a Gemini API call fails due to non-transient quota
    exhaustion (HTTP 429 RESOURCE_EXHAUSTED), as opposed to a transient
    failure (e.g. HTTP 503 model overload) that is safe to retry.

    Only raised by LLMProvider.generate_text() when the caller opts in
    via raise_on_quota_exhaustion=True. Callers that opt in receive this
    exception instead of a silent developer-mock fallback, so they can
    produce an honest, evidence-grounded degraded response specific to
    their own stage rather than serving unrelated canned mock content.

    Callers that do not opt in (the default) see no behavior change:
    quota exhaustion still falls through to get_mock_response() exactly
    as before, it just no longer wastes retries getting there.
    """
    pass
