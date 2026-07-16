---
name: regression-to-the-mean
description: "Activate when: someone says 'things always bounce back,' wonders why an intervention seemed to work on a struggling team, is surprised their star performer regressed, is evaluating whether a coaching/bonus/firing had an effect, or is interpreting before-vs-after performance changes without a control group. Do NOT activate when: the measurement is genuinely noise-free (e.g., deterministic process outputs); the underlying signal has demonstrably changed due to a structural shift (new product launch, technology change). More: deciqai.com/s/regression-to-the-mean"
---

# Regression to the Mean

## Overview

**Regression to the mean** is the statistical regularity that any noisy measurement producing an extreme value tends to be followed on retest by a less-extreme value — because the extreme portion was partly driven by non-repeating random noise. There is no "force pulling back to average"; it is a mathematical consequence of signal + noise structure.

Named by Francis Galton (1886) studying parent-child height: tall parents have tall children, but slightly shorter; short parents have short children, but slightly taller. Kahneman's Israeli Air Force example (2011, Ch. 17) is the most-cited operational case — flight instructors concluded punishment works and praise doesn't, but were observing regression, not causation.

Composes with [`survivorship-bias`](../survivorship-bias/SKILL.md) (extreme survivors regress), [`probabilistic-thinking`](../probabilistic-thinking/SKILL.md) (regression is probabilistic), [`narrative-fallacy`](../narrative-fallacy/SKILL.md) (regression drives post-hoc narratives), [`fundamental-attribution-error`](../fundamental-attribution-error/SKILL.md) (attributing regression to character/intervention is FAE).

## When to Use

- Evaluating the effect of an intervention on extreme performers (struggling teams, top sales reps, low-rated branches)
- Designing or interpreting A/B tests or pilot programs
- Reviewing year-over-year performance changes
- Hiring or promoting top performers
- Evaluating investment fund performance
- Analyzing acquisition outcomes
- Building or critiquing causal claims about training, coaching, or feedback
- Judging whether an AI startup's viral quarter, a fund's AI hot streak, or a model's benchmark spike is a durable trend or an outlier reverting toward average (AI hype extrapolation)
- Someone says "regression to the mean," "things will average out," "they always come back"

**Not when:** the measurement is noise-free (rare in business); the underlying signal is genuinely changing (e.g., the business model fundamentally improved); the intervention is so substantial that no plausible regression can explain the effect.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user brings a specific performance change → run The Process directly.
- **Coach mode:** user is new to the framework → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **One-line:** when an extreme performance is followed by a less-extreme one, regression to the mean is the default explanation — not the intervention.
2. **Check fit.** Did we observe an extreme value followed by retest? If yes, regression applies.
3. **Elicit the structure.** What was the extreme observation? What was the follow-up? What intervention happened in between? Is there a control or baseline?
> **[WAIT — do not advance until user responds]**
4. **One question at a time:** how much regression would we expect without the intervention? Does the observed change exceed it? What's the noise level in the measurement?
> **[WAIT — do not advance until user responds]**
5. **Close:** regression vs. causal effect separated + control or baseline identified + claim calibrated.
> **[WAIT — do not advance until user responds]**

## The Process

**1. Identify the extreme observation** — value, subject, how extreme, any intervention.
**2. Identify the retest** — follow-up measurement, period, direction (toward mean?).
**3. Estimate expected regression** — noise level, historical variance; formula: `regression ≈ (1 − reliability) × distance from mean`.
**4. Compare to control** — untreated extreme performers; intervention effect = treatment change − control change. Without control, regression cannot be ruled out.
**5. Calibrate causal claim** — did the change exceed the regression baseline? By how much? Confidence?
**6. Adjust action** — credit/blame intervention only if it exceeds regression; recommend control structure for future tests.

## Output: Regression Analysis

```markdown
# Regression Analysis: <observed change>
Extreme observation — Subject: | Value: | Period:
Intervention — What: | When: | By whom:
Retest — Follow-up value: | Toward mean (Y/N): | Magnitude:
Expected regression — Noise level: | Predicted magnitude:
Control — Group: | Change: | Intervention effect = treatment − control:
Causal calibration — % regression: | % intervention: | Confidence:
Adjusted action — Credit/blame verdict + future evaluation process:
```

*→ Method in Action: [Galton 1886 + Kahneman 2011 Chapter 17 Israeli Air Force](examples/galton-1886-kahneman-2011-israeli-air-force.md)*
*→ 2026 lens: [The AI Hot Streak — viral quarters, fund streaks & benchmark spikes (2023–2026)](examples/ai-hot-streak-benchmark-spike-2023-2026.md)*

## Pack: Regression Across Domains

| Domain | Extreme obs. | Regression artifact | Discipline |
|---|---|---|---|
| Sales | Top/worst quarter | Regresses next quarter | 4-quarter averages + control |
| Athlete | Breakout season | Sophomore slump | Multi-season average |
| Stock fund | Hot year | Underperforms next year | 5-year track record |
| Customer sat. | Low quarter | Improvement next quarter | Control group |
| Manager intervention | Struggling team improves | Mostly regression | Compare untreated peer |

## Applying It Well

- Use longer time windows to reduce noise (yearly vs. quarterly)
- Always ask: "what would regression alone predict?" before crediting an intervention
- Control groups are not optional when evaluating interventions on extreme performers
- "Praise hurts, punishment helps" is the signature cognitive error of regression blindness

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "The bonus motivated her / criticism got through to him" | Exceptional quarter → regresses; bad quarter → improves. Both are regression, not intervention effect. |
| [D] "Our turnaround plan / new CEO is working" | Trough is partly noise. Compare to untreated peers before crediting the plan or leader. |
| [D] "This pilot is working on our struggling teams" | Extreme performers are the worst pilot group — regression is the null. Use a control. |
| [D] "Star performers will keep starring / sophomore slump is real" | Single-period peaks include noise; regression is the default on retest, not a slump. |
| [D] "After we fired him the team improved" | Could be regression. Disentangle by comparing to teams with no change. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- An intervention is being evaluated on extreme performers without a control group
- A single-period change is being treated as evidence of a stable trend
- Causal credit/blame is being assigned to interventions that coincided with regression
- "The intervention worked" claims lack baseline regression estimates
- Promotion / firing decisions are based on single-period extreme performance
- "Comeback" narratives credit decisive action, not regression

## Verification

- [ ] Extreme observation identified; retest compared to it
- [ ] Noise level and regression magnitude estimated
- [ ] Control group (or baseline regression expectation) used
- [ ] Causal effect separated from regression; claim calibrated
- [ ] Long-window measurements used where possible; future evaluation process set

*→ Primary sources: [references/sources.md](references/sources.md)*

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/regression-to-the-mean** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/regression-to-the-mean.json*
