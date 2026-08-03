# MerchSage — Authoritative Product Intelligence Workflow

## Status and purpose

**Status: CURRENT AUTHORITATIVE PRODUCT-WORKFLOW CONTEXT**

This document exists to make the intended MerchSage product unambiguous to Claude or any other AI working on the project.

It defines:

- what MerchSage fundamentally is;
- what information the seller provides;
- how the product reasons about an underperforming Etsy business/listing;
- the responsibilities of the specialized AI agents;
- how evidence, reviews, business history, finances, competitors, and seller claims are used;
- how problems are discovered, confirmed, ordered, resolved, checked, formatted, and localized;
- which statements from older project documents are superseded.

This document primarily defines the **product intelligence workflow**. A separate document will define the **production engineering requirements**: security, authentication, authorization, payment protection, file-upload security, privacy, reliability, retries, databases, observability, deployment, abuse prevention, testing, backups, and other requirements needed to operate a real SaaS.

### Authority rule

If an older document conflicts with a statement explicitly marked **CURRENT / HARD DECISION** here, **this document wins for current product intent**. The older statement may still be retained as project history, but it must not be used to reconstruct the current product.

Do not silently simplify this architecture because an older version was easier to build.

---

# 1. The product in one sentence

> **MerchSage is a specialized multi-agent Etsy business diagnosis-and-resolution system that determines why a seller's product/listing is underperforming, constructs a product-specific map of every materially relevant problem that should be investigated, researches which of those problems actually exist using available evidence, orders the confirmed problems by root cause and resolution priority, generates or executes solutions for every supported solvable problem, verifies that those solutions are correct and mutually compatible, and delivers the result in a clear form and the seller's preferred supported language.**

MerchSage is **not primarily a listing rewriter**.

A rewrite is only one possible solution when copy is actually part of the diagnosed problem.

MerchSage is also **not**:

- a generic Etsy score;
- a static SEO checklist;
- a system that always returns only 2–3 recommendations;
- a generic ChatGPT wrapper;
- a single giant AI prompt that tries to perform every business responsibility at once.

---

# 2. The central product philosophy

The seller should not need to know what is wrong.

The seller gives MerchSage the product/listing/shop context and any private business information that the system cannot obtain externally.

MerchSage must then answer, in order:

1. **What is this business/product?**
2. **What performance problem are we dealing with?**
3. **What could plausibly be causing that problem for this specific product/business?**
4. **Which of those possibilities are actually supported by evidence?**
5. **What are the real root problems, and in what order should they be solved?**
6. **What can MerchSage actually do to solve each problem?**
7. **Are the proposed solutions correct, evidence-supported, feasible, and mutually compatible?**
8. **How should the verified result be presented so the seller can understand and act on it?**

The system must reason like a business investigator, not blindly optimize listing text.

---

# 3. Authoritative end-to-end workflow

The intended full-product workflow is:

```text
SELLER
  |
  v
INTAKE + AUTHORIZED DATA COLLECTION
  |
  +--> Etsy listing/shop/product context
  +--> Seller-stated differentiators / USP claims
  +--> Seller's own explanation of what they bring to the table
  +--> Relevant performance/history context
  +--> Optional business/cost documents when needed
  |
  v
SHARED STRUCTURED EVIDENCE BASE
  |
  v
PRODUCT UNDERSTANDING / CLASSIFICATION AGENT
  |
  v
PERFORMANCE DIAGNOSIS / ROUTING
  |
  +-------------------------------+
  |                               |
  v                               v
NO / LOW VIEWS                VIEWS BUT NO SALES
DISCOVERABILITY               CONVERSION
  |                               |
  +---------------+---------------+
                  |
                  v
ENTREPRENEUR AGENT
"What could plausibly be wrong for THIS exact business/product?"
                  |
                  v
PRODUCT-SPECIFIC INVESTIGATION / HYPOTHESIS MAP
                  |
                  v
RESEARCHER AGENT
"Which hypotheses are actually supported, contradicted,
unknown, mixed, or not applicable?"
                  |
                  v
EVIDENCE-BACKED FINDINGS
                  |
                  v
TRIAGE / PRIORITY ("LISTING") AGENT
- merge duplicates
- identify root causes vs symptoms
- build problem/dependency graph
- order resolution priority
                  |
                  v
RELEVANT SPECIALIST AGENTS
invoked dynamically for the confirmed domains/problems
                  |
                  v
RESOLUTION AGENT(S)
generate / execute / assist with solutions
                  |
                  v
SUPERVISOR / QC
checks task completion and targeted failures throughout pipeline
                  |
                  v
BUSINESS VERIFIER
checks each solution against evidence + root problem
and checks all solutions together for conflicts
                  |
                  v
VERIFIED SOLUTION SET
                  |
                  v
FORMATTER AGENT
                  |
                  v
LINGUISTIC / LOCALIZATION AGENT
                  |
                  v
FINAL SELLER DELIVERABLE
```

