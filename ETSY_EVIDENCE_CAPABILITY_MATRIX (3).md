# ETSY_EVIDENCE_CAPABILITY_MATRIX.md
### FINAL — re-verified line-by-line against source, 2026-08-03

## Status and purpose

This is the mandatory build artifact defined in **Section 59** ("Etsy evidence
capability audit — mandatory build task") of
`MerchSage_Production_Engineering_Requirements.md`, using the registry
template specified in **Section 5.4** of the same document:

`| Evidence | Available? | Endpoint/source | OAuth scope | Historical depth | Freshness | Notes/fallback |`

## Sourcing — corrected

**Primary source: `Etsy_s_capability.md`.** An earlier version of this matrix
described that document as sourced "exclusively from Etsy's own official
documentation." **That was inaccurate and is corrected here.** `Etsy_s_capability.md`
is *mostly* sourced from Etsy's official developer docs (Authentication,
Rate Limits, Webhooks, Listings/Fulfillment/Shop Management tutorials,
Definitions, URL Syntax, API Terms of Use, Enterprise Tier Terms) — but it
also draws, for a specific, named set of items, on:

- Etsy's own Open API GitHub discussions (staff-visible, but a community
  discussion board, not formal documentation) — used for the review-schema
  example, the `review_id` absence, and the views-history feature request.
- Community-reported rate-limit defaults (GitHub discussions, a Make.com
  community thread) — used only for the ~10 QPS / 10,000 QPD default figure.
