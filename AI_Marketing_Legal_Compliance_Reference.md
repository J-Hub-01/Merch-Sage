# Legal & Regulatory Compliance Reference for AI-Generated Marketing Content and Sales Advice

**Version:** 1.0 | **Date:** August 2026 | **Purpose:** Engineering-ready guardrails reference

---

## How to Use This Document

This document is designed to be converted directly into content-generation rules and guardrails. Every boundary is labeled with one of three tiers:

- **[HARD LEGAL REQUIREMENT]** — Violating this exposes the platform and/or seller to legal liability (fines, lawsuits, criminal charges). These MUST be enforced in the system's logic.
- **[PLATFORM POLICY]** — Violating this may get content or seller accounts removed from major marketplaces (Amazon, eBay, Etsy, Shopify, TikTok Shop, etc.). Often stricter than government law.
- **[BEST-PRACTICE CAUTION]** — Not strictly illegal, but carrying significant risk. Recommended for an automated system to enforce proactively.

Where law is still evolving or ambiguous, entries are tagged **[EVOLVING AREA]** or **[UNSETTLED]**.

Each entry includes:
1. Plain-language rule statement
2. Jurisdiction(s) where it applies
3. Concrete COMPLIANT example
4. Concrete NON-COMPLIANT example
5. Relevant law / regulatory body / enforcement example

---

# SECTION 1: Advertising and Marketing Law

---

## 1.1 Truth-in-Advertising / Deceptive Advertising

