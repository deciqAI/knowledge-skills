---
name: power-law-distribution
description: "Activate when: user is allocating capital or resources across a portfolio and wants to know where to concentrate; user says 'our average customer / deal / employee performs at X' and is making decisions from that average; user is building a risk model using standard deviation or VaR; user asks why a few customers or deals drive almost all revenue; user is evaluating VC fund returns or startup portfolio outcomes.
  Do NOT activate when: the distribution is demonstrably Gaussian (e.g., manufacturing tolerances under statistical process control); stakes are low enough that distribution shape does not affect the decision. More: deciqai.com/s/power-law-distribution"
---

# Power-Law Distribution

## Overview

A **power-law distribution** is a statistical distribution where probability of size *x* is proportional to *x^(−α)*: large events are rare but far more probable than a Gaussian model predicts, and the largest events dominate the total — there is no "typical" case.

First quantified by Pareto (1896) in wealth; formalized by Mandelbrot (1963) for financial returns; surveyed universally by Newman (2005) across cities, earthquakes, citations, and web traffic.

Composes with [`pareto-principle`](../pareto-principle/SKILL.md) (80-20 is the most famous application; this skill provides the math foundation), [`black-swan`](../black-swan/SKILL.md) (black swans are the extreme upper-tail events power laws make far more probable), [`expected-value-and-kelly`](../expected-value-and-kelly/SKILL.md) (Kelly sizing breaks under infinite-variance power laws), and [`antifragile`](../antifragile/SKILL.md) (antifragile strategies exploit the upper tail).

## When to Use

- Allocating capital or resources across a portfolio — power-law returns mean design must prioritize outliers
- Prioritizing customers, channels, content, or features where a small number account for most value
- Assessing business risk — Gaussian risk models (VaR, std dev) systematically underestimate extreme risk
- Any domain where "average" is the planning assumption and extreme outcomes are possible
- Evaluating AI/compute concentration — AI capex, chip export controls, frontier-lab funding, or "AI bubble" questions where value is capturing into a thin tail of companies

**Not when:** distribution is demonstrably Gaussian; stakes are low enough that shape doesn't affect the decision; audience will misuse power-law framing as nihilism.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete portfolio, risk, or allocation decision → run The Process directly.
- **Coach mode:** user is new to the concept → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-liner: a tiny number of items account for a disproportionate fraction of the total. Using averages in a power-law world is systematic error.
2. Check fit: extreme outcomes dominate the total; no natural "typical" scale; recursive self-similarity (top 20% of top 20% still follows the same ratio).
3. Elicit: what is being distributed? What does the top 1%, 5%, 10% account for as a fraction of the total?
> **[WAIT — do not advance until user responds]**
4. One question: are you designing for the average case or the extreme case? What would strategy look like if top 1% drove 50% of total value?
> **[WAIT — do not advance until user responds]**
5. Close: distribution type confirmed + implications for allocation / risk named + Gaussian errors identified and corrected.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Identify the distribution:** What is distributed? Preliminary hypothesis: Gaussian or power-law?

**Step 2 — Check power-law indicators:** Top __% accounts for __% of total. High mean-to-median ratio? Long right tail? Log-log plot roughly linear?

**Step 3 — Estimate tail exponent (if data available):** α < 2 → infinite variance; α < 1 → infinite mean. Practical implication:

**Step 4 — List Gaussian errors being made:** Using mean as planning assumption? VaR as risk measure? Designing for "typical" case? Averaging portfolio returns?

**Step 5 — Redesign for power-law structure:** Concentrate resources on upper-tail upside. Maximize shots at outliers. Size tail risk using extreme value theory, not std dev.

**Step 6 — Define monitoring triggers:** Track top-N performance, not average. Set review cadence and signal for when distribution shifts.

## Output Template
```
# Power-Law Analysis: <domain>
Distribution: top __% = __% of total | mean-to-median ratio: | long tail: Y/N
Tail exponent α ≈  | implication:
Gaussian errors being made: 1. 2. 3.
Redesigned approach: concentrate on / defocus from / tail risk sized at
Monitoring: metric | review trigger
```

*→ Method in Action: [Pareto 1896, Mandelbrot 1963, and VC Return Data](examples/pareto-1896-mandelbrot-1963-and-vc-return-data.md)*

*→ 2026 lens: [AI & venture returns concentration — a few labs plus Nvidia capture the tail (2023–2026)](examples/ai-venture-returns-concentration-2023-2026.md)*

## Pack: Power-Law Patterns Across Business Domains

| Domain | Power-law variable | Top-N share | Gaussian error | Correct approach |
|---|---|---|---|---|
| VC / startup investing | Return multiples | Top 1% → ~50% of fund | Average IRR | Maximize shots at outliers; write off tail fast |
| B2B revenue | Customer LTV | Top 10% → 50-80% revenue | Avg revenue per customer | Concentrate on top-tier; cost-to-serve long tail |
| Knowledge work | Individual output | Top 10% → 50%+ of value | Average performance review | Identify and amplify top performers |
| Content / media | Post virality | Top 1% → 50%+ of reach | Average engagement rate | Optimize conditions for outlier content |
| Operational risk | Event severity | Top 1% → 99% of damage | VaR based on std dev | Extreme value theory; fat-tail scenarios |

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Our average customer LTV is $X — healthy business." | If power-law, average is dominated by top 10%. Median customer may be barely profitable. |
| [D] "We track average deal size to forecast pipeline." | Deal size is power-law. Losing one large deal can collapse a forecast the average made look safe. |
| [D] "Our VaR model shows maximum likely loss is $Y." | VaR assumes Gaussian. Real tail risk is orders of magnitude larger. LTCM and 2008 validated this. |
| [D] "We lost money on 65% of investments, so portfolio is failing." | 65-75% loss rate is consistent with a top-quartile VC fund if the winners are large enough. |
| [D] "Risk model is validated because extreme events have been rare." | Power-law distributions can go long periods without a tail event — then produce a devastating one. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Planning assumptions built on averages where mean-to-median ratio is high
- Risk models use std dev, VaR, or normal distribution for outcomes that historically show fat tails
- Portfolio strategy aims to make most investments "work" rather than maximizing outlier access
- Top 10% of customers, deals, or investments are not tracked as a distinct priority category

## Verification

- [ ] Distribution examined empirically: top-N share calculated
- [ ] Mean-to-median ratio checked: high ratio confirms power-law
- [ ] Log-log plot examined (if data available)
- [ ] Specific Gaussian errors listed and corrected
- [ ] Resource allocation redesigned to concentrate on upper tail
- [ ] Risk model tail assumptions updated to power-law
- [ ] Monitoring metric tracks top-N, not average

**Stop rule:** if empirical data shows mean ≈ median and symmetric shape, Gaussian tools are appropriate. Do not force power-law framing onto genuinely Gaussian domains.

---

*Part of **deciqAI Knowledge Skills** — 233 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/power-law-distribution** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/power-law-distribution.json*
