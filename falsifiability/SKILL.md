---
name: falsifiability
description: "Activate when: user says 'what would prove this wrong', 'how do we know if our strategy is working', 'what would change your mind', 'this claim feels unfalsifiable', or is designing a hypothesis/experiment/investment thesis that needs to be made testable.
  Do NOT activate when: the claim is genuinely non-empirical (ethical, aesthetic, philosophical); or the cost of running the test exceeds the value of the knowledge."
---

# Falsifiability

## Overview

A meaningful empirical claim must specify what observations would refute it. Claims that resist all possible refutation are not science — they are unfalsifiable belief. Formalized by Karl Popper (1934): science progresses not by accumulating confirmations but by surviving rigorous attempts at falsification. More-specific claims are more falsifiable; ad-hoc modifications that explain away failures destroy a claim's scientific status.

Composes with [`confirmation-bias`](../confirmation-bias/SKILL.md) (falsifiability is the structural counter), [`abductive-reasoning`](../abductive-reasoning/SKILL.md) (generates hypotheses; this skill tests them), [`bayesian-reasoning`](../bayesian-reasoning/SKILL.md), [`critical-thinking`](../critical-thinking/SKILL.md).

## When to Use

- Designing OKRs, KPIs, or strategic goals; writing or evaluating investment theses
- Designing experiments (A/B tests, product hypotheses, market entry)
- Evaluating consultant/advisor recommendations or diagnosing vague leadership claims
- Someone says "what would change your mind," "how would you know you're wrong," "Popper"

**Not when:** genuinely non-empirical (philosophical, ethical, aesthetic); test cost exceeds its value.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a specific claim → run The Process directly.
- **Coach mode:** user is new → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: before acting on a claim, ask what observation would refute it — if "nothing would," it's belief, not knowledge.
2. Check fit: if the claim is genuinely metaphysical (ethical, aesthetic), falsifiability doesn't apply.
3. Elicit the claim and its current evidential basis.
> **[WAIT — do not advance until user responds]**
4. Ask: what specific observation would falsify this? When and how would you observe it?
> **[WAIT — do not advance until user responds]**
5. Close: falsifiability conditions specified + monitoring plan + commitment to act on disconfirming evidence.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — State the claim:** claim / who asserts it / decision dependent on it / current evidential basis.

**Step 2 — Test whether empirical:** claim about how the world works (empirical) or values/aesthetics (non-empirical)? If non-empirical, stop here.

**Step 3 — Specify falsification conditions:** complete "This claim would be falsified if I observed: ___" — specific, observable, time-bounded. If you cannot complete it, the claim is not falsifiable as stated.

**Step 4 — Plan to observe:** when is the observation possible / how measured / who tracks it / threshold for "falsified."

**Step 5 — Pre-commit to action:** if the falsifying observation occurs, what will you do? Is any theory modification itself falsifiable?

**Step 6 — Iterate:** confirmed → keep monitoring; falsified → revise/abandon; unfalsifiable → recognize as belief.

## Output Template

```markdown
# Falsifiability Analysis: <claim>
Claim: | Asserted by: | Decision at stake: | Current basis:
Empirical: Y/N | Observation type:
Falsified if: | Threshold: | Observable when/how: | Owner:
If falsified, action: | Ad-hoc preservation risk:
```

*→ Method in Action: [Popper 1934 + Eddington 1919 Eclipse + Modern Applications](examples/popper-1934-eddington-1919-eclipse-modern-applications.md)*

## Pack: Vague → Falsifiable

| Vague (unfalsifiable) | Falsifiable form |
|---|---|
| "We have PMF" | "≥40% of users would be 'very disappointed' without the product" |
| "Our outbound is working" | "5% of cold emails convert to qualified opps within 30 days" |
| "Our culture is strong" | "Employee NPS ≥40 in next quarterly survey" |
| "This stock is undervalued" | "Stock <12 P/E within 12 months; otherwise thesis is wrong" |
| "Users want feature X" | "≥30% complete the new flow within 14 days of launch" |

## Applying It Well

- Specify falsifiability conditions *before* the observation window opens — post-result conditions are rationalization.
- More specific = more falsifiable. Quantify wherever possible.
- When a prediction fails, ask: is the modification of your theory itself falsifiable?
- Apply to others: "What would change your mind?" is the highest-leverage critical-thinking question.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "I just have a strong gut feeling" | Gut feelings are not falsifiable. Without a test, you can't tell right from wrong. |
| [D] "We need more data to decide" | If you can't specify what data would change your mind, you're not doing data-driven analysis. |
| [D] "The strategy just needs more time" | Specify the timeframe and metrics in advance. |
| [D] "It's because of external factors" | If external factors can always be invoked, the original claim was unfalsifiable. |
| [D] "It's too early to evaluate" | If you can't specify when evaluation is appropriate, the claim is unfalsifiable. |
| [D] "We're in a special situation" | This defense converts a falsifiable claim into an unfalsifiable one. Resist. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Claim asserted without specifying what would refute it
- "The strategy is working" without metrics or thresholds
- Predictions modified ad-hoc to accommodate failures
- "External factors" invoked to explain disconfirming evidence
- Person cannot specify what would change their mind

## Verification

- [ ] Claim specifically stated; empirical vs. non-empirical determined
- [ ] Specific, observable, time-bounded falsification conditions defined
- [ ] Monitoring mechanism in place with a named owner
- [ ] Advance commitment to act on falsification made
- [ ] Risk of ad-hoc preservation recognized

---

*Part of **deciqAI Knowledge Skills** — 189 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/falsifiability** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
