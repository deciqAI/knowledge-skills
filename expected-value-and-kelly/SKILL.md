---
name: expected-value-and-kelly
description: "Activate when: user asks 'how much should I bet/invest on this?', 'what's the expected value here?', 'Kelly criterion', 'optimal bet size', 'fractional Kelly', 'how big a position should I take?', or is allocating capital across repeated decisions (ad spend by segment, VC portfolio construction, position sizing, A/B test ramp).
  Do NOT activate when: the decision is one-shot and non-repeating (career change, marriage) — use regret-minimization instead; or when the user cannot estimate probabilities or payoffs even roughly."
---

# Expected Value and the Kelly Criterion

## Overview

Two questions decide most repeated bets: **is this bet good?** (EV) and **how big?** (Kelly). Most professional ruin comes from positive-EV bets sized wrong. **EV = p · W − q · L.** If EV ≤ 0, do not bet. **Kelly f\* = (bp − q) / b** maximizes long-term geometric growth (Kelly, Bell Labs, 1956). Full Kelly requires casino-grade certainty; default to half- or quarter-Kelly for estimated edges.

Neighbors: [first-principles](../first-principles/SKILL.md) · [occams-razor](../occams-razor/SKILL.md) · [second-order-thinking](../second-order-thinking/SKILL.md) · [inversion](../inversion/SKILL.md) · [regret-minimization](../regret-minimization/SKILL.md) (for non-repeating life decisions).

## When to Use

- Decision **repeats many times** — capital allocation, position sizing, VC portfolio, ad spend, A/B test budget
- *How big to bet* matters as much as *whether to bet*; you have a **measurable or estimable edge**
- Someone says: "expected value," "EV," "Kelly," "optimal bet size," "how much should we put on this?"
- Sizing bets in a boom with power-law payoffs and possible ruin — **how much to allocate to AI startups / GPU-compute capex / AI-exposed equities** given frothy AI valuations, uncertain AI adoption, and correlated bets

