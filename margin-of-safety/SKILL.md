---
name: margin-of-safety
description: "Activate when: user asks how much buffer to build into a budget, timeline, or investment; someone says 'I might be wrong on my estimate — how much cushion do I need?'; a project or position is running lean and someone wonders if there's enough runway; user mentions Ben Graham, value investing, or 'buying a dollar for fifty cents'; someone is deciding how much to raise or reserve before committing.
  Do NOT activate when: the domain is fully deterministic with no estimation error; the user is using margin as an excuse to avoid committing to anything (perpetual deferral, not safety)."
---

# Margin of Safety

## Overview

**Benjamin Graham** introduced margin of safety in *Security Analysis* (1934) as the founding principle of value investing: buy assets at prices substantially below your estimate of intrinsic value so that estimation errors and adverse events don't produce permanent loss. The principle generalizes to engineering load factors, project budgets, founder runway, and any commitment where your estimate could be wrong.

The unifying insight: **point estimates are systematically optimistic.** Margin of safety is the structural discipline that survives that optimism.

Composes with [`antifragile`](../antifragile/SKILL.md) (margin = bounded-downside half), [`black-swan`](../black-swan/SKILL.md) (margin is what survives the tail you didn't predict), [`expected-value-and-kelly`](../expected-value-and-kelly/SKILL.md) (margin sizing relates to Kelly fractional-betting), and [`first-principles`](../first-principles/SKILL.md) (audit the estimate first; then apply margin).

## When to Use

- Sizing any commitment under uncertainty: investment positions, project budgets, fundraising timelines, hiring plans, capacity reservations
- A point estimate is being used as the basis for a major decision
- "Just-in-time" or "lean" or "fully utilized" pressure is removing buffers from a critical system
- A historically reliable system has been gradually de-buffered until it operates at the edge
- Weighing whether a stretched valuation leaves any buffer — AI capex assumptions, AI-era valuations, or whether a price already extrapolates optimistic AI adoption
- Someone says: "margin of safety," "Ben Graham," "value investing," "buffer," "load factor," "buy a dollar for fifty cents," "Mr. Market"

**Not when:** the domain is genuinely deterministic with no estimation error (rare); the cost of the buffer exceeds the expected loss from going without; you are using margin as an excuse to avoid any commitment ("perpetual margin" is procrastination).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: when your estimate of value or required resources is uncertain, commit only at a level where being 30-50% wrong still leaves you intact.
2. Check fit against When to Use / When NOT to use.
3. Elicit the real situation — what commitment are they sizing?
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time with their input: point estimate → uncertainty bounds → margin choice → discipline check.
> **[WAIT — do not advance until user responds]**
5. Close by naming the specific commitment level with the margin built in.
> **[WAIT — do not advance until user responds]**

## The Process

**1. Compute the point estimate honestly.** For investments: intrinsic value via DCF, comparables, or asset value. For projects: expected cost and time. Be specific — "worth more than the price" is not an estimate.

**2. Quantify realistic uncertainty.** What does a 20% and 50% adverse scenario look like? What is the historical base rate of being wrong by this margin in this domain?

**3. Choose the margin explicitly.** Value investing: 30-50% discount. Engineering structural: 2-4x load. Project budget: 50-100% time buffer. Founder runway: 1.5-2x expected time to milestone. Adjusted commitment = point estimate × (1 − margin%).

**4. Refuse to commit beyond the margin.** Will you walk away if the price/scope/timing doesn't meet it? Most failures are commitment-discipline failures, not analytical ones.

**5. Stress test.** If assumptions are wrong by 30% / 50%, does the position survive? If any answer is no, increase the margin or don't commit.

## Output: Margin of Safety Audit

```markdown
# Margin of Safety Audit: <commitment>
- Point estimate: <value> | Method: <…>
- 20% adverse: <…> | 50% adverse: <…> | Base rate of being this wrong: <…>
- Margin %: <…> | Adjusted commitment: <point estimate × (1−margin)>
- Discipline check: walk away if margin not met? <yes/no>
- Survives 30% adverse: <yes/no> | Survives 50% adverse: <yes/no>
```

*→ Method in Action: [Graham's 1934 Framework and Buffett's Lifelong Application](examples/grahams-1934-framework-and-buffetts-lifelong-application.md)*

*→ 2026 lens: [Margin of Safety Against AI-Era Valuations (2024–2026)](examples/ai-era-valuations-margin-of-safety-2024-2026.md)*

## Pack: Margin of Safety by Domain

| Domain | Typical margin |
|---|---|
| Value investing | 30-50% discount to intrinsic value |
| Aerospace / civil engineering | 1.5-4x expected load |
| Cloud capacity | 1.5-2x expected peak |
| Founder runway / software project | 1.5-2x expected time to milestone |
| Personal emergency fund | 6-12 months expenses |

*→ Primary sources: [references/sources.md](references/sources.md)*

## Applying It Well

- Margin is a **discipline**, not just a number — the skill is refusing to commit when the margin isn't there.
- Match margin size to the domain's base rate of estimation error.
- "Lean/just-in-time/fully utilized" pressures systematically remove margins — diagnose whether saved cost exceeds expected loss from un-buffered failure.
- Margin enables aggressive bets within a safe envelope; it is not cowardice.

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "My estimate is accurate, no margin needed" | People are wrong by 30%+ more often than expected. Margin is for the cases where you're wrong. |
| [D] "Margin is too expensive — competitors will outbid me" | True in normal times. False in stress times, when un-margined competitors blow up. |
| [D] "I'll add margin later when I see how it goes" | Cannot. Margins must be built in at commitment time. |
| [D] Using margin as procrastination | "I need bigger margin" → "I'll never commit." Margin enables commitment, not prevents it. |
| [D] Computing margin on the wrong base | Graham's 50% is on intrinsic value, not price. Project margin is on expected duration, not best case. |
| [D] "I have insurance / hedges, so I don't need margin" | Insurance has counterparty risk and model errors. Margin in the asset is more reliable. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Point estimates used for major commitments without explicit uncertainty bounds
- Margins eroded over time by optimization pressure with no risk diagnosis
- Margin claimed but not quantified; or computed on optimistic rather than expected base
- Analyst computed right margin, committed anyway (discipline failure)
- "We can't afford the margin" applied to mission-critical capacity

## Verification

- [ ] Point estimate is explicit and methodologically grounded
- [ ] Uncertainty bounds are quantified (20%, 50% adverse scenarios)
- [ ] Historical base rate for being wrong by similar margin has been considered
- [ ] Margin percentage is chosen and justified for the domain
- [ ] Discipline check: would walk away if margin isn't met
- [ ] Stress test: position survives 30% and 50% adverse scenarios

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/margin-of-safety** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
