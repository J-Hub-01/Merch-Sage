**Review Intelligence/API uncertainty — VALID.**  
 Solution: live-test review endpoints **immediately during Etsy integration**, before making Review Intelligence dependent on them. If unavailable/limited → seller-provided review evidence or UNKNOWN. This is exactly what the Evidence Capability Matrix is for.

**Etsy Stats ingestion — VALID and actually important.**  
 We need an **Etsy Stats ingestion/parser capability**, not necessarily another AI agent:  
 `CSV/upload → validate → normalize → structured Evidence Objects → Researcher`.  
 Mostly deterministic parsing. Add this as an implementation requirement.

**“Seller Action Required” vs AI-native requirement — NOT an architecture defect.**  
 Some problems physically cannot be executed by software—for example changing manufacturing or fulfillment operations. Keep the category. For the competition/demo, foreground cases where MerchSage **actually executes** solutions: rewritten copy, tags, generated creative, pricing recommendation/range, etc. Don't pretend AI can execute physical seller actions.

**EU AI disclosure — needs verification before calling it a blocker.**  
 Claude is making a legal applicability interpretation. Don't redesign anything from that statement. Verify what the compliance document actually establishes and, if necessary, current law/applicability before launch. Until then classify it as **Compliance Review Required**, not “MerchSage definitely has an Article 50 obligation.”

**Deadline — CORRECT.**  
 Today is **August 4, 2026**. Stop carrying old “days remaining” numbers. Use the actual deadline timestamp and dynamically calculate remaining time.

**Devpost/demo — VALID and urgent.**  
 Add a submission workstream **now**, not after development. Don't demonstrate 10 agents individually. A 3-minute demo should show:  
 `seller problem → MerchSage investigates → evidence-backed diagnosis → MerchSage executes fixes → verified final result`.  
 The architecture is backstage; **the outcome is the demo**.

**Revenue/refunds — ALREADY SOLVED conceptually.**  
 Store transaction-level raw facts:  
 `gross paid | refunds | chargebacks | net | customer | timestamp | payment ID`.

 Then report **gross \+ refunds \+ net transparently**, while using whatever official XPRIZE definition is ultimately confirmed for the scored revenue figure. No need for another revenue architecture.