**When NOT to use:** one-shot life decisions → [regret-minimization](../regret-minimization/SKILL.md); negative-EV bets (don't bet); unestimable probabilities; correlated bets without portfolio adjustment.

## Coaching Novices (Adaptive Front Door)

**Engine mode:** user has a concrete repeated bet → run The Process directly. **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: EV tells you **whether the bet is worth taking**; Kelly tells you **what fraction of bankroll to stake** — sized to maximize long-term growth without ruin.
2. Check fit against When to Use / When NOT to use. If one-shot life decision, redirect to [regret-minimization](../regret-minimization/SKILL.md). If EV is negative, say "don't bet" and stop.
3. Elicit their real bet. Ask for a concrete repeated decision with measurable inputs. > **[WAIT — do not advance until user responds]**
4. Walk The Process one step per turn: outcomes → probabilities → payoffs → EV → Kelly → fractional Kelly. > **[WAIT — do not advance until user responds]**
5. Close by naming their sizing rule: "bet f\* × bankroll, use half-Kelly given estimation uncertainty" — and the trigger that would change it. > **[WAIT — do not advance until user responds]**

## The Process

Run the **EV-Kelly Sizing** (EV → Kelly → fractional Kelly → stop trigger):

1. **Confirm the decision is repeated.** If "once," stop → use [regret-minimization](../regret-minimization/SKILL.md).
2. **Map the bet.** Win prob *p*, loss prob *q = 1−p*, payoff on win *W*, loss *L*, odds *b = W/L*.
3. **Compute EV.** EV = Σ(pᵢ · payoffᵢ). State per unit staked.
4. **Edge gate.** EV > 0? If no, stop — do not bet.
5. **Estimate input uncertainty.** Are *p* and *W* measured or estimated? Write 80% CI on edge.
6. **Compute Kelly fraction.** f\* = (bp − q) / b. For continuous: f\* ≈ μ/σ².
7. **Apply fractional Kelly.** Half-Kelly under modest uncertainty; quarter-Kelly under serious uncertainty.
8. **Set stop trigger.** "I will re-estimate if: (a) drawdown > X%, (b) outcomes diverge N σ over Y trials, (c) regime change invalidates edge model."

### Output: EV-Kelly Sizing

```markdown
# EV-Kelly Sizing: <bet/decision>
## Repeatability: <count or "ongoing"> — if one-shot, STOP.
## Bet map: p=<>, q=<>, W=<>, L=<>, b=<>
## EV: p·W − q·L = <number> — Edge: <positive/negative/zero>
## Estimation uncertainty: <measured/estimated>; 80% CI on edge: <range>
## Kelly fraction: f* = <full Kelly> → practitioner: <half/quarter-Kelly> = <number>
## Stop trigger: "I will re-estimate if <condition>."
## Correlation check: bets independent? <yes/no — adjustment>
```
*→ Method in Action: [Ed Thorp, Blackjack, and Princeton-Newport (1961 → 1988)](examples/ed-thorp-blackjack-and-princeton-newport-1961-1988.md) · [Bill Benter, Hong Kong Horse Racing (1985 → 2001)](examples/bill-benter-hong-kong-horse-racing-1985-2001.md)*
*→ 2026 lens: [Sizing Hyperscaler GPU/Compute Capex (2023–2026)](examples/hyperscaler-gpu-capex-kelly-2023-2026.md) — one CFO's repeated capex bet: wide CI, stranded-capital ruin tail, and fractional Kelly as staged, survivable capex.*
## Sizing Packs

| Domain | Fractional-Kelly | Stop trigger |
|---|---|---|
| Active equity | quarter-Kelly or less | drawdown > 2× expected annual vol |
| Venture capital | portfolio-level quarter-Kelly | hit rate diverges from model by vintage |
| Ad spend by segment | half- to full Kelly | ROAS falls >2σ over N conversions |
| A/B test ramp | fractional Kelly on traffic % | regression in primary metric |

## Applying It Well

- **Positive EV is necessary but not sufficient.** A positive-EV bet sized too large still wrecks you.
- **Default to fractional Kelly.** Full Kelly is for measured edges. Half- or quarter-Kelly for estimated edges — growth cost is small, protection is large.
- **Correlation eats Kelly fast.** All positions long tech, all VC bets in one vintage — adjust portfolio Kelly down.
- **Kelly is for bankroll, not for life.** Use [regret-minimization](../regret-minimization/SKILL.md) for career, marriage, time.
- **Update continuously.** Static Kelly on a stale edge is how winning strategies ride into ruin.

*→ Primary sources: [references/sources.md](references/sources.md)*
## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] Applying Kelly to **one-shot** decisions | Kelly maximizes long-run geometric growth rate across many bets. For a one-time bet, EV is the right concern; for life decisions, use [regret-minimization](../regret-minimization/SKILL.md). |
| [D] Treating **estimated *p*** as **known *p*** | Kelly is brutal when probability estimates are wrong. Use fractional Kelly to compensate for estimated inputs. |
| [D] Using **full Kelly with subjective probabilities** | Full Kelly is for casino-grade certainty. Half-Kelly costs ~25% of growth and cuts ruin risk by far more (Thorp 1997). |
| [D] Confusing **positive EV** with **"should bet"** | EV ignores variance, bankroll, path-dependency. A +1% EV bet that ruins you 1% of the time is not equivalent to one that ruins you 0%. |
| [D] **Ignoring correlation** across bets | Kelly assumes independent bets. Correlated bets (same sector, same vintage) require a lower portfolio-level Kelly. |
| [D] Using Kelly on **negative-EV** bets | Kelly returns zero or negative fraction when EV ≤ 0. No sizing rescues a -EV bet. Don't bet. |
| [D] Treating EV as the **only number that matters** | Bernoulli 1738: utility of money is non-linear. A +$1000 EV bet that risks your rent ≠ one that risks your rounding error. |
| [D] Forgetting Kelly's **brutal variance** | Even correct full-Kelly expects 50%+ drawdowns. Most professionals use half/quarter-Kelly to survive psychologically. |
| [D] Applying Kelly to **non-financial "bets"** | Kelly assumes a compoundable bankroll. Relationships, careers, time, attention don't compound across independent trials. |
| [D] Computing Kelly **once**, ignoring updates | A static fraction on a now-stale edge is the textbook path to ruin. Pre-commit to a re-estimation trigger. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Kelly applied to a decision that happens only once
- Full Kelly used with subjective probabilities and no calibration check
- EV is negative but a positive fraction is being computed
- No stop-and-re-estimate trigger is named
- Bets are obviously correlated but Kelly is computed per-bet without portfolio adjustment
- The "bankroll" is not liquid or fungible (career time, relationship capital)
- A historical drawdown wiped out the strategy; same fraction still applied without re-examining the edge

## Verification

- [ ] Decision confirmed *repeated*, not one-shot
- [ ] Outcomes, probabilities, and payoffs stated explicitly in correct units
- [ ] EV computed per unit staked; edge gate (positive/zero/negative) named
- [ ] Estimation uncertainty named (measured/estimated/mixed); 80% CI on edge given
- [ ] Kelly fraction computed with correct formula (binary vs. continuous)
- [ ] Fractional-Kelly adjustment applied with explicit justification
- [ ] Stop-and-re-estimate trigger named with concrete conditions
- [ ] Correlation across bets considered; per-bet Kelly adjusted if needed

---
*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/expected-value-and-kelly** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