**Important:** The Supervisor/QC function is not limited to one point in this diagram. It can validate agent outputs throughout the workflow and trigger targeted retries when an assigned task was not completed correctly.

---

# 4. Both performance branches are definite parts of the product

## 4.1 Branch A — No / Low Views: Discoverability

This branch investigates why the product/listing is not being sufficiently discovered.

Possible investigation dimensions can include, depending on the product and evidence:

- search demand;
- search intent;
- keyword strategy;
- title/search alignment;
- tags;
- category/taxonomy;
- niche competitiveness;
- demand level;
- product-market/search fit;
- positioning;
- competition;
- listing presentation where it affects discovery;
- seasonal or historical changes;
- other category-specific discoverability factors.

These are examples, **not a closed checklist**.

The Entrepreneur Agent must be capable of identifying additional product-specific possibilities.

### Discoverability comparison requirement

Where the permitted evidence is available, Discoverability research should explicitly compare:

```text
Seller positioning / keywords
          ↕
Actual buyer search intent
          ↕
Competitor / category language and positioning
```

The purpose is not merely to copy competitor keywords. The system should determine whether the seller is aligned with how relevant buyers search, whether competitors reveal useful category/search patterns, and where the seller's current discoverability strategy diverges from buyer intent or marketplace language.

## 4.2 Branch B — Views But No Sales: Conversion

This branch investigates why people are discovering the product but not buying it.

Possible investigation dimensions can include:

- product differentiation;
- value proposition;
- price and perceived value;
- photos;
- video;
- trust;
- reviews;
- product/customer fit;
- positioning;
- description/copy;
- shipping or processing friction;
- policies;
- customization experience;
- quality concerns reflected in evidence;
- seller reputation/customer experience;
- competitive offer differences;
- category-specific purchase expectations;
- historical changes;
- other relevant causes.

Again, these are examples, not a closed checklist.

## 4.3 CURRENT / HARD DECISION — development order

**Both branches will be built.**

The development sequence is:

### Phase 1
Build the **No / Low Views — Discoverability** branch properly and completely enough to function as intended. Test it, debug it, refine it, and make it work reliably.

### Phase 2
After the Discoverability branch is successfully working, move to the **Views But No Sales — Conversion** branch and similarly build, test, debug, refine, and improve it.

This is an **order of development**, not a reduction in product scope.

The Conversion branch is **not optional**, **not abandoned**, and **not "only if time remains."**

Any older statement saying:

- Conversion is the launch-first branch;
- Discoverability is deferred;
- No-views will only be built if time remains;

is **SUPERSEDED**.

---

# 5. Intake: ask the seller what they bring to the table

MerchSage should explicitly ask the seller what they believe differentiates their product/business.

Possible selectable options can include:

- better quality;
- lower price / better value;
- customization / personalization;
- materials;
- handmade craftsmanship;
- unique design;
- sustainability;
- trust / reputation;
- faster or better service/shipping;
- another differentiator.

There should also be an **Other / seller-written field** where the seller explains, in their own words, what they believe they bring to the table.

This information is important because the AI cannot infer every private business advantage from an Etsy page.

### Critical rule: seller claims are hypotheses, not truth

Internally, these should be treated as:

`SELLER-CLAIMED STRENGTHS`

not automatically as:

`VERIFIED PRODUCT STRENGTHS`

Later evidence—especially customer reviews and market evidence—should test these claims.

The system must allow outcomes such as:

- **SUPPORTED** — customers/evidence strongly validate the claimed strength;
- **CONTRADICTED** — evidence pushes against the seller's belief;
- **MIXED** — evidence supports and contradicts it;
- **UNKNOWN / INSUFFICIENT EVIDENCE**;
- **NOT APPLICABLE**.

The system should also identify **unexpected strengths** customers value that the seller did not recognize.

Example:

```text
Seller believes:
"Our advantage is superior quality."

Customer evidence reveals:
- quality feedback is mixed;
- customization receives repeated praise.

Possible conclusion:
The seller's strongest customer-valued differentiator may be
customization rather than the quality claim they currently emphasize.
```

The purpose is not to tell the seller they are wrong arbitrarily. It is to compare seller belief against actual available evidence.

---

# 6. Shared structured evidence base

All agents should reason from a shared structured evidence base rather than repeatedly rediscovering facts or passing uncontrolled prose between themselves.

Potential evidence sources include:

- seller's Etsy listing/shop/product information obtained through sanctioned access;
- seller-authorized Etsy data;
- seller answers;
- seller-claimed differentiators;
- transaction/order/revenue history where sanctioned access provides it;
- reviews where sanctioned access provides them;
- comparable/competitor marketplace evidence;
- category and buyer-intent research;
- uploaded business documents;
- structured financial values extracted from those documents;
- other legally and technically permitted external research.

Important findings should preserve:

- source/provenance;
- evidence identifier where possible;
- timestamp/recency where relevant;
- whether the item is an observed fact, seller claim, external evidence, or inference;
- confidence/uncertainty.

### Hard rule

**Do not invent evidence because a useful data point is unavailable.**

Unavailable evidence is itself a valid state.

---

# 7. Product Understanding / Classification Agent

A dedicated Product Understanding / Classification Agent determines what the seller actually sells.

It can identify:

- product type;
- category;
- subcategory;
- likely buyer/use context;
- relevant product characteristics;
- other information needed for correct business reasoning.

Classification matters because different products fail for different reasons.

A jewelry listing, digital template, soap, clothing product, personalized gift, and home-decor item should not all receive the same investigation map.

This does **not** require hardcoding a separate permanent category agent for every possible Etsy category.

Instead, product/category understanding informs the Entrepreneur, Researcher, and dynamically selected specialist agents.

---

# 8. Performance diagnosis and routing

The system establishes the primary performance problem:

- No / Low Views → Discoverability investigation;
- Views But No Sales → Conversion investigation.

These branches are the major investigation missions.

However, the system should not become artificially blind to secondary evidence. If a seller's primary problem is discoverability but evidence also reveals another materially relevant issue, the system may preserve it as a secondary finding rather than pretending it does not exist.

The exact technical ordering of classification and routing does not need to be artificially frozen. They may interact.

The invariant is:

> **The system must understand the product and the performance problem before performing deep product-specific business diagnosis.**

---

# 9. Entrepreneur Agent — generate the complete investigation space

## 9.1 Why this agent exists

The Entrepreneur Agent is one of the defining parts of MerchSage.

Its job is **not** to decide what is actually wrong.

Its job is to think like an experienced entrepreneur/business operator and ask:

> **"For this exact product, category, seller, performance state, market context, seller claims, and available history, what could plausibly be preventing better performance, and what should be investigated before we reach a conclusion?"**

The reason this responsibility is separate from the Researcher is deliberate.

If the same agent must:

- decide what to investigate;
- research it;
- interpret the evidence;
- diagnose;
- prioritize;
- solve;

it may skip areas, forget tasks, or decide prematurely that something is not worth checking.

The Entrepreneur Agent creates an explicit investigation mandate.

The Researcher must then investigate that mandate.

## 9.2 The Entrepreneur must go beyond hardcoded developer knowledge

The Entrepreneur Agent should not merely expand a static list written by the developers.

It should use broad business dimensions as a safety net, then reason product-specifically to identify failure modes that the seller, developer, or earlier documentation may not have anticipated.

Examples of broad dimensions include:

- demand;
- customer;
- differentiation;
- value proposition;
- competition;
- pricing/value;
- trust;
- discoverability;
- presentation;
- conversion friction;
- reviews/customer feedback;
- historical change;
- seller reputation;
- product-specific expectations.

But the output must be **dynamic**.

The Entrepreneur Agent should be capable of saying:

> "For this particular type of personalized wedding product, there are three additional risks worth checking that are not relevant to most Etsy products."

That is the intended behavior.

## 9.3 Required output

The Entrepreneur Agent produces a structured **Investigation / Hypothesis Map**.

Each hypothesis should ideally contain:

- hypothesis/problem possibility;
- why it is plausible;
- evidence required;
- potential evidence source;
- whether that evidence appears available;
- relevant specialist domain if later required.

The Entrepreneur Agent must not manufacture conclusions.

---

# 10. Researcher Agent — test what could be wrong

The Researcher receives the Entrepreneur Agent's investigation map.

Its job is:

> **Determine what the evidence actually says about each required investigation item.**

### Hard requirements

The Researcher must:

- investigate every mandatory hypothesis unless it is explicitly not applicable or evidence is unavailable;
- not silently skip an Entrepreneur-mandated investigation because it personally considers it unimportant;
- gather the permitted evidence required for each hypothesis;
- distinguish observation from inference;
- preserve evidence/provenance;
- identify contradictions;
- state uncertainty;
- mark unavailable questions as unknown rather than hallucinating an answer;
- perform product-specific/category-specific research rather than a generic Etsy audit.

### Researcher may discover additional hypotheses

If research reveals a plausible new problem that the Entrepreneur Agent did not include, the Researcher should not ignore it.

It should:

1. record the new hypothesis;
2. identify why it emerged;
3. obtain or request the relevant evidence;
4. subject it to the same evidence standards as the original investigation map.

The Entrepreneur Agent is therefore a coverage mechanism, not a prohibition against learning new things during research.

---

# 11. Review intelligence

Reviews are not merely a star-rating metric.

They are evidence about what customers actually value, dislike, misunderstand, or experience.

Review analysis should identify:

- recurring strengths;
- recurring weaknesses;
- mixed themes;
- unexpected customer-valued differentiators;
- recurring complaints;
- changes in themes over time;
- whether seller-claimed strengths are supported;
- whether customers dislike something the seller believes is a strength;
- category-specific themes such as sizing, shipping, packaging, customization, durability, material quality, value, accuracy to photos, service, and other relevant dimensions.

### Efficient review analysis

If thousands of reviews exist, the system should not blindly feed every review to a model.

The objective is:

> **Maximum representative information with efficient processing.**

A future implementation can use techniques such as:

- recency sampling;
- positive/negative coverage;
- semantic clustering;
- representative review selection;
- theme frequency;
- distinct/outlier themes;
- temporal comparison.

Do not assume "top 10 most-liked reviews" is available unless the sanctioned data source actually provides a useful engagement/helpfulness field.

The number of representative reviews is not inherently fixed at 10.

### Shop-level seller reputation / trust evidence

Product-level reviews are only one part of the trust picture.

Where sanctioned Etsy access or other permitted evidence makes it available, the Researcher should also investigate relevant **shop-level seller reputation and customer-experience evidence**, such as:

- overall shop rating;
- recurring service/customer-support complaints or praise;
- shipping/processing experience themes;
- communication/service themes;
- repeated trust concerns;
- shop history or reputation signals relevant to buyer confidence;
- other shop-level evidence that is materially relevant to the diagnosed problem.

The purpose is to distinguish a problem with the individual listing/product from a broader seller/shop trust or customer-experience problem.

As everywhere else in this architecture, unavailable shop-level evidence must be marked unavailable rather than inferred or invented.

### Important data constraint

Exact Etsy review-access capabilities must be verified against the sanctioned Etsy interfaces during implementation.

Do not assume an undocumented capability exists.

---

# 12. Historical / temporal diagnosis

Current performance alone may be misleading.

The system must distinguish situations such as:

- the product has always struggled;
- the product previously performed well and later declined;
- views dropped while conversion remained stable;
- views remained stable while sales/conversion declined;
- reviews or customer sentiment changed;
- performance is seasonal;
- another meaningful change event occurred.

If a product sold well before and later declined, the Entrepreneur Agent should explicitly investigate **what changed**.

Possible hypotheses can include:

- price changes;
- review/rating deterioration;
- new complaint clusters;
- shipping/processing changes;
- listing changes where history is available;
- product/variant availability;
- competitor entry;
- competitor pricing/offer changes;
- seasonality;
- demand shifts;
- traffic/discoverability changes;
- seller reputation/customer experience;
- other category-specific changes.

Again: these are hypotheses to test, not automatic diagnoses.

If historical evidence cannot be obtained, the system must say so.

---

# 13. Financial documents and profitability analysis

A seller may optionally upload documents/files containing private business economics, such as:

- production/manufacturing costs;
- material costs;
- packaging costs;
- seller-paid shipping costs;
- advertising costs;
- supplier information;
- other variable costs;
- relevant fixed costs;
- other information needed for a requested financial analysis.

The seller should not be forced to manually type every value if a usable file already contains the information.

Financial uploads are **not mandatory for every audit**.

They are requested/used when financial or profitability analysis is relevant.

## 13.1 Financial Extraction Agent

This specialized agent extracts structured financial values from seller-provided files.

For each important value it should preserve:

- extracted value;
- source;
- confidence;
- relevant period/unit;
- whether human/seller confirmation is required.

It must not invent missing costs.

## 13.2 Profitability / Financial Analysis Agent

This agent receives verified structured financial values plus relevant sales/revenue evidence.

It performs the appropriate business calculation.

**Revenue must never be confused with profit.**

Profitability requires costs that Etsy alone may not know.

If required cost information is missing, return:

- insufficient data;
- the missing values required;
- or a clearly qualified estimate only if the user explicitly supplies/approves assumptions.

Do not silently guess.

---

# 14. Evidence-backed problem set

The goal of research is not to produce a predetermined number of problems.

The goal is:

> **Find every materially relevant problem supported by the available evidence.**

If there are 2 real problems, return 2.

If there are 8, return 8.

If there are 15, return 15.

Do **not**:

- cap the output at 2–3;
- invent additional faults to make the analysis appear comprehensive;
- treat weak speculation as a confirmed problem.

Every important hypothesis/finding should be capable of ending in states such as:

- SUPPORTED;
- CONTRADICTED;
- MIXED;
- UNKNOWN / INSUFFICIENT EVIDENCE;
- NOT APPLICABLE.

---

# 15. Triage / Priority Agent ("Listing Agent")

The user's term **Listing Agent** refers here to the agent that takes the confirmed problem set and determines **what should be resolved first**.

It is not simply the agent that writes Etsy listing copy.

Its responsibilities include:

- merge duplicate findings;
- separate root causes from symptoms;
- identify dependencies;
- estimate severity/importance;
- consider evidence confidence;
- consider likely impact;
- consider feasibility;
- determine resolution order.

## 15.1 Problem graph, not merely a flat list

