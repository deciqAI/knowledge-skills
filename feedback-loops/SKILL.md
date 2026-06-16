---
name: feedback-loops
description: >
  Activate when: user says "we keep overshooting/undershooting", "the cure is causing the disease",
  "we're stuck in a loop", "why does this keep happening?", "the system keeps fighting back",
  "bullwhip effect", "death spiral", "growth flywheel"; system shows oscillation or sudden collapse;
  user is planning an intervention in an org/market/supply chain and wants to predict how it will respond.
  Do NOT activate when: the decision is a one-shot linear choice with no feedback to future decisions,
  or an exogenous shock so large it dominates all internal dynamics is the obvious explanation.
---

# Feedback Loops

## Overview

A system has a **feedback loop** when its output circles back as input to the next cycle. **Reinforcing loops** amplify (compound interest, viral growth, bank runs, death spirals). **Balancing loops** self-correct (thermostats, price discovery, immune response). The critical complication is **delay**: when delay is long relative to response time, even well-designed balancing loops produce oscillation and overshoot — and operators systematically mismanage the system (Sterman 1989: supply-line underweight = 0.34 on a 0–1 scale).

Composes with: [`second-order-thinking`](../second-order-thinking/SKILL.md) · [`s-curve-technology-adoption`](../s-curve-technology-adoption/SKILL.md) · [`prisoners-dilemma`](../prisoners-dilemma/SKILL.md) · [`probabilistic-thinking`](../probabilistic-thinking/SKILL.md)

## When to Use

Apply when: system shows non-linear surprise (collapse, oscillation, death spiral, growth flywheel); you are intervening in a complex system and success depends on how it responds; trends are not extrapolating well; bullwhip or oscillation in any quantity that should be steady.

**When NOT to use:** one-shot linear decision with no feedback; insufficient data to map loops (hand-waving without structure); decision too time-bounded for delays to matter; exogenous shock dominates internal dynamics.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** concrete case → run The Process directly.
- **Coach mode:** unfamiliar or no concrete case → guide, don't lecture.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: when a system's output circles back as input, you have a feedback loop — it self-amplifies (reinforcing) or self-corrects (balancing), and delays make behavior far worse than expected.
2. Check fit against When to Use / When NOT to use. If it's a one-shot linear decision, redirect.
3. Elicit their real case: a specific behavior or dynamic they face right now — not a hypothetical.
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time with their input — map the loop, classify it, locate the delay.
> **[WAIT — do not advance until user responds]**
5. Close by naming the leverage point uncovered and why it is higher than a parameter fix.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Feedback-Loop Diagnosis** — map structure, find dominant loop, predict behavior, find leverage.

1. **Name system + variable of interest.** Without a specific variable, analysis becomes vague narrative.
2. **List drivers and outputs.** What inputs change your variable? What does it change in turn? Stay concrete.
3. **Identify loops.** Trace chains where a variable feeds back to itself. Most systems have several.
4. **Classify each loop (R or B).** Count negative signs around the loop — even = reinforcing; odd = balancing.
5. **Locate delays.** Where does a cause take significant time to produce its effect? Delays are where intuition fails.
6. **Identify dominant loop.** Growth phase = R dominant; maturity = B catching up; crisis = suppressed R taking over.
7. **Map stocks and flows.** Stocks = accumulations; flows = rates. A positive flow can still leave a stock dangerously low.
8. **Predict behavior pattern.** Pure R → exponential growth/collapse. Pure B → equilibrium. R+delay → overshoot/oscillation. R+B competing → S-curve. Mismatch with observed behavior = missed loop.
9. **Find leverage (Meadows hierarchy).** Parameters → buffers → structures → delays → balancing loops → reinforcing loops → goals → paradigm. Most failed interventions push parameters; move up.
10. **Stress-test against system response.** Balancing loops fight back; reinforcing loops restore trajectory. Intervention must change structure, not just symptom.

### Output: Feedback-Loop Diagnosis

```
System / variable: <…>
Loops: R1 <chain>; B1 <chain>
Delays: <where; rough magnitude>
Dominant loop: <…> — matches observed behavior because <…>
Stocks: <…>  Flows: <…>
Predicted behavior without intervention: <pattern + timeframe>
Leverage (Meadows): lowest <param>; higher <structural>; highest <goal/paradigm>
Intervention: <move> | System response: <…> | Backfire risk: <…>
Falsifier: <observable that would prove the diagnosis wrong>
```

*→ Method in Action: [Forrester's Beer Distribution Game & Sterman's 1989 Measurement](examples/forresters-beer-distribution-game-stermans-1989-measurement.md)*

## Pack: Loop Patterns

- **R growth:** network effects, viral k>1, compounding learning curves. Risk: hits a balancing limit you don't control.
- **R collapse:** death spirals, bank runs, adverse selection cascades. Defense: structural circuit breakers, fast intervention.
- **B working:** market price discovery, wages, thermostats. Don't suppress healthy balancing loops.
- **B + long delay → oscillation:** bullwhip, cobweb cycles, capacity build-out. Defense: shorten delays, damp response, share end-demand data.
- **R + B → S-curve:** technology adoption. See [`s-curve-technology-adoption`](../s-curve-technology-adoption/SKILL.md). To extend growth, kick off a second R loop before the first saturates.

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Just be more careful / disciplined" | Identical structures produce similar dysfunction regardless of who operates them (Sterman 1989). Exhortation = marginal; structural redesign = real. |
| [D] Treating delay as friction to reduce rather than a structural feature to model | Many delays are irreducible. For those, model them explicitly — don't pretend to reduce them. |
| [D] Extrapolating recent trends in a feedback system | Feedback systems switch regime when dominant loop changes; recent observations are loop outputs, not reliable baselines. |
| [D] Confusing stocks and flows | "Higher hiring rate" ≠ "enough people." Flow ≠ stock. Check both. |
| [D] "It's the market / external event" | Often the operators created the variability themselves (Sterman's subjects blamed constant demand). Check internal generators first. |
| [D] Parameter adjustment when structure is the problem | "Raise the bonus / add a metric" = noise in a structurally-driven system. Move up the Meadows hierarchy. |
| [D] "Death spiral = inevitable doom" | Death spirals are loops with modifiable structural components. Find the most modifiable arrow. |
| [D] "Let's push harder on the growth loop" | Leverage is in understanding what balancing loop catches up, and when — not in pushing parameters harder. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Trends extrapolated in a feedback-driven system · Oscillation blamed on external variability without checking internal loop generators · Intervention at parameter level when loop structure is the source · "Be more careful" proposed in a Forrester-adversarial structure · Stocks and flows confused · Death spiral or growth narrative with no loop/nodes/delays specified · All interventions at lowest (parameter) leverage level

## Verification

- [ ] System and variable named · At least one R and B loop identified with causal chain · Each loop classified by sign-counting
- [ ] Delays identified with rough magnitudes · Dominant loop identified; observed behavior consistent with it
- [ ] Stocks and flows distinguished · Predicted behavior matches actual (if not, re-classify)
- [ ] Leverage points ranked; recommendation not at lowest level if higher leverage is accessible
- [ ] System response to intervention considered · Observable falsifier named

*→ Primary sources: [references/sources.md](references/sources.md)*

---

*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/feedback-loops?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=feedback-loops** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
