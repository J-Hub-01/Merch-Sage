# MerchSage — Production Engineering Requirements
## Authoritative v2 Amendment / Integration Patch

**Status: REQUIRED AMENDMENT TO CURRENT AUTHORITATIVE PRODUCTION-ENGINEERING REQUIREMENTS**

This amendment is designed to be integrated into the current authoritative
`MerchSage_Production_Engineering_Requirements.md` without weakening, replacing,
or contradicting any existing HARD / MUST requirement.

The current document remains authoritative in full. The requirements below make
previously implicit or partially covered failure modes explicit.

---

# A. Classification and performance-routing integrity

## A.1 Classification is a high-impact upstream decision

Product/category classification is not cosmetic. It changes the investigation
space, evidence sought, specialist agents invoked, and downstream business reasoning.

**HARD / MUST**

- Classification output must be structured and schema validated.
- Preserve the evidence used to support the classification.
- Preserve uncertainty and plausible alternative classifications when material.
- Do not force a single confident classification when available evidence is ambiguous.
- Low-confidence or materially ambiguous classification must trigger a defined
  clarification, verification, or degraded-analysis path rather than silently
  propagating an uncertain classification through the entire audit.
- Downstream stages must be able to determine which classification/version they
  were given.
- Reclassification must invalidate or explicitly re-evaluate downstream work whose
  assumptions materially depended on the previous classification.

## A.2 Performance-routing verification

The Discoverability / Conversion routing decision is also upstream and high impact.

**HARD / MUST**

- The routing decision must preserve the evidence used to reach it.
- The system must not infer "no views" merely because traffic evidence is unavailable.
- The system must not infer "views but no sales" merely because sales evidence is unavailable.
- Missing or structurally unavailable evidence must remain UNKNOWN / INSUFFICIENT
  rather than being converted into a branch decision.
- If both branches are materially implicated, the system must preserve that fact rather
  than forcing a false binary conclusion.
- A branch decision that is materially uncertain must be explicitly represented as uncertain.
- Before deep branch-specific diagnosis, deterministic orchestration must confirm that
  required routing fields and evidence references exist.
- If later evidence contradicts the original routing decision, the system must support
  controlled re-routing/re-evaluation instead of continuing blindly.

## A.3 Propagation-error containment

**MUST**

The system must be designed so that an upstream classification/routing error does not
silently contaminate every downstream conclusion.

At minimum:

- classification and routing versions are recorded;
- downstream outputs identify the upstream assumptions they relied on;
- material upstream changes trigger dependency-aware invalidation/recomputation;
- stale downstream conclusions are not presented as current after their assumptions change.

---

# B. Confidence and uncertainty integrity

## B.1 Model self-reported confidence is not calibrated confidence

**HARD / MUST**

A model saying "90% confident" does not make a conclusion 90% reliable.

MerchSage must not present raw model self-confidence as statistically calibrated probability
unless calibration has actually been established through evaluation.

## B.2 Confidence must be evidence-aware

Where confidence is exposed, it should be derived from explicit factors such as:

- evidence availability;
- evidence quality;
- source reliability;
- freshness;
- directness vs inference;
- agreement/conflict between independent evidence;
- completeness of mandatory investigation;
- known missing evidence;
- classification/routing uncertainty;
- verifier/QC results.

The exact scoring formula remains an implementation/evaluation decision.

**MUST**

- confidence must decrease or become explicitly limited when material evidence is missing;
- contradictory evidence must not be hidden by a single high-confidence number;
- confidence labels must not imply guaranteed causation or guaranteed business outcomes;
- UNKNOWN / INSUFFICIENT EVIDENCE remains a valid result.

---

# C. Etsy OAuth binding and lifecycle hardening

Existing OAuth requirements remain in force.

## C.1 Callback binding

**HARD / MUST**

An OAuth callback must be cryptographically/securely bound to the MerchSage flow that
initiated it.

The backend must verify, as applicable:

- authenticated MerchSage user/session;
- expected OAuth state;
- intended Etsy connection;
- intended audit/order/customer context;
- callback has not already been consumed;
- callback has not expired.

A user-controlled audit/order identifier inside a callback is not sufficient proof of ownership.

The callback must never allow one MerchSage customer to attach an Etsy account/token to
another customer's audit/order.

## C.2 State and PKCE

- Use unpredictable, single-use, short-lived OAuth `state`.
- Validate state server-side before accepting the callback.
- Use PKCE where required/supported by the sanctioned Etsy OAuth flow.
- Do not place secrets or sensitive reusable credentials inside OAuth state.

