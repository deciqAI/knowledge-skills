---
name: tipping-point
description: "Activate when: user asks 'how close are we to critical mass', 'why did growth suddenly explode (or collapse)', 'will this trend keep spreading', 'is there a network effect threshold here', 'what if we concentrated effort on early adopters'. Do NOT activate when: the phenomenon is genuinely linear with no network effects or social-proof dynamics; the question is purely 'do we have product-market fit' before any diffusion has started."
---

# Tipping Point

## Overview

A **tipping point** is the threshold at which gradually accumulating change produces a sudden, self-reinforcing reorganization of a system. Below the threshold the system absorbs incremental change; above it, dynamics compound rapidly toward a qualitatively different state — often irreversibly. Formalized by Schelling (1969, segregation models), generalized by Granovetter (1978, threshold distributions), popularized by Gladwell (2000).

Composes with [`network-effects`](../network-effects/SKILL.md) (most common tipping mechanism), [`s-curve-technology-adoption`](../s-curve-technology-adoption/SKILL.md) (cumulative-adoption visualization), [`feedback-loops`](../feedback-loops/SKILL.md) (positive loops produce tips; balancing loops prevent them), and [`pmf-crossing-the-chasm`](../pmf-crossing-the-chasm/SKILL.md) (the chasm is a specific tipping point).

## When to Use

- Designing growth strategy for a network-effect product or platform
- Evaluating whether a market trend is about to accelerate or fade
- Predicting whether a social movement, behavior change, or policy initiative will diffuse
- Diagnosing why a previously-growing community / platform / business is in decline
- Investing in trends where the question is "are we pre- or post-tipping?"
- Someone says "critical mass," "phase transition," "network effect threshold," "crossing the chasm"

**Not when:** the phenomenon is genuinely linear; the system is far below any plausible tipping point and the question is just product-market fit; timescales are too short to observe tipping dynamics.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a specific growth / diffusion question → run The Process directly.
- **Coach mode:** user is new to the framework → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **One-line:** before assuming linear growth or decline, ask whether there is a threshold structure underneath — small effort may produce nothing below the threshold, disproportionate effect near it, and unstoppable change above it.
2. **Check fit.** If the system is genuinely linear (no network effects, no social-proof dynamics, no positive feedback), tipping-point analysis adds little. Otherwise, check for thresholds.
3. **Elicit the system and the current state.** What is the phenomenon? Where is it now? What is the proposed intervention?
> **[WAIT — do not advance until user responds]**
4. **One question at a time:** is there a threshold? where is it approximately? how far is the system from it? where does marginal effort have leverage?
> **[WAIT — do not advance until user responds]**
5. **Close:** threshold-distance estimate + concentration of effort near the threshold + monitoring for downward-tipping risk.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — System:** phenomenon | hypothesized tipping point (network effect / critical mass / behavior threshold) | self-reinforcement mechanism | direction (up / down).

**Step 2 — Threshold:** critical-mass user count for network products (often 100-1000 active in a segment); fraction of adopters for social diffusion (~10-25% empirically); social-proof threshold for behavior change. Document empirical basis.

**Step 3 — Current state:** adopters / incidence | distance from threshold | trajectory | rate of approach.

**Step 4 — Leverage + monitoring + defense:** far below threshold → foundational work beats diffusion; approaching → referrals / influencer / social-proof signaling have outsized leverage; past threshold → defend fast; far above → watch downward-tip early warnings. Set threshold-crossing criterion: "when [metric] crosses [value]." Document conditions + triggers for downward-tipping defense.

## Output: Tipping-Point Analysis
```
# Tipping Analysis: <system>
System: phenomenon | tipping point | self-reinforcement mechanism | direction (up/down)
Threshold estimate: estimated location | empirical basis
Current state: adopters/incidence | distance from threshold | trajectory
Leverage zones: where marginal effort has disproportionate effect | recommended concentration
Monitoring metrics: forward-looking indicators | threshold-crossing criteria
Downward-tipping defense: conditions that drop below threshold | early-warning signs | triggers
```

*→ Method in Action: [Schelling Segregation + Hush Puppies + Modern Platform Tipping](examples/schelling-segregation-hush-puppies-modern-platform-tipping.md) · [Measles Herd-Immunity Threshold](examples/measles-herd-immunity-threshold.md)*

## Pack: Tipping-Point Application Patterns

| Domain | Threshold dynamic | Tipping signal |
|---|---|---|
| Social network | User density per geographic segment | Each new user brings more friends |
| Two-sided marketplace | Supply-demand density per micro-market | Retention compounds |
| SaaS / B2B | % of team using the tool | Tool becomes infrastructure |
| Tipping down | Activity decline; key creators leaving | Users falling faster than acquisition |

## Applying It Well

- Identify the self-reinforcement mechanism explicitly — different mechanisms have different threshold shapes
- Estimate threshold from comparable historical cases, not intuition
- Concentrate marginal effort near the threshold, not uniformly across the funnel
- Design downward-tipping defenses before you need them; individual preferences don't predict system outcomes

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Linear growth is the model; let's just keep doing what works" | If there is a threshold, linear extrapolation is wrong. Identify the threshold or argue why one doesn't exist. |
| [D] "We're not at the tipping point yet, so growth is bad" | Below threshold, leverage is low — the question is whether marginal investment is positioned correctly. |
| [D] "The product is great; tipping will happen naturally" | Product quality is rarely sufficient. Distribution, social-proof signaling, and network-density engineering matter. |
| [D] "We need to wait for organic momentum" | Often "waiting" is a euphemism for absence of deliberate threshold-targeting strategy. |
| [D] "Tipping points are mystical; we can't predict them" | They are statistical. Thresholds can be estimated from comparable historical cases. |
| [D] "Once tipped, we're safe" | False. Tipped systems can tip down. Defensive design and early-warning monitoring are required. |
| [D] "Network effects are our moat; we're untouchable" | Network effects produce upward tips and downward tips. Below critical mass, the same dynamics work against you. |
| [D] "We can engineer a tipping point with marketing" | Sometimes. Often the product or distribution structure must support diffusion; marketing alone cannot tip an undifferentiated product. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Growth strategy assumes linear extrapolation in a system with network effects
- The team cannot articulate where the tipping point is
- Marginal effort is being scaled even though leverage is low (below threshold)
- A platform / community is showing early signs of downward tipping with no defensive plan
- Investment is being made in a trend that has already tipped (late, expensive entry)
- Micro-individual preferences are being treated as predictive of macro-system outcome

## Verification

- [ ] Tipping-point dynamic (mechanism + direction) has been specified
- [ ] Estimate of the threshold location is documented
- [ ] System's current state relative to threshold is known
- [ ] High-leverage intervention zones have been identified
- [ ] Monitoring metrics for threshold-distance are in place
- [ ] Downward-tipping risk has been considered
- [ ] Historical comparables have been consulted for threshold-location calibration
- [ ] Marginal effort is concentrated near (not far from) the threshold

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/tipping-point?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=tipping-point** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
