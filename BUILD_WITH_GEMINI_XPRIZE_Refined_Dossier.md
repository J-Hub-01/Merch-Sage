# BUILD WITH GEMINI XPRIZE — RESEARCH DOSSIER
### Prepared for: solo, $0-budget, self-taught, no-audience, India-based, vibe-coding builder

*A genuine merge of two source documents — the competition-requirements intelligence report and the opportunity-elimination report — with duplicated material consolidated rather than repeated. Nothing in either original document has been cut, summarized, or reinterpreted; only the overlapping framing (headers, timeline framing, and shared sources) has been collapsed into one copy. Compiled from the original research passes of July 25–26, 2026; this front matter was refreshed August 1, 2026.*

---

## How to read this document

- **Part One — Definitive Intelligence Document.** Everything about the competition itself: eligibility, judging, submission requirements, prizes, risks. (Originally "Doc 1.")
- **Part Two — Opportunity Elimination Document.** Market research, idea elimination, and the single surviving product concept. (Originally "Doc 2," written after Part One and treating it as established context.)
- **Unified Source Log** (end of document) — every citation from both originals, deduplicated. Entries cited by both original documents (e.g. the XPRIZE press release, the Devpost homepage) now appear once.

---

## ⏱ Current timeline (reconciled)

The two original documents were compiled a day apart and each described "days remaining" as of their own compile date — Part One said **~23 days as of July 25, 2026**; Part Two said **~22 days as of July 26, 2026**. Both are correct for the date they were written, but neither is current by the time anyone actually reads this.

**Deadline: August 17, 2026, 1:00pm PT.** Do not trust either "~22" or "~23" days as a live figure — recompute from *today's* actual date against Aug 17, 2026 every time this document is opened. As of this refresh (Aug 1, 2026), that's **~16 days remaining**.

---

## 🔗 Live pages to check every session (not static — check fresh each time)

These two pages change without notice and are the fastest way to catch organizer clarifications or new deadlines before they blindside a submission:

- **Updates:** https://xprize.devpost.com/updates
- **Discussions / forum topics:** https://xprize.devpost.com/forum_topics

**⚠ Discrepancy flagged, unresolved as of Aug 1, 2026:** both original documents cite specific forum threads and updates in the **44000–45400 ID range** (e.g. `44263`, `44581`, `45364`) and state **"21,900+ registered participants"** as a verified fact. A live check of the two links above on Aug 1, 2026 showed only **4 forum threads, IDs in the 43827–43830 range**, **zero posted updates**, and a participant counter reading **392–533** (the two pages disagreed with each other on the exact number). None of the specifically-cited threads from the original research were visible on the live pages at check time. This could mean the counter/thread numbering behaves differently when not logged in, that the original figures were mistaken, or something else — it wasn't resolved, only flagged. **Before relying on any specific participant count, forum thread, or update cited in Part One or Part Two, re-verify it against the live links above rather than trusting the number as-is.**

---
## PART ONE — DEFINITIVE INTELLIGENCE DOCUMENT
### (Competition requirements, eligibility, judging, submission mechanics, risks)

## **1\. EXECUTIVE SUMMARY — THE 15 THINGS THAT SHOULD CHANGE WHAT YOU BUILD**

Ranked strictly by how much each item should alter build decisions **today** (not by how impressive the fact is). Every item is derived from the rules, FAQ, glossary, workshop transcript, or organizer forum answers cited in Section 11\.

