---
name: antifragile
description: "Activate when: user asks whether their system/business/portfolio would survive a crisis; user says 'this has been fine for years but I'm nervous'; user wants to stress-test a plan against worst-case scenarios; user mentions Taleb, barbell strategy, via negativa, or skin in the game; user is deciding how to allocate across risky vs. safe options under high uncertainty.
  Do NOT activate when: the decision is small and fully reversible with no meaningful downside; the system is simple, well-understood, and low-stakes."
---

# Antifragile

## Overview

Nassim Nicholas Taleb (2012) identified a third response to stress beyond fragile/robust: **antifragile** — systems that *gain* from disorder, with bounded downside and unbounded upside.

- **Fragile:** concave — absorbs small stress, breaks catastrophically at the tail. (Over-leveraged banks, just-in-time supply chains.)
- **Robust:** linear — unchanged by stress. (Physical infrastructure, traditional skills.)
- **Antifragile:** convex — improves under stress. (Evolution, the immune system, the restaurant industry as a whole.)

Core warning: **most modern complex systems are hidden-fragile** — stable only because the tail event hasn't arrived yet. Composes with [`inversion`](../inversion/SKILL.md), [`black-swan`](../black-swan/SKILL.md), [`expected-value-and-kelly`](../expected-value-and-kelly/SKILL.md), [`feedback-loops`](../feedback-loops/SKILL.md).

## When to Use

- A system looks stable but may be hidden-fragile
- Designing a portfolio (financial, career, organizational) under uncertainty
- A "this can't happen" assumption is embedded in a strategic plan
- Recurrent small problems are suppressed rather than learned from
- User says: "Taleb," "barbell strategy," "convex," "skin in the game," "via negativa"

**Not when:** decision is small and reversible; system is simple and low-stakes; you confuse high-variance with antifragile.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete system → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step. In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: some things break under stress, some survive, **some get stronger** — most "stable" things are in the first category, just before stress arrives.
2. Check fit: small reversible decisions → not this lens.
3. Elicit their real system — what specifically are they stress-testing?
> **[WAIT — do not advance until user responds]**
4. Walk through The Process one step at a time with their input.
> **[WAIT — do not advance until user responds]**
5. Close by naming the specific design move (barbell / via negativa / optionality / skin-in-the-game) that fits their case.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Classify exposure:** Under small / medium / tail stress, does the system improve, hold steady, or suffer catastrophic loss? → Antifragile (convex) / Robust (linear) / Fragile (concave).

**Step 2 — Identify hidden fragility:** Search for leverage (financial, operational, organizational), single points of failure (one vendor, one customer >25%, one key person), concentration, and assumptions that have "always been fine" only because the tail hasn't arrived.

**Step 3 — Apply four design moves:**
- **Barbell:** extreme safety + extreme upside; avoid the fragile middle.
- **Via negativa:** subtract leverage, dependencies, complexity before adding anything.
- **Optionality:** add convex exposures — small loss in normal cases, large gain in tail-favorable cases.
- **Skin in the game:** align decision-makers with the downsides they create.

**Step 4 — Stress-test the claim:** Verify bounded downside + upside that scales with disorder. High-variance with high downside is risky, not antifragile.

## Output: Antifragile Audit

```markdown
# Antifragile Audit: <system>
## Exposure shape
- Small / medium / tail stress result: <…>
- Classification: fragile / robust / antifragile
## Hidden fragility
- Leverage / SPOF / concentration / untested assumptions: <…>
## Design moves
- Barbell / Via negativa / Optionality / Skin-in-the-game: <…>
## Stress test
- Bounded downside: <yes/no> | Convexity verified: <how>
```

*→ Method in Action: [Taleb's Framework, 2007-2012, and the 2008 Financial Crisis](examples/talebs-framework-2007-2012-and-the-2008-financial-crisis.md) · [1956 Grand Canyon Collision & Aviation Safety](examples/1956-grand-canyon-collision-and-aviation-safety.md)*

## Pack: Antifragile Patterns

| Domain | Fragile | Antifragile |
|---|---|---|
| Investing | Leveraged long, narrow concentration | Barbell (cash + convex options) |
| Career | One employer, one specialty | Portfolio (employment + side income + skill diversification) |
| Supply chain | Just-in-time, single-supplier | Buffer inventory + multi-supplier redundancy |
| Startup capital | Thin runway, one VC | Buffered runway, diverse cap table |

**Applying it well:** Hidden fragility is the rule — search proactively. Via negativa (subtract complexity) is usually the highest-leverage move. Don't over-apply to simple, reversible decisions.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "It's been fine for years" | The tail hasn't tested it. Diagnose by exposure shape, not history. |
| [D] "We have insurance / hedges" | Most insurance is fragile to correlated tail events. Verify it works in *actual* tail scenarios. |
| [D] "Diversification handles it" | True for normal-distribution risks; false when tail correlations spike to 1. |
| [D] "It would take a black swan to break this" | Black swans happen routinely. This is the fragile-thinker's tell. |
| [D] Treating high-variance as antifragile | High variance + high downside = risky. Antifragile requires **bounded** downside. |
| [D] "Optimization always good" | Over-optimization removes slack. Slack absorbs shocks. |
| [D] Adding features and complexity | Via negativa: subtract first; add only with explicit fragility budget. |
| [D] "We're antifragile" as a label | Show bounded downside + convex upside or don't claim it. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- "It hasn't happened in N years" / risk model assumes normal distribution for fat-tailed phenomena
- Single point of failure not yet stressed; high leverage with no slack
- Customer or vendor concentration on one party for mission-critical function
- "It's antifragile" claim without specified bounded downside + unbounded upside

## Verification

- [ ] Exposure shape diagnosed (concave / linear / convex) under small / medium / tail stress
- [ ] Hidden fragility searched: leverage / SPOF / concentration / untested assumptions
- [ ] At least one design move applied: barbell / via negativa / optionality / skin-in-the-game
- [ ] Bounded downside and convexity verified, not assumed; skill not over-applied to simple decisions

---

*Part of **deciqAI Knowledge Skills** — 189 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/antifragile** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
