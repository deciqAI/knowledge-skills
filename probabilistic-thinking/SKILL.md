---
name: probabilistic-thinking
description: "Activate when: user says 'what are the odds,' 'base rate,' 'Bayesian update,' 'calibration,' or 'what's the probability'; user is making a forecast or estimating a conversion/close/hire/outcome probability; someone claims 'I'm 90% sure' without any evidence grounding; a vivid story is being used in place of a prior frequency; team is treating an uncertain outcome as binary will/won't.
  Do NOT activate when: the problem has a deterministic answer from its inputs (math, well-defined engineering); the question is about identity, ethics, or meaning rather than fact."
---

# Probabilistic Thinking

## Overview

Most reasoning is binary: *will it happen, or won't it?* That framing discards the most useful information — the **degree** of confidence — and produces predictions that cannot be checked, updated, or scored. Probabilistic thinking replaces binary with **calibrated probability estimates**: numbers anchored in base rates, updated with evidence, and scored after the fact. Rooted in Bayes (1763), Knight's risk-vs-uncertainty distinction (1921), and Tetlock's empirical work showing calibration is a trainable skill.

Composable neighbors: [first-principles](../first-principles/SKILL.md) · [occams-razor](../occams-razor/SKILL.md) · [second-order-thinking](../second-order-thinking/SKILL.md) · [inversion](../inversion/SKILL.md) · [regret-minimization](../regret-minimization/SKILL.md) · [expected-value-and-kelly](../expected-value-and-kelly/SKILL.md). This skill is the *upstream input* the others depend on — the probability estimate here feeds EV-Kelly, calibrates inversion's failure-path weights, and gives second-order's hops their confidence decay.

## When to Use

Use when reasoning about an uncertain outcome (forecast, diagnosis, pipeline conversion, hire, deal close, geopolitical event); when binary "will/won't" predictions are being made; when a vivid story is replacing a base rate; when "I'm 90% sure" appears with no calibration evidence.

**When NOT to use:** deterministic problems (math, well-defined engineering); pure Knightian uncertainty with no usable base rate (give a range + humility statement instead); decision is robust across all likely probabilities; question is identity/ethics/meaning (→ [regret-minimization](../regret-minimization/SKILL.md)).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete forecasting question → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What-it-is.** Probabilistic thinking replaces "will it happen or not" with a number (0–1) anchored in base rates, updated with evidence, and scored after the fact.
2. **Check fit.** Match against *When to Use / When NOT to use*. Redirect if deterministic or pure Knightian.
3. **Elicit their real question.** "Odds of success" is vague; "probability customer X signs by Q3 given yesterday's call" is a question.
> **[WAIT — do not advance until user responds]**
4. **Walk The Process one step per turn.** Base rate first, then evidence, then update *with* them.
> **[WAIT — do not advance until user responds]**
5. **Close.** State the probability number and the one piece of evidence that would move it most.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Probability Estimate**. Base rate first, then evidence, then update, then calibration check.

