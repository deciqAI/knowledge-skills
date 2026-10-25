---
name: outcome-based-ai-pricing
description: "Activate when: user says 'how should we price our AI product?', 'per seat or per usage / per outcome?', 'how do we design pay-for-results pricing?', 'inference costs are eating our margin', 'price per resolution', or AI is shrinking the number of people a customer needs, so seat pricing has started to cannibalize itself.
  Do NOT activate when: the product's value has no measurable link to usage or outcomes (a flat platform subscription fits better); there are no paying customers and value is unproven (run pricing interviews first); the question is general price level, anchoring, or tiering rather than the AI charge unit (use pricing-strategy). More: deciqai.com/s/outcome-based-ai-pricing"
---

# Outcome-Based AI Pricing

## Overview

When AI replaces human work, the customer needs fewer seats — so seat pricing moves in the opposite direction from the value delivered. The more the product works, the less it earns. The charge unit has to move to **a measure of value the customer recognizes**: a usage unit close to the work, or the outcome itself.

Core mechanism: **pick a charge unit that is measurable, attributable, and grows with value → add a floor and a cap to share risk → check gross margin against inference cost at the tail.** The charge unit is a product decision, not a billing detail — the argument of Ramanujam & Tacke's *Monetizing Innovation* (2016): design the product around the price, not the other way round. Paying for measured results also has long precedent outside software: in U.S. federal Energy Savings Performance Contracts, the agency repays the contractor out of the energy-cost savings the project delivers.

Compose with [pricing-strategy](../pricing-strategy/SKILL.md) (the value-based pricing frame) · [unit-economics-cac-ltv-payback](../unit-economics-cac-ltv-payback/SKILL.md) (margin and payback) · [principal-agent](../principal-agent/SKILL.md) (attribution disputes) · [goodharts-law](../goodharts-law/SKILL.md) (the metered unit gets gamed).

## When to Use

- An AI agent or automation product replaces human workload
- Customers ask "why do we pay the same when we need fewer people?"
- Per-customer inference cost swings widely and a flat subscription leaves margin unstable

**When NOT to use:** the outcome cannot be measured or attributed · the customer's budget only accepts a fixed fee (offer fixed + usage add-on first) · value is unproven.

## Coaching Novices (Adaptive Front Door)

**Engine mode:** user has a concrete product and cost data → run The Process directly.
**Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What-it-is:** "Charge for the result the customer actually cares about — or the closest usage unit — and use a floor and a cap so both sides can live with the risk."
2. **Check fit:** "When your product finishes a piece of work, can the customer count it?"
3. **Elicit the real case:** "Name one specific job the product does for a customer, and what the customer spends on it today in money or people."
> **[WAIT — do not advance until user responds]**
4. **Run The Process:** "List three candidate charge units and score each on measurable, attributable, grows with value, and budgetable."
> **[WAIT — do not advance until user responds]**
5. **Name the insight:** "The charge unit is a product decision, not a finance detail."

## The Process

**Output:** Pricing plan card

1. **Choose the value metric.** Candidates: seat · usage (calls, tasks, documents) · outcome (resolved tickets, qualified leads, hours saved). Score each 1–5 on four tests: measurable, attributable, grows with value, budgetable by the customer. *Gate: no candidate scores ≥3 on all four → use fixed + usage hybrid → stop.*
2. **Define success and attribution.** Write down what counts as one success, whose data decides it, the dispute window, and exclusions (results the customer caused). *Gate: both sides cannot reconcile against the same data source → fall back to usage pricing.*
3. **Anchor the price.** Use the customer's current replacement cost (staff or outsourcing per unit) as the upper anchor and take a share of it. Never price as a markup on inference cost.
4. **Check gross margin.** Per unit: inference + human review + infrastructure, computed for P50 and P90 tasks. *Gate: P90 unit margin is negative → cap the unit, tier it, or change the unit.*
5. **Share the risk.** Monthly minimum commitment (floor) · spend cap (ceiling) · tiered overage price · guaranteed minimum during pilots.
6. **Plan the migration (if coming from seats).** New customers first → existing customers opt in → switch at renewal. Provide a bill simulator and transition price protection. *Gate: the simulation shows most existing customers' bills jumping → adjust; do not force it.*
7. **Stop-rule:** attribution disputes stay high → return to usage pricing and keep the outcome as a reported metric only.

**Output template:**
`charge unit | success definition + deciding data source | unit price | floor / cap | P50 / P90 unit margin | replacement-cost anchor | migration pace | review date`

*→ Method in Action: [Intercom Fin's $0.99 per resolution (2023–2026)](examples/intercom-fin-per-resolution-2023-2026.md)*

## Charge-Unit Packs

Typical patterns (outcome unit / quality counter-metric / attribution risk / fallback unit):
- **Customer support agents:** resolved conversation / reopen rate, CSAT / silent abandon billed as success / per conversation.
- **Sales agents:** qualified lead or booked meeting / downstream conversion / lead quality disputes / per contact worked.
- **Document and back-office work:** document processed correctly / error and rework rate / customer-side input errors / per document.
- **Coding agents:** accepted change / revert or defect rate / credit shared with the developer / per task or usage credits.

## Applying It Well

1. **Outcome pricing fits clear, high-frequency outcomes the customer already counts** — support ticket resolution is the canonical case.
2. **Pilot with 3–5 customers and price from real bills,** not from a model of what bills might be.
3. **Guard the unit against gaming.** Monitor a quality counter-metric alongside it (e.g. reopen rate after a "resolution").
4. **Re-run the margin check on every model price change.** Inference cost moves with each release; the price anchored to replacement cost should not.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Just mark up the token cost" | Customers do not perceive value in tokens, and falling inference prices drag your price down with them. |
| [D] "Outcome pricing always earns more" | Attribution disputes and long-tail tasks can push margin negative. |
| [D] "Move existing customers straight to the new price" | Sudden bill changes cause churn; simulate and phase the transition. |
| [D] "No cap shows confidence" | A customer who cannot budget cannot get the purchase through procurement. |
| [D] "'No complaint' counts as success" | An assumed-success rule bills silent failures. Pair it with a reopen/deduction rule and an escalation path that is never billed. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- The success definition exists only in the sales pitch · no P90 cost data · the customer cannot audit the charge unit themselves · migration planned without a bill simulation

## Verification

- [ ] Charge-unit candidates scored on all four tests, with the scores recorded
- [ ] Success definition and deciding data source written into the contract or terms
- [ ] P90 unit margin is positive
- [ ] Floor, cap, and migration plan defined

---

*Part of **deciqAI Knowledge Skills** — 253 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/outcome-based-ai-pricing** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/outcome-based-ai-pricing.json*
