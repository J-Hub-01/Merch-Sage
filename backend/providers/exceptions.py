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


class GeminiAuthError(Exception):
    """
    Raised when a Gemini API call fails due to authentication or
    authorization failure (HTTP 401 UNAUTHENTICATED / 403
    PERMISSION_DENIED) -- e.g. a missing, invalid, revoked, or
    insufficiently-scoped API key.

    Unlike GeminiQuotaExhaustedError, this is NOT opt-in: it is always
    raised by every caller, regardless of raise_on_quota_exhaustion.
    A bad credential means every stage in the pipeline is about to fail
    identically, not just the calling stage -- so unlike a quota issue,
    there is no reasonable per-stage degraded fallback to construct, and
    silently falling back to mock content here would mean the ENTIRE
    audit silently runs on fabricated data with no signal to the
    customer that nothing real was ever evaluated. This must surface as
    a pipeline-level configuration/infrastructure failure, handled by
    the orchestrator, not swallowed by any individual agent.
    """
    pass
