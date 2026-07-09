---
name: ansoff-matrix
description: "Activate when: user says 'where should we grow next', 'should we enter a new market', 'thinking about diversifying', 'new product vs new market', 'growth strategy', 'adjacent expansion', 'Ansoff', or is spreading resources across too many directions at once.
  Do NOT activate when: the firm has one clear unsaturated market (answer is always penetration — no matrix needed); or the question is about portfolio allocation across existing BUs (use BCG Matrix instead)."
---

# Ansoff Matrix

## Overview

Every growth option a firm has falls into one of four quadrants defined by two axes: existing vs. new product, and existing vs. new market. Risk rises as unknowns multiply: selling your existing product to your existing market adds zero unknowns; diversifying (new product + new market) adds two unknowns simultaneously, compounding risk roughly fourfold. The matrix's job is **prioritization** — selecting one primary direction and committing resources there — not listing all options simultaneously.

AI has compressed execution time for Market Development and Product Development moves, but the relative risk ordering still holds.

Composes with: [`swot-analysis`](../swot-analysis/SKILL.md) (assess strengths per quadrant first); [`bcg-matrix`](../bcg-matrix/SKILL.md) (which BU needs growth, then Ansoff picks direction); [`porters-five-forces`](../porters-five-forces/SKILL.md) (validate target market attractiveness before committing).

## When to Use

Apply when:
- Leadership is debating **where to grow next** without a shared framework
- Resources are **spread across 4+ directions** with no single bet resourced enough to win
- The firm is considering **entering a new geography or demographic** with an existing product
- A product team is **developing a new product** and needs strategic context
- A startup is **past initial PMF** and planning its next phase
- An **AI-native company** is weighing deeper penetration vs. new segments vs. shipping autonomous agents vs. diversifying — under rising AI capex, fast AI adoption, and AI-native competition