1. **Precise question + deadline.** "Will the deal close?" → "Will customer X sign ≥$50K by 2026-09-30?"
2. **Anchor in a base rate.** Historical fraction of similar situations. No base rate = Knightian territory → report range, not point.
3. **Evidence for and against.** Each signal moves estimate ↑ or ↓. Be uncharitable about both sides.
4. **Bayesian update (plain language).** For each signal: P(evidence | outcome happens) vs P(evidence | doesn't happen). The ratio drives the shift.
5. **Number + confidence interval.** Not "70-ish" — "68%, 80% CI 55–80%."
6. **Most-informative next evidence.** If nothing would move your estimate, you have a belief, not an estimate.
7. **Calibration log.** Record estimate, date, resolution criteria. Score after: did 70%-calls land 70% of the time?

### Output: the Probability Estimate

```
Question (precise): <outcome, deadline>
Base rate: <reference class> → <fraction> (source, n=)
Evidence: <signal> ↑/↓ strong/moderate/weak  [repeat per signal]
Bayesian shift: net <↑/↓ to X%> — rationale in one paragraph
Estimate: <point %>  |  80% CI: <%–%>  |  Knightian caveat if needed
Next evidence: <observable> → <% if X> / <% if Y>
Calibration log: date | question | resolution criteria | Brier score after
```

*→ Method in Action: [Tetlock, IARPA, and the Good Judgment Project (2011–2015)](examples/tetlock-iarpa-good-judgment-project-2011-2015.md)*

## Calibration Packs

| Domain | Base rate source | Classic failure |
|---|---|---|
| Medical | Disease prevalence in population | Base-rate neglect → false positives |
| Sales | Conversion-by-stage history | Anchoring on preferred deal |
| Legal | Crime/suspect-pool frequencies | Prosecutor's fallacy |
| Product/startup | Cohort retention, vintage distributions | Survivorship bias |

## Applying It Well

- **Base rate first.** A story without a base rate is fiction with a number attached.
- **Incremental updates.** Superforecasters update *more often* but *less drastically* than amateurs.
- **Risk ≠ uncertainty (Knight 1921).** For Knightian situations give a range + humility statement, not false precision.
- **Name what would change your mind.** If nothing would move your estimate, you have a position, not an estimate.
- **Score yourself.** Write forecasts down and check them — calibration is trainable only this way.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] **Base-rate neglect** | Reaching for a vivid story while ignoring the prior frequency of the outcome class. *Always anchor in a base rate first; updates come from there.* |
| [D] Confusing **P(evidence \| outcome)** with **P(outcome \| evidence)** (prosecutor's fallacy) | A test triggering on 99% of cases of a rare disease will, in a low-prevalence population, produce mostly false positives. Bayes' theorem connects them; they are not interchangeable. |
| [D] Treating "very likely" as a **binary** | "I'm 90% sure" with no calibration history and no number for "what would make it 50%" is a vibe, not an estimate. |
| [D] Confusing **risk** with **uncertainty** (Knight 1921) | An actuarial-table problem and a geopolitical-forecasting problem differ in kind. Inventing a precise number for genuine Knightian uncertainty manufactures false confidence. |
| [D] **One-shot probability fallacy** | "The probability of *this* event is X" implicitly invokes a reference class. Name it; otherwise the probability is undefined. |
| [D] **Survivorship bias** in base-rate construction | Reasoning from winners without including losers gives an inflated base rate. The reference class must include the failures. |
| [D] **Anchoring** on the first number that appears | Even random numbers shift estimates (Tversky & Kahneman 1974). Notice when you are anchoring on the latest news rather than the base rate. |
| [D] **Under-updating** on strong evidence | Stubbornly holding the prior when new information is high-quality. Bayes says update; ignoring evidence is anti-Bayesian. |
| [D] **Over-updating** on weak evidence | Letting noisy or single-source data dominate. Superforecasters' edge is *smaller* updates more often, not bigger ones. |
| [D] **Pseudo-precision** | "73.2% probability" when inputs justify nothing tighter than "60–80%." Match precision to evidence strength. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Point estimate with no base rate · "high probability" with no number · no evidence named that would change the estimate · single story doing all the work · reference class silently chosen to favor a conclusion · Knightian situation with no humility statement · same person makes many forecasts but has never scored them

## Verification

- [ ] The question is stated with a specific outcome and a deadline
- [ ] A base rate is named with an explicit reference class and a source
- [ ] Evidence is listed in both directions, with direction and strength tags
- [ ] The Bayesian shift from base rate is explained in one paragraph
- [ ] The point estimate is a number, with an 80% confidence range
- [ ] The single most-informative next piece of evidence is named
- [ ] The estimate is recorded with date and unambiguous resolution criteria for later scoring

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/probabilistic-thinking?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=probabilistic-thinking** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
