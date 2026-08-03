# MerchSage — Final Working Pipeline
### Status: FINALIZED implementation authority. No open/proposed decisions remain. Where a choice was genuinely undecided in every source document and left to engineering discretion, it is explicitly marked **Implementation choice (may be changed if equivalent behavior is preserved)** — Antigravity may vary these as long as the described behavior is preserved. Everything else is a fixed decision, not a suggestion.

---

## 0. Source authority, in order of precedence

1. Explicit decisions made directly with the project owner (Exception Manager, retry policy, capability-vs-agent calls, this document itself) — highest precedence, supersede anything older.
2. `More_context.md` / `More_context (1).md` — post-document architectural decisions. Their absence from older docs does not mean rejection; where they refine an older doc, the refinement wins.
3. `MerchSage_Authoritative_Product_Workflow.md` — the core pipeline architecture.
4. `MerchSage_Production_Engineering_Requirements.md` + its `v2_Amendment.md` — engineering/security/legal-integrity controls layered on top of the architecture.
5. `ETSY_EVIDENCE_CAPABILITY_MATRIX.md` (finalized) — the current capability authority for what Etsy data may be architecturally depended on.
6. `AI_Marketing_Legal_Compliance_Reference.md` — content/output legality, separate axis from Etsy access legality.
7. `Gensparks_psycholgy_doc.md` — reference material, consumed by the Psychology/Commercial Intelligence capability, not authoritative on its own.

---

## 1. The Evidence Object

Everything in this pipeline flows through evidence: every agent consumes it,
every verifier checks it, Supervisor tracks its IDs, Researcher creates it,
Thin Evidence Mode reasons about its sufficiency. It was implicit across
multiple sections of the Workflow doc but never unified — this section
fixes that.

**Every verified fact, seller claim, hypothesis, external observation, and
derived calculation must exist as a structured Evidence Object.** No agent
may invent or modify evidence outside this lifecycle.

**Minimum fields:**