## C.3 Token lifecycle

**MUST**

Explicitly handle:

- access-token expiry;
- refresh-token expiry where applicable;
- token refresh;
- revoked authorization;
- user disconnect;
- reauthorization;
- invalid/changed scopes;
- refresh failure;
- Etsy-side account/access changes.

Token refresh must be concurrency-safe so multiple workers do not corrupt/overwrite token state.

A failed or revoked Etsy credential must produce an authentication/evidence-unavailable state,
not fabricated Etsy evidence.

---

# D. Worker ownership, duplicate execution, cancellation and shutdown

## D.1 Stage ownership / leasing

Before concurrent workers or parallel agents are enabled:

**HARD / MUST**

A single logical audit stage must not be executed simultaneously by multiple workers unless
the stage is explicitly designed for safe parallel execution.

Use an appropriate deterministic mechanism such as:

- database locking;
- compare-and-set state transition;
- job lease with expiry/heartbeat;
- unique execution key;
- equivalent infrastructure guarantee.

The exact mechanism is an implementation choice.

## D.2 Duplicate-stage protection

Every expensive or state-changing stage must define:

- execution identity/idempotency key;
- whether duplicate execution is safe;
- how duplicate results are detected;
- which result becomes authoritative;
- how duplicated model/API cost is prevented or bounded.

Retries must not create duplicate evidence, duplicate reports, duplicate generated assets,
or duplicate paid entitlements.

## D.3 Cancellation semantics

Cancellation must be an explicit state transition, not merely a UI label.

**MUST**

When an audit is cancelled:

- stop scheduling new model/tool work;
- prevent retry loops from resurrecting cancelled work;
- allow already-running external calls to finish only where they cannot be safely cancelled;
- discard or quarantine late results that are no longer valid for the cancelled execution;
- preserve completed durable work needed for reconciliation/debugging;
- do not corrupt payment/account state;
- record who/what initiated cancellation.

## D.4 Safe shutdown/restart

Workers must handle shutdown/redeploy/restart without silently losing paid work.

**MUST**

- persist meaningful state before/after external side effects;
- release or expire worker leases safely;
- resume only from a valid durable state;
- do not rerun completed non-idempotent operations;
- detect abandoned/stuck jobs;
- recover them through a controlled retry/requeue process.

---

# E. External AI/provider privacy and fallback policy

## E.1 Provider data-use review

Before sending customer data to any AI/model/image/video provider:

**MUST**

Review and document, for the production account/configuration actually used:

- what customer data is transmitted;
- retention behavior;
- logging behavior;
- whether provider training/data improvement uses submitted content;
- available opt-out/no-training controls;
- regional/storage implications where relevant;
- subprocessors/terms/privacy obligations where relevant;
- deletion controls where offered.

Private seller data must not be sent to a provider merely because doing so is convenient.

## E.2 Provider fallback must preserve safety

A fallback model/provider may not silently bypass:

- evidence requirements;
- schema validation;
- prompt-injection boundaries;
- privacy rules;
- agent/tool permissions;
- verifier/QC requirements;
- cost ceilings.

**MUST**

- fallback use is observable and recorded;
- fallback model/provider/version is recorded with the audit;
- known quality differences are accounted for;
- if no validated fallback can satisfy the task safely, degrade/fail explicitly rather than
  silently delivering lower-integrity analysis.

---

# F. Generated-content factual and legal integrity

## F.1 Seller claims vs verified facts

The system must preserve the distinction between:

- seller-provided claim;
- observed marketplace fact;
- external evidence;
- MerchSage inference;
- verified conclusion.

**HARD / MUST**

Generated listing text, recommendations, image/video prompts, or other deliverables must not
silently convert a seller claim into a verified fact.

Examples include claims about:

- materials;
- handmade process;
- origin;
- sustainability;
- certifications;
- safety;
- performance;
- durability;
- shipping;
- guarantees;
- customization;
- product composition.

If a claim is not independently verified, the generated content must treat it according to
its actual evidence state.

## F.2 Unsupported claims

Resolution agents must not invent:

- certifications;
- awards;
- customer testimonials;
- product specifications;
- medical/safety claims;
- legal/regulatory compliance;
- performance guarantees;
- discounts;
- shipping promises;
- scarcity/stock claims;
- any other factual product/business assertion not supported by authorized evidence.

## F.3 Intellectual-property guardrails

