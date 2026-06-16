---
name: compound-interest
description: "Activate when: user asks about starting early vs. later for savings/investing, wonders if small consistent gains add up, wants to know how long to double money, is evaluating long-term wealth or skill-building decisions, mentions 'Rule of 72' or 'exponential growth.' Do NOT activate when: the time horizon is short (under 3 years) and compounding is negligible; the underlying process is genuinely linear with no reinvestment or accumulation."
---

# Compound Interest

## Overview

Compound interest: a quantity grows at a rate proportional to its current size — growth itself grows — producing exponential accumulation. Formula: A = P × (1 + r)^t. Humans underestimate long-horizon outcomes because cognition extrapolates linearly. Two consequences: **Rule of 72** (doubles in ≈ 72/r periods); **late-period dominance** (most final value comes from the last few periods).

Composes with [`lindy-effect`](../lindy-effect/SKILL.md), [`hyperbolic-discounting`](../hyperbolic-discounting/SKILL.md), [`expected-value-and-kelly`](../expected-value-and-kelly/SKILL.md), [`network-effects`](../network-effects/SKILL.md), [`deep-work`](../deep-work/SKILL.md).

## When to Use

- Evaluating any long-horizon investment, savings, or wealth decision
- Deciding between starting earlier vs. starting later; intensity vs. duration paths
- Evaluating compound advantages in business (data, brand, switching cost)
- Skill-development planning; recognizing compound decay (fees, atrophy, trust erosion)

**Not when:** horizon is short; rate is so low linear approximation is fine; process is genuinely linear; situation requires immediate one-shot intensity.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete long-horizon case → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: duration of compounding dominates rate — starting earlier with small consistency beats starting later with large intensity.
2. Check fit. Short horizon or very low rate? Compound effects are small — save it for genuinely long horizons.
3. Elicit the specific decision, time horizon, and rate.
> **[WAIT — do not advance until user responds]**
4. Walk through Rule of 72, precise compound outcome, late-period dominance, and other life domains one question at a time.
> **[WAIT — do not advance until user responds]**
5. Close: decision informed by compound math + compound dynamics identified + commitment to early consistent action.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Specify the situation**
`Starting value / Rate (per period) / Time horizon / Decision / Alternative options`

**Step 2 — Rule of 72 intuition**
`Doubling time = 72/r | Doublings in horizon | Approximate multiplier = 2^doublings`

**Step 3 — Precise compound result**
`A = P × (1+r)^t | Linear-extrapolation comparison | Gap between linear and compound`

**Step 4 — Late-period dominance**
`Value at half-time (much less than half) | Value gained in last 25% (typically 50%+ of total)`

**Step 5 — Option comparison**
`Option A compound outcome | Option B compound outcome | Where duration dominates | Recommendation`

**Step 6 — Generalize**
`Other life domains with compound dynamics | Compound decay risks | Commitment to early action`

## Output Template

```
Compound Interest Analysis: <decision>
Situation: value / rate / horizon / decision
Rule of 72: doubling time / doublings / multiplier
Compound math: final (compound) vs. final (linear) / gap
Late dominance: value at half-time / last-25%-gains
Options: A vs. B / recommended
Generalization: other dynamics / decay risks / commitments
```

*→ Method in Action: [Bernoulli 1683, Graham/Buffett, and the Compound-Advantage Tradition](examples/bernoulli-1683-graham-buffett.md)*

## Pack: Compound Interest Application Patterns

| Domain | Compound mechanism | Operational implication |
|---|---|---|
| Retirement savings | Returns + reinvested dividends | Start early; minimize fees; hold 40+ years |
| Skill / expertise | Daily practice → expert capability | 30 min/day for 10 years beats intensive bootcamp |
| Brand / reputation | Loyalty compounds into market position | Consistency of promise over decades |
| Compound decay (fees) | 1% fee × 40 years ≈ 33% wealth loss | Low-fee structures; avoid recurring small costs |
| Compound decay (trust) | Single violation destroys decades of compound | Protect trust like the compound asset it is |

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "I'll start saving / investing later" | Destroys the compound horizon. $100/mo at 25 beats $300/mo at 45 at 7% to age 65 — early starter wins despite saving less. |
| [D] "1% better isn't worth it" | 1.01^365 ≈ 37×. Compounded over 10 years = expert vs. novice. |
| [D] "I'll catch up by working harder later" | Duration dominates intensity. Missing compound years cannot be made up with later intensity. |
| [D] "Fees are small" | 1% × 40 years compound = ~33% wealth destruction. Small fees are catastrophic long-term. |
| [D] "It hasn't grown much in the first few years" | Compound growth concentrates in the last years. Patience is the operative virtue. |
| [D] "I can time the market" | Missing the 10 best days of a decade destroys decades of compound. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Long-horizon decision made by linear extrapolation, not compound calculation
- Recurring fees or losses dismissed as "small"
- Plan is to "start later when I make more" — intensity substituted for duration
- Compound asset (trust, brand, skill) treated as something other than a compound asset

## Verification

- [ ] Rule of 72 applied to estimate doubling time
- [ ] Precise compound calculation done for the full horizon
- [ ] Late-period dominance identified
- [ ] Both option compound outcomes computed (if comparing options)
- [ ] Compound dynamics identified in non-financial life areas
- [ ] Compound decay risks named; early action recommended

---

*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/compound-interest?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=compound-interest** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