| Field | Description |
|---|---|
| Evidence ID | Unique identifier, referenced by every downstream consumer instead of restating the underlying fact |
| Source type | One of: **observed fact** (e.g. a listing currently uses a given tag) · **seller claim** (e.g. seller believes customization is their edge) · **external evidence** (e.g. reviews repeatedly praise packaging) · **inference** (MerchSage-derived, e.g. "customization may be underused as a differentiator") — the four categories fixed in Workflow §23 |
| Origin | The specific mechanism that produced it — an Etsy API endpoint, a seller upload, the Researcher's hypothesis-testing process, etc. |
| Timestamp | When the underlying fact was observed/collected, not when the record was written |
| Confidence | How strongly the evidence supports whatever conclusion cites it — never inflated past what the evidence justifies (Workflow §23: no promising outcomes the evidence doesn't support) |
| Evidence state | For anything tested against a hypothesis: SUPPORTED / CONTRADICTED / MIXED / UNKNOWN-INSUFFICIENT EVIDENCE (Workflow §10, §24) |
| Provenance | The chain back to origin — required so Supervisor can verify it wasn't fabricated and Business Verifier can check it's actually being used to justify what it's cited for |
| Supporting data | The actual underlying content (the review text, the field value, the seller's uploaded figure) |
| Downstream consumers | Which agents/solutions cite this Evidence Object — lets a correction or a seller-revision propagate to everything that depended on it, and lets Supervisor detect orphaned or unused evidence |

**Hard rule (already fixed in Workflow §23, now binding at the data-model
level too):** unavailable evidence is a valid state (UNKNOWN/INSUFFICIENT
EVIDENCE), never a reason to fabricate an Evidence Object. An Evidence
Object is never created to fill a gap — it either reflects something real,
or it doesn't exist and the gap is represented explicitly.

---

## 2. Pipeline overview (single diagram, all stages)

```
Intake
  │  (seller-claimed strengths preserved as a CLAIM-type Evidence Object,
  │   never auto-promoted to fact — §8)
  │  (evidence-sufficiency pass — see §7 Thin Evidence Mode)
  ▼
Classification (product category / taxonomy)
  ▼
Diagnosis routing (No/Low Views → Discoverability | Views-But-No-Sales → Conversion)
  ▼
Entrepreneur Agent (hypothesis generation)
  │   may consult Psychology/Commercial-Intelligence capability for additional
  │   plausible hypotheses — hypotheses ONLY, never a diagnosis (§3)
  ▼
Researcher Agent (creates/tests Evidence Objects: SUPPORTED / CONTRADICTED /
  MIXED / UNKNOWN)
  │   tests seller's claimed differentiator against customer evidence (§8)
  │   requests additional seller evidence where it would materially help (§7)
  ▼
Triage / Priority Agent (problem dependency graph, not flat list)
  ▼
Resolution layer — per confirmed problem:
  ├─ Directly solvable      → Specialist Agent generates the fix
  ├─ Assistively solvable   → Specialist Agent produces creative direction/plan
  └─ Seller action required → clearly explained, not solved
  │
  │   Specialist Agents (dynamically invoked, only as implicated):
  │   Discoverability/SEO · Pricing · Profitability · Financial Extraction ·
  │   Review/Trust · Positioning/Differentiation · Copy · Image/Visual · Video/Creative
  │
  │   Text/data specialists may consult Psychology/Commercial-Intelligence
  │   capability for stronger solution design (§3) — evidence/compliance/
  │   strategy override psychology if they conflict
  │
  │   Any generative specialist call is assembled via the Prompting
  │   Capability before the model call (§4)
  ▼
Domain-Specific Verification (per output type, before global verification — §6, §12)
  │
  │   Visual/Creative sub-flow (§5):
  │   Verified problem → Creative Strategy → Prompting Capability →
  │   image/video generation → Visual Verification → accept OR
  │   targeted regeneration (bounded, cost-aware — §9)
  ▼
Supervisor / QC (pipeline execution integrity: coverage, schemas,
  Evidence Object IDs/provenance, missing domain checks, failed stages, retries)
  ▼
Business Verifier (GLOBAL: is each solution justified by its cited Evidence
  Objects, AND do all solutions work together without contradicting seller strategy)
  ▼
Formatter (canonical report)
  ▼
Localization (presentation/language ONLY — never touches numbers,
  evidence, confidence, diagnoses, facts, or priorities)
  ▼
Delivery (email/dashboard)
  │
  ▼
[Post-delivery] Revision requests (§9) · Complaints/Refunds (§10) ·
Exception Manager watches the whole pipeline throughout (§EM)
```

---

## 3. Exception Manager — finalized

**Not a reasoning agent.** Its only job: classify exceptional events, log
them, notify the owner when appropriate, and enforce blocking/non-blocking
behavior per policy. It observes every stage above; it does not replace
Supervisor, Domain Verifiers, or the Business Verifier — those still do the
actual judgment. The Exception Manager decides what happens *once* one of
them raises something exceptional.

### Severity levels — finalized

| Severity | Notification | Blocking behavior |
|---|---|---|
| **Critical** | Email immediately to `jayssawant12@gmail.com` | Blocking **only if** the event requires owner approval (currently: refund approval only) |
| **High** | Email immediately | Non-blocking unless explicitly configured otherwise |
| **Medium** | Dashboard + daily summary email | Non-blocking |
| **Low** | Dashboard only | Non-blocking |

### Current policy — finalized

**Blocking (pipeline/process pauses for owner action):**
- Refund approval — only case that blocks today.

**Non-blocking, with finalized severity tier:**

| Event | Severity |
|---|---|
| Security anomaly | Critical |
| Compliance/legal flag | Critical |
| Repeated similar complaints (systemic signal) | High |
| Internal system failure | High |
| Repeated Visual Verification failures (regeneration budget exhausted on an asset) | Medium |
| Seller revision conflicts with evidence/strategy | Medium |

---

## 4. Psychology / Commercial Intelligence — finalized as shared capability

Used in two places only: (A) Entrepreneur Agent, as a source of additional
plausible hypotheses, never a diagnosis; (B) Resolution specialists, to
strengthen a solution for an already-verified problem. Evidence, seller
reality, compliance, and business strategy always override a psychological
principle if they conflict. Does not run on every audit.

**Finalized: a shared capability** (a principles lookup/retrieval function
callable by Entrepreneur and by Resolution specialists), not a dedicated
agent with its own standing LLM call — confirmed, matches the project's
cost-efficiency posture throughout.

---

## 5. Prompting Capability — finalized as shared capability

Assembles verified problem, Evidence Objects, product context, audience,
seller differentiator, constraints, commercial strategy (where relevant),
compliance constraints, output requirements, and verification criteria into
one precise execution instruction for a downstream generative call. Goal:
high first-attempt quality, fewer retries. Must not become an automatic
extra LLM call for trivial tasks.

**Finalized: a shared capability**, not a dedicated agent — confirmed.
Implemented primarily as deterministic template assembly (structured data
→ structured prompt, no model call), used for most Copy/SEO/Pricing
generation. Escalates to a lightweight LLM call only where genuine
synthesis is needed — the clearest case is assembling the Creative Strategy
brief into a generation-ready image/video prompt (§6 below), where
free-text nuance plausibly beats a template. Every other generative call
uses the deterministic path by default unless a specific specialist agent's
contract says otherwise. **Implementation choice (may be changed if
equivalent behavior is preserved):** the exact deterministic/LLM split
per call type.

---

## 6. Visual/Creative Generation sub-pipeline

**Flow is fixed, not a choice:**

```
Verified problem
  → Creative Strategy (what the visual must communicate, based on product,
    audience, positioning, verified problem, seller differentiator,
    commercial/psychological principles where appropriate, platform/context,
    compliance constraints — contextual, not a blanket "make it luxury")
  → Prompting Capability (precise generation instruction)
  → Image/Video generation
  → Visual Verification (malformed anatomy/objects, extra/missing limbs,
    broken geometry, unreadable text, impossible product structure,
    AI artifacts, product fidelity, unintended product changes,
    audience/positioning fit, Creative Strategy adherence, whether it
    actually addresses the verified problem, compliance/safety)
  → accept OR targeted regeneration of that asset only (1 regeneration —
    see §9 retry policy)
```

A failed asset never triggers regeneration of the whole audit. Exhausting
the regeneration budget routes to Exception Manager, Medium severity,
non-blocking (§3).

---

## 7. Domain-Specific Verification

Every solution type gets appropriate validation *before* global Business
Verification. Domain-Specific Verification checks whether one output is
technically/contextually acceptable for its own domain. Supervisor/QC
checks pipeline process integrity, not output quality. Business Verifier
checks global justification and cross-solution coherence. These three stay
distinct — never collapsed into one step (§12).

**Implementation choice (may be changed if equivalent behavior is
preserved)** — deterministic-vs-model split per domain:

| Output type | Check | Suggested mechanism |
|---|---|---|
| Copy | Factual support (against cited Evidence Objects), tone/authenticity, unsupported claims, seller voice, platform suitability | Model-based (needs judgment on tone/authenticity/claims) |
| Pricing | Evidence support, range sanity, positioning consistency, no fabricated precision | Deterministic (range/sanity checks, Evidence Object linkage validation) |
| SEO/tags | Platform constraints (e.g. ≤13 tags, char limits), evidence/category relevance, duplication/invalid structure | Deterministic for structure/limits; model-based only for relevance judgment |
| Calculations | Deterministic validation | Deterministic — no ambiguity here |
| Images/video | Full Visual Verification list (§6) | Model-based (multimodal) — deterministic checks cannot catch malformed anatomy or unreadable text |

Do not create unnecessary verifier agents purely for architectural
elegance; deterministic checks are used wherever sufficient.

---

## 8. Thin Evidence Mode — refined trigger logic

- **Does NOT trigger** merely because several fields are UNKNOWN.
- **Triggers** only when evidence required for a *meaningful normal
  diagnosis* is materially insufficient.
- **Before** accepting that limitation: request missing seller evidence
  where it could materially improve diagnosis (Etsy Stats exports/
  screenshots, historical changes, cost information, customer feedback, or
  other evidence relevant to the specific hypothesis).
- Then proceed with every analysis that *can* legitimately run on available
  structural/seller-provided/competitor/permitted Evidence Objects.
- Never convert missing evidence into an invented Evidence Object.
- Final output distinguishes three states explicitly: verified problems /
  hypotheses needing more evidence / areas that could not be evaluated.
- It is an evidence *state*, never a cheaper product tier.

**Implementation choice (may be changed if equivalent behavior is
preserved)** — where the "request missing evidence" step sits: a
two-part approach — (1) a lightweight, category/branch-driven checklist
runs right after Classification/Diagnosis routing and asks for common items
upfront during Intake; (2) Researcher can flag additional,
hypothesis-specific evidence requests reactively while testing a particular
hypothesis, batched and surfaced together in the final deliverable's
"hypotheses needing more evidence" section rather than pausing the pipeline
mid-run. No new async pause/resume pipeline state is introduced — this
stays a single synchronous run per audit.

---

## 9. Seller Differentiator / Claim Validation

Seller's believed differentiator is preserved as a **seller-claim-type
Evidence Object**, not fact. Researcher tests it against customer evidence
— SUPPORTED, CONTRADICTED, or revealing a different actual
strength/weakness. A discrepancy between what the seller believes and what
evidence shows becomes an inference-type Evidence Object in its own right,
not just a data point to discard.

---

## 10. Retry Policy — finalized

No source document defined a universal cap; this fixes it.

| Retry type | Cap |
|---|---|
| Internal correction attempts — text-based components | 2 retries after initial attempt |
| Internal correction attempts — image/video generation | 1 regeneration after initial attempt |
| Seller-requested revision rounds — per affected deliverable | Maximum 3 revision rounds |

All retries and revisions remain subject to the per-audit cost ceiling
(Requirements doc). Exceeding a cap routes to Exception Manager rather than
looping further (§3).

---

## 11. Revision / Retry Experience (post-delivery)

```
Seller requests revision (free-text: what they disliked / wanted changed)
  ▼
System determines:
  - which component is being challenged
  - whether the request is compatible with the cited Evidence Objects
  - whether it conflicts with audience/positioning/compliance
  - whether clarification is needed
  ▼
If request would make the solution worse or contradict verified strategy:
  → explain why, do NOT silently comply
Else:
  → rerun only the affected component (subject to §10 revision cap)
  → must re-pass its relevant Domain-Specific Verification before redelivery
```

---

## 12. Complaint / Refund Principle

```
Complaint received (with reason/comment)
  ▼
Evaluated against: what was purchased/promised, cited Evidence Objects,
QC/verifier records, delivered output, seller's stated issue
  ▼
If genuine:
  → identify affected component
  → correct/regenerate it free where reasonably possible (subject to §10 caps)
  → re-verify (Domain-Specific Verification again)
  → redeliver
  ▼
Refund only if MerchSage genuinely failed to deliver the purchased
deliverable AND cannot satisfactorily correct it within remediation
  ▼
Refund payout → Exception Manager, Critical severity, BLOCKING —
owner approval required (the only current blocking case)
```

Explicitly not automatic grounds for a refund: an honest UNKNOWN/
INSUFFICIENT EVIDENCE conclusion, or "I didn't get more sales" (MerchSage
guarantees the deliverable, not a business outcome). Repeated similar
complaints trigger a systemic-issue investigation (Exception Manager, High
severity, non-blocking), not default suspicion of the customer.

---

## 13. Supervisor / Domain Verifiers / Business Verifier — final distinction

| Layer | Checks |
|---|---|
| **Domain-Specific Verification** | Is this *one* output technically/contextually acceptable for its domain (§7 table) |
| **Supervisor/QC** | Pipeline execution integrity — coverage, required checks ran, Evidence Object IDs/provenance, schemas, failed stages, retry behavior, missing mandatory domain checks |
| **Business Verifier** | Is each solution justified by its cited Evidence Objects, AND do all solutions work together without contradicting each other or the seller's overall strategy |

Never collapsed into one vague "verification" step.

---

## 14. Etsy Capability / Legal Uncertainty — how it's held architecturally

`ETSY_EVIDENCE_CAPABILITY_MATRIX.md` (finalized version) is the current
capability authority. No architectural dependency on anything tagged
UNVERIFIED in that matrix. Historical traffic/views Etsy cannot supply must
come from seller-provided evidence (§8, as a seller-upload-origin Evidence
Object) or remain UNKNOWN — never fabricated. The Etsy API's AI/ML-use
restriction remains an **unresolved compliance gate** — this pipeline does
not assume it is solved.

The pipeline stays data-source-agnostic by design: every Evidence Object
carries a source type (§1) rather than the pipeline being hard-wired to a
specific Etsy endpoint. This means resolving the AI/ML clause later (via
Etsy written authorization, or by permanently restricting AI analysis to
seller-uploaded content) is a data-sourcing-layer change, not a pipeline
redesign.

---

## 15. Build / Validation Timing

Implementation and real-user validation proceed **in parallel**, given the
Aug 17, 2026 deadline. `SESSION_STATE.md`'s framing of validation as the
sole gating milestone before further build investment is superseded by
this instruction for timing purposes; the validation work itself is not
descoped, only its sequencing relative to build.

---

## 16. Implementation-choice register (all remaining flexibility, in one place)

Everything Antigravity may vary, provided the described behavior is preserved:

1. Domain-Specific Verification's exact deterministic-vs-model split per output type (§7).
2. The exact deterministic/LLM split within the Prompting Capability (§5).
3. The precise mechanics of the "request missing seller evidence" step — upfront checklist vs. reactive batching implementation (§8).

Nothing else in this document is open.
