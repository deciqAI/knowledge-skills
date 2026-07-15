---
name: goodharts-law
description: "Activate when: our KPI is going up but the real outcome isn't improving; people seem to be gaming the metric; we're about to tie bonuses or promotions to a number; an algorithm is producing results nobody intended; a test or audit system is being designed.
  Do NOT activate when: the metric IS the goal with no proxy gap; measurement is purely descriptive with zero stakes attached."
---

# Goodhart's Law

## Overview

**Goodhart's Law:** when a metric controls behavior, people optimize the metric rather than the underlying goal. Formulated by economist Charles Goodhart (1975) on UK monetary policy; sharpened by Marilyn Strathern (1997): *"When a measure becomes a target, it ceases to be a good measure."* Four failure mechanisms (Manheim & Garrabrant 2018): **Regressional**, **Extremal**, **Causal**, **Adversarial**. Countermeasure is always multi-metric + audit + rotation.

Composes with [`feedback-loops`](../feedback-loops/SKILL.md), [`principal-agent`](../principal-agent/SKILL.md), [`okr-goal-setting`](../okr-goal-setting/SKILL.md), [`survivorship-bias`](../survivorship-bias/SKILL.md).

## When to Use

- A KPI is being introduced or its weight is increasing in performance evaluation
- A metric is "improving" without corresponding improvement in the underlying goal
- People are visibly optimizing for a number rather than the work it was meant to track
- Algorithmic optimization is producing outcomes the designers didn't intend
- Resource allocation is driven by a single composite score or ranking
- An AI model, benchmark, or engagement metric is being optimized (or used to justify AI capex / adoption / AI-native competition) and the score is rising faster than real capability or user value

**Not when:** metric and goal are identical; stakes too low for gaming; metric is purely descriptive with no reward/punishment; question is which metric to use, not whether the measurement-reward system is sound.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete metric or system → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: before relying on a metric to control behavior, predict how people will game it — choose the system that survives that prediction.
2. Check fit: if the metric is purely descriptive (no reward attached), Goodhart's law doesn't apply yet.
3. Elicit the specific metric and the underlying goal: what's being measured? What's the actual outcome you care about?
> **[WAIT — do not advance until user responds]**
4. One question at a time: proxy gap? How would a clever agent game this? Which Goodhart category? What countermeasure fits?
> **[WAIT — do not advance until user responds]**
5. Close: name the gaming-resistant design (multi-metric, audit, rotation, paired-constraint) + monitoring schedule.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — State metric and goal:** metric being targeted / underlying goal / current proxy-goal correlation / who is measured / stakes.

**Step 2 — Predict the gaming:** list ≥3 ways to game the metric with minimum effort on the goal. If you can't list 3, you haven't thought hard enough.

**Step 3 — Categorize mechanism:**

| Mechanism | Test |
|---|---|
| Regressional | Is there noise that optimization will push into? |
| Extremal | Does metric-goal correlation break at extremes? |
| Causal | Is the metric a symptom, not a cause? |
| Adversarial | Will agents actively game with intelligence? |

**Step 4 — Choose countermeasure:** Regressional → constrain range. Extremal → paired constraint metrics. Causal → closer-to-causation metric + direct audit. Adversarial → multi-metric + randomized audits + rotation.
**Step 5 — Design the system:** primary metric / constraint metric(s) / audit mechanism (sampled direct goal observation) / rotation schedule / separation of measure-for-control from measure-for-diagnosis / gaming-detection threshold.
**Step 6 — Schedule re-evaluation:** independent goal measurement (how/when/who) / drift threshold / retirement criteria / owner.

## Output template

```markdown
# Goodhart-Robust Design: <metric>
Metric: | Underlying goal: | Correlation: | Who measured: | Stakes:
Gaming vectors (≥3):
Mechanism: Regressional / Extremal / Causal / Adversarial
Primary metric: | Constraint metric(s): | Audit: | Rotation: | Separation: | Gaming threshold:
Goal measurement (independent): | Drift threshold: | Retirement criteria: | Owner:
```

*→ Method in Action: [Goodhart 1975 (M3) and Strathern 1997 (RAE)](examples/goodhart-1975-m3-and-strathern-1997-rae.md)*
*→ 2026 lens: [AI benchmarks and engagement metrics as targets (2023–2026)](examples/ai-benchmark-and-engagement-gaming-2023-2026.md)*

## Pack: Goodhart's Law Patterns

| Domain | Common gaming | Defense |
|---|---|---|
| Sales quotas | Sandbagging, channel stuffing, end-of-quarter discounts | Multi-period averaging; quality metrics; clawback |
| Hospital wait targets | Ambulance parking, patient reclassification | Outcome audits; paired metrics; randomized inspection |
| Standardized testing | Teaching to test, curriculum narrowing | Sample-based assessment; multi-measure; reduce single-test stakes |
| Algorithmic engagement | Clickbait, outrage, misinformation | Multi-objective optimization; quality + harm constraints |

## Applying It Well

- All metrics are proxies — narrower than the goal. Pre-commit to gap analysis before deployment.
- Gaming is rational under measurement pressure. Fix the system, not the people.
- Rotation and audit are the only durable defenses. Plan metric retirement at design time.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

| Fake move | Reality |
|---|---|
| [D] "If you can't measure it, you can't manage it" | Often false. Judgment, trust, and direct observation are also valid management tools. |
| [D] "Our metric is well-defined; it won't be gamed" | Precision invites precise gaming. Basel II capital ratios were well-defined — extensively gamed. |
| [D] "Our people wouldn't game the metric" | Goodhart's law is structural; individual virtue is insufficient in aggregate. |
| [D] "We just need a better metric" | Often the issue is any single metric under pressure; fix is multi-metric + audit. |
| [D] "We've used this metric for years" | Long use = more time for gaming to mature. Tenure is a warning, not an endorsement. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

## Red Flags

- Metric tied to high-stakes rewards or punishments
- Metric "improves" without obvious improvement in the underlying goal
- People being measured can already articulate ways to game it
- Single metric is the primary evaluation tool, no audit or paired-constraint

## Verification

- [ ] Goal underlying the metric specifically named
- [ ] Proxy gap explicitly described; ≥3 gaming vectors listed
- [ ] Goodhart mechanism category identified
- [ ] Countermeasure design (multi-metric, audit, rotation) in place
- [ ] Independent goal measurement scheduled with owner and retirement date

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/goodharts-law** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*