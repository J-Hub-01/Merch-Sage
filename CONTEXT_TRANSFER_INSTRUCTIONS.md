STAGE: CONTEXT TRANSFER

STATUS: READ / UNDERSTAND / REPORT ONLY

NO IMPLEMENTATION, FIXES, OR MODIFICATIONS ARE AUTHORIZED.

You are taking over an existing MerchSage project from another Antigravity

session because the previous session reached its model quota.

IMPORTANT:

This is NOT a fresh project.

Do NOT restart, regenerate, improve, repair, or continue the implementation

during this stage.

The workspace contains:

\- authoritative MerchSage project documentation,

\- the protected finished frontend (index.html),

\- Git history/baselines created before implementation,

\- and an existing Discoverability vertical-slice implementation produced

  by the previous agent.

The previous agent reported that the vertical slice was completed

successfully. That report has NOT yet been independently verified or

accepted by the project owner.

Therefore, do not assume the implementation is correct merely because it

exists.

\============================================================

1\. YOUR ONLY TASK IN THIS STAGE

\============================================================

Establish complete context before any independent audit or further work.

You may:

\- Read all authoritative project documents in the workspace.

\- Inspect the existing project structure and implementation.

\- Inspect Git history, status, and diffs in read-only ways.

\- Review existing recorded test results and Antigravity task/walkthrough

  artifacts where already available.

\- Report what you find.

You may NOT:

\- modify any file;

\- create any file;

\- delete, rename, move, format, refactor, or rewrite anything;

\- fix anything you notice;

\- continue implementation;

\- install or update dependencies;

\- stage or commit anything;

\- reset, restore, checkout, rebase, amend, or otherwise modify Git state;

\- modify index.html;

\- run the full implementation audit yet;

\- re-run tests during this context-transfer stage.

If you discover a problem, record it for later. Discovery of a problem is

NOT authorization to fix it.

\============================================================

2\. AUTHORITATIVE DOCUMENTATION

\============================================================

Read the authoritative MerchSage documents currently present in the

workspace and reconstruct their authority/precedence.

Do not substitute generic SaaS, Etsy, AI-agent, or software-engineering

conventions for decisions established in these documents.

Where the documents deliberately leave something unresolved, preserve it

as unresolved.

Where a higher-precedence source has already resolved something, do not

reopen the decision.

\============================================================

3\. ESTABLISHED PROJECT CONTEXT

\============================================================

The following constraints and decisions have already been established and

must be treated as binding context while you reconstruct the project:

FRONTEND

\- index.html is a finished, approved frontend deliverable.

\- It is NOT a draft and is NOT something to reconcile against older

  research documents.

\- Its $19 / $79 / $99 pricing is final and correct.

\- Do not modify, restyle, restructure, optimize, rewrite, or otherwise

  change index.html.

\- Any future frontend change requires separate explicit authorization.

BACKEND

\- Python \+ FastAPI is the resolved backend stack.

\- Do not reconsider the language/framework choice.

CURRENT IMPLEMENTATION SCOPE

\- The only implementation authorized so far was the smallest correct

  Discoverability (No/Low Views) vertical slice.

\- This does NOT authorize implementation of the full MerchSage product.

EVIDENCE ARCHITECTURE

\- MarketplaceEvidenceProvider and HistoricalStatsProvider are intentionally

  separate abstractions.

\- MarketplaceEvidenceProvider represents marketplace/listing evidence that

  the capability documentation permits the architecture to depend upon.

\- HistoricalStatsProvider represents seller-provided historical statistics

  such as Etsy Stats CSV-derived views/visits/traffic evidence.

\- The current slice uses fixture/mock evidence.

\- Live Etsy integration is NOT authorized.

\- Do not conflate marketplace API evidence with seller-provided historical

  statistics.

\- Every factual pipeline input/output must follow the project's structured

  Evidence Object requirements, including provenance and state/confidence.

SELLER CLAIMS

\- Seller-provided claims/differentiators are hypotheses or claims to be

  evaluated.

\- They must never automatically be promoted to verified facts.

\- Their evidence state must be preserved.

PIPELINE

\- The authorized slice follows the Discoverability path through the

  project's Intake/Evidence Collection, Classification, Diagnosis,

  Entrepreneur, Researcher, Triage, Discoverability/SEO Specialist,

  Verification, Business Verifier, and Report Formatter responsibilities.

\- Entrepreneur generates hypotheses; it does not determine truth.

\- Researcher tests hypotheses against evidence and must not fabricate

  missing evidence.

\- Triage preserves verified problems while prioritizing/root-causing them.

\- Only the Discoverability/SEO specialist belongs in this slice.

\- Structural verification and factual/legal integrity verification are

  mandatory.

\- Business Verifier must preserve the required traceability from solution

  through confirmed problem, evidence, and hypothesis.

\- Report formatting is deterministic.

STORAGE / ORCHESTRATION

\- Production database selection remains deferred.

\- The current slice uses LocalJsonAuditStore only.

\- Orchestration is synchronous/sequential Python.

\- No orchestration framework is authorized.

OUT-OF-SCOPE SYSTEMS

\- No production database.

\- No payment integration.

\- No additional specialists.