* **This is not a hackathon. It is a compressed operating-business audit.** Judges do not score potential, features, prototypes, or ideas. They score three things — Business Viability, AI-Native Operations, Category Impact — with equal weight, and Business Viability is explicitly defined as *earned revenue from arms-length customers plus a business model that can sustain the activity beyond the hackathon window*. **\[VERIFIED — 2+ independent sources: [Official Rules §6](https://xprize.devpost.com/rules), \[Business Viability Workshop transcript\]\]([https://www.youtube.com/watch?v=5BgvnDyP2dw](https://www.youtube.com/watch?v=5BgvnDyP2dw))**  
* **"Newly created" is enforced against the business, not the code or entity.** The GitHub repo may reuse open-source, boilerplate, or generic frameworks (disclose them), and you may use a **pre-existing LLC or company**, but the *business activity* — the specific product/service being sold — must have started **on or after May 19, 2026**. Reusing an existing product with a new feature is explicitly disqualified. **\[VERIFIED — 2+ sources: [FAQ](https://xprize.devpost.com/details/faq), [Orientation transcript](https://www.youtube.com/watch?v=tf5RPGJvQKw)\]**  
* **The single hardest, least-appreciated hurdle for a $0/no-audience/India builder is not the tech — it is arms-length paying customers with harvestable name/email/phone.** Rules require customer contact info (name, email, phone), and the submission form specifically asks you to confirm no single customer \>40% of revenue. Friends/family/existing network sales get segmented into "Related-Party Revenue" and **judges explicitly strip that out** when assessing viability. **\[VERIFIED — 2+ sources: [Submission Deep-Dive](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it), \[Business Viability Workshop transcript\]\]([https://www.youtube.com/watch?v=5BgvnDyP2dw](https://www.youtube.com/watch?v=5BgvnDyP2dw))**  
* **"AI-Native" is legally defined and it disqualifies most naive interpretations.** The Hacker Fund glossary defines AI-native as *"designed with artificial intelligence as the core component from the ground up, rather than bolted on later as a feature."* Judges assess **the extent to which AI is live in production and executes key decisions.** A ChatGPT-wrapper SaaS with a human ops team is technically compliant but will score at the floor of the AI-Native dimension. **\[VERIFIED — 2+ sources: [Glossary of Terms](https://docs.google.com/document/d/1-V-Wwr6NwhBQ6kj0pVGy5FfMBSQ-gkXSfc6BRoZ9CBA/edit), [Official Rules §6](https://xprize.devpost.com/rules)\]**  
* **You are effectively running against a 21,900+ person cohort with 25 total prize slots**, meaning a bare pass on all three criteria is not competitive — the winning submission must be excellent on at least two dimensions and defensible on the third. Approx. 21,866–21,925 registered participants per the live Devpost header as of late July 2026\. **\[VERIFIED — 2+ sources: [Devpost header captured on rules page](https://xprize.devpost.com/rules), [homepage snapshot](https://xprize.devpost.com/)\]**  
* **India IS eligible. India is not on the OFAC/prohibited list** (Russia, Crimea, Cuba, Iran, North Korea explicitly excluded). Age of majority in India (18) is met. No adverse rule for Indian participants in the official rules. **\[VERIFIED — single official source: [Rules §3](https://xprize.devpost.com/rules)\]** Because prize payout requires W-8BEN and a bank account capable of receiving USD, plan the banking pipeline now.  
* **Solo participation is explicitly permitted.** No team-size penalty. No prize-split adjustment for solo winners. FAQ confirms individuals may enter alone. **\[VERIFIED — [FAQ](https://xprize.devpost.com/details/faq)\]** This eliminates one competitive disadvantage but does not offset the marketing/audience gap versus larger teams.  
* **The $300 Google Cloud credit is for NEW GCP customers only, is a 90-day credit, and CANNOT be used to pay Gemini API in AI Studio.** If you have ever been a paying Google Cloud/Firebase/Maps user, you are not eligible for the free trial. This is a hidden budget-killer for anyone who used GCP for a college project. **\[VERIFIED — [Google Cloud Free Trial docs](https://docs.cloud.google.com/free/docs/free-cloud-features)\]** Route Gemini through Vertex AI (which the $300 credit does cover) or use the Gemini API free tier for a fallback.  
* **There is a separate, discretionary "affordability" coupon program** offering 3 months free of the Google AI Ultra plan — subject to ID verification and organizer review. Apply immediately: [Affordability form](https://forms.gle/fim2oukB7hq6zZnk8). Independent of the $300 GCP credit. **\[VERIFIED — [FAQ](https://xprize.devpost.com/details/faq), organizer comment in [$300 credit forum thread](https://xprize.devpost.com/forum_topics/44263-clarification-on-300-cloud-credit)\]**  
* **"Revenue" is cash-basis, in USD, arms-length, and reported by-month (May, June, July, August 2026).** Grants, donations, sponsorship, and investment are explicitly disqualified as revenue for the Business Viability score — nonprofit "earned revenue" from services is acceptable but donations are not. **\[VERIFIED — 2+ sources: [Business Viability Workshop transcript](https://www.youtube.com/watch?v=5BgvnDyP2dw), [Orientation transcript](https://www.youtube.com/watch?v=tf5RPGJvQKw)\]**  
* **The demo video is capped at 3 minutes. Judges are instructed not to watch past 3:00.** It must show the AI *live in production executing decisions*, not slideware. Sub-optimal videos are the single most common way a technically strong project loses points. **\[VERIFIED — [Rules §4](https://xprize.devpost.com/rules), [Submission Deep-Dive](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it)\]**  
* **Every submission survives an initial pass/fail gate before any scoring.** Stage One is a binary check — did the entrant "reasonably fit the theme" and "reasonably apply the required APIs/SDKs"? Miss the Gemini API integration or the Google Cloud product requirement and the submission never reaches scoring. **\[VERIFIED — [Rules §6](https://xprize.devpost.com/rules)\]**  
* **Judging includes a mandatory response window: if organizers email you, you have 2 business days to respond, and they may require a live demo call.** Miss that window and you can be disqualified. **\[VERIFIED — [Rules §6](https://xprize.devpost.com/rules)\]** Set up a monitored email \+ a phone number reachable during PT business hours.  
* **The written narrative (500–1,000 words) is where the "jobs & economic opportunities beyond the founding team" question is scored.** This is not a soft PR question — Category Impact judges look here for the "widespread adoption is credible" language. Ignoring this section leaves a full third of your score on the table. **\[VERIFIED — [Homepage](https://xprize.devpost.com/), [Submission Deep-Dive](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it)\]**  
* **The screening/verification body is Hacker Fund, not Google.** Justin Brezhnev / Hacker Fund conducts screening and verification before an "expert panel" selects five finalists to pitch live in Los Angeles on Sept 25, 2026 at the Moonshots Gathering. Judges are NOT publicly named. **\[VERIFIED — 2+ sources: [XPRIZE press release](https://www.xprize.org/news/xprize-launches-hackathon-with-2-million-prize-pool-backed-by-google), [Moonshots.com](https://moonshots.com/)\]** This means the judges are Peter Diamandis's curated network — expect operators, capital allocators, and moonshot founders, not academics.

---

## **2\. FULL TIMELINE & DEADLINES (All times US Pacific unless noted)**

| Milestone | Date/Time | Confidence |
| :---- | :---- | :---- |
| **Submission Period Opens** | May 19, 2026 – 10:00 AM PT | **\[VERIFIED — 2+ sources: [Rules §1](https://xprize.devpost.com/rules), [Press release](https://www.xprize.org/news/xprize-launches-hackathon-with-2-million-prize-pool-backed-by-google)\]** |
| **Submission Period Closes** | **August 17, 2026 – 1:00 PM PT** (Devpost also shows this as "Aug 17, 2026 @ 8:00 PM UTC" — these are consistent) | **\[VERIFIED — 2+ sources: [Rules §1](https://xprize.devpost.com/rules), [Devpost header](https://xprize.devpost.com/)\]** |
| **Judging Period** | Aug 18, 2026 – Sept 15, 2026 (10 AM – 5 PM PT bookends) | **\[VERIFIED — [Rules §1](https://xprize.devpost.com/rules)\]** |
| **Finalist Pitch \+ Winners Announcement** | On or around **September 25, 2026 – 2:00 PM PT**, at the Moonshots Gathering, Downtown Los Angeles (United \[Theater\]) | **\[VERIFIED — 2+ sources: [Rules §1](https://xprize.devpost.com/rules), [Moonshots.com](https://moonshots.com/), [Metatrends Substack](https://metatrends.substack.com/p/moonshots-summary-june-17-2026)\]** |
| **Winner "Required Forms" (W-8BEN, affidavits) deadline** | 10 business days after they are sent | **\[VERIFIED — [Rules §8](https://xprize.devpost.com/rules)\]** |
| **Prize delivery** | Within 60 days of Sponsor's receipt of completed forms | **\[VERIFIED — [Rules §8](https://xprize.devpost.com/rules)\]** |
| **Verification response window during judging** | 2 business days from any email inquiry | **\[VERIFIED — [Rules §6](https://xprize.devpost.com/rules)\]** |
| **Monthly revenue reporting bins** | May, June, July, August 2026 | **\[VERIFIED — [Rules §4](https://xprize.devpost.com/rules)\]** |

**Conflict flag:** The Devpost participant header at one point renders the deadline as "Aug 17, 2026 @ 8:00 PM UTC," which equals 1:00 PM PDT — consistent, not conflicting. No inter-source date conflicts detected. **\[VERIFIED\]**

**Non-obvious implication for a solo India builder:** the finalist pitch is in-person in Los Angeles. If you make top-5 you need to be visa-ready and financially able to travel on \~10 days' notice from the winners' announcement window. [**REASONABLE INFERENCE — the rules do not confirm in-person attendance is mandatory for finalists, but the press release explicitly says "compete live on September 25, 2026 in Los Angeles."**](https://www.xprize.org/news/xprize-launches-hackathon-with-2-million-prize-pool-backed-by-google) Get this clarified with organizers immediately — see Section 8\.

**As of today (July 25, 2026), you have \~23 days until the submission deadline** (deadline Aug 17). Revenue has been in-play since May 19 — so anyone starting today is already 66 days behind the front-runners on the revenue-by-month curve.

---

## **3\. ELIGIBILITY & ENTRY RULES**

### **Who IS eligible**

* **Individuals** at or above the legal age of majority in their country of residence. **\[VERIFIED — [Rules §3](https://xprize.devpost.com/rules)\]**  
* **Teams** of eligible individuals (no maximum team size, one Representative must be designated). **\[VERIFIED — [Rules §3](https://xprize.devpost.com/rules), [FAQ](https://xprize.devpost.com/details/faq)\]**  
* **Small Organizations** with **fewer than 25 employees** that exist and are incorporated at time of entry. **\[VERIFIED — [Rules §3](https://xprize.devpost.com/rules)\]**  
* **Solo participants:** explicitly allowed. Individual may also join multiple teams simultaneously. **\[VERIFIED — [FAQ](https://xprize.devpost.com/details/faq)\]**  
* **Students:** allowed if they meet age of majority. **\[VERIFIED — [FAQ](https://xprize.devpost.com/details/faq)\]**  
* **Multiple submissions:** allowed but each must be "unique and substantially different" at organizer's sole discretion. **\[VERIFIED — [Rules §4](https://xprize.devpost.com/rules)\]**

### **Who is NOT eligible**

* Residents/organizations in countries prohibited by US law or under OFAC sanctions (Russia, Crimea, Cuba, Iran, North Korea explicitly, plus any other Treasury-designated jurisdictions). **\[VERIFIED — [Rules §3](https://xprize.devpost.com/rules)\]**  
* **Employees, contractors, immediate family, or household members of XPRIZE, Devpost, Hacker Fund, or any judge.** This ejects the entire hackathon organizer network. **\[VERIFIED — [Rules §3](https://xprize.devpost.com/rules)\]**  
* Any project developed with financial/preferential support from XPRIZE or Devpost prior to Aug 17, 2026\. **\[VERIFIED — [Rules §4](https://xprize.devpost.com/rules)\]**  
* Minors (they can participate but are ineligible for prizes). **\[VERIFIED — [FAQ](https://xprize.devpost.com/details/faq)\]**

### **India specifically**

India is **NOT on any prohibited-country list** and eligibility is based on legal residence, not citizenship. Age of majority in India is 18 (met). Prize delivery for non-US residents requires a W-8BEN and the winner is responsible for local tax reporting (relevant for India's tax residency & TDS provisions on foreign income). **\[VERIFIED — 2+ sources: [Rules §3](https://xprize.devpost.com/rules), [Rules §8](https://xprize.devpost.com/rules)\]**

### **Non-obvious eligibility trap: pre-existing business \+ new AI product**

This is the most-asked question in the forum and the answer changes what many builders should submit:

* **You MAY use an existing legal entity (LLC/company).** The entity itself does not need to be new. **\[VERIFIED — [FAQ](https://xprize.devpost.com/details/faq)\]**  
* **You MAY use your existing social-media audience, existing employees, and generic templates.** **\[VERIFIED — [FAQ](https://xprize.devpost.com/details/faq)\]**  
* **The BUSINESS (the activity, the product/service being sold) must be new — created on or after May 19, 2026\.** **\[VERIFIED — [FAQ](https://xprize.devpost.com/details/faq)\]**  
* **Explicit forbidden patterns (from the FAQ):** *"a restaurant can't release a new menu item, and an app can't release a new feature and be considered a new business."* **\[VERIFIED — [FAQ](https://xprize.devpost.com/details/faq)\]**  
* **If you use employees of a pre-existing business,** you must attest work did not start pre-May 19 and expense their labour cost in the P\&L. **\[VERIFIED — [FAQ](https://xprize.devpost.com/details/faq)\]**  
* **Existing customer revenue must be reported as Related-Party** and will be **removed from consideration** by judges. **\[VERIFIED — [FAQ](https://xprize.devpost.com/details/faq), [Business Viability Workshop](https://www.youtube.com/watch?v=5BgvnDyP2dw)\]**

### **Non-obvious implication for you (solo India, $0)**

* You do **not** need to incorporate to enter or to sell. A sole proprietorship / individual PAN-based invoicing is sufficient at entry, since rules do not mandate an entity structure at submission. **\[VERIFIED — [Business Viability Workshop transcript](https://www.youtube.com/watch?v=5BgvnDyP2dw)\]**  
* But **you will need an entity/bank account to receive a prize.** XPRIZE requires a legal entity to pay to (or the individual if you entered as an individual). **\[VERIFIED — [Orientation transcript](https://www.youtube.com/watch?v=tf5RPGJvQKw)\]** For India, plan the receiving mechanism (individual foreign remittance via authorized dealer bank, or an LLP/Pvt Ltd if you scale) *before* winning becomes plausible.

---

## **4\. JUDGING CRITERIA — FULL BREAKDOWN**

### **Stage One (Pass/Fail Gate)**

Binary check: does the project *reasonably fit the theme* and *reasonably apply the required APIs/SDKs* (Gemini API \+ at least one Google Cloud product). **\[VERIFIED — [Rules §6](https://xprize.devpost.com/rules)\]**

**Failure modes:** No Gemini API call in the deployed app; no Google Cloud product; wrong category selection with obviously misaligned project. These are pass/fail — no score partial credit.

### **Stage Two (Three equally-weighted criteria)**

#### **Criterion 1 — Business Viability (\~33.3%)**

**Official language:** *"Teams must launch a real business during the hackathon, acquire real users, and generate real revenue. Judges assess both actual revenue achieved during the 90-day window and the sustainability of the underlying business model."* **\[VERIFIED — [Rules §6](https://xprize.devpost.com/rules)\]**

**Operational definition (from glossary):** *"the ability to sustain activities that provide goods or services to customers beyond the hackathon period."* **\[VERIFIED — [Glossary](https://docs.google.com/document/d/1-V-Wwr6NwhBQ6kj0pVGy5FfMBSQ-gkXSfc6BRoZ9CBA/edit)\]**

**How it is actually scored (from Business Viability Workshop):**

* **Two sub-halves**: (a) revenue during 90 days; (b) sustainability of the business model beyond 90 days. **\[VERIFIED — [Workshop](https://www.youtube.com/watch?v=5BgvnDyP2dw)\]**  
* **Arms-length revenue only** counts toward viability. Related-party is disclosed and stripped. **\[VERIFIED — [Rules §4](https://xprize.devpost.com/rules)\]**  
* **No minimum revenue threshold, no minimum customer count** — but "you must show the revenue, if any, that was earned." $0 in May is not disqualifying. **\[VERIFIED — [FAQ](https://xprize.devpost.com/details/faq)\]**  
* **Higher profit does not automatically mean higher score.** Judges assess model sustainability, not raw profit. **\[VERIFIED — [FAQ](https://xprize.devpost.com/details/faq)\]**  
* **No single customer \>40% of revenue** — the submission form asks you to certify this explicitly. **\[VERIFIED — [Submission Deep-Dive](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it)\]** This is a customer-concentration test lifted from due-diligence practice; a single-whale business will be flagged.

**What "real revenue" is (definitional):** *"money received from customers as a result of conducting the activities of the business"* — **cash basis, USD** — donations, grants, sponsorships, investment, and internal transfers do NOT count. **\[VERIFIED — 2+ sources: [Glossary](https://docs.google.com/document/d/1-V-Wwr6NwhBQ6kj0pVGy5FfMBSQ-gkXSfc6BRoZ9CBA/edit), [Orientation transcript](https://www.youtube.com/watch?v=tf5RPGJvQKw)\]**

**Ambiguity flagged:** the rules say "earned revenue" but the workshop said "cash-basis." For subscriptions, the workshop guidance was that cash-basis is preferred but you can *explain* nuance in the submission form. **\[VERIFIED — single source: [FAQ](https://xprize.devpost.com/details/faq)\]** — plan to report cash-basis with a footnote if MRR/ARR framing helps sustainability narrative.

#### **Criterion 2 — AI-Native Operations (\~33.3%)**

**Official language:** *"Teams must run their business through AI. Judges assess the extent to which AI is live in production and executes key decisions."* **\[VERIFIED — [Rules §6](https://xprize.devpost.com/rules)\]**

**Operational definition (glossary):** *"AI-native is a characteristic defined by a design with artificial intelligence as the core component from the ground up, rather than bolted on later as a feature."* **\[VERIFIED — [Glossary](https://docs.google.com/document/d/1-V-Wwr6NwhBQ6kj0pVGy5FfMBSQ-gkXSfc6BRoZ9CBA/edit)\]**

**Live participant question (unresolved by organizers):** does AI-native apply to the *product* the customer uses, the *business ops* of the founder, or both? Organizers explicitly deferred to judges. **\[VERIFIED — [AI-Native forum thread, no organizer answer](https://xprize.devpost.com/forum_topics/44258-clarification-on-ai-native-operations)\]** **Defensive interpretation: both.** The safest position is to have AI executing decisions in **both** the customer-facing product **and** the founder's own operations (support, marketing, ops), and to *document both explicitly* in the video and narrative.

**Rule-required LLM constraint:** if you use ANY LLM, at least one call in the deployed app must use the Gemini API. Other LLMs are allowed alongside. **\[VERIFIED — [Rules §4](https://xprize.devpost.com/rules)\]**

**What "key decisions executed by AI" means practically (inferred from workshop language):** decisions where the outcome affects a real customer or a business metric — pricing, routing, generation, response, matching, allocation — as opposed to decorative uses (copywriting a landing page, generating a logo). **\[REASONABLE INFERENCE — extrapolated from Brezhnev's repeated "live in production" phrasing in the [Workshop transcript](https://www.youtube.com/watch?v=5BgvnDyP2dw)\]**

#### **Criterion 3 — Category Impact (\~33.3%)**

**Official language:** *"Teams built something that meaningfully moves the needle in their chosen category — either by redefining how something works at a fundamental level, or by reaching a scale where widespread adoption is credible."* **\[VERIFIED — [Rules §6](https://xprize.devpost.com/rules)\]**

**Two disjoint scoring paths — pick one strategically:**

* **Redefinition path**: novel mechanism / 10× improvement / paradigm shift, may be niche  
* **Scale path**: demonstrable adoption trajectory or credible widespread reach

The five categories:

* **Education & Human Potential** — transforming how we learn, grow, and achieve  
* **Entrepreneurship & Job Creation** — tools for new founders/economies  
* **Small Business Services** — tools for everyday businesses  
* **Money & Financial Access** — banking, capital, financial freedom  
* **Professional Services Access** — connecting people with expert guidance (legal, tax, health admin) **\[VERIFIED — [Rules §4](https://xprize.devpost.com/rules), [Homepage](https://xprize.devpost.com/)\]**

**Non-obvious insight:** *"widespread adoption is credible"* means judges are not looking for actual widespread adoption in 90 days — they are looking for *credible trajectory evidence*. A small paying audience with steep organic growth beats a large flat audience.

**Small target audience is explicitly allowed** — organizers confirmed in the forum that focus/niche is compatible with Category Impact as long as the narrative connects to widespread applicability. **\[VERIFIED — [Small-audience forum thread, organizer answer](https://xprize.devpost.com/forum_topics/44074-is-a-small-target-audience-allowed)\]**

### **Tie-breaking**

If tied, the first criterion listed (Business Viability) wins. Then AI-Native. Then Category Impact. Then judge vote. **\[VERIFIED — [Rules §6](https://xprize.devpost.com/rules)\]**

**Non-obvious implication:** *In effect, Business Viability is not equally weighted — it is a tiebreaker.* If two entries are close, the one with more/better arms-length revenue wins. Optimize for verifiable revenue over pure novelty when close.

### **Who the judges are**

* **NOT publicly named.** Rules explicitly state judges "may or may not be listed individually on the Hackathon Website, and may change before or during the Judging Period." **\[VERIFIED — [Rules §6](https://xprize.devpost.com/rules)\]**  
* **Screening/verification body:** Hacker Fund (Justin Brezhnev, founder). Uses private repo access via `judging@hacker.fund` \+ `testing@devpost.com`. **\[VERIFIED — 2+ sources: [Rules §4](https://xprize.devpost.com/rules), [Press release](https://www.xprize.org/news/xprize-launches-hackathon-with-2-million-prize-pool-backed-by-google)\]**  
* **Finalist selection panel:** described as "expert panel" — no names. **\[VERIFIED — [Press release](https://www.xprize.org/news/xprize-launches-hackathon-with-2-million-prize-pool-backed-by-google)\]**  
* **Donors named:** Richard Merkin, Dan Martell, and others. **\[VERIFIED — [Press release](https://www.xprize.org/news/xprize-launches-hackathon-with-2-million-prize-pool-backed-by-google)\]**  
* **XPRIZE leadership involved in framing:** Peter Diamandis (founder), Anousheh Ansari (CEO). **\[VERIFIED — [Press release](https://www.xprize.org/news/xprize-launches-hackathon-with-2-million-prize-pool-backed-by-google)\]**

**Non-obvious inference:** with judges undisclosed and finalists selected by an "expert panel" that operates in Peter Diamandis's network, expect judges to skew *operator/investor* rather than *academic*, and expect a bias toward businesses that "expand access" — a phrase used repeatedly in the CEO's press quote. **\[REASONABLE INFERENCE — based on donor list and press positioning\]**

---

## **5\. REQUIRED SUBMISSION EVIDENCE — EXHAUSTIVE CHECKLIST**

Execute against this literally. Every item is required for Stage One pass and Stage Two scoring.

### **A. Project artifact**

*  **Project must be new** (built during May 19–Aug 17, 2026). Disclose any reused generic templates / boilerplate / snippets in the submission description. **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **Category selected** (exactly one of the five). **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **Gemini API used for at least one LLM call** in the deployed application (if any LLM is used). **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **At least one Google Cloud product used** — Vertex AI counts, Gemini API via AI Studio counts. **\[[FAQ](https://xprize.devpost.com/details/faq)\]**

### **B. Code repository**

*  **URL to code repo** — public with a license, OR private and shared with BOTH `testing@devpost.com` AND `judging@hacker.fund`. **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  Repo contains **all necessary source code** to understand and run the project. **\[[Submission Deep-Dive](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it)\]**

### **C. Demo video**

*  **Under 3 minutes** (judges cut off at 3:00 — anything longer will not be viewed) **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **Publicly viewable on YouTube, Vimeo, or Youku** — link on the submission form **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **Shows the project functioning on its intended device** **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **Shows AI live in production executing key decisions** — not a slideware overview **\[[Submission Deep-Dive](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it)\]**  
*  **No third-party trademarks or copyrighted music** unless licensed **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  Uploaded early (large files take hours to process) **\[[Submission Deep-Dive](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it)\]**  
*  All English or English-translated **\[[Rules §4](https://xprize.devpost.com/rules)\]**

### **D. Written narrative**

*  **500–1,000 words** **\[[Homepage](https://xprize.devpost.com/)\]**  
*  Explains **how AI does what versus what humans do** day-to-day **\[[Submission Deep-Dive](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it)\]**  
*  Explains **jobs and economic opportunities the business creates or enables for people beyond the founding team** (actual and potential) **\[[Homepage](https://xprize.devpost.com/), [Submission Deep-Dive](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it)\]**  
*  The **story of building the business this way** **\[[Submission Deep-Dive](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it)\]**

### **E. Revenue evidence**

*  **Total revenue** in USD from arms-length third-party customers during the hackathon window **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **Revenue-by-month breakdown**: May 2026, June 2026, July 2026, August 2026 **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **Stripe dashboard export OR bank statement** as raw evidence **\[[Homepage](https://xprize.devpost.com/), [Submission Deep-Dive](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it)\]**  
*  **Filled P\&L** using the [official P\&L template](https://docs.google.com/spreadsheets/d/1pAJrEMo7_QID6V62sA4C8XwGBHkxDTVX3wtYNE2fulI/edit) — download it, fill locally, upload. **\[[Submission Deep-Dive](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it), [Workshop transcript](https://www.youtube.com/watch?v=5BgvnDyP2dw)\]**  
*  **Corporate ID** if you have one (optional if individual entrant) **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **Cash-basis reporting** — cash received is cash reported **\[[Workshop transcript](https://www.youtube.com/watch?v=5BgvnDyP2dw)\]**  
*  **Related-Party Revenue disclosed separately** — team members, family, related entities, pre-existing customers **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **Confirmation no single customer \>40% of revenue** — submission form asks this **\[[Submission Deep-Dive](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it)\]**

### **F. Expense evidence**

*  **Total expenses during the hackathon period** — hosting, AI API usage, contractor fees, salary (yours, if applicable), etc. **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **Marketing & customer-acquisition spend disclosed even if $0** **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  Split into COGS (production costs) and SG\&A (go-to-market) per the template **\[[Workshop transcript](https://www.youtube.com/watch?v=5BgvnDyP2dw)\]**  
*  If using resources that existed before the hackathon, explain them in the submission **\[[Workshop transcript](https://www.youtube.com/watch?v=5BgvnDyP2dw)\]**

### **G. Product evidence (proof of "AI live in production continuously")**

*  **Agent execution logs** (timestamps, decisions, inputs/outputs) **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **API usage records** (Gemini API dashboard exports, GCP billing/usage) **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **Dashboard screenshots** showing continuous operation, not one-off demo runs **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  Anything else that "strengthens the case that playbooks are running in production continuously" **\[[Submission Deep-Dive](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it)\]**

### **H. Customer evidence**

*  **Number of individual users \+ high-level breakdown of who they are** **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **Testimonials or feedback** from real customers **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **Customer contact info: name, email, phone** — collectable via the submission form and specifically requested during verification **\[[Rules §4](https://xprize.devpost.com/rules), [Homepage](https://xprize.devpost.com/)\]**  
*  **Explicit user consent that their info is being shared with organizers** — required by rules ("Please ensure your users are aware that their information is being shared.") **\[[Rules §4](https://xprize.devpost.com/rules)\]**

### **I. Access for judging**

*  **Working link/demo/test build** — must be **free of charge** and unrestricted for the Sponsor, Administrator, and Judges through the end of Judging (Sept 15, 2026\) **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
*  **Login credentials in testing instructions** if private **\[[Rules §4](https://xprize.devpost.com/rules)\]**

### **J. Form questions to prep for**

The submission form asks (per the submission deep-dive):

*  Category and how project creates impact within it  
*  Business model — five-year goal, path to profitability, traction so far  
*  Extent to which AI is live in production  
*  Which Google Cloud product used and how  
*  How Gemini API is used for at least one LLM call  
*  Revenue, expenses, users acquired, paying users  
*  Certification: no single customer \>40% of revenue  
*  Disclosure of any related-party revenue **\[[Submission Deep-Dive](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it)\]**

### **K. Privacy/consent implications of customer PII**

The rules require you to collect and share **name \+ email \+ phone** of real customers. Under Indian DPDP Act 2023 (and GDPR if EU customers exist), you must obtain **explicit informed consent** before sharing this with a third party (XPRIZE, Devpost, Hacker Fund, judges). **Practical implication:** design your signup/onboarding flow with a specific opt-in ("I consent to my contact info being shared with XPRIZE competition organizers for verification") **now**, not at submission time. Retroactive consent is legally weak. **\[REASONABLE INFERENCE — rules do not spell out DPDP/GDPR compliance obligations, but transferring PII across borders to US organizers plainly triggers them.\]**

---

## **6\. TECHNICAL & PLATFORM REQUIREMENTS**

### **Mandatory Google integrations**

* **At least one product from Google Cloud** — Vertex AI counts, Gemini API via AI Studio counts. **\[VERIFIED — [FAQ](https://xprize.devpost.com/details/faq)\]**  
* **Gemini API for at least one LLM call in the deployed application** if the app uses any LLM at all. **\[VERIFIED — [Rules §4](https://xprize.devpost.com/rules)\]**  
* Additional LLM providers alongside Gemini are permitted. **\[VERIFIED — [Rules §4](https://xprize.devpost.com/rules)\]**

### **Available credits / free tier layers (mapped for a $0-budget builder)**

| Layer | Amount | Duration | Constraints | Confidence |
| :---- | :---- | :---- | :---- | :---- |
| **Google Cloud Free Trial** | $300 in credits | 90 days from signup | **New users only** (never previously paid GCP/Maps/Firebase). **Cannot pay Gemini API in AI Studio.** Cannot buy GPUs, use Marketplace, request quota increases, or run Windows Server VMs during the trial. | **\[VERIFIED — [GCP Free Trial docs](https://docs.cloud.google.com/free/docs/free-cloud-features)\]** |
| **Google Cloud Free Tier (always-free)** | Perpetual free quotas on 20+ products | Ongoing | Includes: Cloud Run (2M req/mo, 360k GB-sec memory, 180k vCPU-sec), Cloud Run functions (2M invocations/mo), BigQuery (1 TiB query/mo, 10 GiB storage), Firestore (1 GiB storage, 50k reads/day, 20k writes/day per project), Cloud Storage (5 GB in US regions), Compute Engine (1 e2-micro VM in specific US regions), Vertex AI Agent Engine (180k vCPU-sec/mo, 360k GB-sec/mo) | **\[VERIFIED — [GCP Free Tier table](https://docs.cloud.google.com/free/docs/free-cloud-features)\]** |
| **Gemini API free tier (via AI Studio)** | Free with rate limits | Ongoing | Rate limits described by community sources as \~5–15 RPM depending on model (e.g., Gemini 3 Flash vs. Pro) — NOT authoritative for competition purposes. Free tier availability is subject to change. | **\[REASONABLE INFERENCE — [community source aifreeapi.com](https://www.aifreeapi.com/en/posts/gemini-api-rate-limits-per-tier); NOT verified against a Google official source in this research pass\]** |
| **Google Antigravity Individual plan** | $0/month | Ongoing | Access to Gemini 3.5 Flash, Gemini 3.1 Pro, Gemini 3 Flash, Claude Sonnet & Opus 4.6, gpt-oss-120b. Unlimited Tab completions & Command requests. "Basic weekly rate limits." | **\[VERIFIED — [Antigravity Pricing](https://antigravity.google/pricing)\]** |
| **Google AI Ultra affordability coupon** | 3 months free | 90 days | Discretionary, requires application \+ ID verification. Reserved for "actively building" registered participants who "will struggle to afford to continue without help." | **\[VERIFIED — [FAQ](https://xprize.devpost.com/details/faq), [Application form](https://forms.gle/fim2oukB7hq6zZnk8)\]** |

### **Critical technical trap \#1 — Gemini API billing**

The $300 GCP credit **cannot** be applied to Gemini API in AI Studio (the free tier's own hosted endpoint). To burn the $300 credit on Gemini calls, you must call Gemini **via Vertex AI in GCP**. **\[VERIFIED — [GCP Free Trial docs](https://docs.cloud.google.com/free/docs/free-cloud-features)\]**

**Practical decision tree for a $0 builder:**

* Prototype and early revenue → **Gemini API free tier via AI Studio** (rate-limited but $0)  
* Production traffic that exceeds free tier → **Route to Vertex AI**, burning the $300 GCP credit  
* If credit exhausts before Aug 17 → **Antigravity $0 Individual** for coding assistance, but you still need production Gemini calls; apply for the Ultra affordability coupon early

### **Critical technical trap \#2 — Data residency & PII**

For India-collected customer PII, note that Vertex AI region selection matters if you have EU customers (GDPR data-residency). US-only VM regions in the always-free tier (us-central1, us-east1, us-west1) may create data-residency exposure. **\[REASONABLE INFERENCE — this is standard cross-border compliance; not spelled out in rules\]**

### **Critical technical trap \#3 — Anthropic / export-control precedent**

There is a June 2026 precedent where **Anthropic disabled Fable 5 and Mythos 5 for foreign nationals under US export-control directive**. **\[VERIFIED — [BBC](https://www.bbc.com/news/articles/c932g3v3e13o), [CNBC](https://www.cnbc.com/amp/2026/06/12/anthropic-disables-access-to-fable-5-and-mythos-5-to-comply-with-government-directive.html)\]** No similar action exists against Gemini today, but a solo India builder is a foreign national from a US compliance perspective — **do not architect a critical dependency on a non-Google frontier model** where a similar directive could interrupt production the week before submission. Google routing removes this risk for the required call; Anthropic/other-model fallbacks should be optional, not load-bearing.

### **Optional Google stack mentioned in press release**

Cloud Run, Stitch (design), and Flow (video) are name-checked. **\[VERIFIED — [Press release](https://www.xprize.org/news/xprize-launches-hackathon-with-2-million-prize-pool-backed-by-google)\]** Using these does not confer scoring advantage, but it signals AI-nativeness in the video and narrative when demonstrable.

---

## **7\. PRIZE STRUCTURE & WHAT WINNING ACTUALLY GRANTS**

### **Monetary prize pool**

Total: **$2,000,000 across 25 winners**

| Prize | Amount | Slots |
| :---- | :---- | :---- |
| 1st place | $500,000 | 1 |
| 2nd place | $200,000 | 1 |
| 3rd–5th place | $100,000 each | 3 |
| Runner-up | $50,000 each | 15 |
| **Category Prize** — Education & Human Potential | $50,000 | 1 |
| **Category Prize** — Entrepreneurship & Job Creation | $50,000 | 1 |
| **Category Prize** — Small Business Services | $50,000 | 1 |
| **Category Prize** — Money & Financial Access | $50,000 | 1 |
| **Category Prize** — Professional Services Access | $50,000 | 1 |

**\[VERIFIED — 2+ sources: [Rules §8](https://xprize.devpost.com/rules), [Homepage](https://xprize.devpost.com/)\]**

**A project is eligible for a maximum of one prize.** **\[VERIFIED — [Rules §8](https://xprize.devpost.com/rules)\]** This means winning a category prize is a *consolation* if you also placed top-5 — you cannot double-dip. Strategically: if you are top-5 material, category prizes are irrelevant; if you are strong-but-not-top-5, target the smallest category with the weakest field.

### **Prize delivery mechanics**

* Paid electronically to individual or Team Representative's bank account, or by mail. **\[VERIFIED — [Rules §8](https://xprize.devpost.com/rules)\]**  
* Requires **completed affidavits \+ tax forms (W-9 for US, W-8BEN for non-US including India)** returned within 10 business days. **\[VERIFIED — [Rules §8](https://xprize.devpost.com/rules)\]**  
* **Delivered within 60 days of receipt of the forms.** **\[VERIFIED — [Rules §8](https://xprize.devpost.com/rules)\]**  
* **Winner is responsible for all fees, currency conversion, and taxes** in own jurisdiction (India's TDS/foreign remittance rules apply). **\[VERIFIED — [Rules §8](https://xprize.devpost.com/rules)\]**

### **Non-monetary value (realistic assessment)**

* **In-person pitch at Moonshots Gathering, LA, Sept 25, 2026** — top-5 finalists only, in front of Peter Diamandis, Anousheh Ansari, and their network. Real career-defining visibility if you make it. **\[VERIFIED — [Press release](https://www.xprize.org/news/xprize-launches-hackathon-with-2-million-prize-pool-backed-by-google), [Moonshots.com](https://moonshots.com/)\]**  
* **Publicity rights**: XPRIZE \+ Devpost get non-exclusive license to use your name, likeness, and Submission for promotion for 3 years. **\[VERIFIED — [Rules §7, §10](https://xprize.devpost.com/rules)\]**  
* **IP retained by entrant**: you keep all IP. Judges \+ reviewers are under confidentiality/NDA per organizer statement in the workshop. **\[VERIFIED — 2+ sources: [Rules §7](https://xprize.devpost.com/rules), [FAQ](https://xprize.devpost.com/details/faq)\]**  
* **Access to Hacker Fund network**: implied from Justin Brezhnev's role, not codified as a prize benefit. **\[REASONABLE INFERENCE\]**

### **Realistic odds**

* **\~21,900+ registered participants** (Devpost site tracker showed 21,866 → 21,925 during research). **\[VERIFIED — [Devpost site header](https://xprize.devpost.com/rules)\]**  
* **25 total prize slots (1 project \= 1 prize).**  
* **Naive base rate: \~1 in 876 (\~0.11%) for any prize.**  
* **Effective base rate is higher for actual submitters** — most registrants don't submit. Devpost hackathons historically see 5–15% of registrants submit. **\[REASONABLE INFERENCE — pattern from analogous Devpost hackathons, not confirmed for this one\]**  
* **Assuming \~2,000–3,000 real submissions, top-25 is \~1%**; category-winning odds within a niche category are much better.

### **5-Finalist live pitch**

Hacker Fund screens; an "expert panel" selects five finalists; live pitch in LA on \~Sept 25\. **\[VERIFIED — [Press release](https://www.xprize.org/news/xprize-launches-hackathon-with-2-million-prize-pool-backed-by-google)\]** **Unresolved: whether the 5 finalists correspond to the 5 top-cash prizes (1st \+ 2nd \+ 3rd–5th), or a separate live-pitch subset.** **\[UNVERIFIED / COULD NOT CONFIRM\]** — most likely reading is they are the top-5, but organizer clarification is warranted. See Section 8\.

---

## **8\. AMBIGUITIES, LOOPHOLES & OPEN QUESTIONS**

Every item is a real interpretive gap. Recommended defensive interpretations are what a $0/solo builder should assume until organizers say otherwise. **File a written clarification request** for anything flagged as high-risk here (Rules §11 explicitly requires written clarification requests before the deadline).

| \# | Ambiguity / silent gap | Defensive interpretation | Risk if guessed wrong |
| :---- | :---- | :---- | :---- |
| **1** | "AI-native operations" is defined but does not specify product-AI vs. internal-ops AI weighting. Organizers deferred to judges. | Cover **both**: AI in customer product AND AI running your own ops (support, marketing, ops). Show both in video. | Losing a full third of AI-Native score. |
| **2** | "Real revenue" is cash-basis-preferred but "earned revenue" is the rules wording. SaaS/subscription accounting split. | Report cash-basis primary, disclose MRR/ARR narratively. | Judges may discount inflated ARR framing. |
| **3** | "Newly created business" — is a v2 rewrite of a stealth product from before May 19 eligible? | Only submit if the *customer value proposition* \+ *product being sold* both did not exist pre-May 19\. If any part predates it, either scrap or explicitly disclose. | Disqualification (worst-case) or high-integrity flag from judges. |
| **4** | **Are finalists required to physically attend Sept 25 LA event?** Not answered anywhere in rules. Press release says "compete live." Rules §8 says "Prize Delivery" is remote-capable via bank transfer. | Assume mandatory in-person for finalist pitch. Book contingent flight/visa. | Missing a finalist slot due to visa timing. |
| **5** | "Minimum revenue threshold" — organizers confirm none exists. But there is no floor at which a submission is considered non-competitive on Business Viability. | Aim for 3-figure USD from ≥10 arms-length paying customers as a minimum defensible baseline. | Too-low revenue reads as "hobby project" to judges. |
| **6** | **What counts as "arms-length"?** Rules and glossary exclude team, family, related entities, pre-existing customer relationships. But what about strangers in your existing social-media audience? | If they were a passive follower before May 19 and became a paying customer during the hackathon due to the new product's marketing, treat as arms-length. If they were a customer of a prior product, treat as related-party. | Judges strip suspected related-party revenue. |
| **7** | **Chargebacks/refunds**: rules do not specify whether refunded revenue counts. | Assume net revenue (gross minus refunds) is what counts, cash-basis. Disclose gross \+ net in P\&L notes. | Overstated revenue triggers verification. |
| **8** | **What if Gemini API rate limits interrupt production near submission?** — precedent: Fable/Mythos suspension. | Build a graceful degradation path where Gemini is core but not single-point-of-failure. Cache/queue calls where possible. Do NOT design in a way that requires 24/7 unrate-limited Gemini access. | Full production outage during verification window → judges see broken product. |
| **9** | **Same project to another hackathon?** — Forum question exists, no organizer answer at time of research. | Rules require "solely owned by Entrant" — doesn't forbid multi-submission. But `newly created` rule \+ IP rules of other hackathons could conflict. Safe default: do not double-submit for prizes. | Cross-competition disqualification. |
| **10** | **Judges' NDAs** — rules do not name the NDA, only assert "confidentiality." Private-repo code is exposed to judging@hacker.fund. | Redact or externalize any patentable secrets; watermark demos; keep truly proprietary IP in a separate module. | Low-probability IP leakage; unlikely but architected NDA is weaker than a mutual signed NDA. |
| **11** | **Prize IP ownership**: retained by entrant per Rules §7, but XPRIZE \+ Devpost get a 3-year non-exclusive license for promotional use. | Assume they may screenshot / re-post your submission. Don't put un-clearable third-party material in the video or narrative. | Publicity conflicts. |
| **12** | **Solo → Prize disbursement**: as an individual entrant in India, receipt of a large USD prize triggers FEMA reporting \+ potential TDS. Rules mention "compliance with foreign exchange and banking regulations." | Consult a CA now on whether individual receipt vs. an incorporated entity is cleaner. **\[Do this in July, not September.\]** | Prize delay or partial withholding. |
| **13** | **What is "reasonable" for Stage One's "reasonably fits the theme"?** Undefined. | Choose a category and align your narrative \+ video \+ product to it explicitly. Do not straddle categories. | Stage-One fail. |
| **14** | **Can generative-AI content (video, marketing) be used in your submission's demo video?** Rules require you own IP and no third-party trademarks. Nano Banana / Veo generated content is derivative — TOS-dependent. | Generate only with your own account, keep prompts \+ outputs, and license per Google TOS. Prefer your own footage where possible. | Video re-record days before deadline. |
| **15** | **Small Organizations "\<25 employees"** — is contractor headcount included? Rules do not define. | Treat FTEs \+ material contractors as headcount for safety. | Eligibility challenge on verification. |

---

## **9\. RISKS OF DISQUALIFICATION OR SCORE LOSS**

Every listed risk is either a rules-derived hard fail (**HARD**) or a scoring-derived soft fail (**SOFT**).

### **HARD (Stage One fail or disqualification)**

* **No Gemini API call in the deployed app** despite using an LLM. **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
* **No Google Cloud product used.** **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
* **Business pre-existed May 19, 2026** (product was live pre-hackathon). **\[[FAQ](https://xprize.devpost.com/details/faq)\]**  
* **Private repo not shared** with BOTH `testing@devpost.com` AND `judging@hacker.fund`. **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
* **Failure to respond within 2 business days** to organizer verification email. **\[[Rules §6](https://xprize.devpost.com/rules)\]**  
* **Product not accessible for judging** through end of Judging Period. **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
* **Video not publicly viewable on YouTube/Vimeo/Youku** at deadline. **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
* **Materials not in English** and no English translation provided. **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
* **Third-party trademarks / copyrighted music** in video without license. **\[[Rules §4](https://xprize.devpost.com/rules)\]**  
* **Fabricated revenue / customers** (verification will catch — organizers explicitly said they verify). **\[[Workshop transcript](https://www.youtube.com/watch?v=5BgvnDyP2dw)\]**  
* **Entrant in prohibited country** or affiliated with organizers/judges. **\[[Rules §3](https://xprize.devpost.com/rules)\]**  
* **Late submission** (Aug 17, 2026 1:00 PM PT hard cut) — Devpost auto-locks. **\[[Rules §5](https://xprize.devpost.com/rules)\]**  
* **Winner fails to return Required Forms within 10 business days.** **\[[Rules §8](https://xprize.devpost.com/rules)\]**

### **SOFT (compliant but low-scoring)**

* **Related-party revenue \>0 without disclosure** → verification flag → possible disqualification, minimum score deduction.  
* **Video \>3:00** → cutoff at 3:00; the best part of your pitch never gets seen.  
* **Narrative missing "jobs/economic opportunities beyond founding team"** → Category Impact deficit.  
* **Slideware demo video** (not showing AI live in production) → AI-Native deficit.  
* **No revenue-by-month breakdown** → Business Viability sustainability half unable to be scored.  
* **Marketing spend field left blank** (must disclose even if $0) → verification flag.  
* **P\&L not filled from the official template** → judges have to reconstruct; you look unserious.  
* **Single-customer concentration \>40%** → customer-concentration flag, low sustainability score.  
* **AI is "bolted on"** (chatbot skin over a CRUD app) → AI-Native floor.  
* **Straddling multiple categories** → Category Impact ambiguity.  
* **Missing product-evidence logs/dashboards** → judges cannot verify "AI live in production continuously."

---

## **10\. STRATEGIC IMPLICATIONS FOR A $0-BUDGET SOLO INDIA BUILDER**

### **Category selection (recommended order of consideration)**

* **Professional Services Access** — matches your ability to sell internationally, low incumbency, strong "expert access" narrative that fits Ansari's press quote. Easiest path to Category Impact scoring with a niche.  
* **Small Business Services** — enormous total addressable universe of SMBs globally; India has the highest global density of self-employed SMBs, so you have organic distribution familiarity.  
* **Entrepreneurship & Job Creation** — "meta" category; risky because judges may compare you against tooling companies with existing distribution.  
* **Money & Financial Access** — regulatory risk from cross-border compliance is high for a solo builder.  
* **Education & Human Potential** — most crowded category (typical hackathon pattern); hardest to differentiate. **\[REASONABLE INFERENCE — pattern from prior Google/hackathon competitions\]**

### **Build priority (Day-1 sequencing)**

* **Ship a paid-first, arms-length-first customer acquisition mechanism *before* the product is fully built.** Waitlist → paid pre-order → build. This is orthogonal to standard hackathon MVP behavior and is the single highest-leverage decision.  
* **Have Gemini executing at least one *material* customer-affecting decision within 7 days.** Not chat — a decision. Ranking, matching, pricing, routing, response generation with real stakes.  
* **Log everything from Day 1 — every agent call, every decision, every customer touchpoint.** These become your product evidence in Section 5G. Do not try to reconstruct at submission time.  
* **Set up Stripe (or Razorpay if Stripe is unavailable) \+ a dedicated business email \+ a business phone number immediately.** Payment infrastructure lives on the critical path.  
* **Draft the 500–1000-word narrative in Week 1, not Week 12\.** Iterate it as the business evolves. It is scored, not fill-in-the-blank.  
* **Record raw demo footage weekly.** The 3-minute video is easier to edit from 40 minutes of authentic footage than to record clean at deadline.  
* **File the Google AI Ultra affordability coupon application today** ([form](https://forms.gle/fim2oukB7hq6zZnk8)).  
* **File the $300 GCP credit today** if eligible ([console.cloud.google.com/freetrial](https://console.cloud.google.com/freetrial)).

### **Evidence to start collecting from Day 1**

* Stripe/payment dashboard export template (weekly cadence)  
* P\&L worksheet ([official template](https://docs.google.com/spreadsheets/d/1pAJrEMo7_QID6V62sA4C8XwGBHkxDTVX3wtYNE2fulI/edit)) filled monthly  
* Customer contact list with an explicit "consent to share with XPRIZE" checkbox in onboarding  
* Agent execution logs (persistent, searchable, exportable)  
* Weekly product-usage dashboard screenshot  
* Weekly testimonial solicitation ("would you share a one-sentence quote?")

### **Deliberately avoid**

* **Multi-category ambition** — pick one and commit.  
* **Non-Google frontier-model core dependencies** — Fable/Mythos suspension precedent.  
* **Charity/donation/grant revenue** — does not count.  
* **Selling primarily to your friends/family/network** — becomes related-party, stripped from viability score.  
* **Feature-rich, low-conversion product** — the P\&L is being scored, not the feature list.  
* **Enterprise sales cycles** — Brandon Kessler (Devpost CEO) explicitly said "provide context" for slow cycles but the 90-day window works against you. Prefer prosumer / SMB with days-not-months cycles.  
* **YouTube video \>3:00** — hard rule; judges cut at 3:00.  
* **Uncontrolled Gemini API cost burn** — $300 credit runs out fast at production loads. Cache aggressively; use Gemini Flash / Flash-Lite for latency-tolerant workloads; reserve Pro for premium moments.  
* **A GitHub repo without judging emails added** if private.  
* **Naive assumption that the LA finalist trip is remote** — plan for physical travel.

### **If you are starting the build TODAY (July 25, 2026\)**

You have **\~23 days**. Realistic minimum defensible submission:

* Week 1 (Jul 25–31): Category commit \+ Stripe \+ skeleton product with Gemini executing one decision \+ 5 real paying customers.  
* Week 2 (Aug 1–7): Marketing loop live; production logs flowing; 20+ arms-length paying customers; testimonials collected; narrative first draft.  
* Week 3 (Aug 8–14): Product-evidence dashboards; P\&L filled; video shot; customer PII consent audit; verification-ready.  
* Days Aug 15–17: Final edits, upload video early (multi-hour processing), submission draft to final, repo private-shared, contingency for Devpost outage.

**Do not confuse this with a standard hackathon** where 48 hours of code \+ a demo works. It won't.

---

---

## PART TWO — OPPORTUNITY ELIMINATION DOCUMENT
### (Market research, idea elimination, the single surviving product concept — written treating Part One as established context)

## **1\. EXECUTIVE SUMMARY**

**The single most important insight in this document:** with \~22 days remaining, the win condition is no longer "build the best AI-native business" — it is "**find the smallest, most painful, most time-critical decision that a self-selecting stranger with a credit card is already making today, and insert a Gemini-orchestrated deliverable into that exact decision point.**" 90% of the ideas commonly proposed for AI hackathons (agent platforms, AI SDRs, ops copilots, entrepreneur/co-founder AI, industry-specific chatbots) collapse under the \~22-day timeline because they require distribution the builder does not have and buyers who move too slowly.

**Categories ranked (with justification, not symmetric coverage):**

* **🟢 SMALL BUSINESS SERVICES — STRONGEST.** \~5.6M active Etsy sellers, \~1.9M Amazon third-party sellers, millions of Fiverr/Upwork freelancers. This is a population that already pays $10–$50/month for optimization tools, is discoverable via public marketplaces (so a solo builder can find them without an audience), and 76% of Etsy shops fail to achieve 2 sales/day in year one — a documented, high-frequency, self-diagnosed pain. **\[🟢 [Marketplace Pulse](https://www.marketplacepulse.com/stats/etsy-number-of-active-sellers), [SalesDoe first-year Etsy data](https://salesdoe.com/average-etsy-sales-first-year), [InsightAgent competitor pricing](https://www.insightagent.app/comparisons/insight-agent-vs-erank-everbee-marmalead)\]**  
* **🟡 PROFESSIONAL SERVICES ACCESS — SECOND, narrow slice only.** The immigration/visa document space has a documented $100K H-1B fee shock ([USCIS](https://www.cdflaborlaw.com/blog/uscis-clarifies-the-100000-h-1b-visa-fee)) creating urgent buyer psychology, and resume rewriting is a $395–$895 per-deliverable market ([iGotAnOffer](https://igotanoffer.com/en/advice/best-resume-writing-services)). But most of this category is regulated (legal advice) or trust-heavy (health) — the builder cannot enter those without credentials.  
* **🔴 ENTREPRENEURSHIP & JOB CREATION — AVOID for the main entry.** The "AI co-founder / researches your idea for you" idea (stress-tested in Section 19\) fails on buyer economics: pre-revenue entrepreneurs are the single most price-resistant buyer segment, ChatGPT/Claude/Gemini free tiers do 80% of this job, and there is no time-critical decision forcing payment.  
* **🔴 MONEY & FINANCIAL ACCESS — AVOID.** Regulatory approval before revenue is possible in almost every meaningful wedge (lending, banking, capital access). Fails Mandatory Exclusion Filter item 6\.  
* **🔴 EDUCATION & HUMAN POTENTIAL — AVOID for competition; possibly Tier 3 for business.** Most crowded category in hackathon history; buyers (students, learners) rarely pay; free substitutes (Khan Academy, YouTube, ChatGPT tutoring) are excellent.

**FINAL RECOMMENDATION (previewed here, defended in Section 20):** **Build a Gemini-powered Etsy Listing Audit \+ Rewrite service** — a one-shot paid deliverable priced at $19–$39, sold to Etsy sellers with \<500 sales via cold DM to public shops, delivering a structured audit \+ rewritten titles, tags, and descriptions within 24 hours. This is the only opportunity that survives every filter in Sections 2–18 with 🟢 evidence.

---

## **2\. CATEGORY-BY-CATEGORY MARKET LANDSCAPE**

Deprioritized categories are covered briefly and honestly. **Coverage is intentionally asymmetric per operating instructions.**

### **🟢 Small Business Services (deep dive)**

* **Population:** \~5.6M active Etsy sellers (Q1 2026, Marketplace Pulse); Etsy total statistics range 5.6M–8.7M depending on source (🟡 sources disagree — use conservative). \~1.9M active Amazon third-party sellers globally. Fiverr \+ Upwork together host millions of freelance profiles. Shopify hosts \~4.6M merchants. **\[🟢 [Marketplace Pulse](https://www.marketplacopulse.com/stats/etsy-number-of-active-sellers), [Business of Apps](https://www.businessofapps.com/data/etsy-statistics/), [Red Stag](https://redstagfulfillment.com/how-many-third-party-sellers-are-on-amazon/)\]**  
* **AI adoption:** SMB AI adoption in marketing surged from 26% (2023) to 87% (April 2026); investment in AI among SMBs sat at 57% in 2025 rising further; 74% report improved productivity. **\[🟢 [PRNewswire/Constant Contact](https://www.prnewswire.com/news-releases/the-rise-of-the-smb-creator-how-small-businesses-are-leveraging-social-media-and-ai-to-capture-consumer-attention-302796180.html), [Upwork State of AI in SMBs](https://www.upwork.com/resources/state-of-ai-in-smbs)\]** — market is warmed up; sellers now *expect* AI tools rather than resist them.  
* **Existing paid tools:** eRank ($5.99–$9.99), EverBee ($9.99–$49.99), Marmalead (\~$19), Alura, InsightAgent ($36.84–$59.04). **Sellers already pay.** **\[🟢 [InsightAgent comparison](https://www.insightagent.app/comparisons/insight-agent-vs-erank-everbee-marmalead)\]**  
* **The gap:** those tools give *data* (keywords, competitor tags). None deliver a *rewritten listing*. The gap between "here are your problem keywords" and "here is your new title, description, and tag set" is exactly the gap Gemini can close *this weekend*.  
* **Failure evidence:** \~76% of Etsy shops in their first year fail to reach 2 sales/day; 90% never hit 300 sales. **\[🟡 [SalesDoe analysis of 60,000 shops](https://salesdoe.com/average-etsy-sales-first-year), [r/Etsy anecdotal](https://www.reddit.com/r/Etsy/comments/zdfwsp/starting_out_saw_a_depressing_stat/)\]** — pain is real, self-diagnosed, and expensive (sunk inventory \+ Etsy fees).

### **🟡 Professional Services Access (partial)**

* **Immigration:** the September 2025 $100K H-1B fee ([American Immigration Council](https://www.americanimmigrationcouncil.org/blog/trump-100000-fee-h-1b-visa/), [CDF](https://www.cdflaborlaw.com/blog/uscis-clarifies-the-100000-h-1b-visa-fee)) and the July 2026 $750 B1/B2 expedite fee ([Ogletree](https://ogletree.com/insights-resources/blog-posts/need-a-u-s-visa-faster-new-750-expedited-interview-option-launches-on-july-1/)) have both created buyer urgency around visa document quality — but *actual immigration advice is unauthorized practice of law*. Any product here must be a document/checklist assistant, not a lawyer.  
* **Resume/career:** established one-time deliverable market at $395–$895 for entry-level–executive resumes ([iGotAnOffer](https://igotanoffer.com/en/advice/best-resume-writing-services), [Forbes](https://www.forbes.com/sites/forbes-personal-shopper/article/best-resume-writing-services/)). Buyer decides alone. But saturated — TopResume, ZipJob, dozens of Fiverr sellers.  
* **Legal/tax/health advice:** eliminated on regulatory grounds.

### **🔴 Entrepreneurship & Job Creation (thin — see Section 19\)**

Deprioritized because the highest-recall idea in this category (the "AI co-founder" stress-tested in Section 19\) fails on buyer economics. Adjacent opportunities (helping people *become* Etsy sellers or Fiverr freelancers) collapse into Small Business Services anyway.

### **🔴 Money & Financial Access (excluded)**

Excluded by Mandatory Filter \#6: nearly every meaningful revenue path (lending, deposits, capital access, remittance) requires regulatory approval before revenue is possible. Small carve-outs (a personal finance planner for Indian salaried employees) are excluded on Filter \#3 (customers who rarely pay for software in that category — Indian personal finance software has notoriously low willingness-to-pay).

### **🔴 Education & Human Potential (excluded)**

Excluded on two grounds: (a) most crowded hackathon category historically; (b) buyers (students) rarely pay individually, and B2B (schools) fails Filter \#4 (long procurement).

---

## **3\. PROBLEM DISCOVERY**

Problems are ranked by evidence strength. Only problems with 🟢/🟡 evidence advance.

### **P1. "My Etsy listing gets impressions but no sales — I don't know if it's my SEO, my images, my price, or my copy." 🟢**

* **Who:** new/struggling Etsy sellers, typically 0–500 lifetime sales  
* **Frequency:** continuous during any 30-day period without sales  
* **Severity:** existential (they either fix it or quit); measurable in lost inventory cost \+ Etsy listing fees ($0.20/listing)  
* **Current workaround:** buy eRank/EverBee ($10–$50/mo) → get numbers → not know what to do; or pay $19–$56 for a Fiverr/Etsy shop audit ([Etsy sell\_services listing](https://www.etsy.com/market/sell_services)) — but these are human-delivered, slow, inconsistent  
* **Existing solutions & why they fail:** SEO tools give data, not decisions; Fiverr audits are inconsistent quality and take 3–7 days; Etsy's own "Search Analytics" surfaces symptoms not fixes  
* **Evidence of real pain:** [SalesDoe 60K-shop analysis](https://salesdoe.com/average-etsy-sales-first-year) (76% fail to hit 2/day year one); Fiverr's `sell_services` marketplace already lists paid audits at $19–$56 with review counts \>160; multiple $19.99 audit gigs actively selling ([Instagram DavB gig](https://www.instagram.com/p/DavB_W_O81Y/)) 🟢

### **P2. "I need a stellar Upwork proposal in 15 minutes or I lose 15 connects." 🟡**

* **Who:** Upwork freelancers (millions), especially newer ones with \<10% conversion  
* **Frequency:** several times/day  
* **Severity:** medium — 15 connects ≈ $2.25 sunk cost per lost proposal; but real cost is time  
* **Current spend:** freelancers already pay for Upwork connects; no dominant AI proposal tool as of mid-2026 despite obvious demand  
* **Evidence:** documented 1–2h/proposal time cost ([Reddit r/Freelancers](https://www.reddit.com/r/Freelancers/comments/1og7bhd/spent_an_hour_on_one_proposal_is_that_just_part/), [Medium — Pennington](https://medium.com/@ms.laurapennington/how-much-time-should-you-spend-on-a-freelance-proposal-912d903e71e3)); typical conversion is \~10% ([Reddit r/Upwork](https://www.reddit.com/r/Upwork/comments/1u9v8i4/10_conversion_rate_so_far_in_2026_goodbadok/))  
* **Why weaker than P1:** freelancers are highly price-resistant (they discount their own time to zero); free ChatGPT can already draft a proposal — the AI wedge is thin

### **P3. "I run a home-service business and I'm missing calls / losing revenue while I'm on jobs." 🟡→🟢 on pain, 🔴 on solo feasibility**

* **Who:** SMB owners in trades (plumbing, HVAC, electrical, cleaning)  
* **Frequency:** daily  
* **Severity:** documented $126K/year in lost revenue per SMB from missed calls ([Leadlock](https://www.leadlock.ai/blog/ai-receptionist-small-business/), [Beside](https://www.beside.com/blog/the-hidden-cost-of-missed-calls-how-ai-receptionists-boost-revenue))  
* **Existing solutions:** Dialzara, Leadlock, RingCentral — this space is *already crowded* with well-funded incumbents (Fails Filter \#2)  
* **Why deprioritized:** requires trust, phone number provisioning, integration with the SMB's existing phone system — impossible in 22 days by a solo builder from India selling into US SMBs who need to trust the phone answering their livelihood

### **P4. "I run a wedding vendor / small local business and lead inquiries pile up." 🟡**

* Similar to P3, well-covered by Wedy Pro, ChatBot.com, etc. Deprioritized.

### **P5. "I'm a Shopify merchant with 10–200 products and my product descriptions are copy-paste supplier text." 🟡**

* Real, but Shopify Magic (built-in, free) and PageFly free tools address this in one click ([Shopify Magic](https://help.shopify.com/en/manual/products/details/product-descriptions/shopify-magic), [PageFly](https://pagefly.io/pages/ai-product-description-generator))  
* **Wedge collapsed:** you cannot beat Shopify's own free integrated tool. Eliminated.

### **P6. "I need to convince a client my Fiverr gig / freelance profile is worth hiring." 🟡**

* Real pain, but sub-market of P2 and the buyer is the same skeptical price-resistant freelancer

### **P7. "H-1B / visa applicants under fee shock need a defensible document package." 🟡**

* Documented $100K H-1B fee shock creates real urgency; but any offer that touches "will this get approved" is unauthorized practice of law. A pure grammar/completeness auditor is possible but the buyer psychology is fear-driven — they will pay a lawyer, not a stranger's SaaS.

**Advances to next section:** P1 (🟢), P2 (🟡), P7 (🟡). P3–P6 eliminated.

---

## **4\. CUSTOMER ANALYSIS**

| Attribute | P1 Etsy sellers | P2 Upwork/Fiverr freelancers | P7 Visa applicants |
| :---- | :---- | :---- | :---- |
| **Primary customer** | Etsy shop owner, 0–500 sales, 6–18 months old | Individual freelancer | Individual applicant |
| **Buyer \= user?** | Yes (same person) 🟢 | Yes 🟢 | Yes 🟢 |
| **Purchasing authority** | Sole 🟢 | Sole 🟢 | Sole 🟢 |
| **Budget** | Already spends $10–$50/mo on eRank/EverBee ([InsightAgent](https://www.insightagent.app/comparisons/insight-agent-vs-erank-everbee-marmalead)) | $10–$60/mo on Upwork connects; low SaaS budget | $500–$3000 already spent on filing fees; adjacent $20–$100 spend plausible |
| **Price sensitivity** | Medium — pay for tools that promise revenue | High — undervalue own time | Low near fee-shock moment |
| **Discovery** | Reddit r/Etsy, r/EtsySellers, YouTube tutorials, Etsy public shop directory | r/Upwork, r/Freelancers, Fiverr forums | Immigration forums, Reddit r/USCIS |
| **Sales cycle** | Minutes (impulse purchase for a "fix my shop" offer) 🟢 | Minutes 🟢 | Hours (fear-checked) |
| **Sophistication** | Low technical, high domain (they know Etsy jargon) | Medium | Medium |
| **Geographic concentration** | US 50%+, UK/Canada/Australia strong secondary; India small but growing ([Podbase](https://www.podbase.com/blogs/etsy-statistics)) | Global; US/UK/India heavy on Upwork | US-bound applicants from India/China/Philippines |
| **India-specific note** | India has growing Etsy seller base — you can start with Indian sellers for feedback, sell globally | India \= high freelancer supply | Indian applicants a specific H-1B segment |

**Non-obvious implication:** P1 buyers are **directly findable** via Etsy's public shop directory and reverse-search on shop age. You don't need an audience — the audience is a URL scrape away.

---

## **5\. WILLINGNESS-TO-PAY ANALYSIS**

**P1 (Etsy audit) — 🟢 STRONG.**

* Already-paying evidence: eRank ($5.99–$9.99/mo — hundreds of thousands of paying subs implied by revenue), EverBee ($9.99–$49.99/mo), Marmalead, Alura, InsightAgent, Fiverr audits at $19–$56 ([iGotAnOffer](https://igotanoffer.com/en/advice/best-resume-writing-services), [InsightAgent](https://www.insightagent.app/comparisons/insight-agent-vs-erank-everbee-marmalead), [Etsy sell\_services](https://www.etsy.com/market/sell_services))  
* **Reads as investment**, not expense — tied to a decision they've already committed to (opening the shop, paying for inventory)  
* Price elasticity: sellers reflexively spend $10–$30 without deliberation; $50+ requires a decision  
* Switching cost: low (they don't have to switch off eRank — this is *additive*)  
* **Sweet spot: one-time $19–$39 audit deliverable, upsell to $9/mo watch-and-refresh subscription**

**P2 (Upwork proposals) — 🟡 WEAKER.**

* Freelancers pay for Upwork connects, but rarely for proposal-generation SaaS  
* Free substitutes (ChatGPT) are excellent for proposal drafting  
* No dominant paid proposal tool — could be because *no one has cracked distribution* or because *the market doesn't want to pay*. Base rate favors the latter.

**P7 (Visa) — 🟡 CONDITIONAL.**

* Willingness-to-pay is high (fear-driven), but liability is high — one wrong recommendation and you're facing UPL claims. Legal risk too high for solo India builder to bear.

**Advances:** P1 alone.

---

## **6\. COMPETITIVE LANDSCAPE (P1)**

* **Direct competitors:** eRank, EverBee, Marmalead, Alura, InsightAgent (data tools, not rewrite deliverables); Fiverr audit gigs (human, slow, inconsistent quality)  
* **Indirect:** Etsy's own Search Analytics; YouTube tutorial creators (free educational content); community groups (free peer advice)  
* **Free substitute test — ChatGPT/Claude/Gemini:** a seller *can* paste their listing into ChatGPT and get a rewrite. **But**: (a) they don't know what to paste, (b) they don't know what Etsy's algorithm actually rewards vs. Google's, (c) they don't have visibility into competitor tags to compare against, (d) they won't invest the 30 minutes of prompt engineering. The wedge survives the free-substitute test because the product is **structured extraction from a live Etsy URL \+ benchmarked rewrite in one shot**, not a chat interface. 🟢  
* **Market saturation:** Data-tool space is saturated. **Audit-as-deliverable space is empty at scale** — Fiverr is fragmented humans; no dominant SaaS occupies "$19 push-a-button audit."  
* **Why Fiverr audits are beatable:** 3–7 day turnaround, inconsistent quality, no data anchor to Etsy's algorithm. Gemini-powered version delivers in \<60 minutes, deterministically, at 1/3 the price.

---

## **7\. AI-NATIVE SUITABILITY & AGENT ARCHITECTURE (P1)**

**Is AI decorative or load-bearing?** Load-bearing. Every atomic step is AI-executed. Human labor scales linearly; this business scales at Gemini API cost.

**Agent architecture (executed autonomously per audit; each numbered step is a distinct autonomous decision, not an "AI helps" veneer):**

* **Ingest agent** (Gemini 3 Flash) — accept an Etsy shop URL, use browser tools / scrape structured HTML for all listings, images, prices, review counts, favorites. **Decision:** which listings to prioritize (lowest-conversion by views/favorites ratio).  
* **Benchmarking agent** (Gemini 3.5 Pro with Google Search grounding) — search Etsy for the seller's top target keywords, extract top 20 competitor tags/titles, structure into a comparison JSON. **Decision:** which keyword clusters are under-optimized.  
* **Diagnosis agent** (Gemini 3.5 Pro with structured output) — score each listing against a rubric: title keyword density, tag utilization (Etsy allows 13; underuse is common), category alignment, price-to-competitor delta, image count. **Decision:** which specific flaw dominates for each listing.  
* **Rewrite agent** (Gemini 3.5 Pro) — produce a rewritten title (140 char), 13 tags (20 char each), and description (opening 160 chars optimized for Etsy's search snippet). **Decision:** the actual replacement copy the seller ships.  
* **Delivery agent** (Gemini 3 Flash) — assemble a PDF report with before/after, ship to seller's email via a scheduled Vertex AI Cloud Function.  
* **Self-ops agents** — same architecture powers the founder's own ops: (a) inbound Instagram/Reddit DM triage agent that qualifies leads and pushes them to a Stripe checkout URL, (b) post-delivery follow-up agent that solicits a testimonial 72 hours after delivery, (c) refund-triage agent for the 7-day guarantee.

**Why Gemini specifically is load-bearing (not swappable):**

* **Gemini's Google Search grounding** is the differentiator for step 2 — competitor benchmarking requires live web access; Claude and GPT-4 need extra tooling; Gemini has it native. **\[🟢 [Gemini API docs — Google Search grounding](https://ai.google.dev/gemini-api/docs/rate-limits)\]**  
* **Gemini 3 Flash's speed \+ free tier** makes the unit economics work at $19/audit (1000+ tokens generated per audit × \~4 rewrites per listing × \~10 listings \= \~40K tokens; at Flash pricing this is \<$0.10 in COGS)  
* **Vertex AI \+ $300 free credit** covers scheduled orchestration  
* **Antigravity Individual ($0)** covers the coding assistance for build

**AI-Native scoring impact:** covers BOTH the customer-facing product (agents do the work the customer bought) AND the founder's ops (agents do the sales, delivery, follow-up, refund). This directly addresses the XPRIZE ambiguity flagged in the prior intelligence doc — the safest defensive position for "AI-native operations" scoring.

---

## **8\. XPRIZE ALIGNMENT (P1)**

**Business Viability (0–5): 4.5** — Demonstrable arms-length revenue possible within days of ship (Section 15 validation test). Recurring MRR possible via a $9/mo "monitor-and-refresh" upsell. Sustainable model: unit economics ($19 revenue \- $0.10 Gemini \- $0.60 Stripe fees ≈ $18 gross margin per audit).

**AI-Native Operations (0–5): 4.5** — Every business function is AI-executed. Documented via API logs and dashboard screenshots (Section 5G of prior doc).

**Category Impact (0–5): 4.0** — Category \= Small Business Services. **Specific underserved population:** Etsy sellers in the $0–$500 lifetime sales bucket, \~75% of the platform, disproportionately women-owned micro-businesses ([Etsy 2024 seller census data — reported widely, \~80% women-identifying sellers](https://www.printful.com/blog/etsy-statistics)). Countable outcome: "for every 1000 sellers audited, X% report a Y% lift in views/sales within 30 days" — measurable, testimonial-friendly.

**Underserved-population narrative advantage:** aligns exactly with the Ansari quote from the XPRIZE press release ("more people, especially those with lived experience, can turn ideas into action and help close gaps... support for small business support") — this is the underserved-solopreneur wedge in her own words.

---

## **9\. SOLO-FOUNDER FEASIBILITY (P1)**

**Timeline check against Aug 17, 2026 (\~22 days from July 26, 2026):**

* **MVP complexity:** ONE web form (paste URL) → one backend pipeline → PDF email. No login, no dashboard, no billing platform (Stripe Payment Link only).  
* **Infrastructure:** Cloud Run (free tier: 2M req/mo, more than sufficient) \+ Firestore (free tier) \+ Vertex AI ($300 credit) \+ Gemini API free tier for overflow \+ Stripe Payment Links (no code) \+ SendGrid free tier for email  
* **Time to MVP:** 3–5 days with Antigravity coding assistance (this is standard vibe-coding scope)  
* **Time to first customer:** cold DM to Etsy shops with 0–20 sales, 6+ months old — day 1 of launch, target 20 DMs → 1 sale at 5% conversion (Etsy audit is a $19 impulse purchase; realistic)  
* **Time to first revenue:** day 6 (day 1 MVP finish \+ day 5 first outreach cycle)  
* **Operational complexity:** near-zero once agents are live. Human ops \= refund triage \+ edge cases (\~30 min/day)

**This is the only opportunity in this list that survives a 22-day timeline for a solo India builder.**

---

## **10\. "WHY NOW?" (P1)**

* **Gemini 3.5 Pro's Google Search grounding** — the *competitor benchmarking* step (Section 7 Step 2\) was not economically viable 18 months ago; earlier Gemini versions lacked reliable grounded search, and doing this with a scraper on Etsy was fragile. Now it's a single API call.  
* **Etsy's 2025 "Creativity Standards" update** ([Marmalead](https://blog.marmalead.com/etsy-print-on-demand/)) reshuffled algorithm weightings, invalidating older SEO advice — sellers are actively searching for updated help.  
* **SMB AI adoption jumped 26% → 87% for marketing use** in \~24 months ([PRNewswire/Constant Contact](https://www.prnewswire.com/news-releases/the-rise-of-the-smb-creator-how-small-businesses-are-leveraging-social-media-and-ai-to-capture-consumer-attention-302796180.html)) — sellers now *expect* AI-powered tools; skepticism has collapsed.  
* **eRank/EverBee price ceiling** is at \~$50/mo — the \~$20 one-shot deliverable slot is empty because incumbents have anchored on recurring pricing.

---

## **11\. UNFAIR ADVANTAGE**

If 500 hackathon participants read this tomorrow, the specific reasons this builder still wins:

* **Distribution barrier of speed, not scale.** DMing Etsy shops directly is a manual grind (or a Cloud-Run cron job doing it politely at 20/day per throwaway account). Most builders will chase easier distribution (Twitter, Reddit) and fail. The builder who accepts the grind wins the first 20 customers.  
* **India cost basis.** At Etsy audit COGS of $0.10 \+ $0.60 Stripe fee, gross margin per audit is \>$18. India-cost builder can sustain lower price ($19 vs $39 typical) without margin pain — a 2× price undercut that a US builder can't match without losing money after taxes.  
* **Deliverable, not a login.** Most hackathon builders will ship a SaaS with a dashboard. This ships an email attachment. Lower friction wins impulse buyers.  
* **XPRIZE narrative fit.** The Ansari "close gaps... support for small business" quote in the [official press release](https://www.xprize.org/news/xprize-launches-hackathon-with-2-million-prize-pool-backed-by-google) is a near-direct pitch line for this opportunity. Most builders won't optimize their submission narrative against organizer quotes.  
* **Compounding evidence.** Every completed audit is a customer contact (name, email, sometimes phone from Etsy shop info) — you accumulate the required Customer Evidence artifact *as a byproduct of the business*, not as a submission chore.

---

## **12\. TRUST & CREDIBILITY RISK (P1)**

**Why a stranger might hesitate:**

* No brand recognition; solo builder from India selling to a US/UK seller  
* "AI-generated audit" sounds like a low-effort ChatGPT dump — perceived commodity  
* Fear of getting a template

**How to prevent it (concrete, not vague):**

* **Structured, deterministic output format** — visible "12-point checklist" instead of prose; buyers can verify each check  
* **Named accountability** — a real name \+ real face on the landing page; response guarantee ("I personally respond within 24h")  
* **7-day money-back guarantee** — burn refunds up to some fraction; higher trust ROI than any marketing spend  
* **Public sample audit** — one anonymized real audit posted on the landing page  
* **Live competitor comparison in the audit** — hard to fake; each audit references 3 specific competitor shop URLs with tag data, proving it's not template output

---

## **13\. RISK ANALYSIS (P1)**

* **Assumption that must be true:** Etsy sellers with 0–500 sales will impulse-buy a $19 audit from a cold DM at ≥3% conversion. If conversion is \<1%, unit economics break even at massive DM volume, but competition scoring still passes because *some* revenue is generated. **\[Test cheaply in Section 15.\]**  
* **Regulatory:** none — this is a copywriting service. Etsy TOS prohibits certain scraping but a *seller-authorized* audit (buyer paste their own URL) sidesteps this. 🟢  
* **Technical:** Etsy anti-bot could block automated fetches. Fallback: seller pastes their listing text into a form field. Degrades UX slightly, unit economics unchanged.  
* **Market:** Etsy could ship a first-party AI listing tool (they already have Search Analytics). Response: Etsy's tool won't rewrite copy; and if they do, the incumbent seller-base with existing eRank subscriptions is our market anyway.  
* **Adoption:** cold DMs may get flagged as spam. Solution: personalize each DM using Gemini \+ reference a specific listing's specific problem in the DM (turns spam into consultation).  
* **Monetization:** buyers may pay once and never return. Response: this is fine — the business model is one-shot \+ optional $9/mo monitor upsell (\~20% conversion baseline for post-purchase upsells).  
* **Concentration:** 40%-customer rule (XPRIZE) is trivially satisfied at $19/unit — no single customer can hit 40% at any realistic revenue level.  
* **Category Impact score risk:** small businesses × \~$19 audits could read as "small potatoes." Mitigation: the narrative frames impact as **total shops helped** (aim for 100+ paying customers \= 100+ small businesses helped in 90 days), which is a countable, credible-scale story.

---

## **14\. GO-TO-MARKET FEASIBILITY (P1) — HIGH-LEVEL**

* **First 10 paying customers acquisition channel:** direct outreach to Etsy shop owners identifiable via Etsy's public shop directory (shop info is public; the "Announcement" and "About" sections often include contact info; sellers are reachable via Etsy's Messages system for authenticated senders, and via Instagram if their shop links to it).  
* **Reachable by solo, $0-budget, zero-audience builder?** Yes — this is precisely the profile Etsy sellers themselves inhabit, and the tools/data (public shop URLs, public sales counters via EverBee's own scraping data) are freely accessible.  
* **Secondary channels for 11–100:** r/EtsySellers, r/Etsy, Etsy seller Facebook groups (join-and-help pattern, not spam), Twitter Etsy seller community, TikTok short-form (a 60-second "before/after listing" video is highly shareable).  
* **Not viable within timeline:** paid ads, SEO, influencer partnerships — all require capital or audience.

---

## **15\. VALIDATION TEST (P1)**

**Cheapest possible pre-build test (executable in 24 hours, before writing agent code):**

**The test:** Create a barebones one-page landing site (Carrd or a static HTML on Cloud Run — $0). Copy: "24-hour Etsy audit \+ rewrite. $19. Refund if you don't get 10 concrete fixes." Stripe Payment Link. DM 30 Etsy shops in the 0–100 lifetime sales bucket with a personalized note referencing one specific listing they have.

**Pass condition:** 1+ paid conversion within 24 hours (\~3% conversion on 30 DMs). Deliver that first audit MANUALLY using Gemini in the browser (no product built yet). If the audit takes \>90 minutes manually with Gemini's help, unit economics don't work — kill the idea.

**Fail condition:** 0 conversions on 30 well-targeted DMs. Either the price is wrong, the DM is wrong, or the market doesn't want this. Retest at $9 for another 30 DMs before killing.

**Why this test is decisive:** it separates "sellers will impulse-buy" (the load-bearing assumption) from "sellers won't" without building any product. Total cost: your time \+ $0 in infrastructure.

---

## **16\. OPPORTUNITY RANKING**

Weighted scoring (0–5 each). Weights reflect this builder's constraints — evidence \+ solo feasibility \+ urgency-to-buy heavily weighted; scalability and defensibility weighted less because those are post-competition concerns.

| Criterion (weight) | P1 Etsy Audit | P2 Upwork Proposal | P7 Visa Audit | (Ref) "Entrepreneur AI" |
| :---- | :---- | :---- | :---- | :---- |
| Customer pain (2×) | 5 | 3 | 5 | 2 |
| Urgency (2×) | 4 | 3 | 5 | 1 |
| Existing spend (2×) | 5 | 2 | 3 | 1 |
| Willingness to pay (2×) | 5 | 2 | 3 | 1 |
| Ease of validation (1×) | 5 | 3 | 2 | 2 |
| Solo feasibility in 22d (2×) | 5 | 4 | 2 | 3 |
| AI-native fit (1×) | 5 | 4 | 3 | 4 |
| Gemini load-bearing (1×) | 5 | 3 | 3 | 3 |
| Defensibility (0.5×) | 3 | 2 | 3 | 1 |
| Scalability (0.5×) | 4 | 3 | 3 | 3 |
| XPRIZE alignment (1.5×) | 4.5 | 3 | 3.5 | 2 |
| Evidence confidence (1.5×) | 5 | 3 | 3 | 1 |
| **Weighted total** | **86.75** | **50.5** | **58.75** | **31.5** |

**P1 dominates by \~50%.** No other opportunity is close. The elimination filter has done its job.

---

## **17\. REJECTION LOG (specifically why each was cut)**

* **"AI SDR / cold email tool"** — market saturated (Apollo, Autobound, tofu HQ, snov.io), buyers require 30-day trial cycles, fails 22-day timeline. **\[[snov.io pricing](https://snov.io/blog/cold-email-ai/)\]**  
* **"AI receptionist for SMBs"** — Dialzara, Leadlock, RingCentral already dominant; trust barrier insurmountable for solo India builder in 22 days.  
* **"Shopify product description generator"** — Shopify Magic is free, first-party, one-click. Wedge dead. **\[[Shopify Magic](https://help.shopify.com/en/manual/products/details/product-descriptions/shopify-magic)\]**  
* **"AI resume rewriter"** — market saturated with TopResume/ZipJob and dozens of Fiverr sellers; ATS-check tools like TealHQ commoditized; hard to acquire without SEO budget.  
* **"AI legal intake for solo attorneys"** — B2B sales cycle \>90 days; procurement approvals; regulated professional context. **\[[Clio pricing analysis](https://www.clio.com/resources/ai-for-lawyers/legal-ai-tool-pricing/)\]**  
* **"Invoice collections agent for SMBs"** — Flexpoint, Beam, Moveo, Apifonica dominant; trust barrier; integration complexity blows 22-day window. **\[[FlexPoint](https://www.getflexpoint.com/post/ai-agents-payments-billing)\]**  
* **"Wedding vendor AI intake"** — Wedy Pro, ChatBot.com dominant; niche too small and B2B trust required.  
* **"Cross-border ecommerce tax compliance"** — regulatory approval required in most jurisdictions; fails Filter \#6.  
* **"Amazon FBA listing optimizer"** — Sellerprite, Sellerlabs dominant; sellers reflexively spend on tools *within* Amazon-native suites; harder to insert as outsider vs. Etsy's more open ecosystem.  
* **"Personal finance planner for Indian salaried employees"** — low WTP for personal finance in India; fails Filter \#3.  
* **"Tenant screening AI"** — regulatory (Fair Housing Act, civil rights concerns), documented adverse-impact scrutiny. **\[[Civil Rights Coalition](https://civilrights.org/resource/ai-tenant-screening/), [TechEquity paper](https://techequity.us/wp-content/uploads/2025/03/Screened-out-of-housing-paper-2025-updates.pdf)\]**  
* **"Job application autofill Chrome extension"** — Simplify Copilot, JobHuntr, LazyApply, TealHQ dominant and cheap. **\[[JobHuntr](https://www.jobhuntr.fyi/blog/best-autofill-job-application-tools-2025), [Simplify](https://simplify.jobs/copilot)\]**  
* **"AI blog post SEO writer"** — Jasper, Stacc, NotionX dominant; commoditized to $3.30/article. **\[[Stacc](https://thestacc.com/blog/ai-content-generators-test-2026/)\]**  
* **"LinkedIn profile optimizer"** — Careerflow, Flashfire dominant; buyer perception "profile alone won't get me a job" ([Pearce Nathan](https://www.linkedin.com/posts/pearcenathan_paying-someone-to-optimize-your-linkedin-activity-7397276293072998400-9MV_)).  
* **"AI-simulated customer feedback / entrepreneur research tool"** — see full stress-test in Section 19\.

---

## **18\. STARTUP IDEA (single surviving opportunity)**

### **The only surviving idea: Gemini-powered one-shot Etsy Listing Audit \+ Rewrite**

* **Working name (placeholder):** *ShopFix* or *ListingLens*  
* **Problem addressed:** Etsy shop owner has 0–500 lifetime sales, is getting impressions but no conversions, doesn't know if it's SEO, copy, or price. eRank/EverBee give them data, not decisions or rewritten copy.  
* **Target customer (specific):** Etsy shops open 6–18 months, 0–500 lifetime sales, 10–200 listings, based in US/UK/Canada/Australia primarily. Discoverable via Etsy's public shop directory \+ sales-counter scrape via EverBee-style tooling.  
* **Value proposition:** "Paste your Etsy shop URL. 24 hours later, get a PDF with rewritten titles, tags, and descriptions for your 5 lowest-performing listings, benchmarked against your top 3 real Etsy competitors. $19. Money back if you don't get 10 concrete fixes."  
* **AI agent workflow:** as detailed in Section 7 (Ingest → Benchmark → Diagnose → Rewrite → Deliver → self-ops for sales/follow-up/refund)  
* **Business model:** one-shot $19–$29 audit deliverable. Optional $9/mo "watch & refresh" upsell (agents re-audit monthly, ping seller if a competitor updated). Optional $49 "power audit" tier for 15+ listings.  
* **Revenue model:** transactional (Stripe Payment Link) \+ subscription (post-purchase upsell)  
* **Why Gemini is load-bearing:** Google Search grounding for competitor benchmarking (Claude/GPT would require third-party search tools \+ more engineering), Gemini 3 Flash for cheap high-volume rewrites, Vertex AI \+ $300 credit for orchestration. Removing Gemini forces additional infra (Serper API, DIY search wrappers) that blows the 22-day timeline.  
* **MVP scope:** landing page \+ Stripe Payment Link \+ Cloud Run pipeline (ingest → 4 Gemini calls → PDF assembly → email) \+ 1 lightweight admin dashboard for you  
* **Estimated build time:** 3–5 days with vibe-coding via Antigravity  
* **Estimated validation time:** 24–48 hours (Section 15 test)

---

## **18b. DEVIL'S ADVOCATE REVIEW (mandatory)**

Actively trying to disprove P1. Three attacks:

**Attack 1: "Etsy will detect and ban shop scraping — you get shut off mid-competition."**

* Rebuttal: seller-authorized ingestion (paste URL, or paste listing text) sidesteps this. Even if Etsy blocks automated fetches, degrading to a form-paste UX loses \~15% conversion but preserves the business. **Verdict: real risk, but degrades gracefully. Not disqualifying.**

**Attack 2: "eRank or EverBee will ship this feature within a week of you launching."**

* Rebuttal: incumbents are anchored on recurring pricing and would cannibalize their $10–$50/mo customers by offering a $19 one-shot. This is a classic innovator's-dilemma protection. Even if they eventually copy, the 22-day competition window closes first. **Verdict: real long-term risk, irrelevant to XPRIZE timeline.**

**Attack 3: "Cold DMs to Etsy sellers will get flagged as spam; you'll never reach 100 customers."**

* Rebuttal: this is the strongest attack. It could genuinely gate the business. Mitigations: (a) DM personalization citing a specific listing's specific flaw (turns spam into consultation), (b) parallel outreach on Reddit/Facebook groups (join-and-help, not sell), (c) TikTok short-form before/after content (organic distribution, zero cost), (d) offer the first 5 audits free in exchange for testimonials to seed social proof. **Verdict: real risk to volume beyond 20 customers; not disqualifying at the level of "some paying customers" required for XPRIZE. Reduces expected 90-day revenue estimate but does not kill the opportunity.**

**Did devil's advocate change the ranking?** **No, ranking unchanged.** P1 is still dominant. But it does change the *narrative in the submission*: emphasize customer count (helped) over revenue magnitude, since revenue may be modest ($1–3K over the remaining window) while customer count can plausibly reach 50–150.

---

## **19\. MANDATORY STRESS-TEST: THE ENTREPRENEUR / CO-FOUNDER AI IDEA**

**Attacking, not defending.** The proposed idea: an AI tool that takes a business idea as input and researches market gaps, competitors, legal/regulatory steps, financial planning, and includes an AI-simulated customer feedback feature.

**Why won't people pay:**

* **The buyer is pre-revenue and price-resistant.** Aspiring entrepreneurs are the single most-optimistic-and-least-committed segment. They will pay $0 for research (they'll do it themselves) but $2K+ for legal incorporation (they hire a lawyer). There is no natural price point in between for a tool. 🟢  
* **Adverse selection.** Anyone willing to pay for AI market research is by definition someone who couldn't do it themselves — meaning they will also be unable to *act* on the research, so they won't renew or upsell.  
* **AI-simulated customer feedback is uniquely unreliable.** Judges (per the XPRIZE press release framing — "real customers, real revenue") will read AI-simulated feedback as *the opposite* of what the competition is testing. This feature actively hurts XPRIZE alignment.

**What free substitutes already solve this (mostly):**

* **ChatGPT/Claude/Gemini free tiers** already do market research, competitor scans, and financial modeling at 80%+ quality  
* **YC Startup School** (free, comprehensive, higher trust)  
* **Perplexity Pro's Deep Research** at $20/mo dominates the "market research" wedge  
* **Product Hunt, IndieHackers, r/SaaS** — free community feedback

**Assumptions that must be true (and whether evidence supports):**

* ❌ "Aspiring entrepreneurs will pay for research" — evidence *contradicts* this; they cannibalize their own time to zero  
* ❌ "AI-simulated customer feedback is trusted" — no evidence; strong intuition against  
* ❌ "This is differentiated from ChatGPT" — evidence *contradicts*; the workflow is a canonical LLM use case  
* ❌ "Can acquire customers in 22 days with zero audience" — aspiring entrepreneurs are scattered across all social platforms; no crisp channel

**Does narrowing to a one-time paid deliverable tied to a real financial commitment change the verdict?** Marginally, yes. Example: **"$99 pre-incorporation legal-checklist package for a specific US state, delivered same day"** — this attaches to the LLC formation decision, which is a real financial commitment ($50–$300 to Stripe Atlas / LegalZoom \+ $50–$500 state fees). But:

* LegalZoom / Stripe Atlas / Firstbase already occupy this wedge with strong distribution and brand trust  
* The India-based solo builder has zero credibility signaling for US-state legal advice  
* Regulatory: bordering on UPL if positioned as advice

**Is there a structurally superior adjacent opportunity?** Yes: **help people who have already committed to a specific niche entrepreneurial path** (i.e., Etsy sellers who have already paid to open a shop). That's exactly P1. **The Etsy audit is structurally the "entrepreneur helper" idea repositioned to a segment that has already crossed the paying threshold.** This substitution is the entire point of Section 19's stress test.

**Verdict:** the Entrepreneur / Co-Founder AI idea is **rejected** and Section 17's rejection line stands. The adjacent superior opportunity is P1 (Etsy Listing Audit).

---

## **20\. FINAL RECOMMENDATIONS**

### **TIER 1 — BUILD IMMEDIATELY**

**P1: Gemini-powered one-shot Etsy Listing Audit \+ Rewrite ($19–$29).** Only opportunity with 🟢 evidence across willingness-to-pay, solo feasibility, AI-native fit, 22-day timeline, and XPRIZE alignment. Buyer is a self-selecting stranger with a credit card who is already actively searching for help and already paying incumbents for weaker offerings.

### **TIER 2 — VALIDATE FIRST**

**P2 variant: Upwork proposal auto-drafter with buyer-side history scraping and job-post signal extraction, priced at $9/mo.** Only build if P1's Section 15 validation test somehow fails. Would need 3-day pre-purchase landing-page test.

### **TIER 3 — INTERESTING BUT RISKY**

**P7: Visa document pre-flight audit** — real urgency and pain, but liability / UPL exposure is a real risk a solo India builder cannot underwrite. Risk that holds it back: legal exposure without professional credentials.

### **TIER 4 — AVOID**

* Entrepreneur / co-founder AI (Section 19 verdict)  
* AI SDRs, AI receptionists, AI legal intake, invoice collections agents — market saturated with well-funded incumbents  
* Any regulated wedge (finance, health, legal advice, housing screening)  
* Any product requiring an existing audience (creator tools without distribution)  
* Any B2B product with \>7-day sales cycle

---

### **THE ONE SINGLE FINAL RECOMMENDATION**

**Build the Gemini-powered Etsy Listing Audit \+ Rewrite service ($19 one-shot deliverable, 24-hour turnaround, target Etsy shops with 0–500 lifetime sales via personalized cold DMs and Reddit/TikTok organic distribution).**

Reasoning tied directly to this builder's constraints:

* **Solo:** entire pipeline is 5–6 autonomous Gemini agents; no team required.  
* **$0 budget:** Cloud Run \+ Vertex AI \+ Firestore \+ Gemini API free tier \+ Antigravity Individual \+ Stripe Payment Links \= $0 fixed, \~$0.70 marginal per audit; $300 GCP credit is pure runway.  
* **No audience:** customers are found via Etsy's public directory; no follower count required to send a personalized cold DM.  
* **Vibe-coding:** MVP is a form → 4 Gemini calls → PDF → email; explicitly the type of scope Antigravity \+ Gemini 3.5 Pro can build in 3–5 days.  
* **India-based, selling internationally:** the buyer is 90% US/UK/Canada/Australia; Stripe processes the payment; India cost basis lets you price at $19 without margin pain.  
* **Remaining timeline (\~22 days):** validation test in 24–48 hours; MVP in 3–5 days; first customer within 6 days; realistic path to 30–100 paying arms-length customers by Aug 17 → clean Business Viability evidence, obvious AI-Native Operations story, clean Category Impact narrative aligned to Ansari's own press-release framing.

**Do not build anything else. Every other opportunity in this document scores lower and would cost days to switch to. Every day starting today costs \~4.5% of remaining runway. Move.**

---
---

## UNIFIED SOURCE LOG

*Combines Part One's Section 11 and Part Two's Section 21. Sources cited by both originals (the XPRIZE press release, the Devpost homepage) are listed once, under Part One, with a note where Part Two also relied on them.*

### From Part One — Official (highest weight)

### **Official (highest weight)**

* [**Official Rules**](https://xprize.devpost.com/rules) — supports: timeline, eligibility, submission requirements, judging criteria, prizes, IP, publicity, disputes, tax obligations  
* [**FAQ**](https://xprize.devpost.com/details/faq) — supports: age/residency, solo/team, multi-submission, credit resources, "newly created" interpretation, business model neutrality, related-party revenue rules, judge NDA, revenue reporting basis  
* [**Homepage**](https://xprize.devpost.com/) — supports: category descriptions, submission checklist, prize breakdown, judging criteria, video that anchors expectations  
* [**Submission Deep-Dive Update (7 days ago)**](https://xprize.devpost.com/updates/45364-submission-deep-dive-exactly-what-to-include-and-how-judges-read-it) — supports: form-question preview, 40% customer-concentration certification, video guidance, product-evidence guidance  
* [**Glossary of Terms (Hacker Fund)**](https://docs.google.com/document/d/1-V-Wwr6NwhBQ6kj0pVGy5FfMBSQ-gkXSfc6BRoZ9CBA/edit) — supports: legal definitions of project, business, business entity, customer, business model, revenue, expenses, operations, business viability, sustainability, AI-native, impact  
* [**Business Viability Workshop (July 15, 2026\)**](https://www.youtube.com/watch?v=5BgvnDyP2dw) — supports: cash-basis reporting, COGS vs SG\&A, related-party treatment, judge behavior, "no minimum revenue," verification/anti-cheating stance, 60-day prize-delivery reasoning  
* [**Innovation Orientation Session (June 12, 2026\)**](https://www.youtube.com/watch?v=tf5RPGJvQKw) — supports: category framing, judging criteria, entity vs business distinction, Vertex AI/AI Studio dual acceptance, earned-revenue-only for nonprofits, small-audience acceptance  
* [**Glossary/Build-in-Public Update**](https://xprize.devpost.com/updates/45227-new-event-build-in-public-rewards-and-a-glossary-of-terms) — supports: existence of separate $10,000 Moonshots build-in-public reward, glossary link, workshops  
* [**Business Viability Workshop announcement**](https://xprize.devpost.com/updates/45239-don-t-miss-the-business-viability-workshop) — supports: workshop existence, Logan Kilpatrick session, Moonshots $10K build-in-public reward  
* [**Google Cloud Free Trial docs**](https://docs.cloud.google.com/free/docs/free-cloud-features) — supports: $300/90-day, new-user eligibility, exclusions (Gemini API in AI Studio, third-party models, GPUs, Marketplace), Free Tier per-product limits  
* [**Antigravity Pricing**](http://antigravity.google/pricing) — supports: $0 Individual plan, model access, basic weekly rate limits  
* [**XPRIZE Press Release**](https://www.xprize.org/news/xprize-launches-hackathon-with-2-million-prize-pool-backed-by-google) — supports: Diamandis/Ansari quotes, Hacker Fund screening role, 5 finalists live pitch in LA, donor names (Merkin, Martell), Moonshot Gathering context, Google stack (Gemini, AI Studio, Antigravity, Cloud Run, Stitch, Flow)  
* [**Moonshots.com**](https://moonshots.com/) — supports: Sept 25 event confirmed  
* [**Metatrends Substack (Peter Diamandis newsletter)**](https://metatrends.substack.com/p/moonshots-summary-june-17-2026) — supports: Moonshot Gathering venue (United Theater, DTLA) and date/time

*(The Press Release and Homepage entries above are also the sole XPRIZE-specific sources Part Two cites — see Part Two's original "XPRIZE-specific reference points" note, now merged here rather than repeated.)*

### From Part One — Forum threads (community + organizer clarifications)

### **Forum threads (community \+ organizer clarifications)**

* [**Revenue evidence mandatory?**](https://xprize.devpost.com/forum_topics/44581-revenue-evidence-requirement-mandatory-for-all-submissions) — participant question, unanswered at time of research  
* [**LLC \+ new AI product eligibility**](https://xprize.devpost.com/forum_topics/44562-does-an-existing-an-llc-still-qualify-if-it-didn-t-start-making-an-app-until-may-19th) — participant question, key ambiguity example  
* [**AI-Native Operations clarification**](https://xprize.devpost.com/forum_topics/44258-clarification-on-ai-native-operations) — participant question, unanswered — the product-vs-ops-AI ambiguity  
* [**$300 Cloud credit clarification**](https://xprize.devpost.com/forum_topics/44263-clarification-on-300-cloud-credit) — organizer (Michelle Brain) confirms credit routing \+ Ultra affordability coupon  
* [**Same project to another hackathon**](https://xprize.devpost.com/forum_topics/44474-can-i-submit-the-same-project-to-another-hackathon) — participant question, unanswered  
* [**AI-Operated Business \+ Gemini agent architecture**](https://xprize.devpost.com/forum_topics/44076-clarification-on-ai-operated-business-criteria-gemini-agent-architecture) — participant question, organizer deferred to rules  
* [**Business model clarification (no payment gateways in country)**](https://xprize.devpost.com/forum_topics/44565-clarification-on-the-project-business-model) — supports payment-infrastructure-neutral rule interpretation  
* [**Individual entrant business registration**](https://xprize.devpost.com/forum_topics/44265-does-business-need-to-be-registered-as-legally-if-joining-individual) — organizer confirms no entity required at submission  
* [**Mobile app subscription revenue**](https://xprize.devpost.com/forum_topics/44080-can-we-have-a-business-model-around-a-mobile-app-and-revenues-via-subs-in-the-mobile-app) — organizer confirms business model unrestricted  
* [**Prototype fully built?**](https://xprize.devpost.com/forum_topics/44075-does-the-prototype-have-to-be-fully-built-built) — organizer defers to rules  
* [**Small target audience**](https://xprize.devpost.com/forum_topics/44074-is-a-small-target-audience-allowed) — organizer confirms niche audiences acceptable per Category Impact criterion  
* [**MCP integrations with 3rd parties**](https://xprize.devpost.com/forum_topics/44122-mcp-integrations-with-3rd-parties) — organizer confirms MCP-on-existing-third-party is acceptable if the *business* is new

### From Part One — Contextual / analogous / risk

### **Contextual / analogous / risk**

* [**Anthropic Fable 5 / Mythos 5 suspension — BBC**](https://www.bbc.com/news/articles/c932g3v3e13o) — supports: export-control precedent for foreign nationals, risk of relying on non-Google frontier models  
* [**Anthropic Fable/Mythos — CNBC**](https://www.cnbc.com/amp/2026/06/12/anthropic-disables-access-to-fable-5-and-mythos-5-to-comply-with-government-directive.html) — cross-verification of the June 2026 suspension  
* [**Gemini API Rate Limits Guide (aifreeapi.com)**](https://www.aifreeapi.com/en/posts/gemini-api-rate-limits-per-tier) — supports (community-sourced, not Google-authoritative): current free-tier rate-limit approximations  
* [**Gemini API rate limits — Google official**](https://ai.google.dev/gemini-api/docs/rate-limits) — official reference; specific per-model numbers must be checked at build time as they change  
* [**Google Cloud Free Trial Terms**](https://cloud.google.com/terms/free-trial) — supporting reference for Free Trial restriction list  
* [**P\&L Template (official)**](https://docs.google.com/spreadsheets/d/1pAJrEMo7_QID6V62sA4C8XwGBHkxDTVX3wtYNE2fulI/edit) — required submission format  
* [**Devpost Discord (community)**](https://discord.gg/devpost) — supports: fastest organizer answers per Michelle Brain repeatedly in updates  
* [**Moonshots Build-in-Public $10K reward**](https://app.performancecollab.com/campaigns/social-promotion-018dcdd1) — supports: separate, non-hackathon $10K opportunity for building publicly (external to prize pool)

### From Part One — Absence-of-source flags

### **Absence-of-source flags (things I searched for and could not confirm)**

* **Specific named judges** — not publicly disclosed. **\[UNVERIFIED / COULD NOT CONFIRM\]**  
* **Whether finalist pitch is mandatory in-person** — press implies yes, rules do not codify. **\[UNVERIFIED / COULD NOT CONFIRM\]**  
* **Whether the 5 live-pitch finalists \= 1st through 5th place** — inferred but not confirmed. **\[UNVERIFIED / COULD NOT CONFIRM\]**  
* **Exact current Gemini API free-tier RPM per model as of July 25, 2026** — must be pulled from Google's live rate-limits page at build time; values shift. **\[UNVERIFIED / COULD NOT CONFIRM\]**  
* **Judge NDA text** — asserted in FAQ but not published. **\[UNVERIFIED / COULD NOT CONFIRM\]**  
* **Refund/chargeback treatment in revenue reporting** — silent in rules and workshop. **\[UNVERIFIED / COULD NOT CONFIRM\]**  
* **Whether generated media (Veo, Nano Banana) in the 3-minute demo violates the "third-party IP" rule** — silent. **\[UNVERIFIED / COULD NOT CONFIRM\]**

### From Part Two — Category & market landscape

### **Category & market landscape**

* [Marketplace Pulse — Etsy active sellers](https://www.marketplacepulse.com/stats/etsy-number-of-active-sellers) → 5.6M active Etsy sellers Q1 2026  
* [Business of Apps — Etsy statistics](https://www.businessofapps.com/data/etsy-statistics/) → 8.7M sellers, 93M active buyers (higher-end estimate)  
* [Podbase — Etsy statistics](https://www.podbase.com/blogs/etsy-statistics) → 86.5M active buyers Q4 2025  
* [Printful — Etsy statistics](https://www.printful.com/blog/etsy-statistics) → 8.1M active sellers (Yaguara); demographic composition  
* [Insight Agent — Etsy market](https://www.insightagent.app/guides/etsy-market-statistics) → market context  
* [SalesDoe — First-year Etsy shops](https://salesdoe.com/average-etsy-sales-first-year) → 76% of first-year shops fail to reach 2/day  
* [r/Etsy — success rate anecdote](https://www.reddit.com/r/Etsy/comments/zdfwsp/starting_out_saw_a_depressing_stat/) → 90% never hit 300 sales  
* [Red Stag Fulfillment — Amazon seller count](https://redstagfulfillment.com/how-many-third-party-sellers-are-on-amazon/) → \~1.9M active Amazon 3P sellers

### From Part Two — Competitive & pricing evidence

### **Competitive & pricing evidence**

* [InsightAgent vs. eRank/EverBee/Marmalead pricing comparison](https://www.insightagent.app/comparisons/insight-agent-vs-erank-everbee-marmalead) → competitor pricing tiers $5.99–$59.04  
* [eRank homepage](https://erank.com/) → free tier \+ paid tiers exist  
* [EverBee vs eRank comparison](https://everbee.io/everbee-vs-erank-comparison/) → product vs. SEO tool split  
* [Etsy sell\_services marketplace](https://www.etsy.com/market/sell_services) → active $19–$56 audit gigs, real reviews  
* [Shopify Magic help doc](https://help.shopify.com/en/manual/products/details/product-descriptions/shopify-magic) → free first-party AI product descriptions (kills Shopify description wedge)  
* [PageFly free description generator](https://pagefly.io/pages/ai-product-description-generator) → free substitute confirmation

### From Part Two — SMB AI adoption

### **SMB AI adoption**

* [PRNewswire / Constant Contact SMB Creator report](https://www.prnewswire.com/news-releases/the-rise-of-the-smb-creator-how-small-businesses-are-leveraging-social-media-and-ai-to-capture-consumer-attention-302796180.html) → SMB marketing AI 26%→87% (2023→April 2026\)  
* [Upwork — State of AI in SMBs](https://www.upwork.com/resources/state-of-ai-in-smbs) → 74% report productivity gain  
* [Business.com — 2026 SMB AI Outlook](https://www.business.com/articles/ai-usage-smb-workplace-study/) → 57% SMB AI investment in 2025  
* [BayTech — SMB AI adoption guide](https://www.baytechconsulting.com/blog/smb-ai-adoption-guide-use-cases-costs-roadmap) → 90-day pilot norms  
* [Booth Associates — Small business AI stats 2026](https://boothassociatesllc.com/ai-statistics-small-business-2026.html) → 89% of small businesses use AI in some form

### From Part Two — Freelancer economics

### **Freelancer economics**

* [r/Freelancers — 1hr proposal time](https://www.reddit.com/r/Freelancers/comments/1og7bhd/spent_an_hour_on_one_proposal_is_that_just_part/) → proposal time cost  
* [Medium — Pennington on proposal time](https://medium.com/@ms.laurapennington/how-much-time-should-you-spend-on-a-freelance-proposal-912d903e71e3) → 1–3 hours per proposal  
* [r/Upwork — 10% conversion](https://www.reddit.com/r/Upwork/comments/1u9v8i4/10_conversion_rate_so_far_in_2026_goodbadok/) → typical conversion rate  
* [Getmany Upwork proposal tips](https://getmany.com/blog/upwork-proposal-writing-tips-win-more-projects-in-2026) → 15–35% conversion for optimized proposals  
* [LinkedIn — Mirza Faizan Iqbal on rejected proposals](https://www.linkedin.com/posts/mirzafaizaniqbal_i-used-to-spend-2-hours-on-each-upwork-proposal-activity-7319192211542171648-Q3P5) → 2h/proposal baseline

### From Part Two — Solopreneur spending

### **Solopreneur spending**

* [Plutio — solopreneur admin time](https://www.plutio.com/solutions/solopreneurs) → 36% of week on admin  
* [MetaIntro — solopreneur AI stack](https://www.metaintro.com/blog/ai-tools-solopreneurs-productivity-triple-output-2026) → $75/mo stack  
* [Wikidocs — solo software budget](https://wikidocs.net/blog/@solobizstack/25150/) → $45–$75/mo typical

### From Part Two — Visa / immigration urgency

### **Visa / immigration urgency**

* [USCIS $100K H-1B fee — CDF](https://www.cdflaborlaw.com/blog/uscis-clarifies-the-100000-h-1b-visa-fee) → $100K new-petition fee  
* [American Immigration Council — H-1B fee change](https://www.americanimmigrationcouncil.org/blog/trump-100000-fee-h-1b-visa/) → fee increase confirmation  
* [Ogletree — $750 B1/B2 expedite](https://ogletree.com/insights-resources/blog-posts/need-a-u-s-visa-faster-new-750-expedited-interview-option-launches-on-july-1/) → July 1, 2026 $750 fast-track

### From Part Two — Resume / career service pricing

### **Resume / career service pricing**

* [Forbes — best resume writing services](https://www.forbes.com/sites/forbes-personal-shopper/article/best-resume-writing-services/) → $479–$699 tier  
* [iGotAnOffer — best resume writing services 2026](https://igotanoffer.com/en/advice/best-resume-writing-services) → $395–$995 tiers  
* [Resume Optimizer Pro — services 2026](https://resumeoptimizerpro.com/blog/best-resume-writing-services-2026) → $300–$1200 traditional; $10/mo AI  
* [WeAreCareer — resume writing services cost 2026](https://wearecareer.com/blogs/news/resume-writing-services-cost-2026) → range $100–$5000  
* [LinkedIn — 9 best AI resume builders 2026](https://www.linkedin.com/pulse/9-best-ai-resume-builders-2026-experts-honest-breakdown-gerety-qsute) → $150 live review benchmark

### From Part Two — Adjacent-market saturation evidence (used for rejections)

### **Adjacent-market saturation evidence (used for rejections)**

* [Beside — hidden cost of missed calls](https://www.beside.com/blog/the-hidden-cost-of-missed-calls-how-ai-receptionists-boost-revenue) → $24K/year loss claim, 62% unanswered  
* [Leadlock — missed calls SMB revenue](https://www.leadlock.ai/blog/ai-receptionist-small-business/) → $126K/year SMB loss claim  
* [Dialzara — missed call cost](https://dialzara.com/blog/missed-calls-hidden-costs-and-ai-solutions) → cross-verification  
* [SMB Automation — AI receptionist](https://smbautomation.io/blog/ai-receptionist-local-service-business) → market saturation evidence  
* [Wedy Pro blog](https://www.wedypro.ai/blog/wedding-pro-too-many-hats-ai-agents-time-back) → wedding vendor incumbent  
* [ChatBot.com wedding planner](https://www.chatbot.com/solutions/ai-chatbot-for-wedding-planners/) → incumbent  
* [FlexPoint — AI agents payments billing](https://www.getflexpoint.com/post/ai-agents-payments-billing) → invoice collections incumbents  
* [Beam — debt collection AI](https://beam.ai/solutions/debt-collection) → incumbents  
* [Moveo — debt collection AI](https://moveo.ai/blog/what-is-a-debt-collection-ai-agent) → incumbents  
* [Apollo — AI SDRs](https://www.apollo.io/insights/why-are-revenue-teams-starting-to-use-ai-sales-development-representatives) → SDR market  
* [Autobound — outbound playbook 2026](https://www.autobound.ai/blog/outbound-sales-playbook-2026) → SDR market  
* [Snov — AI cold email tools](https://snov.io/blog/cold-email-ai/) → pricing $39–$99/mo  
* [Tofu HQ — B2B email personalization tools](https://www.tofuhq.com/post/best-ai-tools-for-b2b-email-personalization) → SDR incumbents  
* [Simplify Copilot](https://simplify.jobs/copilot) → free autofill incumbent  
* [JobHuntr autofill comparison](https://www.jobhuntr.fyi/blog/best-autofill-job-application-tools-2025) → autofill incumbents  
* [Stacc AI content generators](https://thestacc.com/blog/ai-content-generators-test-2026/) → content commoditized to $3.30/article  
* [Averi — true cost of content 2026](https://www.averi.ai/how-to/the-true-cost-of-content-in-2026-freelancers-vs.-agencies-vs.-ai-platforms) → $49/mo AI vs. $300–$750/article human  
* [Careerflow LinkedIn optimizer](https://www.careerflow.ai/linkedin-optimizer) → LinkedIn optimization free tier  
* [Flashfire — pay to optimize LinkedIn](https://www.flashfirejobs.com/blog/can-i-pay-someone-to-optimize-my-linkedin-profile) → $119–$599 range  
* [Pearce Nathan — LinkedIn optimization waste](https://www.linkedin.com/posts/pearcenathan_paying-someone-to-optimize-your-linkedin-activity-7397276293072998400-9MV_) → market skepticism  
* [Clio — legal AI pricing](https://www.clio.com/resources/ai-for-lawyers/legal-ai-tool-pricing/) → $50–$1200/seat, procurement heavy  
* [AI.Law seat pricing](https://www.ai.law/pricing/) → $149–$699/seat/month  
* [Attorney Journals — small law firm AI](https://www.attorneyjournals.com/ai-for-small-law-firms-work-smarter-cut-costs-win-more) → $80–$135/user/month typical  
* [Civil Rights Coalition — AI tenant screening](https://civilrights.org/resource/ai-tenant-screening/) → regulatory concerns  
* [TechEquity — tenant screening AI harms](https://techequity.us/wp-content/uploads/2025/03/Screened-out-of-housing-paper-2025-updates.pdf) → regulatory scrutiny

### From Part Two — Etsy algorithm / niche context

### **Etsy algorithm / niche context**

* [Marmalead — Etsy print-on-demand 2026](https://blog.marmalead.com/etsy-print-on-demand/) → 2025 "Creativity Standards" update  
* [MyDesigns — best Etsy SEO tools 2026](https://mydesigns.io/blog/best-etsy-seo-tools/) → tool landscape  
* [Listybox — Etsy tools comparison](https://listybox.com/blog/best-etsy-tools-comparison-guide) → tool ecosystem  
* [Insight Agent — Etsy tool comparison](https://www.insightagent.app/comparisons/insight-agent-vs-erank-everbee-marmalead) → pricing tiers cross-verified

### From Part Two — Confidence flags (things Part Two did NOT verify precisely, honestly labeled)

### **Confidence flags (things I did NOT verify precisely, honestly labeled)**

* **Exact Etsy scrape TOS boundary** — not confirmed; degrading UX plan is the mitigation. 🔴  
* **Exact conversion rate on Etsy-seller cold DMs** — no public data; 3% assumption is my inference. 🟡  
* **Actual paying-subscriber counts for eRank/EverBee/Marmalead** — these are private companies; pricing pages verified, subscriber counts inferred from public discussion volume. 🟡  
* **Whether Etsy will ship a first-party AI listing rewriter in the next 90 days** — unverifiable; risk acknowledged. 🔴

---

## Immediate next-step recommendations

*(Originally Part One's closing section — links refreshed, updated with the participant-count discrepancy above.)*

- **File the [affordability coupon](https://forms.gle/fim2oukB7hq6zZnk8) today** — approval takes time.
- **Check the live [Updates](https://xprize.devpost.com/updates) and [Discussions](https://xprize.devpost.com/forum_topics) pages before trusting any specific forum thread, update, or participant count cited in this document** — see the discrepancy flagged at the top.
- **File a written clarification request** with organizers via Devpost Discord (`https://discord.gg/devpost`) or the [Devpost forum](https://xprize.devpost.com/forum_topics) on at minimum these three questions: (a) is finalist pitch mandatory in-person in LA?, (b) does "AI-native operations" require both product AI and ops AI, or is product-only acceptable if excellent?, (c) how are chargebacks/refunds handled in revenue reporting?
- **Recompute "days remaining" from today's actual date** every time this document is opened — do not trust the ~16-day figure above once time has passed.