- One third-party schema mirror (Microsoft Learn's Etsy connector reference)
  — used to cross-check the listing field enumeration.

`Etsy_s_capability.md` itself is disciplined about this: every item sourced
this way is explicitly tagged `UNVERIFIED` or `MEDIUM confidence` in its own
text and collected in its own Uncertainty Register (its Section H). This
matrix preserves that same tagging faithfully rather than presenting
everything as uniformly official. Where a row below is tagged `HIGH`, it
traces to Etsy's own formal documentation. Where it's tagged `MEDIUM` or
`UNVERIFIED`, that is carried over honestly, not upgraded.

**Secondary source: `SESSION_STATE.md`** — used only for the project's own
access-tier decision (Personal App as primary path) and the acknowledgment
that `findAllListingsActive`'s response shape had not yet been checked
against a live authenticated call as of that document's writing. Where
`SESSION_STATE.md` and `Etsy_s_capability.md` differ in confidence level on
the same fact (see note below the access-tier table), both are shown rather
than silently picking one.

---

## Access-tier facts

| Fact | Confidence | Source |
|---|---|---|
| **Personal App** is the correct primary path for MerchSage's own-shop + competitor-survey use case. It is the *entry gate* to Commercial Access, not a separate track — an approved Personal App is a prerequisite for requesting Commercial Access. | HIGH | Etsy_s_capability.md §1.1–1.2 (Etsy Developer Portal, GitHub Discussion #1567); confirmed independently by SESSION_STATE.md |
| **Commercial Access adds no new data fields or endpoints.** It changes only: (a) permission to onboard third-party sellers via OAuth at scale, (b) higher/negotiated rate limits, (c) separate-approval eligibility for the `buyer_email` field. It does not unlock views history, competitor sales, or any analytics — those don't exist in the API at any tier. | HIGH | Etsy_s_capability.md §23 ("Direct answer to the brief's question F") |
| **Enterprise Tier** (>3,000,000 calls/day) changes only rate ceiling, priority support, and Etsy Apps Page placement — still no new data. Requires a trailing-12-month average of >1M calls/day to qualify; paid, fee is the greater of 15% of "Etsy App Revenue" or $2 per 10,000 calls/month. Far outside MerchSage's realistic v1 scope. | HIGH | Etsy_s_capability.md §1.2–1.3, §23; Enterprise Tier Terms |
| **Seller App OAuth** (own-shop only, built regardless of Personal App status) covers reading and writing only the connecting seller's own shop data. It cannot fetch competitor data under any framing — this isn't a policy choice, it's how the credential is scoped. | HIGH | Etsy_s_capability.md §1.1–1.2, §2.3; SESSION_STATE.md |
| `findAllListingsActive` is the sanctioned, API-key-only (no seller OAuth needed) endpoint for marketplace-wide competitor discovery by keyword/taxonomy/price/location. | HIGH | Etsy_s_capability.md §14 |
| **Confidence-level note:** `Etsy_s_capability.md` documents `findAllListingsActive`'s returned fields (title, description, tags, price, taxonomy, materials, style, timestamps, views, favorers, and more) as HIGH confidence, sourced from Etsy's official Reference and Listings tutorial. `SESSION_STATE.md`, written earlier and independently, described the same endpoint more cautiously — confirming only "title, description, tags as base fields" and flagging the full response shape as "not confirmed against a live authenticated response." **Both are accurate for what they claim:** `Etsy_s_capability.md`'s confidence is documentation-based (which fields the schema defines); `SESSION_STATE.md`'s caution is about live-response confirmation (whether a real authenticated call returns exactly what the docs promise). Neither has been superseded by an actual live test yet — that test is still the open item. | — | Both documents, reconciled |
| Scraping etsy.com in any form — public or private pages, regardless of how the target URL was identified — is prohibited by the API Terms of Use. Quoted directly: *"Use or promote the use of automated systems or browser extensions to access, analyze, or scrape the Etsy Site, the Etsy API or any Etsy data."* | HIGH | Etsy_s_capability.md §13, quoting API Terms of Use directly; independently confirmed in SESSION_STATE.md |
| **The API's AI/ML/analytics restriction.** The API Terms of Use prohibit using the Etsy API to *"collect, scan, or otherwise request Etsy content for purposes of analytics, machine learning, training artificial intelligence models, licensing, or content removal, unless expressly authorized in writing by Etsy."* This is a purpose restriction, not a caching restriction, and it applies even to the seller's own data once pulled via API under their OAuth grant — the seller's consent as data subject does not override Etsy's terms as data provider. Sending API-sourced content to any AI provider (Gemini included) is treated in the source document as a "third-party transfer for a prohibited purpose" absent written Etsy authorization. | HIGH on the letter of the terms; MEDIUM on how Etsy's Developer Relations would actually enforce it for an AI-native product | Etsy_s_capability.md §24, quoting API Terms of Use directly |

---

## The capability matrix

Confidence tags are carried directly from `Etsy_s_capability.md`, not
reassigned. `UNVERIFIED` rows are listed in that document's own Uncertainty
Register (its Section H) and require a live empirical test against a real
Personal-Access key, or a direct written question to `developer@etsy.com`,
before any agent contract depends on them.

### Listing-level fields

| Evidence | Available? | Endpoint/source | OAuth scope | Historical depth | Freshness | Confidence |
|---|---|---|---|---|---|---|
| Title, description, state, url | ✅ own + competitor | `getListing`, `getListingsByShop`, `findAllListingsActive` | API key only | Current only | ≤6h | HIGH |
| Tags (max 13) | ✅ own + competitor | Listing endpoints | API key only | Current only | ≤6h | HIGH |
| Taxonomy (`taxonomy_id`) | ✅ own + competitor | Listing + taxonomy endpoints | API key only | Current only | ≤6h | HIGH |
| Price (Money object) | ✅ own + competitor | Listing endpoints | API key only | Current only — no historical price change | ≤6h | HIGH |
| Quantity | ✅ own + competitor | Listing endpoints | API key only | Current only | ≤6h | HIGH |
| Materials, style, who_made, when_made, is_supply | ✅ own + competitor | Listing endpoints | API key only | Current only | ≤6h | HIGH |
| Personalization fields | ✅ own + competitor | Listing endpoints | API key only | Current only | ≤6h | HIGH |
| Processing time (min/max days) | ✅ own + competitor | Listing endpoints | API key only | Current only | ≤6h | HIGH |
| Timestamps (created/updated/ending/original creation/last modified) | ✅ own + competitor | Listing endpoints | API key only | — | ≤6h | HIGH — `updated_timestamp` is bumped by non-copy events (inventory decrement, section reassignment) and is not a reliable "copy was edited" signal |
| **Listing lifetime views** (`views`) | ✅ own + competitor | `getListing.views` | API key only | Lifetime cumulative counter only — no time series, no daily/weekly breakdown | ≤6h | HIGH — semantic trap: cumulative since publish, favors older listings unless normalized by `created_timestamp` |
| **Listing views time series** (daily/weekly) | ❌ | — | — | Not exposed at any tier | — | HIGH — open Etsy feature request, unresolved (GitHub Discussion #1386) |
| Listing favorites (`num_favorers`) | ✅ own + competitor | Listing endpoints | API key only | Cumulative counter only, no time series | ≤6h | HIGH |
| **Listing revision/history — own shop** | ⚠ Partial | `created_timestamp`/`updated_timestamp` only | API key / `listings_r` | Timestamp of last change only — no version/diff history | ≤6h | HIGH — confirms *that* a listing changed and *when*, never *what* changed |
| **Listing revision/history — competitor** | ❌ | — | — | Not exposed at any tier | — | HIGH — confirmed zero ("Any competitor historical anything: ❌ Zero") |
| Inactive/draft/expired listings | ✅ own only | — | `listings_r` | — | — | HIGH — competitor's non-active listings are never exposed |
| Variations/inventory (SKU-level, `getListingInventory`) | ✅ own / ⚠ competitor | `getListingInventory` | API key (public) / `listings_w` for own write | — | ≤6h | Own: HIGH. Competitor-scope: **UNVERIFIED** — docs don't explicitly gate on ownership, but Etsy does not commit to this in writing; community reports vary |
| Listing images/videos (URLs) | ✅ own + competitor | `getListingImage(s)`, `getListingVideo(s)` | API key only | — | ≤6h | HIGH for access; downloading/analyzing with AI is legally gated (see AI/ML clause above), not access-gated |
| Shipping cost/destinations on listing | ✅ own + competitor (per-listing derived only) | Listing detail | API key only | — | ≤24h | HIGH for structure; MEDIUM for how much of a *competitor's* full shipping-profile object is exposed beyond the per-listing derived cost |

### Shop-level fields

| Evidence | Available? | Endpoint/source | OAuth scope | Historical depth | Freshness | Confidence |
|---|---|---|---|---|---|---|
| Shop age (`created_timestamp`), currency, country | ✅ own + competitor | `getShop` | API key only | — | ≤24h | HIGH |
| Shop lifetime sales count (`transaction_sold_count`) | ✅ own + competitor | `getShop` | API key only | Cumulative count only — not revenue, not historical | ≤24h | HIGH — do not treat as revenue; it's a count of completed transactions, unitless |
| Shop review count / average (`review_count`, `review_average`) | ✅ own + competitor | `getShop` | API key only | Aggregate only | ≤24h | HIGH |
| Shop favorers (`num_favorers`) | ✅ own + competitor | `getShop` | API key only | Cumulative only | ≤24h | HIGH |
| Shop policies, sale_message, vacation status | ✅ own + competitor | `getShop` | API key only | — | ≤24h | HIGH |
| Shop "about" / meet-the-artist text | ⚠ | — | — | — | — | **UNVERIFIED** — not enumerated as a first-class field in the official reference pulled; the public shop page has one, API return is unconfirmed |
| **Shop-level views / visits / traffic (any period)** | ❌ | — | — | Not exposed at any tier | — | HIGH — the single most consequential gap for the "diagnose why traffic dropped" use case |
| Own not-yet-public shop description/sections | ✅ own only | — | `shops_r` | — | — | HIGH |

### Reviews

| Evidence | Available? | Endpoint/source | OAuth scope | Historical depth | Freshness | Confidence |
|---|---|---|---|---|---|---|
| Review text, rating (1–5), date | ✅ own + competitor | `getReviewsByListing`, `getReviewsByShop` | API key only | Up to 12,000-offset pagination ceiling | — | HIGH |
| Review image (single `image_url_fullxfull` if attached) | ✅ own + competitor | Same | API key only | Same ceiling | — | HIGH |
| Review video | ❌ / unconfirmed | — | — | — | — | **UNVERIFIED** — schema example does not enumerate a video field; Etsy's site displays buyer-attached video, but the documented payload only shows `image_url_fullxfull` |
| Stable `review_id` | ❌ | — | — | — | — | HIGH — confirmed absent from the schema by Etsy's own GitHub discussion. Must use a composite key `(shop_id, listing_id, transaction_id, buyer_user_id, created_timestamp)` where present |
| Buyer identity (`buyer_user_id`) | ⚠ Partial | — | — | — | — | HIGH — present on shop-scoped responses, not always on listing-scoped ones; no name/handle/avatar in either case |
| Review "helpfulness"/ranking signal | ❌ | — | — | — | — | HIGH — not exposed at any tier; MerchSage cannot mirror Etsy's own "most helpful" ordering and must recompute its own |
| Shop-level trust/reputation (aggregate rating only) | ✅ for the numeric aggregate; ❌ for a native "complaint theme" field | `getShop` | API key only | Aggregate only | ≤24h | HIGH — theme/sentiment extraction from review text is technically derivable but is subject to the AI/ML clause above |

### Sales, orders, financials

| Evidence | Available? | Endpoint/source | OAuth scope | Historical depth | Freshness | Confidence |
|---|---|---|---|---|---|---|
| Own receipts/orders | ✅ own only | `getShopReceipts` | `transactions_r` | As far back as the shop's records go, filterable by `min_created`/`max_created`, subject to the 12,000-offset ceiling | — | HIGH |
| Own line-item transactions | ✅ own only | `getShopReceiptTransactions` | `transactions_r` | Same | — | HIGH |
| Own refunds/cancellations | ✅ own only | Receipt `canceled` status + refund fields | `transactions_r` | Same | — | HIGH |
| Own revenue over time, AOV, product-level revenue | ✅ derived | Aggregated from receipts/transactions | `transactions_r` | Same | — | HIGH — derived by MerchSage, not a direct field |
| Own Etsy fees | ⚠ Partial | `billing_r` endpoints | `billing_r` | — | — | **UNVERIFIED as fully complete** for per-transaction fee detail |
| Own profit / COGS | ❌ | — | — | — | — | HIGH — not derivable from Etsy at all; Etsy has no visibility into seller COGS. Must come from seller-uploaded cost data |
| **Competitor sales/orders/receipts** | ❌ | — | — | Not exposed at any tier, under Personal, Commercial, or Enterprise access | — | HIGH |
| Competitor revenue | ❌ (only `transaction_sold_count`, a cumulative transaction *count*, not $) | `getShop` | API key only | — | — | HIGH |

### Search, discovery, taxonomy

| Evidence | Available? | Endpoint/source | OAuth scope | Historical depth | Freshness | Confidence |
|---|---|---|---|---|---|---|
| Marketplace-wide active-listing search (keyword/category/price/location) | ✅ | `findAllListingsActive` | API key only | Current only | ≤6h | HIGH — cannot rank by sales/revenue/behavioral signal; 12,000-offset ceiling |
| Shop search by name | ✅ | Shop search endpoint | API key only | — | — | HIGH — by name string only, not by category-of-shop |
| Taxonomy tree + category properties | ✅ | `getSellerTaxonomyNodes`, `getPropertiesByTaxonomyId` | API key only | — | — | HIGH — one of the API's strongest points for MerchSage's Classification agent |
| Etsy search-ranking/position for any listing | ❌ | — | — | Not exposed at any tier | — | HIGH — no search-position API exists |

### Rate limits, pagination, freshness

| Evidence | Available? | Endpoint/source | OAuth scope | Historical depth | Freshness | Confidence |
|---|---|---|---|---|---|---|
| Rate-limit headers (`x-limit-per-second`, `x-limit-per-day`, `x-remaining-this-second`, `x-remaining-today`) | ✅ | Response headers on every call | — | — | — | HIGH on structure |
| Actual default QPS/QPD values | ⚠ | — | — | — | — | **MEDIUM/UNVERIFIED** — not disclosed as fixed public values on Etsy's Rate Limits page; community-reported default of ~10 QPS / 10,000 QPD is not officially confirmed. Actual per-key limits are checkable live via response headers |
| Pagination | ✅ default 25 / max 100 per call | — | — | Hard ceiling: offset max 12,000 | — | HIGH |
| Listing content freshness/caching rule | ✅ | — | — | — | Must not display data >6 hours older than what's on Etsy | HIGH — quoted directly from the API Terms of Use, a contractual obligation, not just a technical suggestion |
| Non-listing content freshness/caching rule | ✅ | — | — | — | Must not display data >24 hours older than what's on Etsy | HIGH — same source |
| QPD reset behavior | ✅ | — | — | — | — | HIGH — rolling 24-hour sliding window, not a fixed midnight reset |
| Rate-limit increase path | ✅ | — | — | — | — | HIGH — email `developer@etsy.com` with app description and estimated QPD/QPS; still free below the Enterprise (>3M/day) threshold |

### OAuth scopes

| Evidence | Available? | Endpoint/source | OAuth scope | Historical depth | Freshness | Confidence |
|---|---|---|---|---|---|---|
| Minimum recommended scopes for the diagnose-why-not-selling flow | ✅ | — | `listings_r`, `shops_r`, `transactions_r` | — | — | HIGH — direct recommendation in source document §2.5 |
| Optional scopes (only if MerchSage acts, not just recommends) | ✅ | — | `listings_w`, `shops_w`, `listings_d` | — | — | HIGH |
| Scopes to avoid requesting without specific justification | — | — | `email_r`, `address_r`, `profile_r`, `billing_r`, `cart_r`, `favorites_r/w` | — | — | HIGH — minimal-necessity principle stated directly in the source document and independently required by Requirements §26 |
| `buyer_email` on `transactions_r` | ⚠ | Receipts | `transactions_r` + separate Etsy approval | — | — | HIGH — Commercial-Access apps must request separate approval for this specific field even with `transactions_r` granted |
| Order webhooks | ✅ | `order.paid`, `order.canceled`, `order.shipped`, `order.delivered` — exhaustive, no others exist | `transactions_r` (in practice) | — | Real-time push | HIGH — no listing/review/favorite/inventory/pricing webhook events exist at any tier; everything else must be polled |

### Personal App vs. Commercial Access vs. Enterprise Tier

| Evidence | Available? | Endpoint/source | OAuth scope | Historical depth | Freshness | Confidence |
|---|---|---|---|---|---|---|
| New data fields/endpoints from Commercial Access | ❌ None | — | — | — | — | HIGH — confirmed identical field set to Personal Access |
| New data fields/endpoints from Enterprise Tier | ❌ None | — | — | — | — | HIGH — Enterprise raises only rate ceiling, adds priority support and Apps Page placement |
| Third-party seller onboarding at scale | ❌ Personal (scale-limited) / ✅ Commercial | — | — | — | — | HIGH — this is the only thing Commercial Access actually unlocks for MerchSage |

---

## Confirmed structurally impossible (do not design around)

Directly from the source document's own "Impossible / unsupported" list:

- Retrospective "views/traffic dropped" diagnosis via API — no view time series exists at any tier, own or competitor.
- Retrospective or prospective search-visibility/ranking diagnosis — no search-term or ranking data is exposed.
- Any competitor behavioral or historical data (sales, orders, historical views, historical prices, promo history, listing-edit history).
- Real-time detection of listing edits, new reviews, or new favorites — webhooks cover exactly 4 order events; everything else is poll-based only.
- Programmatic shipping-label purchase.
- Enumerating a competitor's active coupons or shop-wide promotions.
- A stable per-review identifier.
- AI/LLM analysis of any API-sourced content, without written Etsy authorization (legal gate, not a technical gap — see the AI/ML clause above).

## Confirmed derivable, not direct (must be built by MerchSage)

- Own revenue over time, AOV, product-level revenue — derived from receipts/transactions.
- Competitor price positioning vs. category — derived from `findAllListingsActive` + own listing price.
- Listing-age normalization for `views`/`num_favorers` — derived from `created_timestamp`, needed because both counters are lifetime-cumulative and otherwise favor older listings.
- Prospective (going-forward only) view/favorite velocity — MerchSage must poll and diff the cumulative counters itself on its own cadence; this **cannot** reconstruct the past.
- Review sentiment/theme clustering — derivable technically, but subject to the AI/ML clause above.

## Confirmed must come from the seller directly, not the API

| Missing from API | Seller-intake replacement |
|---|---|
| Historical views/visits/impressions/CTR | Etsy Stats CSV export upload (available in Etsy's own Seller Stats UI back to Nov 2017, just not via API) |
| Historical traffic sources & search terms that produced visits | Same CSV export |
| Historical favorites velocity | Not in Etsy Stats either — screenshot or seller estimate only |
| Conversion rate | Only computable once the seller supplies historical visits; the API supplies only the transaction numerator, never a visits denominator |
| COGS / profit margins | Seller-uploaded cost sheet — Etsy has no visibility into this at all |
| Off-Etsy marketing spend | Seller-reported form field |
| Target audience / brand positioning / competitor list of interest | Onboarding questionnaire |
| Competitor sales estimates | **Not available anywhere, from Etsy or the seller** — the UI must state "not available," not estimate |

---

## Open items requiring escalation before further build

1. **The AI/ML clause is an Etsy API-contract compliance issue — acquisition-layer, not content/output-layer.** It maps directly onto a control the engineering docs already require: Amendment §E.1 ("Provider data-use review") already mandates reviewing what data is sent to any AI provider before doing so — this finding is exactly what that review is supposed to catch. As written, sending API-sourced content (including the seller's own listings/reviews pulled via their OAuth grant) to Gemini or any AI provider for analysis is presently out of terms without Etsy's written authorization. This needs a decision before the Researcher/Review-Intelligence/Creative-Strategy agents are built against API-sourced content: (a) request written authorization from `developer@etsy.com`, describing the intended AI use, data flow, and retention, or (b) restrict AI analysis to seller-uploaded (non-API) content only, per the seller-intake replacement map above. Note: option (b) resolves the Etsy-contract problem only — it does not by itself satisfy separate data-privacy consent obligations (GDPR/CCPA/DPDP) that apply to AI-personalized recommendations regardless of data source; that is a distinct, non-Etsy compliance track, intentionally out of scope for this matrix.
2. **Thirteen items remain in the source document's own Uncertainty Register** and require either a live empirical test against a real Personal-Access key, or a direct written question to `developer@etsy.com` — not further reading. The highest-priority ones for MerchSage's launch scope: exact default rate limits (confirm via live `x-limit-*` response headers on a real key), competitor-scope of `getListingInventory`, whether Etsy will grant written AI/ML authorization at all (submit the request early — no stated turnaround time), and whether `findAllListingsActive`'s full documented field set actually returns as described on a live authenticated call.
3. This matrix should be reconciled into the registry template specified in Requirements §5.4 as the project builds, and every `HIGH (documentation-based)` row should be re-tagged `CONFIRMED (live-tested)` once verified against a real Personal-Access key — this matrix is accurate to the source documentation as of 2026-08-02/03, but documentation confidence is not the same as a live-response guarantee.