**Rule:** All marketing claims — whether express or implied — must be truthful and not misleading. A claim is "deceptive" if it contains a misrepresentation or omission likely to mislead a reasonable consumer acting reasonably under the circumstances, and the representation or omission is material (affects the consumer's purchasing decision).

**Jurisdictions:** US, UK, EU, India, and virtually all major e-commerce markets.

**Key laws & bodies:**
- **US:** Federal Trade Commission Act Section 5 (15 USC §45) — prohibits "unfair or deceptive acts or practices in or affecting commerce." FTC Policy Statement on Deception (1983). Enforcement: FTC can seek civil penalties up to **$53,088 per violation** (as of 2025, adjusted for inflation) under 16 CFR 1.98.
- **UK:** Consumer Protection from Unfair Trading Regulations 2008 (CPRs) (implementing EU UCPD), enforced by the **CMA** (Competition and Markets Authority) and **ASA** (Advertising Standards Authority) / **CAP** (Committee of Advertising Practice) / **BCAP** (Broadcast Committee of Advertising Practice) codes.
- **EU:** Unfair Commercial Practices Directive 2005/29/EC (UCPD) — establishes a general prohibition on unfair commercial practices, including misleading actions and misleading omissions. Enforced by national consumer protection authorities in each member state.
- **India:** Consumer Protection Act 2019 (Section 2(47) defines "unfair trade practice"), enforced by the **Central Consumer Protection Authority (CCPA)**. **ASCI** (Advertising Standards Council of India) Code for Self-Regulation — requires ads to be "legal, decent, honest and truthful." ASCI reported in FY 2024-25 that **94% of flagged ads were misleading**, with 97% of violations originating digitally.

**Enforcement examples:**
- FTC has brought numerous cases against companies for deceptive advertising claims across health, beauty, and consumer products.
- ASA (UK) routinely bans advertisements for misleading claims, including digitally altered beauty ads (e.g., L'Oréal cosmetics ads banned in 2011 for excessive airbrushing).

**✅ COMPLIANT:** "This handmade ceramic mug holds 350ml and is dishwasher safe." (Verifiable, factual claim.)
**❌ NON-COMPLIANT:** "The world's best ceramic mug — guaranteed to last forever." (Superlative without substantiation + absolute guarantee without basis.)

**Tier: [HARD LEGAL REQUIREMENT]**

---

## 1.2 Substantiation Requirements

**Rule:** Before making any objective claim in advertising — especially performance claims, comparative claims, superlatives ("best," "#1"), or scientific claims ("clinically proven") — the advertiser must possess competent and reliable evidence supporting the claim BEFORE it is published. The level of substantiation must match the type of claim made. Health and safety claims require a higher level of substantiation (typically competent scientific evidence, such as controlled studies).

**Jurisdictions:** US, UK, EU, India (universal principle).

**Key laws & bodies:**
- **US:** FTC Policy Statement Regarding Advertising Substantiation — "Advertisers must substantiate express and implied claims, however conveyed, that make objective assertions." FTC Act Section 5. Civil penalties up to $53,088 per violation.
- **EU:** UCPD Article 6(1)(b) — misleading if a trader claims without substantiation that a product has particular characteristics. UCPD Annex I, No. 7 — claiming to be a signatory to a code of conduct when not.
- **UK:** CPRs 2008, Regulation 5 (misleading actions) and Regulation 6 (misleading omissions).
- **India:** ASCI Code Chapter 1, Section 1.4 — "Advertisements must be truthful and not contain claims that cannot be substantiated."

**Critical for AI system:** The AI platform itself may not have the evidence to substantiate claims it generates. The system must either (a) only generate claims that can be verified from the seller's product data, or (b) clearly flag claims that require seller substantiation and prevent their publication until evidence is confirmed.

**Enforcement examples:**
- FTC has brought dozens of cases against companies for unsubstantiated health claims (e.g., weight loss products, supplements). Companies like Cure Encapsulations (2018) were charged for unsubstantiated weight loss claims.
- FTC Notice of Penalty Offenses (2023) sent to ~670 companies warning that false claims could result in civil penalties up to $50,120 per violation.

**✅ COMPLIANT:** "In a survey of 500 customers, 87% reported their skin felt more hydrated after 2 weeks of use." (Substantiated by survey data.)
**❌ NON-COMPLIANT:** "Clinically proven to reduce wrinkles by 50%." (Generated without any clinical study to support it.)

**Tier: [HARD LEGAL REQUIREMENT]**

---

## 1.3 Reference-Price / "Was-Now" Pricing Rules

**Rule:** When advertising a discount or sale price alongside a "was" / "original" / "regular" / "compare at" price, the reference price must be a genuine, recently-offered price that the product was actually sold at for a meaningful period. Inflated reference prices to make discounts appear larger are prohibited.

**Jurisdictions:** EU (most prescriptive), UK, US, India.

**Key laws & bodies:**
- **EU:** Directive (EU) 2019/2161 ("Omnibus Directive," amending UCPD 2005/29/EC) — came into force 28 May 2022. Requires that any announced price reduction must indicate the **lowest price applied by the trader during the preceding 30 days** prior to the reduction. This is known as the "30-day lowest price rule." The European Commission published guidance on price promotions under the Omnibus Directive. Non-compliance is an unfair commercial practice under UCPD.
- **UK:** CMA pricing guidance — "was-now" pricing is legal only if the "was" price was the most recent genuine selling price and was available for a meaningful period (generally interpreted as 28 days). Digital Markets, Consumers and Competition Act 2024 also empowers the CMA to enforce consumer protection law directly with fines.
- **US:** FTC Deceptive Pricing guidelines — reference prices must be actual, recent prices. State attorneys general have brought actions against retailers for deceptive "compare at" pricing. In 2024, several major DTC brands faced litigation for reference pricing likely to deceive consumers. FTC Rule on Unfair or Deceptive Fees (effective May 12, 2025) addresses drip pricing and hidden fees in ticketing and short-term lodging.
- **India:** ASCI Code and Consumer Protection Act 2019 prohibit misleading reference pricing.

**Critical for AI system:** If the AI generates pricing suggestions including discount claims, it must either (a) have verified data on the actual prior selling price, or (b) not generate reference-price comparisons without seller-confirmed price history. The EU 30-day lowest price rule is a specific, auditable metric.

**Enforcement examples:**
- EU member states actively enforce Omnibus Directive pricing rules with fines against online retailers.
- UK CMA has investigated and taken action against retailers for misleading reference pricing.
- In the US, class action lawsuits have been filed against DTC brands for deceptive strike-through pricing (2024-2025, ongoing litigation).

**✅ COMPLIANT (EU):** "Was €40 (lowest price in last 30 days), now €30." (Genuine 30-day reference price.)
**✅ COMPLIANT (US):** "Regular price $40 (sold at this price for the past 3 months), now $30." (Genuine prior price.)
**❌ NON-COMPLIANT:** "Was $99, now $39!" (When the product was never actually sold at $99, or was sold at $99 for only 1 day before the "sale.")

**Tier: [HARD LEGAL REQUIREMENT]**

---

## 1.4 Fake or Exaggerated Scarcity / Urgency Claims

**Rule:** Claims that create a false sense of urgency or scarcity — such as "only 2 left," "limited time offer," "ends tonight," "selling fast" — are prohibited if not genuinely true. These are treated as misleading commercial practices.

**Jurisdictions:** EU, UK, US, India.

**Key laws & bodies:**
- **EU:** UCPD 2005/29/EC Annex I (the "blacklist" of 31 practices banned in all circumstances) — No. 17: "Stating or creating the impression that a product will only be available for a very short period or otherwise available only for a limited time, in order to elicit an immediate decision and deprive consumers of sufficient opportunity or time to make an informed choice." This is banned **per se** — no case-by-case assessment needed.
- **UK:** CPRs 2008, Schedule 1 (banned practices list) — mirrors EU UCPD Annex I.
- **US:** FTC Act Section 5 — false scarcity claims are deceptive. FTC has taken action against companies for fake urgency claims.
- **India:** ASCI Code and Consumer Protection Act 2019 — false scarcity is an unfair trade practice.

**Critical for AI system:** The system must NOT generate scarcity or urgency claims unless it has real, verified data (e.g., actual inventory count, actual offer end date set by the seller). Generating "only 2 left" without inventory data, or "ends tonight" without a real deadline, is a banned practice in the EU/UK and a deceptive practice in the US/India.

**✅ COMPLIANT:** "Only 3 remaining in stock" (When inventory data confirms 3 units.)
**❌ NON-COMPLIANT:** "Only 3 left — order now before they're gone!" (When the seller has 500 units in stock, or the system has no inventory data.)

**Tier: [HARD LEGAL REQUIREMENT]**

---

## 1.5 Endorsement & Testimonial Disclosure Requirements

**Rule:** When endorsements or testimonials are used in advertising, the connection between the endorser and the product (if not reasonably expected by the audience) must be clearly and conspicuously disclosed. Endorsements must reflect the honest opinions, beliefs, or experience of the endorser. Fabricated or AI-generated endorsements are a **distinct and higher-risk** category — see sub-entry below.

**Jurisdictions:** US, UK, EU, India.

**Key laws & bodies:**
- **US:** FTC Endorsement Guides (16 CFR Part 255) — updated July 2023. The 2023 update specifically addresses: (1) **fake reviews** — procuring a fake positive review is itself an endorsement violation; (2) **AI-generated endorsements** — using AI to create fake reviews or testimonials that appear to be from real people is deceptive; (3) influencer disclosure requirements (#ad, #sponsored must be clear and conspicuous). The Guides apply Section 5 of the FTC Act to endorsements.
- **EU:** UCPD Annex I — No. 11: "Using editorial content in the media to promote a product where a trader has paid for the promotion without making that clear in the content or by images or sounds clearly identifiable by the consumer." UCPD Annex I — No. 13: claiming a trader or product has been approved/endorsed by a public or private body when it has not.
- **UK:** CAP Code Section 2 (Recognition of marketing) and Section 3 (Misleading advertising). ASA enforces influencer disclosure rules. CMA has taken action against influencers for non-disclosure.
- **India:** ASCI Guidelines for Influencer Advertising in Digital Media — mandatory disclosures required (#ad, #sponsored). Health, nutrition, and financial influencer claims require additional substantiation. Doping and supers are also covered.

**Enforcement examples:**
- FTC warning letters (2023) sent to companies and influencers for non-disclosure of paid endorsements.
- FTC finalized settlement with LendEDU (2020) for fake reviews — the company fabricated rankings and reviews that appeared independent but were actually paid placements.

### 1.5a AI-Generated or Fabricated Testimonials — HIGHER RISK

**Rule:** Generating fake reviews, testimonials, or endorsements — including using AI to create reviews that appear to be from real customers — is a **distinct and higher-risk violation**. This is explicitly addressed by the FTC's 2023 Endorsement Guide update and the FTC's 2024 final rule banning fake reviews.

**Key laws & bodies:**
- **US:** **FTC Final Rule on Fake Reviews and Testimonials** (effective October 21, 2024) — prohibits: (1) fake reviews (including AI-generated reviews that don't reflect actual customer experience); (2) buying positive or negative reviews; (3) insider reviews that don't disclose the relationship; (4) suppressing negative reviews. Civil penalties can reach **$50,120 per violation** (adjusted for inflation). This is a standalone rule with direct penalty authority — the FTC does not need to go to court first.
- **EU:** UCPD Annex I No. 13 — falsely claiming a product has been approved/endorsed. The EU is also developing AI-specific transparency rules under the AI Act.
- **UK:** CPRs 2008 — fake reviews are a misleading commercial practice. DMCC Act 2024 strengthens CMA enforcement.

**Enforcement examples:**
- FTC's fake reviews rule (2024) is designed for direct enforcement against platforms and companies that generate or facilitate fake reviews.
- Amazon blocked over 275 million suspicious reviews in 2024; FTC has signaled willingness to fine marketplaces that don't adequately police fake reviews (potential fines up to $5 billion under the new rule).

**Critical for AI system:** The platform must NEVER generate testimonials, reviews, or endorsements that appear to be from real customers. The system must NOT generate star ratings, review quotes, or "customer testimonials" unless they come from verified, real customer data provided by the seller. Even if the seller requests "a testimonial," the system must refuse to fabricate one.

**✅ COMPLIANT:** Featuring a real, verified customer review that the seller provides, with clear attribution to the actual reviewer.
**❌ NON-COMPLIANT:** "⭐⭐⭐⭐⭐ 'This is the best product I've ever bought!' — Sarah M." (Where "Sarah M." is an AI-generated persona, not a real customer.)

**Tier: [HARD LEGAL REQUIREMENT] — highest-risk category in this entire document for an AI content generation system.**

---

## 1.6 Dark Pattern Regulation

**Rule:** User interface designs and marketing tactics that manipulate consumers into decisions against their interests — including confirm-shaming, hidden fees, drip pricing, forced continuity, roach motels, and pre-checked consent boxes — are regulated and prohibited.

**Jurisdictions:** EU, UK, US.

**Key laws & bodies:**
- **US:** FTC report "Bringing Dark Patterns to Light" (September 2022) — 48-page report documenting dark patterns in e-commerce, subscriptions, and cookie consent. FTC has used Section 5 authority to bring enforcement actions against companies using dark patterns. FTC's Rule on Unfair or Deceptive Fees (effective May 12, 2025) specifically addresses drip pricing and hidden fees in live-event ticketing and short-term lodging — and signals broader enforcement intent. California's automatic renewal law (AB 390) and false advertising law also address dark patterns.
- **EU:** Digital Services Act (Regulation 2022/2065) — Article 25 prohibits providers of online platforms from designing, organising or operating their online interfaces in a way that materially distorts or impairs the ability of recipients of the service to make autonomous and informed choices. Also addresses dark patterns in consent interfaces. The DSA also requires that online platforms do not use deceptive design to manipulate users. UCPD also addresses several dark pattern practices (Annex I list includes fake countdown timers, fake scarcity).
- **UK:** CMA has actively investigated online choice architecture and dark patterns. UK GDPR and PECR also address consent design requirements. DMCC Act 2024 strengthens enforcement.

**Specific dark patterns the system must avoid generating:**

| Dark Pattern | Description | Banned Under |
|---|---|---|
| **Confirm-shaming** | Using guilt or shame to push a choice ("No thanks, I don't want to save money") | FTC Section 5; EU DSA Art. 25 |
| **Hidden fees / Drip pricing** | Advertising a partial price, then adding mandatory fees later | FTC Rule on Fees (2025); EU UCPD Art. 7; UK CPRs |
| **Forced continuity** | Making it easy to subscribe but hard to cancel | FTC Section 5 (e.g., FTC v. ABC Financial); California AB 390 |
| **Roach motel** | Easy to get into a situation, hard to get out | FTC Section 5; EU DSA Art. 25 |
| **Pre-checked consent** | Pre-ticked boxes for paid add-ons or marketing | EU UCPD Annex I No. 20 (banned per se); UK CPRs |
| **Fake countdown timers** | Countdown that resets or has no real deadline | EU UCPD Annex I No. 17 (banned per se) |
| **Disguised advertising** | Ads that look like editorial content without disclosure | EU UCPD Annex I No. 11; FTC Endorsement Guides |

**Critical for AI system:** If the system generates marketing copy or UI elements for the seller's store, it must NOT produce any of the above dark patterns. In the EU, pre-checked consent boxes and fake countdown timers are on the UCPD blacklist — banned per se, no defense possible.

**✅ COMPLIANT:** "Subscribe to our newsletter for 10% off your next order." (Clear, opt-in, no manipulation.)
**❌ NON-COMPLIANT:** "No thanks, I prefer to pay full price and miss out on exclusive deals." (Confirm-shaming opt-out text.)

**Tier: [HARD LEGAL REQUIREMENT]**

---

# SECTION 2: Sexual, Obscene, and Adult Content Boundaries

---

## 2.1 Legal Definitions of Obscenity vs. Lawful Sexual Wellness Product Depiction

**Rule:** Marketing content must not cross the legal threshold of "obscenity" in any jurisdiction where it will be displayed. Legitimate sexual wellness, intimate apparel, and adult products CAN be marketed — but only in a manner that does not constitute legally obscene material. The definition of obscenity varies significantly by jurisdiction.

**Jurisdictions:** US, UK, EU (varies by member state), India.

**Key laws & tests:**
- **US — Miller Test** (from *Miller v. California*, 413 U.S. 15 (1973)): Material is obscene ONLY if ALL THREE prongs are met: (1) The average person, applying contemporary community standards, would find the work appeals to the prurient interest; (2) The work depicts or describes sexual conduct in a patently offensive way (defined by applicable state law); (3) The work, taken as a whole, lacks serious literary, artistic, political, or scientific value (LAPS test — judged by a reasonable person standard, national). Note: community standards vary by locality in the US — what's acceptable in New York may be obscene in a conservative county.
- **UK — Obscene Publications Act 1959** (Section 2): Material is obscene if its effect is "such as to tend to deprave and corrupt persons" who are likely to read, see, or hear it. Test is whether the material has a tendency to deprave and corrupt. UK also has the **Racial and Religious Hatred Act 2006** and **Communications Act 2003 Section 127** for extreme content.
- **EU — varies by member state.** No unified obscenity standard. Some member states (e.g., Germany) are relatively permissive; others (e.g., Poland, Hungary) have stricter rules. The EU does not directly regulate obscenity but member state laws apply. The **E-Commerce Directive 2000/31/EC** provides safe harbor for platforms but does not override national obscenity laws.
- **India — IPC Section 292** (criminalizes sale, distribution of obscene material — test based on "depraving and corrupting" effect, similar to UK Hicklin test historically, though Indian courts have moved toward a more modern standard). **IPC Section 293** specifically targets sale of obscene objects to persons under 20. **IT Act Section 67** criminalizes publishing or transmitting obscene material in electronic form (punishable with imprisonment up to 3 years + fine for first conviction, 5 years for subsequent). **IT Act Section 67A** covers sexually explicit material. **IT Act Section 67B** covers child sexual abuse material.

**Critical for AI system:** The system must apply the MOST RESTRICTIVE applicable obscenity standard. For a global automated system, the safest approach is: generate only non-explicit, non-graphic product imagery for sexual wellness / intimate products. The product itself can be shown (e.g., a vibrator, lingerie on a mannequin) but marketing imagery should NOT include: explicit sexual acts, graphic genital display, or content that would fail the Miller/LAPS test in conservative US jurisdictions or India's Section 292 standard.

**✅ COMPLIANT:** A clean product photo of a vibrator on a neutral background with the product name and features listed.
**❌ NON-COMPLIANT:** An AI-generated image depicting people engaging in sexual activity while using the product, with graphic nudity.

**Tier: [HARD LEGAL REQUIREMENT]**

---

## 2.2 Acceptable Marketing Imagery for Legitimate Sexual Wellness / Intimate Apparel

**Rule:** Marketing imagery for legitimate sexual wellness and intimate apparel products must be non-explicit and non-obscene. The product can be presented (e.g., on a mannequin, as a standalone product shot), but imagery must not depict sexual acts, graphic nudity, or content that would trigger obscenity laws.

**Jurisdictions:** All (standard applies globally for a cross-border system).

**Key platform policies (supplement legal rules):**
- **Amazon:** Prohibits "offensive goods" including products with nudity or sexually suggestive imagery in product images. Adult products must be categorized appropriately and are subject to additional restrictions.
- **eBay:** Adult-only categories exist but with strict listing rules — images must not contain nudity or sexually explicit content. Items restricted to the "Adults Only" category.
- **Etsy:** Prohibits pornographic material. Sexual wellness items are allowed if not pornographic. Intimate apparel is allowed if presented non-sexually.
- **Shopify/Shop app:** Prohibits "adult" and "age-restricted" products on the Shop channel.
- **TikTok Shop:** Prohibits "adult products and services" including sexual wellness devices, intimate apparel with explicit imagery.
- **Meta (Facebook/Instagram):** Restricts ads for sexual wellness products; images must not be sexually suggestive.

**Critical for AI system:** When generating product imagery for sexual wellness or intimate apparel categories, the system must use conservative defaults: mannequin or flat-lay product photography, no human models in suggestive poses, no nudity, no sexually explicit contexts.

**✅ COMPLIANT:** A flat-lay photo of a lingerie set on a neutral background with product description.
**❌ NON-COMPLIANT:** An AI-generated image of a person wearing the lingerie in a sexually suggestive pose.

**Tier: [HARD LEGAL REQUIREMENT] (obscenity laws) + [PLATFORM POLICY] (marketplace restrictions)**

---

## 2.3 Age-Verification / Age-Gating Requirements

**Rule:** Marketing or selling age-restricted products online requires age verification or age-gating mechanisms. The specific requirements vary by jurisdiction and product type.

**Jurisdictions:** UK (most prescriptive), EU, US (state-by-state), India.

**Key laws & bodies:**
- **UK — Online Safety Act 2023:** Requires online services with UK users to implement "highly effective" age assurance checks to prevent minors from accessing age-restricted content. Ofcom oversees compliance. Failure to comply can result in significant fines (up to £18 million or 10% of global revenue). This applies to platforms, not just individual sellers, but the platform's content generation must support age-gating.
- **US — varies by state.** No federal age-verification standard for e-commerce, but states are increasingly passing laws. Louisiana, Utah, Mississippi, Virginia, Texas, and others have passed age-verification laws (primarily targeting adult content sites, but applicable to age-restricted product sales). **COPPA** (Children's Online Privacy Protection Act) — applies to services directed at children under 13; updated rule takes effect April 22, 2026.
- **EU — DSA (Regulation 2022/2065):** Requires online platforms to put in place measures to protect minors. Article 28 specifically addresses protection of minors. No uniform age-verification mandate, but platforms must implement age-appropriate measures.
- **India — IT Rules 2021** require intermediaries to observe due diligence, including age-gating for certain content categories.

**Critical for AI system:** If the system generates content for age-restricted products (sexual wellness, alcohol, tobacco/vaping), the content itself must include age-gating signals or be flagged for age-restricted display. The system should tag any content generated for age-restricted categories so the platform can apply age-gating downstream.

**✅ COMPLIANT:** Generating a product page for an intimate wellness product with an "18+ only" age-gate prompt and non-explicit imagery.
**❌ NON-COMPLIANT:** Generating sexual wellness product content with no age-gating, accessible to all users.

**Tier: [HARD LEGAL REQUIREMENT]**

---

## 2.4 Market/Platform Divergence on Adult Content

**Rule:** Different markets and platforms have vastly different tolerance levels for sexual wellness and adult-adjacent content. Content that is legal and platform-acceptable in one market may be banned in another.

**Jurisdictions:** Global.

**Key divergence examples:**

| Market/Platform | Tolerance Level |
|---|---|
| **US (most states)** | Legal to sell sexual wellness products; marketing must pass Miller test. Amazon/eBay allow with restrictions. |
| **UK** | Legal; ASA/CAP codes require tasteful presentation. Online Safety Act 2023 imposes age-assurance. |
| **EU (Germany, Netherlands)** | Relatively permissive; sexual wellness products openly sold. |
| **EU (Poland, Hungary)** | More conservative; some products may face restrictions. |
| **India** | Highly restricted. IPC 292/293 and IT Act 67 criminalize obscene content. Sexual wellness products can be sold but marketing must be extremely conservative — no suggestive imagery. ASCI prohibits ads that are "indecent, repulsive or offensive." |
| **Middle East / Gulf** | Most sexual wellness products are prohibited entirely. Marketing such products can result in criminal liability. |
| **Amazon** | Restricted; adult category requires approval. No nudity in images. |
| **Etsy** | Allowed if non-pornographic. |
| **TikTok Shop** | Prohibits adult products entirely. |
| **Shopify Shop channel** | Prohibits adult/age-restricted products. |

**Critical for AI system:** The system must apply a **most restrictive applicable jurisdiction** approach for sexual wellness content when the target market is unknown or includes conservative jurisdictions. Default to the most conservative presentation standards (clean product shots, clinical descriptions, no suggestive imagery).

**Tier: [HARD LEGAL REQUIREMENT] (in restrictive jurisdictions) + [PLATFORM POLICY]**

---

# SECTION 3: Discrimination, Hate Speech, and Cultural/Religious Sensitivity

---

## 3.1 Anti-Discrimination / Anti-Hate-Speech Boundaries

**Rule:** Marketing content must not target, disparage, or stereotype based on religion, ethnicity, nationality, gender, sexual orientation, disability, age, or other protected characteristics. Both legal prohibitions and platform policies prohibit discriminatory content.

**Jurisdictions:** US, UK, EU, India.

**Key laws & bodies:**
- **US:** Civil Rights Act of 1964 (Title VII — employment, but principles extended to advertising). FTC Act Section 5 (unfair or deceptive practices can include discriminatory advertising). Fair Housing Act prohibits discriminatory housing ads. State civil rights laws. Platform policies (Meta, Google, Amazon) prohibit hate speech and discriminatory content.
- **UK:** Equality Act 2010 — prohibits discrimination on the basis of: age, disability, gender reassignment, marriage and civil partnership, pregnancy and maternity, race, religion or belief, sex, sexual orientation. ASA/CAP codes prohibit ads that cause harm or offense, including discriminatory content.
- **EU:** Race Equality Directive 2000/43/EC — prohibits discrimination on grounds of racial or ethnic origin. Equal Treatment Directive 2004/113/EC — prohibits sex discrimination in goods and services. EU Framework Decision 2008/913/JHA on combating certain forms of racism and xenophobia (requires member states to criminalize hate speech).
- **India:** Constitution Article 15 — prohibits discrimination on grounds of religion, race, caste, sex, or place of birth. **IPC Section 153A** — criminalizes promoting enmity between different groups on grounds of religion, race, place of birth, residence, language, etc. **IPC Section 295A** — criminalizes deliberate acts intended to outrage religious feelings (see Section 3.2). ASCI Code prohibits ads that "deride any race, caste, color, creed, or nationality."

**Enforcement examples:**
- ASA (UK) routinely bans advertisements for racist, sexist, or homophobic content.
- Meta, Google, Amazon, and other platforms actively remove and ban accounts for hate speech and discriminatory content.
- In India, IPC Section 153A prosecutions have been brought for social media content promoting enmity.

**Critical for AI system:** The system must have filters that block generation of any content that disparages, stereotypes, or targets protected groups. This includes both explicit derogatory language and more subtle stereotyping (e.g., depicting certain ethnicities only in subservient roles, using religious imagery in mocking ways).

**✅ COMPLIANT:** A diverse group of people using a product, with no group singled out or stereotyped.
**❌ NON-COMPLIANT:** "Perfect for REAL men who don't need safe spaces" (Disparaging language targeting perceived vulnerability; gender stereotyping.)

**Tier: [HARD LEGAL REQUIREMENT] + [PLATFORM POLICY]**

---

## 3.2 Religious Symbols / Figures / Practices in Commercial Marketing

**Rule:** Depicting or referencing religious symbols, figures, or practices in commercial marketing carries significant legal and cultural risk, especially in jurisdictions with blasphemy-adjacent laws. What is acceptable in one country may be criminal in another.

**Jurisdictions:** India (most prescriptive blasphemy law), UK, EU (varies), US (First Amendment protects most speech but platform policies still apply).

**Key laws & bodies:**
- **India — IPC Section 295A:** Criminalizes "deliberate and malicious acts, intended to outrage religious feelings or any class by insulting its religion or religious beliefs." Punishable with imprisonment up to 3 years + fine. Cognizable, non-bailable, non-compoundable offense. This is India's de facto blasphemy law. It applies to commercial content — using religious deities or symbols in a way that could be seen as disrespectful is a criminal offense. ASCI Code also prohibits ads that "deride any religion."
- **UK — Racial and Religious Hatred Act 2006:** Criminalizes threatening words/behavior intended to stir up religious hatred. Threshold is high (must be "threatening" and intentional), but applies to commercial content.
- **EU — varies by member state.** Several member states have blasphemy or religious insult laws (e.g., Greece had Article 199 of Penal Code — abolished in 2019; Italy has Article 403 of Penal Code — "offence to religion"; Denmark had blasphemy law until 2017; Ireland had blasphemy offense until 2018). Germany's §166 StGB criminalizes defamation of religion. Poland has Article 196 of Penal Code.
- **US — First Amendment:** Provides strong protection for speech, including speech about religion. No blasphemy law. However, using religious imagery in marketing that mocks or disparages a religion, while generally legal, would violate platform policies and could trigger boycotts and reputational damage. The Lanham Act could apply if the use implies religious endorsement.

**Critical for AI system:** The system must NOT generate marketing content that uses religious symbols, deities, figures, or sacred texts in a commercial context unless the seller explicitly confirms the appropriateness and cultural sensitivity of the usage. For Indian sellers or global audiences, IPC 295A is a particular concern — even inadvertently offensive use of Hindu deities, Islamic symbols, or other religious imagery in product marketing can trigger criminal prosecution. Default approach: do not incorporate religious imagery into generated marketing content unless explicitly authorized and reviewed.

**✅ COMPLIANT:** A product marketed without any religious imagery, or with culturally appropriate, respectful use of a religious holiday theme that the seller has confirmed is appropriate (e.g., "Gift ideas for Diwali" with culturally appropriate imagery).
**❌ NON-COMPLIANT:** An AI-generated image placing a Hindu deity on a beer label, or using a Buddhist symbol as a decorative element on an intimate product.

**Tier: [HARD LEGAL REQUIREMENT] (India IPC 295A, EU member state blasphemy laws) + [BEST-PRACTICE CAUTION] (US — legal but high-risk)**

---

## 3.3 Advertising-Targeting Restrictions Based on Protected Characteristics

**Rule:** If the system recommends or enables targeted marketing based on user/consumer characteristics, it must not target (or exclude) audiences based on protected characteristics (race, religion, ethnicity, sexual orientation, etc.).

**Jurisdictions:** EU, UK, US.

**Key laws & bodies:**
- **EU:** GDPR Article 22 — right not to be subject to decisions based solely on automated processing, including profiling. EU AI Act provisions on prohibited AI practices (Article 5 prohibits AI systems that deploy subliminal techniques or exploit vulnerabilities of specific groups). Race Equality Directive 2000/43/EC.
- **UK:** UK GDPR Article 22 (same as EU). Equality Act 2010.
- **US:** Various civil rights laws. HUD has pursued cases against Facebook for discriminatory ad targeting in housing. State laws on algorithmic discrimination emerging.
- **India:** DPDP Act 2023 — provisions on profiling and automated decision-making (less prescriptive than GDPR).

**Critical for AI system:** If the platform generates audience targeting recommendations, it must NOT recommend targeting based on protected characteristics. It must also NOT recommend excluding certain demographics from seeing a product (e.g., "don't show this ad to people over 50").

**✅ COMPLIANT:** "Target this product to users interested in handmade jewelry and sustainable fashion."
**❌ NON-COMPLIANT:** "Target this product to white women aged 25-35" or "Exclude users in [specific ethnic] neighborhoods."

**Tier: [HARD LEGAL REQUIREMENT]**

---

# SECTION 4: Health, Medical, and Supplement Claims

---

## 4.1 Health Claims / Medical Claims / "Cures-Treats-Prevents" Language

**Rule:** Products that are not licensed/approved as drugs or medical devices must NOT make disease-treatment claims — i.e., claims that the product cures, treats, prevents, mitigates, or diagnoses a disease or health condition. Only products with regulatory approval as drugs/devices may make such claims. Non-drug products (supplements, cosmetics, wellness products) are restricted to structure/function claims (see 4.2).

**Jurisdictions:** US, EU, UK, India.

**Key laws & bodies:**
- **US:** Federal Food, Drug, and Cosmetic Act (FD&C Act). Under **DSHEA** (Dietary Supplement Health and Education Act 1994), dietary supplements may NOT claim to "diagnose, mitigate, treat, cure, or prevent" a specific disease or condition. FDA's Office of Dietary Supplement Programs (ODSP) enforces. FDA labeling regulations: 21 CFR 101.93. Cosmetics are regulated under FD&C Act Section 609 — cosmetic products must not make drug claims (claims that a product affects the body's structure or function in a therapeutic way). FTC also enforces against deceptive health claims under FTC Act Section 5. FTC Health Products Compliance Guidance provides detailed guidelines.
- **EU:** Regulation (EC) 1924/2006 on Nutrition and Health Claims — requires pre-authorization of health claims via EFSA (European Food Safety Authority). Regulation (EC) 1223/2009 on Cosmetic Products — cosmetics must not make medical/therapeutic claims. Medicinal Products Directive 2001/83/EC — defines the boundary between cosmetic and medicinal products (the "borderline products" issue). EU UCPD also prohibits unsubstantiated health claims.
- **UK:** MHRA (Medicines and Healthcare products Regulatory Agency) guidelines — distinguishes between cosmetics and medicines. Post-Brexit, UK has retained EU-derived regulations. UK Cosmetics Regulation (UKCR). ASA/CAP codes prohibit misleading health claims.
- **India:** **FSSR** (Food Safety and Standards Regulations) under the Food Safety and Standards Act 2006 — governs health claims for food products. **DCA** (Drugs and Cosmetics Act 1940) — governs drugs and cosmetics; cosmetics must not make drug claims. ASCI Code prohibits ads for products that "claim to cure ailments or conditions for which qualified medical advice should be sought" unless properly substantiated.

**Enforcement examples:**
- FTC has brought numerous cases against supplement companies for disease-treatment claims (e.g., Goop settled with FTC over unsubstantiated health claims in 2018; CBD companies fined for unproven disease claims).
- FDA issues warning letters routinely to supplement and cosmetic companies making drug claims.
- ASA (UK) routinely bans ads for unsubstantiated health claims.

**Critical for AI system:** The system must maintain a list of **prohibited disease terms** for non-drug products. Any generated content for supplements, cosmetics, food, or wellness products that includes claims like "cures," "treats," "prevents," "fights," "eliminates" + a disease name (e.g., "cures acne," "prevents COVID," "treats diabetes") must be blocked.

**✅ COMPLIANT:** "Supports immune health" (Structure/function claim for a supplement — with required disclaimer.)
**❌ NON-COMPLIANT:** "Cures your acne in 7 days" (Disease-treatment claim for a cosmetic/supplement — illegal.)

**Tier: [HARD LEGAL REQUIREMENT]**

---

## 4.2 Structure/Function Claim Limitations

**Rule:** Non-drug products (supplements, foods, cosmetics) may make structure/function claims — claims about the product's effect on the body's normal structure or function — but these claims have specific requirements: (1) They must not claim to treat disease; (2) In the US, they must include a specific FDA-required disclaimer; (3) In the EU, they must be pre-authorized by EFSA; (4) They must be substantiated.

**Jurisdictions:** US, EU, UK, India.

**Key laws & bodies:**
- **US — FDA 21 CFR 101.93:** Dietary supplement structure/function claims must include the disclaimer: **"This statement has not been evaluated by the FDA. This product is not intended to diagnose, treat, cure, or prevent any disease."** This disclaimer is MANDATORY — its omission makes the product misbranded. Structure/function claims may describe: (a) the role of a nutrient/substance in affecting normal body structure or function; (b) the mechanism by which a nutrient maintains such structure/function; or (c) general well-being from consumption of a nutrient.
- **EU — Regulation 1924/2006:** Health claims must be authorized by EFSA and listed in the EU Register of nutrition and health claims. Only authorized claims may be used. "General function" claims (Article 13) and "new function" claims (Article 14) have different authorization pathways. Non-authorized claims are prohibited.
- **UK:** Retained EU law post-Brexit. MHRA oversees borderline products.
- **India:** FSSR requires pre-approval of health claims for food products. ASCI requires substantiation for all health claims.

**Critical for AI system:** When generating claims for supplements or wellness products:
1. For US: automatically append the FDA disclaimer to any structure/function claim.
2. For EU: only use claims from the EU authorized list, or flag for seller verification.
3. Never generate disease-treatment claims (blocked per 4.1).
4. Flag all health-related claims for seller substantiation review.

**✅ COMPLIANT (US):** "Supports joint health. *This statement has not been evaluated by the FDA. This product is not intended to diagnose, treat, cure, or prevent any disease.*"
**❌ NON-COMPLIANT (US):** "Supports joint health." (Missing FDA disclaimer → misbranded product.)

**Tier: [HARD LEGAL REQUIREMENT]**

---

## 4.3 Special Restrictions for Vulnerable Groups (Children, Elderly, Pregnant Individuals)

**Rule:** Marketing claims directed at or about vulnerable populations — children, the elderly, pregnant or nursing individuals — carry additional restrictions and heightened scrutiny. Claims about product safety or efficacy for these groups require a higher level of substantiation.

**Jurisdictions:** US, EU, UK, India.

**Key laws & bodies:**
- **US:** FDA requires specific labeling for products intended for vulnerable groups. FTC applies heightened scrutiny to health claims targeting vulnerable populations. COPPA restricts data collection from children under 13.
- **EU:** EFSA has specific guidance for health claims targeting children — many health claims are restricted or prohibited for use in marketing to children. EU PARNUT (foods for particular nutritional uses) regulations. Regulation 1924/2006 Article 14 requires specific authorization for claims referring to children's development and health.
- **UK:** ASA/CAP codes have specific rules for ads targeting children or making claims about children's health. MHRA guidance on pregnancy and breastfeeding product claims.
- **India:** ASCI Code Chapter 4 — specific restrictions on advertising to children. FSSR restrictions on claims for infant foods (Infant Milk Substitutes, Feeding Bottles and Infant Foods Act 1992 prohibits advertising of infant milk substitutes and feeding bottles entirely).

**Critical for AI system:** The system must apply additional caution when generating content for products that could be used by vulnerable groups:
1. Do NOT generate health/efficacy claims for products targeting pregnant/nursing individuals without explicit, verified substantiation.
2. Do NOT generate content that markets supplements or health products directly to children.
3. For products for the elderly, do not generate fear-based marketing ("Don't let your family down — buy this supplement").
4. In India, do NOT generate any marketing content for infant milk substitutes or feeding bottles (banned entirely).

**✅ COMPLIANT:** "A gentle, fragrance-free lotion suitable for the whole family" (General claim, not targeting vulnerable groups with unproven safety claims.)
**❌ NON-COMPLIANT:** "Proven safe for your unborn baby — prevents developmental issues" (Unsubstantiated claim targeting pregnant individuals.)

**Tier: [HARD LEGAL REQUIREMENT]**

---

# SECTION 5: Regulated and Restricted Product Categories

---

## 5.1 Category-Specific Advertising/Sale Restrictions

**Rule:** Certain product categories are heavily regulated in how they can be advertised and sold online. The AI system must apply category-specific restrictions when generating marketing content for these categories.

**Jurisdictions:** Varies by category — see below.

### 5.1a Alcohol

**Laws & bodies:**
- **US:** TTB (Alcohol and Tobacco Tax and Trade Bureau) regulates alcohol advertising. FDA has some oversight. State laws vary widely (control states vs. license states). Many states restrict online alcohol sales and advertising. Federal regulations prohibit alcohol ads that appeal to minors, depict intoxication, or make health claims.
- **UK:** ASA/CAP Code Section 18 (Alcohol) — alcohol ads must not: appeal to people under 18, be directed at under-18s, link alcohol to sexual success, depict irresponsible drinking, claim alcohol has therapeutic qualities. Licensing Act 2003. CMA enforcement.
- **EU:** Audiovisual Media Services Directive (AVMSD) 2018/1808 — restricts alcohol advertising in audiovisual media. National laws vary — some countries (France, Norway) have near-total advertising bans on alcohol.
- **India:** ASCI Code Chapter 6 — prohibits advertising of products whose sale is restricted by law (alcohol is subject to state-level prohibition). In states where alcohol is legal, advertising is still heavily restricted. Many platforms simply ban alcohol advertising.

**✅ COMPLIANT:** "A premium artisanal IPA from our local microbrewery — rich hoppy flavor with citrus notes." (Factual product description, no health/sexual/lifestyle manipulation claims, not targeted at minors.)
**❌ NON-COMPLIANT:** "Drink this and you'll be the life of every party — girls will love you!" (Links alcohol to social/sexual success — banned in UK, most EU states, India.)

**Tier: [HARD LEGAL REQUIREMENT]**

### 5.1b Tobacco / Vaping

**Laws & bodies:**
- **US:** FDA regulates tobacco products under the Family Smoking Prevention and Tobacco Control Act 2009. Tobacco advertising is heavily restricted — no TV/radio advertising of cigarettes; warning labels required; cannot target minors; free samples prohibited. E-cigarettes/vaping products regulated as tobacco products since 2016 (Deeming Rule). FDA restrictions on advertising that appeals to youth.
- **EU:** Tobacco Products Directive 2014/40/EU — bans cross-border tobacco advertising and sponsorship (in print, radio, internet). Same restrictions now apply to e-cigarettes. Health warnings required. Ban on menthol cigarettes. Packaging requirements.
- **UK:** Tobacco Products (Safety) Regulations, Tobacco Advertising and Promotion Act 2002 (bans most tobacco advertising). UK TRPR (Tobacco and Related Products Regulations 2016) — implements EU TPD provisions post-Brexit. Vaping products are regulated but with fewer advertising restrictions than tobacco (though ASA/CAP codes apply).
- **India:** Cigarettes and Other Tobacco Products Act 2003 (COTPA) — prohibits all forms of direct and indirect advertising of tobacco products. Section 5 bans advertising of tobacco products. E-cigarettes banned entirely in India (Prohibition of Electronic Cigarettes Act 2019).

**✅ COMPLIANT:** Not generating marketing content for tobacco/vaping products (or if required, only factual product information with mandatory health warnings, in jurisdictions where it's legal).
**❌ NON-COMPLIANT:** "The smoothest vape you'll ever try — perfect for beginners!" (Marketing vaping product in a youth-appealing way — violates FDA, EU TPD, and is entirely illegal in India.)

**Tier: [HARD LEGAL REQUIREMENT]**

### 5.1c Weapons / Weapon Replicas

**Laws & bodies:**
- **US:** Federal and state laws restrict sale and advertising of firearms, ammunition, and weapons. ATF regulates firearms. Many platforms (Amazon, eBay, Etsy, Shopify Shop, TikTok Shop) prohibit weapon sales entirely.
- **UK:** Firearms Act 1968 — strict regulation of firearm sales and advertising. Offensive Weapons Act 2019.
- **EU:** Firearms Directive 2008/51/EC — restricts civilian firearm possession and sale.
- **India:** Arms Act 1959 — strict licensing requirements. ASCI prohibits ads for weapons.

**Platform policies:** Virtually all major marketplaces (Amazon, eBay, Etsy, Shopify Shop, TikTok Shop) prohibit or heavily restrict weapon sales. eBay allows some antique/collectible weapons with restrictions.

**Tier: [HARD LEGAL REQUIREMENT] + [PLATFORM POLICY]**

### 5.1d Drug Paraphernalia

**Laws & bodies:**
- **US:** 21 USC §863 — criminalizes the sale, offer for sale, and import/export of drug paraphernalia. Federal crime. Many states also have their own laws.
- **EU:** Varies by member state. Generally regulated but not uniformly criminalized.
- **UK:** Psychoactive Substances Act 2016 and Misuse of Drugs Act 1971.
- **India:** NDPS Act 1985 (Narcotic Drugs and Psychotropic Substances Act).

**Platform policies:** All major platforms prohibit drug paraphernalia.

**Tier: [HARD LEGAL REQUIREMENT] + [PLATFORM POLICY]**

### 5.1e Pharmaceuticals (Prescription Drugs)

**Laws & bodies:**
- **US:** FDA regulates prescription drug advertising under FD&C Act. Direct-to-consumer (DTC) advertising of prescription drugs is legal but heavily regulated: must include "fair balance" of risks and benefits, brief summary of side effects, and other requirements. OTC drug advertising regulated by FDA and FTC.
- **EU:** Directive 2001/83/EC — **prohibits direct-to-consumer advertising of prescription drugs entirely.** Only disease awareness campaigns (without mentioning specific products) are permitted. This is a MAJOR divergence from US law.
- **UK:** Same as EU — prescription drug advertising to the public is prohibited under the Human Medicines Regulations 2012.
- **India:** Drugs and Magic Remedies (Objectionable Advertisements) Act 1954 — prohibits advertising of certain drugs and remedies, including prescription drugs to the public. DCA 1940.

**Critical for AI system:** The system must NOT generate marketing content for prescription pharmaceuticals directed at consumers, as this is illegal in the EU, UK, and India. Even in the US, prescription drug advertising has complex requirements (fair balance, risk information) that an automated system cannot easily satisfy.

**✅ COMPLIANT:** Not generating consumer-facing marketing for prescription drugs.
**❌ NON-COMPLIANT:** "Ask your doctor about [Prescription Drug X] — it'll change your life!" (Illegal in EU/UK/India; non-compliant with FDA requirements in US without fair balance and risk info.)

**Tier: [HARD LEGAL REQUIREMENT]**

### 5.1f Financial Products

**Laws & bodies:**
- **US:** CFPB (Consumer Financial Protection Bureau) regulates financial product marketing. Truth in Lending Act (TILA), Equal Credit Opportunity Act. SEC regulates investment product advertising.
- **UK:** FCA (Financial Conduct Authority) — strict rules on financial product advertising, including risk warnings, clear and fair presentation, and suitability requirements. ASA/CAP Code Section 13 (Financial products).
- **EU:** MiFID II (Directive 2014/65/EU) — regulates marketing of financial instruments. Prospectus Regulation for investment products.
- **India:** SEBI (Securities and Exchange Board of India) regulations; RBI guidelines for banking products.

**Critical for AI system:** Financial product marketing requires specific risk disclosures, regulatory licenses, and compliance reviews that an automated system cannot provide. The system should flag financial product content for mandatory human review.

**Tier: [HARD LEGAL REQUIREMENT]**

---

## 5.2 Children's Products — Safety & Marketing-Claim Regulations

**Rule:** Children's products are subject to specific safety standards and marketing-claim regulations that go beyond general product rules. Marketing claims about safety, age-appropriateness, and educational benefits are regulated.

**Jurisdictions:** US, EU, UK, India.

**Key laws & bodies:**
- **US — CPSIA (Consumer Product Safety Improvement Act 2008):** 15 USC 2056. Children's products must: (1) undergo third-party testing by CPSC-accepted labs; (2) have a written Children's Product Certificate (CPC); (3) comply with lead content limits (≤100 ppm lead in substrate, ≤90 ppm lead in paint/surface coating); (4) comply with phthalate bans (8 phthalates permanently banned at >0.1%); (5) comply with ASTM F963 Toy Safety Standard; (6) have tracking labels. CPSC enforces. Non-compliance can result in product recalls, fines, and civil/criminal penalties.
- **EU — Toy Safety Directive 2009/48/EC:** Requires CE marking, safety assessments, chemical migration limits, and compliance with EN 71 standards. General Product Safety Regulation (EU) 2023/960 (replaced GPSD).
- **UK — Toy (Safety) Regulations 2011:** Implements EU Toy Safety Directive. UKCA marking required post-Brexit (though CE marking still accepted in some circumstances).
- **India:** BIS (Bureau of Indian Standards) ISI marking required for certain toys. Toys (Quality Control) Order 2020 mandates BIS certification for toys.

**Critical for AI system:** When generating marketing content for children's products:
1. Do NOT generate safety claims ("100% safe," "non-toxic," "lead-free") unless verified from seller-provided test results.
2. Do NOT generate age-range claims without seller verification.
3. Do NOT generate "educational benefit" claims without substantiation.
4. Do NOT generate claims implying the product meets safety standards (CPSIA, EN 71, ASTM) unless the seller has provided certification.

**✅ COMPLIANT:** "A colorful wooden puzzle recommended for ages 3+." (Factual, no unverifiable safety claims.)
**❌ NON-COMPLIANT:** "The safest toy on the market — certified non-toxic, lead-free, and educational!" (Unsubstantiated safety and educational claims — may violate CPSIA, FTC Act, and EU regulations.)

**Tier: [HARD LEGAL REQUIREMENT]**

---

## 5.3 Restrictions on Advertising Directly to Children

**Rule:** Advertising directed at children is subject to additional restrictions beyond general children's product rules. These restrictions apply to both the content of the advertising and the methods of delivery.

**Jurisdictions:** US, UK, EU, India.

**Key laws & bodies:**
- **US:** COPPA (Children's Online Privacy Protection Act) — restricts collection of personal information from children under 13. **Updated COPPA Rule takes effect April 22, 2026** — strengthened requirements. FTC Children's Online Privacy Protection Rule (16 CFR Part 312). FTC guidelines on advertising to children. Better Business Bureau's Children's Advertising Review Unit (CARU) guidelines. Food advertising to children is under particular scrutiny.
- **UK:** ASA/CAP Code Section 5 (Children) — ads must not: exploit children's credulity, loyalty, or vulnerability; encourage children to pester parents; show children in dangerous situations; imply that a product makes a child superior. Online Safety Act 2023 — additional protections for children online. HFSS (High Fat, Salt, Sugar) advertising restrictions — UK ban on TV and online advertising of junk food before 9pm watershed (in effect).
- **EU:** AVMSD 2018/1808 — Article 7b requires protection of minors from audiovisual commercial communications that could cause physical, mental, or moral detriment. Various member state laws on advertising to children.
- **India:** ASCI Code Chapter 4 — ads must not exploit children's vulnerability or encourage them to consume unhealthy products. Infant Milk Substitutes Act 1992 — bans all advertising of infant milk substitutes and feeding bottles. ASCI Guidelines on advertising of food and beverages to children.

**Critical for AI system:**
1. Do NOT generate marketing content that is designed to appeal primarily to children under 13 (e.g., cartoon characters, "ask your parents to buy this" language).
2. Do NOT generate content that exploits children's vulnerability or encourages pestering.
3. For food/beverage products, apply additional scrutiny for content targeting children (HFSS restrictions in UK).
4. In India, block ALL content for infant milk substitutes and feeding bottles.

**✅ COMPLIANT:** "A fun craft kit the whole family can enjoy — parental supervision recommended for younger children." (Marketed to parents, not directly to children.)
**❌ NON-COMPLIANT:** "Kids, tell your mom to buy you this amazing toy NOW!" (Directly targeting children, encouraging pestering — violates CAP Code, ASCI Code, FTC guidelines.)

**Tier: [HARD LEGAL REQUIREMENT]**

---

# SECTION 6: Intellectual Property

---

## 6.1 Copyright — AI-Generated Content Resembling Existing Works

**Rule:** AI-generated marketing content (images, video, text) must not closely resemble or reproduce existing copyrighted works — including specific images, characters, brand assets, artistic styles, or other protected works — without authorization. Even if the AI "invents" the similarity, the platform and seller can face copyright infringement liability.

**Jurisdictions:** US, UK, EU, India.

**Key laws & bodies:**
- **US:** Copyright Act (17 USC). **US Copyright Office** issued its "Copyright and Artificial Intelligence, Part 2: Copyrightability Report" (2025) — confirming that **fully AI-generated content cannot be copyrighted** (no human authorship). However, this does NOT mean AI-generated content is free from infringement risk — if AI output substantially resembles a copyrighted work, it can still infringe. Key cases: *Andersen v. Stability AI* (image generation case, ongoing); *Getty Images v. Stability AI* (UK and US cases — Getty alleged AI image generator reproduced copyrighted images). The question of whether AI training data use is fair use remains **[EVOLVING AREA]**.
- **UK:** Copyright, Designs and Patents Act 1988 (CDPA). UK also has a specific provision (Section 9(3)) for computer-generated works, though its future is uncertain. *Getty Images v. Stability AI* case is being litigated in the UK.
- **EU:** Copyright Directive 2019/790 (Directive on Copyright in the Digital Single Market). Article 4 (text and data mining exception) and Article 17 (online content-sharing platforms) are relevant. Individual member state laws apply.
- **India:** Copyright Act 1957. Indian courts have recognized copyright in AI-assisted works where there is human creative contribution, but fully AI-generated works' copyrightability is **[UNSETTLED]**.

**Enforcement examples:**
- *Getty Images v. Stability AI* — Getty sued Stability AI in both UK and US for training its AI on Getty's copyrighted images without license and for generating outputs that reproduced Getty images (including watermarks).
- Multiple class action lawsuits filed against AI image generation companies (Stability AI, Midjourney, DeviantArt) in the US.
- *Advance Local v. Cohere* — potentially the first case holding that AI "hallucinations" (misattributing content) may create Lanham Act liability.

**Critical for AI system:**
1. The system must have safeguards to prevent generating images, video, or text that closely resembles known copyrighted characters (e.g., Disney characters, anime characters), brand assets, or specific artistic works.
2. Even if the seller doesn't request a copyrighted character, the AI model might inadvertently generate something similar — post-generation similarity checks are recommended.
3. The system should NOT generate content in the style of a specific, identifiable living artist (style itself is generally not copyrightable, but close imitation of specific works is risky).
4. **[EVOLVING AREA]**: The legal framework for AI-generated content copyright and infringement is rapidly evolving. The system should err on the side of caution.

**✅ COMPLIANT:** Generating an original product photo with a unique composition and style.
**❌ NON-COMPLIANT:** Generating a product image that resembles Mickey Mouse or uses a distinctively Pixar-style character to promote a product.

**Tier: [HARD LEGAL REQUIREMENT] — though specific boundaries are [EVOLVING AREA]**

---

## 6.2 Trademark — Unauthorized Use of Real Brand Names/Logos

**Rule:** AI-generated marketing content must not use or imply association with real brand names, logos, or trade dress without authorization. This includes using a competitor's trademark in comparative advertising (which is allowed with conditions) and implying a product is from, sponsored by, or endorsed by a brand it isn't.

**Jurisdictions:** US, UK, EU, India.

**Key laws & bodies:**
- **US:** Lanham Act (15 USC) — prohibits trademark infringement (likelihood of confusion), false designation of origin, and trademark dilution (for famous marks). FTC also enforces against false endorsement claims.
- **EU:** EU Trade Mark Regulation 2017/1001 and national trademark laws. EU Trade Mark Directive 2015/2436.
- **UK:** Trade Marks Act 1994.
- **India:** Trade Marks Act 1999.

**Comparative advertising rules:**
- **US:** FTC Statement of Policy Regarding Comparative Advertising — comparative advertising is permitted if: (1) the comparison is truthful; (2) it is not deceptive; (3) it does not disparage. Naming a competitor's brand is allowed if truthful and not misleading.
- **EU:** UCPD Article 6(2) and Directive 2006/114/EC (Misleading and Comparative Advertising Directive) — comparative advertising is permitted but only under strict conditions: must not be misleading, must compare goods/services meeting same needs, must objectively compare material features, must not create confusion, must not discredit competitors.
- **UK:** CPRs 2008 and Business Protection from Misleading Marketing Regulations 2008.

**Critical for AI system:**
1. Do NOT generate content that includes real brand names/logos unless the seller confirms they own the brand or have authorization.
2. Do NOT generate content that implies a product is "just like [Brand X]" or "a cheaper alternative to [Brand X]" without clear, truthful comparison and no likelihood of confusion.
3. Do NOT generate AI images that include real brand logos as elements (the AI model might insert them inadvertently).
4. Do NOT generate content that implies endorsement by a brand or celebrity without verified authorization.
5. Trademark dilution risk: even non-competing use of a famous mark (e.g., using "Nike-style" swoosh on a jewelry product) can be dilution.

**✅ COMPLIANT:** "Our handmade leather wallet — full-grain Italian leather, hand-stitched." (No unauthorized brand references.)
**❌ NON-COMPLIANT:** "Like a Louis Vuitton but half the price!" (Uses a famous brand name to sell an unrelated product — trademark infringement/dilution risk.)

**Tier: [HARD LEGAL REQUIREMENT]**

---

## 6.3 Right of Publicity / Likeness — Generating Images of Real People

**Rule:** AI-generated marketing content must not use the likeness, image, voice, or other identifiable features of real, identifiable people without their consent. This is a distinct legal issue from copyright (it protects the person, not a creative work).

**Jurisdictions:** US (varies by state), UK, EU, India.

**Key laws & bodies:**
- **US:** Right of publicity is governed by **state law** — varies significantly. States with strong publicity rights: California (Cal. Civ. Code §3344), New York (Civ. Rights Law §50-51), Indiana, Tennessee, and others. Some states recognize post-mortem rights (e.g., California: 70 years after death; Indiana: 100 years). Right of publicity applies most clearly to **commercial use** — using a person's likeness in advertising or to sell a product. Key intersection with AI: AI-generated deepfakes that depict real people in marketing are a growing enforcement area. **[EVOLVING AREA]** — multiple states are passing AI-specific right of publicity laws.
- **UK:** No standalone right of publicity. Instead, protection through: (1) **passing off** (must show misrepresentation that the person endorses the product + goodwill + damage); (2) breach of confidence; (3) UK GDPR data protection (image = personal data).
- **EU:** Varies by member state. Some countries (e.g., France, Germany) have strong personality/image rights. GDPR also applies (image of identifiable person = personal data requiring legal basis). Denmark passed a law in 2025 extending protection to face, voice, and body images against AI misuse.
- **India:** Personality rights have been recognized by Indian courts (e.g., *Titan Industries v. Registrar of Trade Marks*; *Shah Rana Mujibur Rehman v. Tata*; recent cases involving celebrity personality rights in AI context). Right of privacy under Constitution Article 21 and common law.

**Critical for AI system:**
1. Do NOT generate AI images that depict real, identifiable people (celebrities, public figures, or private individuals) in marketing content.
2. Do NOT generate "endorsements" by real people.
3. If using AI-generated human models, ensure they are not designed to resemble specific real people.
4. The system should use AI-generated human figures only when they are clearly synthetic and not designed to mimic any real person.
5. **[EVOLVING AREA]**: AI-specific right of publicity legislation is being actively developed in multiple jurisdictions.

**✅ COMPLIANT:** Using an AI-generated model that does not resemble any specific real person, with the seller's own product.
**❌ NON-COMPLIANT:** "As seen on [Celebrity X]!" with an AI-generated image designed to look like that celebrity.

**Tier: [HARD LEGAL REQUIREMENT]**

---

## 6.4 Counterfeit-Adjacent Risk

**Rule:** Generated marketing content must not imply that a product is from, authorized by, or endorsed by a brand it isn't. This is related to trademark (6.2) but extends to broader misleading implications — visual similarity, trade dress imitation, and marketing language that creates false association.

**Jurisdictions:** All.

**Key laws & bodies:**
- **US:** Lanham Act (trademark infringement, false designation of origin, dilution). Section 32 and 43(a). Also relevant: Stop Counterfeiting in Manufactured Goods Act 2006.
- **EU:** EU Trade Mark Regulation 2017/1001. EU IPR Enforcement Directive 2004/48/EC.
- **UK:** Trade Marks Act 1994.
- **India:** Trade Marks Act 1999.

**Platform policies:** All major marketplaces (Amazon, eBay, Etsy, TikTok Shop) have strict anti-counterfeiting policies. Amazon's Brand Registry and Counterfeit Crimes Unit actively pursue sellers of counterfeit goods. Etsy prohibits items that infringe intellectual property. eBay's VeRO (Verified Rights Owner) program. Shopify has IP complaint processes.

**Critical for AI system:** The system must NOT generate:
1. Product descriptions that name or reference luxury/designer brands when the product is not from that brand.
2. Images that incorporate brand logos or trade dress resembling established brands.
3. "Dupe," "knockoff," or "inspired by [Brand]" language that implies the product is a copy of a branded product.
4. Claims that a product is "genuine," "authentic," or "officially licensed" without verification.

**✅ COMPLIANT:** "A minimalist leather tote with gold hardware — handcrafted in our studio." (No brand references.)
**❌ NON-COMPLIANT:** "Gucci-inspired leather tote — get the luxury look for less!" (Implies association with Gucci — trademark infringement/dilution risk.)

**Tier: [HARD LEGAL REQUIREMENT] + [PLATFORM POLICY]**

---

# SECTION 7: AI-Generated Content Disclosure Requirements

---

## 7.1 Disclosure That Content Was AI-Generated or AI-Assisted

**Rule:** Emerging laws and platform policies increasingly require disclosure when content is AI-generated or AI-assisted, particularly for images, video, and text used in marketing or commercial contexts.

**Jurisdictions:** EU (most prescriptive), US (state-by-state), platform-level (global).

**Key laws & bodies:**
- **EU — AI Act (Regulation 2024/1689), Article 50 (Transparency Obligations):** Effective **2 August 2026**. Requires: (1) Providers of AI systems that generate synthetic content (images, audio, video, text) must ensure outputs are **machine-readable and detectable as artificially generated or manipulated**; (2) Deployers of AI systems that generate text published with the purpose of informing, educating, or influencing the public on matters of public interest must **disclose that the content is AI-generated**; (3) Deployers of emotion recognition systems or biometric categorization systems must inform persons exposed to those systems. The European Commission published guidelines on transparency obligations in 2026. **[EVOLVING AREA]** — enforcement details still being finalized.
- **US — state laws (no federal mandate yet):**
  - **California AB 730** (2019) — requires disclosure for AI-generated/deceptive audio or video in political advertising within 60 days of an election.
  - **California AB 2655 / AB 2839 / AB 2839** (2024) — regulate AI deepfakes in election-related content. California also enacted laws requiring disclosure for AI-generated content in other contexts.
  - **Texas SB 751** (2023) — regulates AI-generated deepfake videos in political advertising. Criminal penalties.
  - **Washington, Minnesota, and 30+ other states** (as of 2026) have passed some form of AI-generated media regulation, primarily focused on political advertising and deepfakes.
  - **[EVOLVING AREA]**: No comprehensive federal AI disclosure law exists yet. FTC has issued guidance on AI-related claims and has used Section 5 authority for AI-deception cases. The FTC's position is that failing to disclose material AI-generated elements (especially synthetic reviews, AI-generated testimonials) can be a deceptive practice.
- **Platform-level requirements:**
  - **Meta (Facebook/Instagram):** Requires labeling of AI-generated or AI-altered photorealistic content. Uses "AI info" labels.
  - **TikTok:** Requires creators to disclose AI-generated content. Auto-labels AI-generated content.
  - **Google/YouTube:** Requires disclosure of AI-generated or altered content in political ads. YouTube requires creators to label altered or synthetic content that's realistic.
  - **Pinterest:** Requires disclosure of AI-generated or modified images.

**Critical for AI system:**
1. **For EU users (mandatory from August 2026):** The system must ensure AI-generated outputs are marked as machine-generated and detectable. This may require embedding metadata or visible labels.
2. **For political/election content (multiple US states):** AI-generated political content must carry disclosures — though this is less relevant to a product marketing platform, it's relevant if the system generates any content touching on public affairs.
3. **For platform compliance:** Generated content published on Meta, TikTok, Google, etc., must comply with each platform's AI labeling requirements.
4. **Best practice:** Even where not legally required, disclosing AI-assisted content (e.g., "Product imagery enhanced with AI") is recommended to avoid deception claims and build consumer trust.
5. **[EVOLVING AREA]**: The legal landscape for AI content disclosure is rapidly evolving. The system should be designed to easily add/adjust disclosure mechanisms as laws develop.

**✅ COMPLIANT (EU post-Aug 2026):** AI-generated product image with visible or metadata disclosure that it was AI-generated.
**✅ COMPLIANT (best practice globally):** "Product photos are AI-enhanced for presentation purposes. Actual product may vary slightly."
**❌ NON-COMPLIANT:** AI-generated photorealistic product image presented as an actual photograph without any disclosure, especially where the AI image implies features the physical product doesn't have.

**Tier: [HARD LEGAL REQUIREMENT] (EU AI Act from Aug 2026) + [PLATFORM POLICY] + [EVOLVING AREA]**

---

## 7.2 AI-Assisted vs. Fully Synthetic / Misleading Content Distinction

**Rule:** There is a critical legal and ethical distinction between (a) AI-assisted content — where a real product exists and AI enhances the presentation (e.g., background removal, color correction, lifestyle context generation around the real product) — and (b) fully synthetic/misleading content — where AI generates imagery or claims implying features, materials, or contexts the product doesn't actually have. These two categories carry very different risk levels and must be treated differently in the system's logic.

**Jurisdictions:** All (principle applies universally under truth-in-advertising law).

**Key legal basis:**
- **US — FTC Act Section 5:** Content that misrepresents the product is deceptive regardless of whether AI was used. The issue is the misrepresentation, not the AI per se. FTC's guidance on AI and advertising emphasizes that AI tools don't change the fundamental requirement that ads must be truthful and not misleading.
- **EU — UCPD:** Misleading commercial practices include presenting a product in a way that does not match its actual characteristics. AI-enhanced presentation that materially changes the product's appearance could be a misleading action under Article 6.
- **UK — CPRs 2008:** Same principles.
- **India — Consumer Protection Act 2019 / ASCI Code:** Misleading advertising is prohibited regardless of the technology used.

**Two-tier framework for the system:**

### Tier A: AI-Assisted (Lower Risk)
- Using AI to enhance a real product photo (background replacement, lighting improvement, color correction)
- Generating lifestyle context (e.g., placing a real product in a generated room setting)
- Writing marketing copy based on real product specifications
- **Risk level:** Low, IF the enhancement doesn't materially misrepresent the product
- **Requirement:** Disclosure of AI enhancement is recommended but not always legally required. Product must still match its real description.

### Tier B: Fully Synthetic / Misleading (Higher Risk)
- Generating product images that show features the real product doesn't have (e.g., generating a "diamond" that's actually cubic zirconia)
- Generating imagery implying the product is made of materials it isn't (e.g., showing "solid gold" when it's gold-plated)
- Generating images showing the product performing functions it can't perform
- Generating lifestyle imagery implying the product comes with accessories it doesn't include
- **Risk level:** HIGH — this is deceptive advertising
- **Requirement:** Must NOT be done. The system must have guardrails to prevent generating imagery or claims that misrepresent the product's actual attributes.

**Critical for AI system:** The system must classify each generated content piece as Tier A or Tier B:
1. If Tier A (AI-assisted enhancement of real product): allow with optional disclosure.
2. If Tier B (fully synthetic/misleading representation of the product): BLOCK.
3. The system must cross-reference generated imagery/claims against the seller's actual product data (materials, size, function, included items) to verify no misrepresentation.

**✅ COMPLIANT (Tier A):** AI enhances a real photo of a handmade ceramic vase by placing it in a generated kitchen setting with improved lighting. The vase itself is unchanged.
**❌ NON-COMPLIANT (Tier B):** AI generates an image of a ceramic vase that appears to have a hand-painted floral pattern, but the actual product is plain white — the AI invented a feature the product doesn't have.

**Tier: [HARD LEGAL REQUIREMENT] (Tier B) + [BEST-PRACTICE CAUTION] (Tier A disclosure)**

---

# SECTION 8: Deceptive Product Representation

---

## 8.1 Misrepresentation of Product Attributes

**Rule:** Marketing imagery and claims must not misrepresent a product's actual size, materials, color, function, or included contents. Even "enhancement" that materially changes how the product appears to consumers is prohibited if it creates a false impression of the product's attributes.

**Jurisdictions:** US, EU, UK, India.

**Key laws & bodies:**
- **US:** FTC Act Section 5 (15 USC §45). FTC's Enforcement Policy Statement on Deceptively Formatted Advertisements. FTC has brought numerous cases for product misrepresentation (e.g., claiming products were "made in USA" when they weren't; claiming a product was "100% cotton" when it was a blend).
- **EU:** UCPD 2005/29/EC — Article 6 (misleading actions): a practice is misleading if it contains false information or in any way deceives or is likely to deceive the average consumer, even if the information is factually correct, in relation to: (a) the existence or nature of the product; (b) the main characteristics of the product (including availability, composition, accessories, fitness for purpose, usage, quantity, specification, geographical or commercial origin, results to be expected from use). **Annex I (blacklist, banned per se):** No. 2 — claiming that a product is able to facilitate winning money or games of chance; No. 6 — claiming a product is different from another similar product when it isn't.
- **UK:** CPRs 2008 — Regulations 5 (misleading actions) and 6 (misleading omissions). Banned practices in Schedule 1.
- **India:** Consumer Protection Act 2019 (Section 2(47) — unfair trade practice includes "making any statement or representation which is false or misleading"). ASCI Code Chapter 1.

**Critical for AI system:** The system must verify that generated content matches the seller's actual product data:
1. Size: if the AI generates a product image, the product must appear at the correct relative scale.
2. Materials: if the product is gold-plated, the AI must not label or depict it as "solid gold."
3. Color: AI-generated images must show the product in its actual available colors, not different colors.
4. Function: AI-generated content must not claim functions the product doesn't have.
5. Included contents: AI-generated imagery must not show accessories or items not included with the product.

**✅ COMPLIANT:** "Solid sterling silver ring with a 6mm turquoise stone. Available in sizes 5-9." (Matches actual product.)
**❌ NON-COMPLIANT:** AI generates an image showing the ring with matching earrings and a necklace (not included), in a color variant that doesn't exist, at a size that appears larger than actual.

**Tier: [HARD LEGAL REQUIREMENT]**

---

## 8.2 "Before/After" Imagery Regulations

**Rule:** "Before/after" imagery is particularly heavily regulated in beauty, health, and wellness categories. Exaggerated or manipulated before/after images that overstate a product's effects are prohibited. Even truthful before/after images may require disclosure of the conditions of the comparison.

**Jurisdictions:** US, UK, EU, India.

**Key laws & bodies:**
- **US:** FTC Act Section 5 — FTC has brought numerous cases against companies for deceptive before/after advertising. The FTC requires that before/after images accurately represent the product's typical results and must not be manipulated. FTC cases include actions against diet pill companies, skin care companies, and hair growth products for deceptive before/after photos.
- **UK — ASA:** The ASA has upheld many complaints about before/after photos that exaggerate product efficacy. ASA advice on before/after photos states that such images must not exaggerate the effect the product can achieve. The ASA has banned multiple ads for beauty and diet products with misleading before/after imagery. In 2011, the ASA banned two L'Oréal cosmetics ads featuring excessively airbrushed images of celebrities (Julia Roberts and Christy Turlington), following complaints from a Member of Parliament.
- **EU:** UCPD — misleading if before/after implies results that are not typical or achievable.
- **India:** ASCI Code — before/after claims require substantiation and must represent typical results.

**Critical for AI system:**
1. Do NOT generate before/after imagery that exaggerates or fabricates the product's effects.
2. If the seller provides genuine before/after photos, the system should require disclosure that results may vary and that the images represent the experience of specific individuals, not guaranteed results.
3. Do NOT use AI to digitally enhance the "after" image to make the difference appear more dramatic than reality.
4. For beauty/wellness/health products, apply maximum scrutiny to any before/after content.

**✅ COMPLIANT:** Genuine before/after photos (provided by seller, unaltered) with clear disclosure: "Individual results may vary. These photos show [name]'s actual results over [time period]."
**❌ NON-COMPLIANT:** AI-generated "before" image showing severe acne and "after" image showing flawless skin, implying the product cured acne (disease claim + fabricated/exaggerated before/after + misrepresentation).

**Tier: [HARD LEGAL REQUIREMENT]**

---

## 8.3 Digital Alteration of Product Appearance

**Rule:** Digitally altering a product's appearance in marketing imagery is acceptable within limits — minor enhancements (lighting, background, minor color correction to match reality) are standard practice. However, alterations that materially change the product's appearance in a way that misleads consumers about its characteristics are prohibited.

**Jurisdictions:** US, UK, EU, India.

**Key laws & bodies:**
- **US:** FTC Act Section 5. FTC has addressed "photographic enhancement" — noting that while some enhancement is acceptable, material alteration of a product's appearance (e.g., making a food product look larger, enhancing a gemstone's clarity beyond reality) can be deceptive.
- **UK — ASA:** The ASA has restricted the use of social media filters and digital manipulation in beauty product advertising. In 2021, the ASA ruled that beauty filters on ads promoting beauty products were misleading if they exaggerated the product's effects. The ASA has specific guidance on digital manipulation in advertising.
- **EU:** UCPD — digital alteration that misleads about product characteristics is a misleading action (Article 6). Several EU member states (e.g., France — Law of 30 September 2020) require labeling of digitally altered body images in advertising. France requires a "photographie retouchée" label on commercial images where a model's body shape/size has been digitally altered.
- **India:** ASCI Code prohibits misleading visual representations.

**Critical for AI system:**
1. The system must distinguish between acceptable enhancement (lighting, background, color accuracy) and misleading alteration (changing product size, material appearance, gemstone quality, fabric texture).
2. For beauty/wellness products, do NOT use AI to alter a human model's appearance (skin, body shape) in a way that implies the product achieves those results.
3. **France-specific:** If marketing content includes images where a model's body has been digitally altered and the target market includes France, a "retouched photograph" label may be required.
4. For food products, do NOT generate images that make portions appear larger or ingredients appear more abundant than reality.

**✅ COMPLIANT:** AI removes the background from a real product photo and adds a neutral studio background, with accurate color representation.
**❌ NON-COMPLIANT:** AI digitally enlarges a gemstone's apparent size and enhances its clarity/color beyond what the actual stone looks like.

**Tier: [HARD LEGAL REQUIREMENT]**

---

# SECTION 9: Data Privacy

---

## 9.1 Baseline Data Protection Obligations

**Rule:** If the platform collects, processes, or uses seller or customer data to personalize recommendations or generate content, it must comply with applicable data protection laws. Key obligations include: lawful basis for processing (consent or other legal basis), data minimization, purpose limitation, transparency, and — in some jurisdictions — restrictions on automated decision-making.

**Jurisdictions:** EU, UK, US (California and other states), India.

**Key laws & bodies:**

- **EU — GDPR (Regulation 2016/679):**
  - **Article 6:** Lawful basis for processing (consent, contract, legitimate interests, etc.).
  - **Article 7:** Conditions for consent — must be freely given, specific, informed, and unambiguous. Pre-ticked boxes are NOT valid consent (per CJEU *Planet49* case).
  - **Article 22:** Right not to be subject to decisions based solely on automated processing, including profiling, which produce legal or similarly significant effects. Data subjects have the right to human intervention, to express their point of view, and to contest the decision.
  - **Article 5:** Data minimization, purpose limitation, accuracy, storage limitation, integrity and confidentiality.
  - **Enforcement:** GDPR fines can reach **€20 million or 4% of global annual turnover**, whichever is higher. Major fines: Meta €1.2 billion (2023, data transfer violation), Amazon €746 million (2021, advertising consent violation). In 2023-2024, GDPR fines totaled approximately €5.88 billion. Meta, Amazon, TikTok, LinkedIn, and Clearview AI among top offenders.

- **UK — UK GDPR / Data Protection Act 2018:** Substantially mirrors EU GDPR. ICO (Information Commissioner's Office) enforces. Post-Brexit, UK has retained GDPR principles with some modifications via the Data (Use and Access) Act 2025 (which modifies certain provisions but retains core principles).

- **US — CCPA/CPRA (California Consumer Privacy Act / California Privacy Rights Act):**
  - Applies to businesses that: (a) have gross annual revenue > $25 million; (b) buy/sell/share personal info of 100,000+ consumers/households; or (c) derive 50%+ of revenue from selling/sharing personal info.
  - California Privacy Protection Agency (CPPA) released draft regulations on **Automated Decision-Making Technologies (ADMT)** — requiring businesses to provide notice and opt-out rights for ADMT, including profiling for marketing personalization. **[EVOLVING AREA]** — draft regulations, not yet final.
  - Other state privacy laws: Virginia (VCDPA), Colorado (CPA), Connecticut (CTDPA), Utah (UCPA), Texas (TDPSA), and 15+ other states have comprehensive privacy laws as of 2026.
  - Sectoral laws: HIPAA (health data), GLBA (financial data), COPPA (children's data under 13).

- **India — Digital Personal Data Protection Act 2023 (DPDP Act):**
  - Requires consent for processing personal data (with some exceptions for "legitimate uses").
  - Data principal rights: access, correction, erasure, grievance redressal.
  - **Section 11:** Notice requirement — must give clear, plain-language notice of personal data processing.
  - **Sections 16-17:** Restrictions on processing children's data (under 18) and persons with disabilities — requires verifiable parental consent.
  - **[EVOLVING AREA]**: Rules and regulations under the DPDP Act are still being finalized. The Act provides for penalties up to ₹250 crore (~$30 million) for certain violations.
  - Automated decision-making provisions in DPDP Act are less prescriptive than GDPR Article 22 but include the right to nominate an individual to exercise rights in case of death/incapacity.

**Critical for AI system:**
1. **Consent:** If the platform uses seller or buyer data to personalize content or recommendations, it must obtain clear, informed consent. No pre-ticked boxes (invalid under GDPR per *Planet49*). Consent must be granular (separate consents for different purposes).
2. **Data minimization:** Only collect data necessary for the stated purpose. Do not collect "extra" data "just in case."
3. **Purpose limitation:** Data collected for one purpose (e.g., order fulfillment) must not be repurposed for another (e.g., marketing personalization) without a new legal basis.
4. **Automated decision-making:** If the platform's AI generates recommendations or content that produces "legal or similarly significant effects" for individuals (GDPR Article 22), users must have the right to human review. Even where the threshold is not met, transparency about automated processing is required.
5. **Children's data:** Under COPPA (US), DPDP Act (India, under 18), and GDPR (under 16, member-state configurable), processing children's data requires parental consent. The system must age-gate and apply heightened protections for minors' data.
6. **[EVOLVING AREA]**: CCPA/CPRA automated decision-making technology regulations are still being finalized. EU AI Act provisions interact with GDPR. The intersection of AI, privacy, and marketing personalization is a rapidly evolving regulatory area.

**✅ COMPLIANT:** Platform obtains explicit, informed consent from sellers to analyze their product data and generate personalized recommendations, with clear privacy notice and opt-out mechanism.
**❌ NON-COMPLIANT:** Platform silently analyzes seller's customer purchase history to generate targeted marketing content without consent or notice, and uses a pre-ticked consent box for marketing emails.

**Tier: [HARD LEGAL REQUIREMENT]**

---

# SECTION 10: Platform-Specific Policy Considerations

---

## 10.1 Marketplace-Level Restrictions Beyond Government Law

**Rule:** Major online marketplaces impose content and product restrictions that go BEYOND what government law requires. Content that is legal may still be prohibited by a marketplace, and marketplace restrictions can change without notice. The system must account for marketplace-specific rules when generating content.

**Jurisdictions:** Global (platform policies apply to all sellers on each platform).

**Key marketplace restrictions:**

### Amazon
- **Prohibited products:** Alcohol, tobacco, drugs/drug paraphernalia, weapons, explosives, certain food items, lock-picking devices, certain medical devices, prescription drugs, pet medication, certain supplements, counterfeit products, recalled products.
- **Content rules:** No nudity or sexually suggestive imagery in product images. No health claims that violate FDA regulations. No comparative claims naming competitors. No "cure," "treat," "prevent" language for non-drug products. Strict review and rating policies — Amazon blocked 275+ million suspicious reviews in 2024. Product images must have white background (for main image).
- **Enforcement:** Listing removal, account suspension, account health point deductions, funds withholding, potential legal action via Amazon's Counterfeit Crimes Unit.

### eBay
- **Prohibited/restricted products:** Weapons, drugs, drug paraphernalia, tobacco, alcohol (restricted, not banned), certain adult items (restricted to "Adults Only" category with strict listing rules — no nudity in images).
- **Content rules:** VeRO (Verified Rights Owner) program for IP enforcement. No counterfeit goods. Adult items must be in Adults Only category.

### Etsy
- **Prohibited products:** Alcohol, tobacco, drugs, weapons, hazardous materials. Pornographic material prohibited (sexual wellness items allowed if not pornographic). Counterfeit items prohibited.
- **Content rules:** Handmade/vintage/craft supplies only (commercial/resold items not allowed). No resold mass-produced items. IP infringement strictly enforced. Intimate apparel allowed if presented non-sexually.

### Shopify (Shop channel)
- **Prohibited on Shop app:** Age-restricted products (alcohol, tobacco, gambling), cannabis, drugs/drug-related products, medications, weapons, adult products. Note: Shopify's e-commerce platform itself is more permissive, but the Shop channel (their consumer-facing marketplace) has strict restrictions.
- **Managed Markets prohibited items:** Artwork that violates copyright/trademark, digital artwork valued > $2,000, and other restricted categories.

### TikTok Shop
- **Prohibited products:** Adult products and services (including sexual wellness devices, intimate apparel with explicit imagery), alcohol, tobacco/vaping, drugs, weapons, pharmaceuticals, certain supplements, live animals, counterfeit products.
- **Content rules:** Content moderation strict. TikTok requires disclosure of AI-generated content. Account suspensions and penalties for policy violations.
- **Enforcement:** Listing removal, account health point deductions, revoked selling access, refunds, potential account ban.

### Meta Commerce (Facebook/Instagram Shopping)
- **Prohibited products:** Per WhatsApp Commerce Policy and Meta Commerce policies — no buying/selling of stolen items, prescription drugs, marijuana, weapons, ammunition, tobacco, adult products, animals, certain medical/healthcare products.
- **Content rules:** AI-generated content must be labeled. No misleading claims. Health and safety product restrictions.

### General patterns across marketplaces:
1. **Most marketplaces prohibit:** weapons, drugs, drug paraphernalia, counterfeit goods, prescription pharmaceuticals, and most age-restricted products.
2. **Adult content:** Highly restricted across all major marketplaces. Etsy and eBay are most permissive (with restrictions). Amazon, TikTok Shop, Shopify Shop, and Meta Commerce are most restrictive.
3. **Health claims:** Most marketplaces enforce FDA-level restrictions on health claims even in jurisdictions where FDA doesn't apply, because they operate globally and default to the strictest standard.
4. **AI-generated content labeling:** TikTok, Meta, and Google now require AI content disclosure. This trend is expanding.
5. **Reviews/testimonials:** Most marketplaces prohibit sellers from generating fake reviews or offering incentives for positive reviews. Amazon's policies are particularly strict.

**Critical for AI system:**
1. The system should maintain a per-marketplace rule set that applies additional restrictions on top of the legal compliance rules in this document.
2. When generating content for a specific marketplace, apply that marketplace's specific rules (e.g., Amazon's white background requirement, Etsy's handmade-only requirement).
3. Default to the most restrictive marketplace's standards when the target marketplace is unknown.
4. Marketplace policies change frequently — the system should have a process for updating marketplace-specific rules regularly.

**✅ COMPLIANT:** Generating a product listing for Amazon with a white-background main image, no health claims, no competitor comparisons, and no prohibited products.
**❌ NON-COMPLIANT:** Generating a TikTok Shop listing for an intimate wellness product with sexually suggestive imagery — violates TikTok Shop's prohibited products policy.

**Tier: [PLATFORM POLICY]**

---

# SECTION 11: Jurisdictional Variance

---

## 11.1 Meaningful Differences Between Major Markets

**Rule:** Laws governing advertising, marketing, product safety, and content differ significantly between major e-commerce markets. Because sellers and buyers may be in different countries, the platform faces conflicting obligations. The system must identify the applicable jurisdiction(s) for each content generation task and apply the correct rules.

**Jurisdictions:** US, UK, EU, India, and others.

**Key jurisdictional differences (summary table):**

| Area | US | UK | EU | India |
|---|---|---|---|---|
| **Truth-in-advertising** | FTC Act Section 5 | CPRs 2008, ASA/CAP | UCPD 2005/29/EC | Consumer Protection Act 2019, ASCI |
| **Substantiation** | FTC substantiation doctrine | CPRs / CAP Code | UCPD Article 6(1)(b) | ASCI Code |
| **Reference pricing** | FTC guidance, state laws | CMA guidance (28-day rule) | Omnibus Directive (30-day lowest price rule) | ASCI / CCPA |
| **Fake scarcity** | FTC Act Section 5 | CPRs Schedule 1 | UCPD Annex I No. 17 (banned per se) | ASCI / Consumer Protection Act |
| **Endorsements/AI testimonials** | FTC Endorsement Guides (16 CFR 255), FTC Fake Reviews Rule (2024) | CAP Code, CPRs | UCPD Annex I No. 11/13 | ASCI Influencer Guidelines |
| **Dark patterns** | FTC Section 5, FTC Fees Rule (2025) | CMA, DMCC Act 2024 | DSA Article 25, UCPD | Consumer Protection Act |
| **Obscenity** | Miller test (community standards) | OPA 1959 | Varies by member state | IPC 292/293, IT Act 67 |
| **Age verification** | State-by-state, COPPA | Online Safety Act 2023 | DSA Article 28 | IT Rules 2021 |
| **Health claims** | FDA (FD&C Act, DSHEA), FTC | MHRA, ASA/CAP | Reg. 1924/2006, Reg. 1223/2009 | FSSR, DCA, ASCI |
| **Structure/function claims** | 21 CFR 101.93 (disclaimer required) | MHRA guidance | EFSA pre-authorization | FSSR pre-approval |
| **Children's products** | CPSIA, ASTM F963 | Toy Safety Regs 2011 | Toy Safety Directive 2009/48/EC | BIS ISI marking |
| **Advertising to children** | COPPA, FTC guidelines | CAP Code Section 5, HFSS restrictions | AVMSD Article 7b | ASCI Chapter 4, Infant Milk Substitutes Act |
| **Alcohol advertising** | TTB, state laws | CAP Code Section 18 | AVMSD, national bans | ASCI, state prohibition laws |
| **Tobacco advertising** | FDA, heavy restrictions | TAPA 2002 | TPD 2014/40/EU | COTPA 2003 (total ban) |
| **Prescription drug ads** | Allowed with FDA requirements | BANNED to public | BANNED to public | BANNED (Drugs & Magic Remedies Act) |
| **Copyright (AI content)** | 17 USC, USCO AI report (2025) | CDPA 1988 | Copyright Directive 2019/790 | Copyright Act 1957 |
| **Trademark** | Lanham Act | TMA 1994 | EUTMR 2017/1001 | TMA 1999 |
| **Right of publicity** | State laws (vary widely) | Passing off, UK GDPR | Varies, GDPR | Constitutional + common law |
| **AI content disclosure** | State laws (30+ states) | [EVOLVING] | AI Act Article 50 (effective Aug 2026) | [EVOLVING] |
| **Privacy / data protection** | CCPA/CPRA, state laws | UK GDPR / DPA 2018 | GDPR 2016/679 | DPDP Act 2023 |
| **Automated decision-making** | CCPA ADMT rules [EVOLVING] | UK GDPR Art. 22 | GDPR Art. 22 | DPDP Act (less prescriptive) |
| **Blasphemy / religious sensitivity** | First Amendment (protected) | Racial & Religious Hatred Act 2006 | Varies (some states have laws) | IPC 295A (criminal) |
| **Discrimination in ads** | Civil Rights Act, FTC Act | Equality Act 2010 | Race Equality Directive 2000/43/EC | Constitution Art. 15, IPC 153A |

**Critical conflicts the system must navigate:**
1. **Prescription drug advertising:** Legal in US (with restrictions), BANNED in EU/UK/India. → System must NOT generate prescription drug marketing for EU/UK/India sellers or buyers.
2. **Tobacco advertising:** Heavily restricted in US, total ban in India (COTPA), near-total ban in EU/UK. → System should not generate tobacco marketing content at all.
3. **Reference pricing:** EU requires specific 30-day lowest price rule that doesn't apply in US. → When targeting EU buyers, apply the 30-day rule.
4. **Structure/function claims:** US requires FDA disclaimer; EU requires pre-authorized claims only. → Apply both requirements (US disclaimer + EU authorized claims list).
5. **AI content disclosure:** EU AI Act Article 50 effective August 2026 requires disclosure; US has state-by-state requirements. → Apply EU disclosure standards as the default (most restrictive).
6. **Blasphemy / religious sensitivity:** US First Amendment allows most religious commentary, but India IPC 295A criminalizes religious offense. → Apply India's standard (most restrictive) for content touching on religion, especially for global audiences.
7. **Obscenity:** US Miller test uses community standards (varies by locality); India IPC 292 is more restrictive. → Apply India's standard (most restrictive) for sexual content.
8. **Privacy/automated decisions:** EU GDPR Article 22 gives the strongest rights against automated decision-making. India DPDP Act is less prescriptive. US is fragmented. → Apply GDPR standard (most restrictive) for automated decision-making features.

**Tier: [HARD LEGAL REQUIREMENT]**

---

## 11.2 "Most Restrictive Applicable Jurisdiction" as Safer Default

**Rule:** For an automated system operating globally, where the applicable jurisdiction is unclear or where content may reach multiple jurisdictions, defaulting to the most restrictive jurisdiction's rules is the safer approach. This reduces the risk of non-compliance across the full range of possible destinations.

**Rationale:**
1. An automated system cannot always determine which jurisdiction's rules apply (seller location, buyer location, and platform server location may all differ).
2. Applying the most restrictive standard ensures compliance with all applicable jurisdictions simultaneously.
3. The cost of over-compliance (slightly more conservative content) is far lower than the cost of under-compliance (fines, lawsuits, account bans, criminal liability).

**Recommended "most restrictive" defaults for the system:**

| Issue | Most Restrictive Standard | Source |
|---|---|---|
| **Obsecenity / sexual content** | India IPC 292 + conservative US community standards | Most restrictive obscenity law |
| **Reference pricing** | EU Omnibus Directive 30-day rule | Most prescriptive pricing rule |
| **Fake scarcity** | EU UCPD Annex I (banned per se) | Strictest treatment |
| **Endorsements / testimonials** | US FTC Fake Reviews Rule (2024) + EU UCPD | Both — comprehensive ban on fake/AI testimonials |
| **Dark patterns** | EU DSA Article 25 + UCPD Annex I | Most prescriptive |
| **Health claims** | EU Reg. 1924/2006 (pre-authorization) + US FDA disclaimer | Both — most restrictive health claim regime |
| **Prescription drug ads** | BANNED (EU/UK/India standard) | Most restrictive = total ban |
| **Tobacco advertising** | BANNED (India COTPA standard) | Most restrictive = total ban |
| **AI content disclosure** | EU AI Act Article 50 | Most prescriptive (effective Aug 2026) |
| **Privacy / automated decisions** | EU GDPR | Most prescriptive data protection |
| **Religious sensitivity** | India IPC 295A | Most restrictive (criminal liability) |
| **Children's advertising** | UK CAP Code Section 5 + India ASCI Chapter 4 | Most restrictive combined |
| **Right of publicity** | US state laws (strong publicity rights states) + EU GDPR | Most restrictive combined |
| **Age verification** | UK Online Safety Act 2023 | Most prescriptive age-assurance |

**Tier: [BEST-PRACTICE CAUTION] — but note that applying the most restrictive standard is effectively mandatory for an automated system that cannot reliably determine jurisdiction.**

---

# APPENDIX A: Quick-Reference Guardrail Checklist for Engineering

---

This checklist distills the document into actionable rules for the content-generation system. Each rule should be implementable as a filter, flag, or block in the system's logic.

## A. Absolute Blocks (NEVER generate)

| # | Rule | Source Section |
|---|---|---|
| B1 | NEVER generate fake/AI-created reviews, testimonials, or endorsements | 1.5a |
| B2 | NEVER generate "cures/treats/prevents [disease]" claims for non-drug products | 4.1 |
| B3 | NEVER generate consumer-facing marketing for prescription drugs | 5.1e |
| B4 | NEVER generate tobacco/vaping marketing content (default ban — most restrictive) | 5.1b |
| B5 | NEVER generate marketing content for infant milk substitutes or feeding bottles (India) | 4.3, 5.3 |
| B6 | NEVER generate content that disparages/stereotypes protected groups | 3.1 |
| B7 | NEVER use real brand names/logos without verified authorization | 6.2 |
| B8 | NEVER generate images resembling real, identifiable people without consent | 6.3 |
| B9 | NEVER generate content implying a product is from/endorsed by a brand it isn't | 6.4 |
| B10 | NEVER generate AI images that show product features the real product doesn't have | 7.2, 8.1 |
| B11 | NEVER generate before/after imagery that fabricates or exaggerates results | 8.2 |
| B12 | NEVER generate content with religious deities/symbols in potentially offensive ways (esp. India IPC 295A) | 3.2 |
| B13 | NEVER generate fake scarcity/urgency claims without verified inventory/deadline data | 1.4 |
| B14 | NEVER generate reference/discount pricing without verified prior price history | 1.3 |
| B15 | NEVER generate drug paraphernalia marketing content | 5.1d |
| B16 | NEVER generate weapons marketing content | 5.1c |

## B. Conditional Blocks (BLOCK unless specific conditions met)

| # | Rule | Condition | Source Section |
|---|---|---|---|
| C1 | Health/supplement structure/function claims | Block unless FDA disclaimer is appended (US) OR claim is on EU authorized list (EU) | 4.2 |
| C2 | Safety claims for children's products | Block unless seller provides verified test results/certification | 5.2 |
| C3 | Age-restricted product content | Block unless age-gating is applied | 2.3 |
| C4 | Sexual wellness product imagery | Block unless non-explicit, non-suggestive, mannequin/flat-lay style | 2.1, 2.2 |
| C5 | Superlative claims ("best," "#1," "clinically proven") | Block unless substantiation evidence is provided | 1.2 |
| C6 | Comparative advertising naming competitors | Block unless truthful, non-misleading, no confusion (EU: must meet Misleading & Comparative Advertising Directive conditions) | 6.2 |
| C7 | AI content published in EU | Must include AI-generated disclosure/marking (effective Aug 2026) | 7.1 |
| C8 | Automated personalization using personal data | Block unless valid consent obtained + GDPR/CCPA/DPDP compliance verified | 9.1 |
| C9 | Financial product marketing | Block — flag for mandatory human review (FCA/CFPB/SEBI requirements) | 5.1f |
| C10 | Alcohol marketing | Block unless jurisdiction permits AND content complies with TTB/CAP/AVMSD/ASCI rules | 5.1a |

## C. Mandatory Flags (Flag for human review or seller verification)

| # | Rule | Source Section |
|---|---|---|
| F1 | Flag all health/wellness/beauty claims for seller substantiation verification | 1.2, 4.1, 4.2 |
| F2 | Flag all pricing/discount suggestions for seller verification of price history | 1.3 |
| F3 | Flag all content for age-restricted product categories for age-gating implementation | 2.3 |
| F4 | Flag content touching on religious/cultural themes for cultural sensitivity review | 3.2 |
| F5 | Flag content for vulnerable-group products (children, elderly, pregnant) for heightened scrutiny | 4.3 |
| F6 | Flag all AI-generated imagery for similarity check against known copyrighted characters/brands | 6.1, 6.2 |
| F7 | Flag content targeting specific marketplaces for marketplace-specific rule application | 10.1 |
| F8 | Flag content where jurisdiction is unclear for "most restrictive" rule application | 11.1, 11.2 |
| F9 | Flag content that uses AI-generated human models for likeness-check against real people | 6.3 |
| F10 | Flag any digital alteration of product appearance for materiality assessment | 8.3 |

## D. Mandatory Append/Include

| # | Rule | Source Section |
|---|---|---|
| D1 | Append FDA disclaimer to all US structure/function claims: "This statement has not been evaluated by the FDA. This product is not intended to diagnose, treat, cure, or prevent any disease." | 4.2 |
| D2 | Include AI-generated content disclosure (EU, from August 2026; best practice globally) | 7.1 |
| D3 | Include age-gating markers for all age-restricted product content | 2.3 |
| D4 | Include "results may vary" disclosure for any before/after content (if genuine) | 8.2 |
| D5 | Include "retouched photograph" label for digitally altered body images (France, and as best practice) | 8.3 |

---

# APPENDIX B: Key Regulatory Bodies Quick Reference

| Body | Jurisdiction | Scope |
|---|---|---|
| **FTC** (Federal Trade Commission) | US | Truth-in-advertising, endorsements, dark patterns, fake reviews, consumer protection |
| **FDA** (Food and Drug Administration) | US | Health claims, supplements, cosmetics, drugs, tobacco, children's products safety |
| **CPSC** (Consumer Product Safety Commission) | US | Children's product safety (CPSIA), general product safety |
| **TTB** (Alcohol and Tobacco Tax and Trade Bureau) | US | Alcohol advertising and labeling |
| **CFPB** (Consumer Financial Protection Bureau) | US | Financial product marketing |
| **US Copyright Office** | US | AI-generated content copyrightability |
| **CMA** (Competition and Markets Authority) | UK | Consumer protection, pricing, dark patterns |
| **ASA** (Advertising Standards Authority) | UK | Advertising standards (CAP/BCAP codes) |
| **MHRA** (Medicines and Healthcare products Regulatory Agency) | UK | Health claims, medicines, medical devices |
| **Ofcom** | UK | Online safety, age verification (Online Safety Act 2023) |
| **ICO** (Information Commissioner's Office) | UK | Data protection (UK GDPR) |
| **European Commission** | EU | AI Act enforcement, consumer protection |
| **EFSA** (European Food Safety Authority) | EU | Health claim authorization |
| **National consumer protection authorities** | EU (each member state) | UCPD enforcement, Omnibus Directive enforcement |
| **CCPA** (Central Consumer Protection Authority) | India | Consumer protection, misleading advertising |
| **ASCI** (Advertising Standards Council of India) | India | Advertising self-regulation |
| **FSSAI** (Food Safety and Standards Authority of India) | India | Food health claims |
| **SEBI** (Securities and Exchange Board of India) | India | Financial product advertising |
| **CPPA** (California Privacy Protection Agency) | US (California) | CCPA/CPRA enforcement, ADMT regulations |

---

# APPENDIX C: Evolving / Unsettled Areas

These areas are flagged as [EVOLVING AREA] or [UNSETTLED] throughout the document. The system should be designed to accommodate changes in these areas:

1. **AI content disclosure law (Section 7.1):** EU AI Act Article 50 effective August 2026, but enforcement guidance is still being finalized. US has no federal law; 30+ state laws in various stages. Platform requirements (Meta, TikTok, Google) are evolving. → Design the system's disclosure mechanism to be modular and easily updatable.

2. **AI copyright and infringement (Section 6.1):** Multiple cases pending (*Getty v. Stability AI*, *Andersen v. Stability AI*). US Copyright Office AI reports issued (2025) but legal framework for AI training data and output infringement is unsettled. → Err on the side of caution; implement similarity checks against known copyrighted works.

3. **AI right of publicity (Section 6.3):** Multiple states developing AI-specific right of publicity legislation. Denmark passed face/voice/body image protection law (2025). → Monitor developments; implement likeness detection safeguards.

4. **CCPA/CPRA automated decision-making technology regulations (Section 9.1):** CPPA released draft ADMT regulations but they are not yet final. → Monitor CPPA rulemaking; design the system's personalization/profiling features to accommodate future opt-out and notice requirements.

5. **EU AI Act enforcement details (Section 7.1):** The AI Act entered into force in 2024, with transparency obligations under Article 50 effective August 2026. The European Commission published guidelines in 2026, but specific enforcement practices and penalties are still being established. → Monitor EU AI Act enforcement developments.

6. **DPDP Act implementation (India, Section 9.1):** The DPDP Act 2023 was passed, but detailed rules and regulations are still being finalized. → Monitor Indian government rulemaking under the DPDP Act.

7. **AI-generated testimonials and reviews (Section 1.5a):** The FTC's 2024 Fake Reviews Rule is new, and enforcement actions under it are just beginning. How strictly the FTC will apply the rule to AI-generated content specifically is still developing. → Treat as a hard block regardless (most conservative approach).

8. **Deepfake regulation (Sections 6.3, 7.1):** Rapid proliferation of state-level deepfake laws, primarily focused on political content but increasingly extending to commercial uses. → Monitor state and national deepfake legislation.

9. **UK DMCC Act 2024 enforcement (Section 1.3, 1.6):** The Digital Markets, Consumers and Competition Act 2024 gives the CMA new direct enforcement powers, but enforcement practice is still developing. → Monitor CMA enforcement actions under the DMCC Act.

10. **Platform AI labeling requirements (Section 7.1):** Meta, TikTok, Google, and other platforms are continuously updating their AI content labeling requirements. → Maintain a regularly updated registry of platform-specific AI labeling requirements.

---

*This document is a compliance reference for engineering guardrails, not legal advice. Laws and regulations change frequently. The platform should conduct regular legal reviews of this document and update guardrails accordingly. Where this document and specific legal advice from qualified counsel in the relevant jurisdiction differ, the specific legal advice should prevail.*

---

**Document End — Total boundaries enumerated: 44+ distinct legal points across 11 sections, with 16 absolute blocks, 10 conditional blocks, 10 mandatory flags, and 5 mandatory append/include rules in the engineering checklist.**
