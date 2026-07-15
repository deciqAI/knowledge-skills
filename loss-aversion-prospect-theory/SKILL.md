---
name: loss-aversion-prospect-theory
description: "Activate when: someone says 'I don't want to lose what I have', a deal is stuck because a concession feels like a loss, a pricing or incentive change gets unexpected pushback, someone is refusing a bet that looks positive in expected value, a free trial cancels at high rate. Do NOT activate when: the loss being avoided is genuinely catastrophic and irreversible (use Kelly/antifragile instead); the decision is small and one-shot where EV approximation is acceptable."
---

# Loss Aversion and Prospect Theory

## Overview

People evaluate outcomes relative to a reference point (not absolute wealth), weight losses ~2.25x as heavily as equivalent gains, are risk-averse in gain frames and risk-seeking in loss frames, and distort probabilities (overweighting small, underweighting large). The same physical outcome feels different depending on framing — this skill diagnoses and corrects that asymmetry.

Composes with [`sunk-cost-fallacy`](../sunk-cost-fallacy/SKILL.md), [`framing-effect`](../framing-effect/SKILL.md), [`expected-value-and-kelly`](../expected-value-and-kelly/SKILL.md), [`anchoring`](../anchoring/SKILL.md), [`pricing-strategy`](../pricing-strategy/SKILL.md).

## When to Use

- A decision involves uncertainty and the chooser is visibly averse to a "loss" framing
- People are refusing positive-EV bets because the downside feels disproportionately bad
- Negotiations are stuck because concessions feel like losses from an anchored reference point
- A product launch, pricing, or incentive is producing unexpected adoption patterns
- Small-probability events are being over- or under-insured against
- An investor is holding a losing AI / Nvidia / semiconductor position waiting to "get back to breakeven," or is reacting to an AI-capex, AI-valuation, or AI-adoption drawdown (e.g. the DeepSeek shock) rather than re-deriving forward EV
- Someone says "loss aversion," "prospect theory," "reference point," "endowment effect," "status quo bias," "disposition effect"

**Not when:** the asymmetric weighting is rational (genuinely catastrophic stakes); the reference point is legitimate; the decision is small and one-shot.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: before calling a risk choice irrational, identify the reference point and check if the decision flips when reframed gain vs. loss.
2. Check fit — if the loss is genuinely catastrophic and irreversible, asymmetric aversion is rational; use Kelly/antifragile, not debiasing.
3. Elicit the specific decision: what's being chosen, and what reference point makes one option feel like a "loss"?
> **[WAIT — do not advance until user responds]**
4. Work through EV for each option; shift the reference point; test gain vs. loss reframing; flag over/underweighted probabilities.
> **[WAIT — do not advance until user responds]**
5. Close: restate decision in EV terms and name explicitly how reference-point and probability-weighting influenced it.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Specify decision:** options, probability × payoff distributions, reference point (explicit or implicit).
**Step 2 — Compute EV:** Σ(probability × payoff) for each option; identify EV-dominant choice.
**Step 3 — Identify distortions:** loss aversion (losses weighted >1x gains?), reference dependence (alternative reference points?), probability weighting (small overweighted? large underweighted?), diminishing sensitivity (large outcomes compressed?).
**Step 4 — Reframe and re-test:** shift the reference point; restate as gain vs. loss; express probabilities numerically. If the decision flips, prospect-theory distortions are doing meaningful work.
**Step 5 — Choose decision rule:** catastrophic+irreversible → respect loss aversion | moderate+repeatable → maximize EV | large+reversible → Kelly criterion | one-shot → add regret minimization.
**Step 6 — Document:** chosen option, its EV, why it dominates, and which distortions were acknowledged/overridden.

## Output Template

```
Decision: | Options (prob × payoff): | Reference point:
EV per option: | EV-dominant option:
Distortions: loss-aversion ratio | alternative reference points | probability weighting | diminishing sensitivity
Reframe test: decision under shifted reference point | gain vs. loss reframe
Stakes class + decision rule applied:
Final choice + acknowledged distortions + rationale:
```

*→ Method in Action: [Kahneman and Tversky's 1979 Prospect Theory](examples/kahneman-and-tversky-1979-prospect-theory.md) · [PGA Tour Par vs. Birdie Putts](examples/pope-and-schweitzer-2011-pga-tour-putting.md)*
*→ 2026 lens: [Holding AI Positions Through Drawdowns — the Disposition Effect (2023–2026)](examples/nvidia-ai-drawdowns-disposition-effect-2023-2026.md)*

## Pack: Prospect Theory Patterns

| Domain | Manifestation | Counter |
|---|---|---|
| Investing | Disposition effect: sell winners early, hold losers | Pre-committed exit rules |
| Negotiation | Concession framed as a loss | Multi-issue packaging; anchor first |
| Pricing | $1000→$500 feels better than $500 direct | Strikethrough + anchor pricing |
| Insurance | Overweighting small-probability catastrophe | Compute true EV vs premium |
| Subscriptions | Free trial creates endowment; cancellation feels like loss | Use trial as conversion engine |
| Health / policy | Surgery refused when framed as mortality | Reframe in survival terms; defaults |

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "I'm just being prudent about the downside" | Often 2:1 weighting making positive-EV bets feel bad. Compute EV explicitly. |
| [D] "The status quo is the safe default" | Status quo bias is a documented bias. Compute EV of change vs. continuing. |
| [D] "I don't want to lose what I have" | Reference dependence — "what I have" is moveable by whoever frames the decision. |
| [D] "It's a sure thing — I'll take the sure thing" | Certainty effect. Rational for catastrophic stakes; irrational for moderate/repeatable. |
| [D] "Even a small chance of disaster is unacceptable" | Probability-weighting artifact. Compute expected disaster damage vs. expected upside. |
| [D] "I'd rather wait and not take the loss" | The loss is already real; waiting chooses whether to recognize or compound it. |
| [D] "I'm not as loss averse as most people" | Bias is robust under self-rated immunity. Use computed EV, not self-rating. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Risk-aversion in gain frame + risk-seeking in loss frame for economically equivalent choices
- Reference point not made explicit; probability language verbal not numerical
- "Sure thing" chosen at significant EV cost
- Negotiation stuck at an arbitrarily-anchored reference point
- Investment held past rational exit because realizing a loss feels worse than its objective magnitude

## Verification

- [ ] EV computed for each option
- [ ] Reference point made explicit; at least one alternative tested
- [ ] Decision re-tested under gain vs. loss reframing
- [ ] Probabilities stated numerically, not verbally
- [ ] Loss aversion respected (catastrophic) or overridden (moderate) deliberately, not by default
- [ ] If overriding, EV justification documented

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/loss-aversion-prospect-theory** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