\- No live Etsy API integration.

\- No real Etsy-data-to-Gemini processing while the relevant authorization

  question remains unresolved.

\- No unrelated infrastructure or architecture expansion.

SECRETS

\- Secrets, API keys, credentials, tokens, and service-account material must

  never be printed, logged, requested unnecessarily, or hard-coded.

\============================================================

4\. CRITICAL MODEL DISTINCTION

\============================================================

There are two completely separate concepts:

A. YOUR OWN ANTIGRAVITY MODEL

This is whichever model Antigravity currently uses to reason about and

work on the codebase.

B. MERCHSAGE'S APPLICATION RUNTIME MODEL

This is the LLM that the MerchSage application itself is architected to

call.

These must NEVER be conflated.

Your own Antigravity model does not determine MerchSage's runtime

architecture.

MerchSage's runtime LLM integration is required to use Gemini through

Vertex AI behind the project's LLMProvider abstraction, according to the

existing project decisions and competition requirements.

Do not introduce your own Antigravity model as an application provider,

fallback, dependency, or architectural decision.

\============================================================

5\. CURRENT IMPLEMENTATION

\============================================================

Inspect the implementation that currently exists.

Your goal during this stage is NOT to determine finally whether it is

correct. That will happen in a separate independent audit.

For now, establish:

\- what files/modules were created;

\- what major components appear to have been implemented;

\- how the current project structure maps to the authorized vertical slice;

\- what appears complete;

\- what appears potentially incomplete;

\- whether anything immediately appears outside the authorized scope.

Do not fix or modify anything you find.

\============================================================

6\. GIT / BASELINE CONTEXT

\============================================================

Inspect Git in read-only fashion and establish the high-level state.

Determine:

\- the relevant pre-implementation baseline;

\- whether the protected frontend baseline/tag exists;

\- current tracked/untracked changes;

\- whether implementation work is currently committed or uncommitted;

\- whether index.html appears changed relative to its protected baseline.

Do not alter Git state in any way.

\============================================================

7\. SECURITY CHECK

\============================================================

Without printing or exposing the contents of any potential credential,

check whether the workspace contains any tracked or untracked file that

looks like it could contain secrets or credentials, including examples

such as:

\- .env

\- .env.\*

\- service-account files

\- credential files

\- private keys

\- token files

\- other obviously security-sensitive configuration

Report ONLY:

\- the filename/path;

\- whether it is tracked or untracked;

\- why it may be security-sensitive.

Do NOT print its contents.

Do NOT expose secret values.

Do NOT modify, delete, stage, or otherwise act on such a file.

If checking the contents would risk displaying a credential, do not

display them.

\============================================================

8\. PRIOR TEST EVIDENCE

\============================================================

Review any existing records of the previous agent's test runs that are

already available, including relevant task/walkthrough artifacts or

recorded test output.

Do NOT re-run tests during this context-transfer stage.

Clearly distinguish between:

1\. what the previous agent CLAIMED passed;

2\. what can actually be verified from recorded test results;

3\. what will still require independent execution during the later audit.

Do not equate "a test was reportedly run" with independently verified

correctness.

If walkthrough.md or similar Antigravity artifacts are stored under

Antigravity's own:

\~/.gemini/antigravity-ide/brain/...

location rather than inside the MerchSage workspace, treat them as

IDE/session artifacts unless evidence indicates otherwise.

Do not modify those artifacts and do not perform broad unrelated

filesystem inspection.

\============================================================

9\. REQUIRED RESPONSE

\============================================================

Return ONE context-transfer report containing exactly these sections:

1\. PRODUCT UNDERSTANDING

   Explain what MerchSage fundamentally is and what the current vertical

   slice is intended to prove.

2\. AUTHORITY / PRECEDENCE

   State the document authority/precedence you reconstructed from the

   workspace.

3\. RESOLVED ARCHITECTURAL DECISIONS

   List the decisions relevant to the current vertical slice that must not

   be reopened.

4\. HARD BOUNDARIES

   State what you understand you are explicitly prohibited from changing

   or expanding.

5\. CURRENT IMPLEMENTATION STATE

   Describe what implementation currently appears to exist, without

   assuming it is correct.

6\. GIT / WORKTREE STATE

   Give the high-level baseline/current-change status and state whether

   index.html appears unchanged.

7\. SECURITY-SENSITIVE FILE CHECK

   Report only filenames/paths and tracked/untracked status for anything

   potentially credential-sensitive. Never reveal contents.

8\. PRIOR TEST EVIDENCE

   Separate previous-agent claims from what the recorded evidence actually

   demonstrates and what remains independently unverified.

9\. UNRESOLVED / UNCLEAR ITEMS

   List only genuinely unclear matters that would prevent or materially

   affect the subsequent independent audit.

10\. READINESS FOR INDEPENDENT AUDIT

    State whether you now have sufficient context to perform a separate

    read-only independent audit when explicitly instructed.

\============================================================

10\. STOP CONDITION

\============================================================

After producing the context-transfer report, STOP.

Do not begin the independent audit.

Do not fix anything.

Do not continue implementation.

Do not create an implementation plan.

Do not modify any files.

Do not make any Git changes.

Wait for my explicit next instruction.