Problems may depend on one another.

Example:

```text
Wrong understanding of buyer search intent
            |
            v
Weak keyword strategy
       /         \
      v           v
Weak title     Weak tags
```

If the root search-intent strategy is wrong, rewriting the title before fixing the strategy may waste work.

The Triage Agent should therefore produce a **problem/dependency graph** or equivalent structured ordering, not merely sort independent bullets.

## 15.2 Prioritization does not hide problems

Prioritization means:

> "Fix these first."

It does **not** mean:

> "Only show the top three and discard the rest."

All materially relevant evidence-supported problems remain part of the diagnosis.

---

# 16. Specialized categorical agents — hard architectural principle

**CURRENT / HARD DECISION**

Every materially distinct categorical AI reasoning responsibility should be assigned to an AI agent purpose-built for that task.

Examples may include:

- Discoverability / SEO Agent;
- Pricing Agent;
- Profitability Agent;
- Financial Extraction Agent;
- Review / Customer Feedback Agent;
- Trust / Reputation Agent;
- Positioning / Differentiation Agent;
- Copy Agent;
- Image / Visual Agent;
- Video / Creative Agent;
- other agents discovered when the complete business-problem taxonomy is researched.

This list is illustrative, not final.

### Why specialization exists

Specialization is intentional because assigning too many unrelated responsibilities to one agent can:

- reduce task coverage;
- make instructions easier to forget;
- blur accountability;
- make verification difficult;
- cause the model to decide prematurely that a category is not worth investigating.

Each specialized agent should eventually have a contract defining:

- purpose;
- inputs;
- mandatory checks;
- allowed evidence/tools;
- required output schema;
- evidence requirements;
- forbidden conclusions/actions;
- pass criteria;
- failure conditions.

### Dynamic invocation

Specialization does **not** mean every customer triggers every agent.

Only agents relevant to the confirmed problems/investigation should run.

For example:

```text
Pricing/profitability implicated -> financial/pricing specialists
Search discovery implicated      -> discoverability specialist
Review trust issue implicated    -> review/trust specialist
Weak images implicated           -> visual specialist
Positioning implicated           -> positioning specialist
```

This gives specialization without unnecessary computation.

---

# 17. Resolution layer — solve the problem, do not merely describe it

For each confirmed problem, MerchSage should determine what kind of resolution is possible.

## 17.1 Directly solvable

MerchSage should generate or execute the actual fix when it can responsibly do so.

Examples:

- improved title;
- better tags;
- rewritten description;
- stronger positioning/message;
- improved tagline;
- structured keyword strategy;
- other generated artifacts.

## 17.2 Assistively solvable

When the system cannot directly execute the final external action, it should still produce concrete assistance such as:

- detailed creative direction;
- image-generation/editing prompt;
- video concept;
- storyboard;
- implementation plan;
- experiment;
- other actionable artifact.

## 17.3 Seller action required

When the system cannot responsibly solve something itself, it should clearly tell the seller:

- what the problem is;
- what evidence supports it;
- uncertainty/confidence;
- exactly what action/test is required.

### Image/video integrations

Image and video generation/editing can be part of the full resolution vision.

No specific provider is permanently locked merely because it was discussed.

Provider selection is an implementation decision unless separately finalized.

### Safety boundary

Do not make unsupported high-stakes judgments such as:

- whether food/ingredients are medically safe;
- medical efficacy;
- other safety conclusions that the available evidence/model cannot responsibly verify.

---

# 18. Supervisor / Quality-Control Agent

A dedicated Supervisor/QC Agent monitors whether other AI agents correctly completed their assigned tasks.

It is a **quality-control agent**, not the application's cybersecurity system.

The Supervisor should be able to detect:

- skipped mandatory hypotheses;
- missing required fields;
- unsupported conclusions;
- evidence that does not support the claim;
- an agent drifting outside its responsibility;
- incomplete task execution;
- generic output that fails to answer the product-specific task;
- missing mandatory domain checks;
- malformed structured output.

### Targeted retries

If one task fails, do not automatically restart the entire audit.

Example:

```text
Researcher was required to investigate H1-H14.
H1-H11 completed.
H12-H14 skipped.

Supervisor:
FAIL H12-H14 only.
Return exact missing tasks and failure reason.
Retry those tasks.
```

Retries must be bounded.

Persistent failure must become an explicit state such as:

- INSUFFICIENT CONFIDENCE;
- INSUFFICIENT EVIDENCE;
- ESCALATION / MANUAL REVIEW REQUIRED;

rather than an infinite retry loop.

### AI verification is not enough by itself

Where possible, deterministic software should validate:

- schemas;
- required fields;
- evidence IDs;
- numeric formats;
- task completion;
- impossible state transitions;
- other machine-verifiable requirements.

The Supervisor handles judgment that deterministic validation cannot fully perform.

---

# 19. Business Verifier Agent