**When NOT to use:** single product with clear unsaturated demand (penetration is the obvious answer); portfolio-level resource allocation across existing BUs (BCG Matrix); industry-level competitive assessment (Porter's Five Forces first); evaluating a single acquisition or partnership deal.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: Ansoff tells you how risky each growth direction is — based on whether you're introducing a new product, entering a new market, or both — so you can pick the right bet given your current resources.
2. Check fit against When to Use / When NOT to use.
3. Elicit their real case: "What's your current product and market, and what growth options are you considering?"
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time with their input.
> **[WAIT — do not advance until user responds]**
5. Close by naming the insight they uncovered: "Ansoff just showed you that [option A] carries [X] unknowns vs. [option B] carrying [Y] unknowns — the resource implication is [specific insight]."
> **[WAIT — do not advance until user responds]**

## The Process

Produce a **Growth Direction Analysis** — a completed matrix with mapped options, feasibility scores, and a prioritized growth agenda.

**Step 1: Define Current Product-Market Baseline.** State what your "existing products" are and who your "existing customers" are. If the team disagrees on what counts as the existing market, resolve that before assigning quadrants.

**Step 2: Enumerate Growth Options by Quadrant.** At least 3 specific options per quadrant. "Enter Asia" is not an option; "launch English-language SaaS in Japan targeting mid-market manufacturing firms" is.

**Step 3: Score Feasibility and Risk.** For each option score 1–5 on: market opportunity size, capability match, competitive intensity (invert), time to revenue, strategic fit. Apply quadrant risk multiplier (penetration 1×, one-axis development 2×, diversification 4×). Regress-test: "If this were the only thing we worked on this year, could we win?"

**Step 4: Select Primary Direction.** One primary quadrant; one optional secondary (≤20% of growth resources); all others explicitly deprioritized. Default sequence: penetration → development (one axis) → diversification. Skip only on evidence of saturation (>40–50% penetration) or a time-sensitive opportunity.

**Step 5: Set Entry Criteria for Next Quadrant.** Named metric + threshold before any resources may move to the next quadrant.

**Step 6: Plan 90-Day Agenda.** For primary option: measurable milestone, resource commitment, single accelerate/stop metric.

### Output: Growth Direction Analysis

```
Current baseline: existing product(s) | existing market | penetration rate %
Penetration (1×): option — score/25 | Development-Market (2×): option — score/25
Development-Product (2×): option — score/25 | Diversification (4×): option — score/25
Primary direction: <quadrant + option> | Secondary (≤20% resources): <optional>
Deprioritized: <list>
Entry criteria for next quadrant: <metric> ≥ <threshold> by <date>
90-day agenda: milestone | resource commitment | accelerate/stop metric
```

*→ Method in Action: [Amazon's Sequenced Growth (1994–2006)](examples/amazon-sequenced-growth-1994-2006.md) · [Disney's Diversification Sequence (1928–1955)](examples/disney-diversification-sequence-1928-1955.md)*
*→ 2026 lens: [An AI Startup's Growth Options (2024–2026)](examples/ai-startup-growth-options-2024-2026.md)*

## Growth Direction Packs

**SaaS / software:** Adding a major new feature for a different buyer persona is *Product Development*, not Penetration — the new buyer has different evaluation criteria and may need a different sales motion. Moving from one vertical SaaS to another with a rebuilt product is genuine Diversification even if the stack is shared.

**Consumer brands:** Distribution depth (40% → 80% ACV) is frequently the highest-ROI penetration move. Validate purchase intent before committing to new-country distribution.

*→ Primary sources: [references/sources.md](references/sources.md)*
## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] Calling a new customer subsegment in the same industry a "new market" | If product, sales motion, and pricing are nearly identical, it's Market Penetration. New market = materially different buyer behavior. |
| [D] Treating product iteration as Product Development | Adding features to better serve an existing need is Penetration. Product Development requires a distinct new job-to-be-done. |
| [D] Framing Diversification as "low-risk because it's adjacent" | Adjacency in technology ≠ adjacency in market behavior. You may know the tech; you don't know the new buyer. Risk multiplier remains ~4×. |
| [D] Using the matrix as permission to pursue all four quadrants | The matrix is a prioritization forcing function. Equal resource across all four quadrants means it was used as a menu, not a decision tool. |
| [D] Setting entry criteria without measuring current penetration | "We've done enough in penetration" is an assertion. State actual market share and growth rate data. |
| [D] Treating Market Development and Product Development as equivalent risk | Both add one unknown, but mitigation differs: new market = distribution/localization/regulatory; new product = R&D/PMF. |
| [D] Launching diversification at startup scale | Diversification requires surplus cash, management bandwidth, and a defensible core. Rarely appropriate below $10M ARR. |
| [D] Confusing "market growth rate" with "our ability to compete in it" | A fast-growing market says nothing about your competitive position within it. |
| [D] Assuming risk multipliers are precise | The 1×/2×/4× gradient is directional, not a precise calculator. |
| [D] Ignoring the sequence principle under competitive pressure | "Competitor X is already there" is not sufficient to skip current-quadrant penetration. Expanding surface area before the core is defensible increases vulnerability. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- All four quadrants in current-year plan with similar resource commitments
- "Existing market" defined so broadly that nearly any move counts as penetration
- Market Development proposed for markets with zero validated demand signal
- Entry criterion is "when we feel ready" rather than a named metric and threshold
- Product Development items serve a different buyer persona with no analysis of the sales motion change required
- Diversification justified primarily by "we have cash" rather than a named transferable capability

## Verification

- [ ] Existing product and market defined precisely, with stated penetration rate
- [ ] Each growth option correctly classified to a quadrant
- [ ] Feasibility scored on at least 3 dimensions per option
- [ ] Primary quadrant selected (one); secondary optional (one); all others explicitly deprioritized
- [ ] Entry criteria for next quadrant = named metrics with thresholds
- [ ] 90-day milestone defined with stated accelerate/stop metric
- [ ] Diversification options carry an identified specific transferable capability

---

*Part of **deciqAI Knowledge Skills** — 189 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/ansoff-matrix** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
