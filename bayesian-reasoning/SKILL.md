---
name: bayesian-reasoning
description: "Activate when: user says 'Bayesian', 'prior', 'posterior', 'base rate', 'likelihood ratio', or 'update my belief'; someone treats 'the evidence is consistent with X' as proof of X; a high-stakes decision rests on interpreting a test result, security alert, fraud flag, A/B result, or hiring signal; base rates are being ignored in favor of a vivid story. Do NOT activate when: the decision is genuinely deterministic and probabilities do not apply; there is no data or domain knowledge to anchor a prior (Bayes amplifies information, it does not create it from nothing)."
---

# Bayesian Reasoning

## Overview

Bayes' theorem: **Posterior odds = Prior odds × Likelihood ratio**. The strength of belief after evidence equals the strength before, multiplied by how diagnostic the evidence is.

This skill applies Bayesian discipline where people reason about probabilities informally — and failures follow predictable patterns: ignoring the base rate (prior), confusing P(E|H) with P(H|E) (prosecutor's fallacy), over-updating on vivid confirming evidence, treating correlated evidence as independent.

Composes with [`probabilistic-thinking`](../probabilistic-thinking/SKILL.md) (Bayes is the operational engine), [`critical-thinking`](../critical-thinking/SKILL.md) (formalizes considering alternatives), [`logical-fallacies`](../logical-fallacies/SKILL.md) (prosecutor's fallacy and base-rate neglect), and [`first-principles`](../first-principles/SKILL.md) (the prior is bedrock).

## When to Use

- High-stakes decision rests on interpreting evidence (medical test, security alert, fraud flag, hiring signal, A/B result)
- "Evidence is consistent with X" is being treated as proof of X
- Base rates ignored — a rare event treated as probable because evidence "looks like" it
- Correlated evidence pieces treated as independent updates
- A benchmark score, AI-capability claim, AI-adoption stat, or AI-capex/valuation figure is being treated as proof without asking how often that signal appears when the underlying claim is false
- Someone says "Bayesian," "prior," "posterior," "base rate," "likelihood ratio," "update"

**Not when:** genuinely deterministic; no data to anchor a prior; cost of formal update exceeds the value of being more right.

## Coaching Novices (Adaptive Front Door)

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output that step's question and nothing more.

1. **One-line:** before believing what the evidence says, ask how common this situation is to start with (prior) and how often evidence would look this way even if the hypothesis is wrong.
2. **Check fit.** Deterministic problems / no prior anchor → not this lens.
3. **Elicit the real claim and the evidence.** What exactly are you deciding, and what evidence do you have?

> **[WAIT — do not advance until user responds]**

4. **One question at a time:** what's the base rate? what would evidence look like if the hypothesis were *false*? how much should that change your belief?

> **[WAIT — do not advance until user responds]**

5. **Close:** specific posterior probability, plus what next evidence would change it most.

> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Name hypothesis and alternatives.** H vs. not-H must be exhaustive.

**Step 2 — Anchor the prior *before* evidence.** P(H) = base rate in the relevant population. Most failures happen here. Examples: disease prevalence (<0.1% for rare conditions); historical fraction of great hires (20-40%); alerts that proved real (<5%); Series A → $1B outcomes (~5%).

**Step 3 — Estimate the likelihood ratio.** LR = P(E|H) / P(E|not-H). LR > 1 supports H; LR < 1 supports not-H; LR ≈ 1 is non-diagnostic. If you cannot articulate P(E|not-H), you have half the story.

**Step 4 — Compute the posterior.** Prior odds × LR = Posterior odds → convert back to probability. Example: 0.1% prevalence, LR = 99 → posterior ≈ 9%. A "highly accurate" test on a rare disease still gives 91% chance of no disease on a positive result.

**Step 5 — Check evidence dependence.** Correlated evidence (three witnesses from the same source) should be treated as ~one piece, not compounded.

**Step 6 — Commit and act.** State the posterior number, the action threshold, and what next evidence would most move it.

## Output: Bayesian Update

```
# Bayesian Update: <decision>
H / not-H:
Prior P(H):          Source:
Evidence E:
P(E|H):              P(E|not-H):          LR:
Posterior P(H|E):    Interpretation:
Independence check:
Decision threshold:  Action:  Next evidence:
```

*→ Method in Action: [Sally Clark Case (1999)](examples/sally-clark-1999.md) · [Air France 447 Search (2009–2011)](examples/air-france-447-search.md)*
*→ 2026 lens: [Updating Beliefs About AI Capability and Safety From Eval Results (2023–2026)](examples/ai-capability-safety-belief-updating-2023-2026.md)*

---

## Pack: Common Bayesian Settings

A "pack" bundles the most common prior and LR patterns for a domain.

| Setting | Common prior | Common LR failure |
|---|---|---|
| Medical screening | Population prevalence | Treating sensitivity as posterior |
| Security alert triage | Fraction of alerts that were real | "Matches signature" = "is the threat" |
| Hiring | Historical fraction of great hires in this role | One strong interview = "great candidate" |
| A/B test | Prior probability the change has a real effect | "p < 0.05" without prior |

*Contribute a pack for your domain — see the template at the repo root.*

*→ Sources: [references/sources.md](references/sources.md)*
## Common Rationalizations

**Note — [D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "This looks just like X" | Not enough. How often does it look like X when it isn't? Without LR, you have rhetoric. |
| [D] Ignoring base rate because "this case feels different" | The base rate captures everything you don't know. "Feels different" is already included. |
| [D] Confusing P(E\|H) with P(H\|E) | The prosecutor's fallacy. They can differ by orders of magnitude. |
| [D] Treating correlated evidence as independent | Multiplying correlated likelihoods overstates the update. Identify common causes. |
| [D] Updating intuitively without numbers | Intuitive updates are miscalibrated — too strong on confirming, too weak on disconfirming. |
| [D] Picking the prior after seeing the evidence | Hindsight contamination. Commit to the prior before evidence. |
| [D] "I'm doing a Bayesian update" without naming P(H), P(E\|H), P(E\|not-H) | Then you are not. You are using the word. |
| [D] Absence of evidence = evidence of absence | Depends on P(E\|H) and P(E\|not-H). If evidence is rarely observable, absence is weak. |
| [D] Posterior keeps drifting toward H every round without calibration check | Either H is increasingly likely or there is a confirmation-bias leak. |
| *To add [O] entries: paste a real failure instance here after each production use* | *Description of what happened* |

## Red Flags

- Prior never named · "Consistent with X" treated as proof of X · Sensitivity without false-positive rate · Correlated evidence summed as independent · Posterior matches vivid story not math · "Highly likely" without a number · Prior chosen after evidence · "Bayesian" invoked without an actual update

## Verification

- [ ] Hypothesis and alternatives explicitly named and exhaustive
- [ ] Prior named with a number and source, before evidence is examined
- [ ] P(E|H) AND P(E|not-H) both estimated · Likelihood ratio computed
- [ ] Posterior computed numerically · Independence of evidence pieces checked
- [ ] Decision threshold and action stated · Next evidence identified

---

*Part of **deciqAI Knowledge Skills** — 223 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/bayesian-reasoning** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