The Business Verifier is different from the Supervisor.

### Supervisor asks:

> **"Did this agent correctly perform the task it was assigned?"**

### Business Verifier asks:

> **"Is this proposed business solution actually justified and coherent?"**

The Verifier should check:

- does the solution address the diagnosed root problem?
- does the evidence support it?
- is it feasible for this seller?
- is it sufficiently product-specific?
- is it merely generic advice?
- does it introduce unsupported claims?
- could it worsen another diagnosed problem?
- does it respect problem dependencies?
- does the complete solution set make sense as one business strategy?

## 19.1 Cross-solution compatibility — hard requirement

One problem's solution must not silently damage another problem's solution.

Example conflict:

```text
Solution A:
Cut price aggressively.

Solution B:
Reposition as a premium handcrafted product.
```

These may be strategically inconsistent.

The Verifier must therefore perform:

1. **individual solution verification**;
2. **solution-to-original-problem/evidence verification**;
3. **cross-solution compatibility checking**;
4. **global strategy coherence checking**.

If a solution fails, it should be rejected/revised rather than quietly delivered.

## 19.2 Verifier feedback loop — targeted correction

Verification is not merely a final pass/fail label.

When the Verifier finds that a specific solution is unsupported, ineffective, infeasible, inconsistent with the diagnosed root problem, or in conflict with another solution, it should return the **exact failed solution and failure reason** to the responsible Resolution/Specialist Agent.

Conceptually:

```text
Resolution / Specialist Agent
          |
          v
Business Verifier
     |         |
    PASS      FAIL
     |         |
     |         v
     |   exact failed solution
     |   + failure reason
     |         |
     |         v
     |   responsible agent revises
     |         |
     |         v
     |      re-verify
     |         |
     +---------+
          |
          v
Verified Solution Set
```

The system should retry the failed solution rather than unnecessarily regenerating unrelated solutions that already passed verification.

These retries must be bounded. If a solution cannot be brought to an acceptable evidence/confidence standard after the allowed attempts, it should become an explicit unresolved/escalated state rather than being silently included in the final deliverable.

After individual corrections, the Verifier must still perform the **global cross-solution compatibility check** before the solution set is considered verified.

---

# 20. Traceability

The final system should preserve a trace from the delivered recommendation back to why it exists.

Conceptually:

```text
FINAL SOLUTION
      |
      v
CONFIRMED PROBLEM
      |
      v
SUPPORTING EVIDENCE
      |
      v
INVESTIGATION HYPOTHESIS / SOURCE
```

A final recommendation should not appear from nowhere.

This traceability is important for:

- credibility;
- debugging;
- verification;
- explaining uncertainty;
- preventing hallucinated advice.

---

# 21. Formatter Agent

After the business solution set has been verified, a dedicated Formatter Agent turns the structured analysis into a human-friendly deliverable.

It should not change the underlying business conclusions.

The final report should make it easy to understand:

- what performance problem was diagnosed;
- what evidence was examined;
- what the seller claimed their strengths were;
- which strengths evidence supports;
- which claims are contradicted/mixed/unknown;
- unexpected strengths discovered;
- confirmed weaknesses/problems;
- root causes and problem dependencies;
- resolution priority;
- what MerchSage has already generated/solved;
- what the seller still needs to do;
- evidence/confidence;
- unavailable evidence and unresolved questions.

---

# 22. Linguistic / Localization Agent

The full intended product includes a final Linguistic / Localization Agent.

It converts the **already verified canonical report** into the seller's preferred supported language/style.

Potential examples:

- English;
- Hindi;
- Hinglish;
- Marathi;
- additional languages later.

The architecture can be extensible to many languages, but the launch product should expose only languages that can be reasonably tested.

Do not assume a separate Google Translate step is required.

Gemini is multilingual and the implementation may use Gemini or other appropriate localization tooling.

### Hard rule

The Linguistic Agent may change **presentation/language only**.

It must not change:

- numbers;
- evidence;
- confidence;
- diagnoses;
- product facts;
- priorities;
- URLs;
- recommendations;
- solution meaning.

Hinglish should be treated as natural localization, not literal formal-Hindi translation.

---

# 23. Evidence and confidence discipline

MerchSage should distinguish:

### Observed fact
Example: a listing currently uses a particular tag.

### Seller claim
Example: the seller says their material quality is superior.

### External evidence
Example: customer reviews repeatedly praise customization.

### Inference
Example: customization may be a stronger differentiator than the seller currently communicates.

### Confidence / uncertainty
The system should communicate how strongly the evidence supports the conclusion.

Do not turn correlation into guaranteed causation.

Do not promise:

> "This change WILL increase your sales."

unless the evidence genuinely justifies that level of certainty.

MerchSage provides evidence-driven diagnosis, solutions, and actionable deliverables—not guaranteed business outcomes.

---

# 24. Data capability must constrain claims

The Entrepreneur Agent may generate excellent questions that the system cannot answer with available data.