Where MerchSage generates customer-facing text, images, video concepts, branding, or other
creative assets:

**MUST**

- avoid deliberately instructing models to copy a specific competitor's protected creative work;
- do not knowingly reproduce competitor trademarks/branding as the seller's own;
- do not represent generated material as guaranteed non-infringing;
- preserve provenance/provider metadata where operationally useful;
- provide a review path for generated assets before the seller publishes them where risk warrants it.

Exact IP review mechanisms are an implementation/legal decision and should not be falsely
presented as a guarantee of non-infringement.

---

# G. Operational kill switches and feature controls

## G.1 Emergency controls

MerchSage must be operable during incidents.

**MUST before real paid production**

Provide a safe mechanism to stop or disable, without corrupting existing customer data:

- creation of new audits;
- expensive model execution;
- a malfunctioning specialist agent;
- an external provider/integration;
- file uploads if a parser/storage issue emerges;
- other high-risk functionality where an incident could amplify loss.

The mechanism may be configuration, feature flags, administrative controls, or equivalent.

## G.2 Global spend stop

There must be a deterministic emergency control that can stop new expensive AI/tool execution
when abnormal spend or runaway execution is detected.

Activating it must:

- preserve existing reports and customer records;
- preserve completed audit work;
- prevent uncontrolled new spend;
- place affected jobs into an explicit paused/degraded state;
- allow controlled recovery after investigation.

## G.3 Feature-flag safety

Feature flags must not become an authorization bypass.

- Server-side security rules remain enforced regardless of UI flags.
- Flag changes affecting production should be auditable.
- Dangerous experimental features should default off.
- Disabling a feature must define what happens to jobs already using it.

---

# H. Required test additions

Add the following to the existing security, reliability, and agent-evaluation suites.

**MUST test:**

1. ambiguous product classification;
2. incorrect classification and downstream invalidation;
3. low-confidence classification;
4. incorrect Discoverability/Conversion routing;
5. missing routing evidence;
6. routing evidence that later changes;
7. both branches materially implicated;
8. raw model confidence conflicting with weak evidence;
9. OAuth callback for the wrong authenticated user;
10. replayed/expired OAuth state;
11. duplicate OAuth callback;
12. concurrent token refresh;
13. two workers attempting the same stage;
14. worker crash after external side effect but before local acknowledgement;
15. cancellation during a model/API call;
16. retry arriving after cancellation;
17. late result from an obsolete execution;
18. provider fallback returning weaker/malformed output;
19. fallback attempting to bypass required verification;
20. generated copy inventing a product claim;
21. seller claim incorrectly promoted to verified fact;
22. emergency model-spend kill switch;
23. disabling a provider/agent while jobs are in flight.

These tests supplement, not replace, the existing IDOR, payment, webhook, file-upload,
prompt-injection, restart, malformed-model-output, budget-ceiling, and dependency-failure tests.

---

# I. Release-gate additions

Add the following to the existing "Must-have controls before accepting real customer payments"
release gate:

- classification/routing uncertainty handling implemented and tested;
- OAuth callback bound to the correct authenticated user/context;
- OAuth state replay/expiry protection tested;
- concurrency-safe token lifecycle;
- worker duplicate-execution protection;
- safe cancellation/restart semantics;
- AI/provider production privacy/data-use settings reviewed;
- generated factual-claim validation;
- operational kill switch for new expensive execution;
- provider/model fallback cannot bypass safety/verification;
- classification/routing propagation-error tests pass.

---

# J. Production-ready definition additions

A feature is also not production-ready if:

- a wrong upstream classification can silently contaminate the whole audit;
- a routing decision is made from missing evidence as though it were evidence;
- model self-confidence is presented as calibrated reliability without validation;
- duplicate workers can execute the same expensive/state-changing stage unsafely;
- cancellation can be undone by a retry;
- provider fallback silently weakens verification/privacy requirements;
- generated customer-facing content can invent factual product claims;
- there is no practical way to stop runaway expensive execution during an incident.

---

# K. Authority and non-regression rule

These additions are **non-regressive**.

They must not be implemented by weakening existing requirements for:

- tenant isolation;
- payment verification;
- evidence provenance;
- prompt-injection protection;
- bounded retries;
- cost ceilings;
- canonical report integrity;
- Business Verifier cross-solution compatibility;
- privacy;
- Etsy sanctioned-access requirements;
- existing security/release gates.

If an implementation approach creates a conflict, preserve the stricter safety/integrity rule
unless the authoritative requirements are deliberately revised after review.
