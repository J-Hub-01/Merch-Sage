### **1\. Etsy AI/ML clause — don't let it block coding**

**Problem:** We don't yet know whether Etsy permits API-derived Etsy content to be sent to Gemini for MerchSage's analysis. The pipeline itself explicitly leaves this unresolved.

**Solution: two-track implementation.**

Send the Etsy authorization/clarification request immediately. But Antigravity builds the pipeline using the Evidence Object abstraction already defined in §1 and the data-source-agnostic design in §14.

Until permission is resolved:

`Etsy API → normal software processing/storage`

but don't enable:

`Etsy API content → Gemini`

in production if that usage hasn't been cleared.

Meanwhile:

`Seller voluntarily uploads/provides permitted evidence → AI pipeline`

can be the fallback **subject to the applicable terms/privacy rules**.

This means **build continues; production data routing remains gated.**

---

### **2\. Gemini quota/cost — solve during implementation with a budget controller**

Claude is right that we shouldn't just hope dynamic invocation stays cheap.

But **do not reduce the architecture because of hypothetical quota problems yet.**

Antigravity should implement a central **Model Budget Controller**.

Every proposed model call goes through:

`Agent → Budget Controller → model`

The controller tracks:

* model used;  
* input/output tokens;  
* estimated/actual cost;  
* calls by agent;  
* total audit cost;  
* retries;  
* expensive media generations.

And the existing rule remains:

> irrelevant specialist \= **zero calls**.

Also, shared evidence means Researcher researches once; specialists consume Evidence Objects rather than independently repeating research.

Then establish actual budgets after measuring several test audits.

So we don't guess today that an audit requires 8, 15 or 30 calls.

**Measure → profile → optimize → set production ceilings.**

The final pipeline already requires retries to remain under the per-audit cost ceiling.

---

### **3\. Aug 17 scope — this is the biggest issue**

Claude is correct here.

**Do NOT try to production-perfect every possible MerchSage capability before August 17\.**

But also **do not create another reduced architecture.**

There's a difference between:

**Product architecture**

and

**competition implementation coverage.**

The Final Working Pipeline remains the product architecture.

Antigravity implements it vertically, prioritizing the most important paths first.

For example:

**Must work end-to-end first:**

`Intake → Classification → Diagnosis → Entrepreneur → Researcher → Triage → selected Specialists → Verification → Business Verifier → Report`

Then add high-value specialist coverage.

You do **not** need every specialist equally mature on Day 1\.

If Video/Creative isn't sufficiently reliable by the submission date, the architecture doesn't change. That specialist simply isn't production-ready yet.

This avoids making a second “MVP architecture” that we'll later have to reconcile again.

---

### **4\. Manual-fulfillment backlog**

Claude is right that if validation suddenly gives you 30 customers while the product isn't finished, manually fulfilling 30 complex audits is ridiculous.

So don't promise unlimited immediate fulfillment.

During validation use a **controlled beta queue**.

For example:

> Early Access / Limited Beta — limited audit slots.

Accept only as many sellers as you can actually service.

If demand exceeds capacity:

`customer → waitlist`

not:

`customer → payment → impossible backlog`.

Once automation is stable, increase capacity.

This is also valuable validation: if people are willing to join a waitlist or pay when capacity opens, that's meaningful demand evidence.

---

### **5\. Razorpay KYC / Etsy Personal App approval**

These should be treated as **parallel external dependencies**, not software blockers.

Start/continue them immediately.

Antigravity should put provider abstractions around both:

`PaymentService`

and

`MarketplaceEvidenceProvider`

so the core MerchSage pipeline isn't coupled to one external approval.

For development:

payment sandbox/test mode \+ mocked/test Etsy evidence can exercise the architecture.

For real production transactions/data, switch to approved credentials when available.

**External approval waiting time should overlap with development time.**

---

### **6\. Organizer questions — we cannot architect our way around these**

Claude is correct.

If XPRIZE/Devpost hasn't explicitly answered:

* what qualifies under AI-Native Operations;  
* how revenue/refunds/customer concentration should be counted;

then these remain **competition-rule uncertainties**.

Solution:

**send the organizer questions now.**

But don't stop development.

For revenue, preserve raw evidence so we can compute whichever interpretation they eventually require:

`gross payments`

`refunds`

`chargebacks`

`net revenue`

`customer`

`transaction date`

`payment ID`

`tier`

etc.

Then if organizers say “use net revenue,” we calculate net.

If they say “gross qualifying revenue,” we calculate gross.

**Store the facts now; decide the reporting formula once clarified.**

---

### **7\. “The architecture is too large”**

This is the important conceptual correction.

We should **not delete agents just to make the diagram smaller**.

Remember one of our original principles:

> Don't run irrelevant agents.

“10+ agent roles” does **not** mean every audit runs 10+ expensive LLM calls.

Some are roles/capabilities.

Some are deterministic.

Some are conditional.

Some share evidence.

Some don't run at all for a given seller.

The implementation strategy should therefore be:

**Build the orchestration skeleton once.**

Then progressively enable specialist capabilities.

That gives us:

`same architecture + increasing capability coverage`

instead of:

`temporary architecture → competition architecture → real architecture`

which would waste even more time.

---

## **So what is ACTUALLY left before coding?**

Nothing architectural.

But there are now **five parallel workstreams**:

| Workstream | Action |
| ----- | ----- |
| **Antigravity** | Start core pipeline implementation immediately |
| **Etsy** | Send AI/API-use clarification \+ continue access verification |
| **Gemini** | Instrument every model call; measure real quota/cost during testing |
| **Payments** | Resolve KYC while implementing test/sandbox payment flow |
| **Competition/Validation** | Ask organizer questions \+ start controlled seller validation/beta |