That is acceptable.

Each investigation should ideally track:

```text
Hypothesis
Evidence required
Potential evidence source
Evidence availability
Finding
Confidence
```

If the evidence is unavailable:

> **UNKNOWN / INSUFFICIENT EVIDENCE**

is the correct answer.

Do not fabricate:

- historical views;
- listing revisions;
- competitor history;
- profitability;
- review engagement;
- any other unavailable fact.

Exact Etsy capabilities—especially review access, historical views/stats, listing history, and competitor-history data—must be verified against sanctioned Etsy documentation during implementation.

---

# 25. Etsy data principles

Automated Etsy scraping is **not** part of the intended system.

Use sanctioned Etsy access/API capabilities.

Current implementation research should verify exactly what Personal App / sanctioned access permits before assuming specific endpoints/data are available.

Comparable/competitor marketplace information should come from permitted mechanisms.

Seller-provided competitor links may supplement the investigation where useful, but they do not justify prohibited automated scraping.

The Etsy API/data layer is evidence infrastructure.

It is **not the product**.

The product value is the diagnosis-and-resolution intelligence built on top of permitted evidence.

---

# 26. No fixed Gemini/model call count

**HARD CORRECTION**

There is no valid current architecture of:

> "~5 Gemini calls/customer."

That came from an obsolete simplified pipeline and must not be used.

The actual number of agent/model executions is dynamic and can depend on:

- product/category;
- performance branch;
- investigation hypotheses;
- evidence availability;
- confirmed problems;
- specialist agents required;
- resolution tasks;
- Supervisor failures;
- bounded retries;
- verification needs.

The engineering phase must still control:

- cost;
- latency;
- token usage;
- quotas;
- runaway loops;

but it must do so against the real dynamic workflow, not by pretending every audit contains five calls.

---

# 27. Full product architecture vs development sequence

Do not confuse these two concepts.

## Full intended product architecture

Includes:

- both performance branches;
- Entrepreneur;
- Researcher;
- specialized domain agents;
- Triage/Priority;
- Resolution;
- Supervisor/QC;
- Business Verifier;
- Formatter;
- Linguistic/Localization;
- evidence/provenance;
- seller private context;
- reviews;
- financial analysis where relevant;
- temporal diagnosis;
- other necessary product-specific capabilities.

## Development sequence

1. Build and perfect the Discoverability / No-Low-Views branch.
2. Then build and perfect the Conversion / Views-But-No-Sales branch.
3. Integrate/refine the complete product.

Do not reinterpret the sequential development order as removal of the second branch.

---

# 28. Known superseded interpretations — DO NOT USE AS CURRENT PRODUCT TRUTH

The following interpretations have repeatedly contaminated older context and must not be used to describe the current product:

### SUPERSEDED
> "MerchSage is mainly an AI listing rewrite tool."

**Current:** diagnosis and resolution; rewrite is only one possible fix.

### SUPERSEDED
> "Find the top 2–3 recommendations."

**Current:** find every materially relevant evidence-supported problem. Prioritize them, but do not cap them.

### SUPERSEDED
> "The complete pipeline is classify -> diagnose -> recommend -> rewrite -> translate."

**Current:** that is an obsolete simplification and omits the Entrepreneur, comprehensive investigation, evidence validation, triage/problem dependencies, specialist agents, resolution, QC, verification, and other current architecture.

### SUPERSEDED
> "~5 Gemini calls/customer."

**Current:** dynamic agent/model execution.

### SUPERSEDED
> "Views But No Sales / Conversion is built first and No Views is deferred."

**Current:** both branches are definite. Discoverability is built/perfected first; Conversion is built/perfected second.

### SUPERSEDED
> "Conversion is only built if time remains."

**Current:** Conversion remains a definite part of the intended product and follows Discoverability in development order.

### SUPERSEDED
> "One general reasoning agent can handle all categorical responsibilities."

**Current:** distinct categorical AI reasoning responsibilities intentionally use specialized agents, invoked when relevant.

### SUPERSEDED
> "Prioritization means only the highest few problems are returned."

**Current:** prioritization determines resolution order; it does not erase lower-priority real problems.

### SUPERSEDED
> "Seller-stated USP is accepted as the product's true differentiator."

**Current:** seller USP is a hypothesis tested against reviews/evidence, and MerchSage can discover different customer-valued strengths.

### SUPERSEDED
> "An AI security agent should enforce application security."

**Current:** Supervisor/QC monitors AI work. Production security must later be enforced primarily by deterministic software controls, covered in a separate engineering document.

---

# 29. Specialized multi-agent architecture — final clarification

This project intentionally uses specialized AI agents.

That does **not** mean:

- every agent runs on every customer;
- every agent needs an independent server/process;
- agents should be allowed unrestricted access to every tool;
- complexity should be added merely to call the product "multi-agent."

It means:

