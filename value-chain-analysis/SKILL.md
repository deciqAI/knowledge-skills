---
name: value-chain-analysis
description: "Activate when: user asks 'where does our competitive advantage come from', 'why are our margins lower than competitors', 'which activities create value', 'how is the competitor doing it cheaper', 'cost structure analysis', 'make vs. buy decision', 'which activities should we outsource', or is evaluating an acquisition for synergies or designing competitive strategy.
  Do NOT activate when: the business is a platform/multisided market (use network effects analysis instead); the question is industry-level rather than firm-level (use Porter's Five Forces instead)."
---

# Value Chain Analysis

## Overview

Porter (1985) separates firm activities into **primary** (inbound logistics, operations, outbound logistics, marketing/sales, service) and **support** (firm infrastructure, HR management, technology development, procurement). Competitive advantage — cost leadership or differentiation — emerges from performing one or more activities better than rivals. Margin is the residual after all activity costs are subtracted from customer willingness to pay.

**Linkages** between activities are often where the most powerful levers hide. Limit: linear value chain framework does not fit platform/multisided market businesses.

Composes with: [`porters-five-forces`](../porters-five-forces/SKILL.md) · [`bcg-matrix`](../bcg-matrix/SKILL.md) · [`economic-moat`](../economic-moat/SKILL.md).

## When to Use

- Margins **below industry average** without a clear explanation; designing competitive strategy; evaluating M&A synergies; new market entry planning
- Someone says: "value chain," "cost structure analysis," "strategic cost analysis," "make vs. buy," "which activities create value"

**When NOT to use:** platform/multisided market (use network effects); portfolio health check (use BCG); industry-level question (use Five Forces); pre-PMF firm.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a specific firm → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **One-line:** Value chain analysis breaks your business into every activity that creates value, then asks: which is the real source of your competitive edge or cost problem?
2. **Check fit** — stable cost structure? Platform business? Pre-PMF? Flag limits before proceeding.
3. **Elicit the real case** — "Margin problem or identifying what makes you different from competitors?"
> **[WAIT — do not advance until user responds]**
4. **Run The Process** — map primaries → supports → allocate cost → compare competitor → linkages → recommend.
> **[WAIT — do not advance until user responds]**
5. **Name the payoff** — "Value chain analysis revealed [specific activity] is the real source of [problem/advantage]."
> **[WAIT — do not advance until user responds]**

## The Process

Produce a **Value Chain Audit** — mapped activities with cost allocation, differentiation sources, competitive comparison, and strategic recommendations.

**Step 1: Map All Activities.** List every primary and support activity using Porter's nine-module structure. Be specific — not "sales" but "enterprise direct sales in North America." Stop rule: if two people assign the same cost item to different activities, break down further.

**Step 2: Allocate Cost.** Estimate cost % of total for each activity. Identify top 3 cost consumers, below-benchmark (potential advantages), above-benchmark (value leakage). Regress-test: cannot estimate to ±50% → fix data or definition.

**Step 3: Identify Differentiation Sources.** Does each activity produce output customers pay a premium for? Evidence required: price realization, win rates, or retention. List 2–3 genuine sources with evidence.

**Step 4: Compare to Key Competitor.** Estimate per-activity relative cost (lower / comparable / higher). Identify structural sources of competitor advantages. Be explicit about estimated vs. observed.

**Step 5: Map Linkages.** Does investment in A reduce cost in B? Does excellence in A enable price premium in C? Most powerful interventions often optimize a linkage, not a single activity.

**Step 6: Formulate Activity-Level Strategy.**

| Activity type | Strategic disposition |
|---|---|
| High-value, differentiation source, hard to replicate | Invest, internalize, protect |
| High-cost, commoditized, no differentiation | Outsource, automate, minimize |
| Strategic bottleneck | Fix or acquire |
| High-cost but essential linkage to differentiated activity | Accept cost as investment |

### Output: Value Chain Audit

```
# Value Chain Audit: <company> | Date: <date> | vs. <competitor>
| Activity | Cost % rev | Differentiation source? | vs. Competitor |
|---|---|---|---|
| [each of 9 activities] | <X>% | Yes/No | Lower/Comp/Higher |
Differentiation sources (top 2–3): <activity + evidence>
Value-leaking activities: <activity + cost gap>
Key linkages: <A × B + optimization opportunity>
Strategic recommendations: invest / outsource / fix / immediate priority
```

*→ Method in Action: [Apple's Value Chain and the iPhone Margin Structure (2007–2023)](examples/apple-iphone-margin-structure-2007-2023.md)*

## Activity Packs

**SaaS:** Operations = engineering/product dev; Outbound Logistics = deployment infra (often overlooked cost driver); differentiation trap: firms claim R&D as source when actual differentiation is customer success (Service).

**Manufacturing:** Procurement is highest-ROI for cost leadership — supplier contracts, geographic sourcing, commodity hedging. Inbound Logistics × Operations linkage: just-in-time reduces working capital but increases operational risk — optimize at system level, not per-activity.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] Listing activities without cost allocation | A map without cost percentages is an org chart. Every activity needs at least an order-of-magnitude cost estimate. |
| [D] Treating all activities as equally important | 2–3 activities account for 80% of differentiation. Distributing attention evenly across all nine modules wastes focus. |
| [D] Claiming differentiation without customer evidence | "Best-in-class operations" is an assertion. Win/loss data, NPS, or price realization must back the claim. |
| [D] Ignoring linkages and optimizing activities independently | Apple's chip-to-software-to-service linkage is the source of ecosystem lock-in — not any single activity. |
| [D] Applying linear template to a platform business | Uber's advantage is matching algorithm and driver density, not "inbound logistics." Force-fitting produces misleading analysis. |
| [D] Treating "make vs. buy" as purely a cost question | Outsourcing a differentiation source destroys durable advantage. Weigh cost and strategic control together. |
| [D] Confirming an already-held conclusion | If differentiation sources match current marketing claims exactly, the analysis added no information. Start from cost data. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- No cost allocation estimates · Differentiation claims without customer evidence · No competitor comparison
- Platform business analyzed using linear template without acknowledging limitations
- Recommendations call for investing in everything — no explicit outsource or exit decisions
- Linkages not analyzed · Value chain not refreshed in 2+ years despite competitive changes

## Verification

- [ ] All nine activity modules mapped with specific sub-activity names (not generic labels)
- [ ] Cost allocation estimates made for each activity (order-of-magnitude acceptable)
- [ ] Differentiation sources identified with customer evidence (not just internal assertion)
- [ ] Competitor comparison completed for at least the top 3 cost-consuming activities
- [ ] At least two linkages identified with an optimization opportunity stated
- [ ] Each activity assigned a strategic disposition (invest/outsource/fix/accept linked cost)
- [ ] Platform-type business limitation noted if applicable

---

*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/value-chain-analysis?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=value-chain-analysis** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
