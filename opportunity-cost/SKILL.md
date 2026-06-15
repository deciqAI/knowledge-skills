---
name: opportunity-cost
description: >
  Activate when: user says "what could we have done instead," "what's the next-best alternative," "is this worth the cost," "what are we giving up by choosing X," "broken window fallacy," or is allocating scarce resources (money, time, attention, people) across competing options.
  Do NOT activate when: all alternatives are genuinely zero-value (nothing else to do with the resource); the decision is fully reversible at near-zero cost.
---

# Opportunity Cost

## Overview

**Opportunity cost** is the true cost of any choice: the value of the *next-best alternative* you give up. Accounting cost is what you pay; opportunity cost is what you forego. The two diverge whenever resources are scarce — which is always.

Bastiat (1850) established the foundational insight: every visible benefit forecloses an invisible alternative. Buchanan (1969) formalized it: cost is subjective, prospective, decision-maker-specific — the accountant's number and the economist's number can diverge by 10x.

Composes with `expected-value-and-kelly`, [`first-principles`](../first-principles/SKILL.md), [`pareto-principle`](../pareto-principle/SKILL.md), [`sunk-cost-fallacy`](../sunk-cost-fallacy/SKILL.md), [`compound-interest`](../compound-interest/SKILL.md).

## When to Use

- Allocating budget, headcount, or founder-time across competing options
- Evaluating an investment vs. holding cash (or vs. another investment)
- Considering a "free" benefit whose hidden cost is time/attention
- Any "this is good for X" claim that ignores the alternative use of the same resources

**Not when:** alternatives are genuinely zero-value; resources are not scarce; decision is reversible at near-zero cost.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete resource-allocation decision → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: before committing resources to X, ask what *next-best alternative* you're giving up — that foregone value is the true cost.
2. Check fit: if alternatives are genuinely zero-value, OC adds no information. Otherwise: apply.
3. Elicit the choice and the resources being committed.
> **[WAIT — do not advance until user responds]**
4. Work through 3-5 realistic alternatives and estimate the value of the best one.
> **[WAIT — do not advance until user responds]**
5. Close: decision named with OC explicit + non-financial OCs surfaced + "would I choose this if I treated the OC as a real expense?"
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1** — State choice + resources committed (what, how much money/time/headcount, timeframe).
**Step 2** — List 3-5 realistic alternatives including "do nothing / hold the resource."
**Step 3** — Estimate value per alternative (financial + non-financial; ranges fine).
**Step 4** — Identify OC = value of the highest-ranked *unchosen* alternative (not average, not worst).
**Step 5** — Compare: Net benefit = Value of chosen − OC. Negative = destroys value vs. the alternative.
**Step 6** — Surface non-financial OCs: time, attention, headcount, reputation, optionality. These often dominate cash.

## Output: Opportunity-Cost Analysis

```markdown
# Opportunity-Cost Analysis: <choice>
Choice: | Resources: | Timeframe:
| # | Alternative | Expected value | Confidence |
|---|---|---|---|
| Chosen X | | | |
| A–C | | | |
OC = next-best: <name> / value: <amount>
Net benefit = Value of chosen − OC: <amount> · Verdict: proceed / reconsider
Non-financial OCs: Time | Attention | Headcount | Reputation | Optionality
Decision + reasoning:
```

*→ Method in Action: [Bastiat's Broken Window, 1850](examples/bastiats-broken-window-1850.md)*

## Pack: Opportunity-Cost Application Patterns

| Domain | Visible cost | Hidden OC |
|---|---|---|
| Marketing budget | Cash spent | Engineering hires; runway extension |
| Founder calendar | $0 | Deep-work hours foregone |
| Custom dev for one customer | Dev hours | Roadmap distortion; founder distraction |
| Acquiring vs. building | Acquisition price | Roadmap capacity during integration |

## Applying It Well

- Surface alternatives *before* evaluating — most decisions skip this step.
- Non-financial OCs (time, attention) usually dominate cash; don't stop at dollars.
- A rough OC estimate beats no OC reasoning — specificity over precision.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "It only costs $X" | Cost is not $X — it's the value of the next-best alternative use of $X. |
| [D] "It's free — no downside" | Free in cash is almost never free in attention, time, or signal. |
| [D] "We've budgeted for it" | Budgeting accounts for cash flow, not opportunity cost. |
| [D] "We won't have lost much if it fails" | You lose the OC of what else you would have done — often large. |
| [D] "The other option wasn't realistic" | Then list 3-5 realistic ones. If none exist, OC is zero (rare). |
| [D] "It's just $50/month" | At 7% compound over 25 years, $50/month becomes ~$40k. Recurring costs have compound OCs. |
| [D] "It's my time, not money" | Founder time has the highest OC in the company. |
| [D] "We can't measure the alternative" | Estimate. Rough OC reasoning beats none. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Decision justified by visible benefit only; no alternatives listed
- "Do nothing" not in the alternatives list; non-financial costs absent
- Decision-maker cannot articulate what else would have been done with the resources

## Verification

- [ ] 3-5 realistic alternatives listed; "do nothing" included
- [ ] Each alternative has an estimated value (financial + non-financial)
- [ ] Next-best alternative identified specifically (not average, not worst)
- [ ] Chosen value compared to OC, not to zero; non-financial OCs surfaced
- [ ] If recurring cost, compound OC over long horizon computed

---

*Part of **deciqAI Knowledge Skills** — open-source thinking skills that make rigor executable for AI agents. These 25 skills are a free taste of the 160+ skills wired into every deciqAI agent, which runs them autonomously to operate your company. **Try it free → https://www.deciqai.com/skills?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=opportunity-cost** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