> **A distinct reasoning responsibility gets a distinct agent contract, and the orchestration layer invokes the agents required for the current investigation.**

The implementation details of orchestration can be decided during engineering.

The product requirement is **specialized responsibility and accountability**.

---

# 30. Production engineering is mandatory but documented separately

The intelligence workflow above is not enough to operate a real website/SaaS.

A separate authoritative **Production Engineering Requirements** document must cover at minimum:

- authentication;
- authorization;
- Etsy OAuth security;
- payment security;
- webhook verification;
- payment bypass prevention;
- secrets management;
- API security;
- rate limiting;
- abuse/fraud;
- prompt injection;
- file-upload security;
- financial-document privacy;
- data retention/deletion;
- agent/tool least privilege;
- database integrity;
- concurrency/isolation;
- retries;
- idempotency;
- external API failures;
- observability/logging;
- error tracking;
- AI output validation;
- cost controls;
- bounded agent execution;
- backups/recovery;
- deployment;
- testing;
- delivery failures;
- legal/compliance boundaries;
- other requirements necessary for a secure, reliable paid SaaS.

**Hard principle for that engineering phase:**

> **AI performs judgment. Deterministic software enforces security, permissions, payment state, integrity, quotas, and other rules that must not depend on model opinion.**

Do not treat the absence of those implementation details from this workflow document as permission to ignore them.

---

# 31. What remains intentionally unresolved

The following should **not** be silently invented by Claude:

- the final complete taxonomy/count of specialist agents;
- exact prompts for every agent;
- exact orchestration framework;
- exact model used for every task;
- exact model-call count;
- exact retry limits;
- exact image/video provider;
- exact set of launch languages;
- exact review-sampling algorithm;
- exact Etsy data available under sanctioned access;
- exact mechanism for historical views/stats if not exposed by Etsy;
- exact implementation of the evidence store;
- exact financial file formats supported;
- exact production security architecture;
- exact current repository implementation state unless the repository is actually inspected.

These are implementation/research decisions, not excuses to reinterpret the product.

---

# 32. Claude understanding test — mandatory before rewriting project context

Before Claude modifies canonical project documentation or produces a major implementation plan from this document, it should first restate the product and answer these questions:

1. What is MerchSage fundamentally: rewrite tool, score/audit, or diagnosis-and-resolution system?
2. Are both performance branches part of the intended product?
3. Which branch is built first, and what happens after it works?
4. What information does the seller provide about what they bring to the table?
5. Why are seller-stated strengths treated as hypotheses?
6. How can reviews reveal both strengths and weaknesses?
7. What is the Entrepreneur Agent's exact responsibility?
8. Why is the Entrepreneur separate from the Researcher?
9. What must the Researcher do with Entrepreneur-mandated hypotheses?
10. What happens when evidence cannot be obtained?
11. What does the Triage/Priority ("Listing") Agent do?
12. Why is the output a problem/dependency graph rather than only a sorted flat list?
13. Does prioritization cap the number of problems?
14. Why are distinct categorical tasks assigned to specialized agents?
15. Do all specialist agents run for every seller?
16. What does the Resolution layer do beyond giving advice?
17. What does the Supervisor/QC Agent check?
18. How is the Business Verifier different from the Supervisor?
19. How does the Verifier ensure one solution does not damage another?
20. What trace should exist from a final solution back to evidence?
21. Is the number of Gemini/model calls fixed?
22. What role does the Linguistic Agent play?
23. What is the difference between the full intended product architecture and the current development sequence?
24. Which recurring older interpretations are explicitly superseded?
25. Why will production security be handled separately and not entrusted to an AI "security agent"?

If Claude's reconstruction contradicts a **CURRENT / HARD DECISION** in this document, Claude must treat its own reconstruction as wrong and correct it before proceeding.

---

# 33. Final instruction to Claude

Do not reduce MerchSage to a generic Etsy audit because that is easier to summarize.

Do not reduce it to:

`classify -> diagnose -> recommend -> rewrite`.

Do not impose a 2–3 recommendation cap.

Do not assume five Gemini calls.

Do not treat seller claims as verified truth.

Do not skip investigation categories merely because the Researcher thinks they are inconvenient.

Do not hallucinate evidence when a data source is unavailable.

Do not confuse prioritization with omission.

Do not confuse Supervisor/QC with Business Verification.

Do not confuse AI quality control with cybersecurity.

Do not treat the Conversion branch as optional.

Do not turn unresolved implementation choices into finalized decisions.

The intended MerchSage product is a **specialized, evidence-driven, hypothesis-driven, multi-agent business diagnosis-and-resolution system**. It should first understand the seller/product and performance state, deliberately construct the complete relevant investigation space, research what is actually wrong, identify root problems and dependencies, invoke the relevant specialists, solve what can be solved, verify the entire solution strategy, and deliver the verified result clearly to the seller.

That is the product architecture this document is intended to preserve.
