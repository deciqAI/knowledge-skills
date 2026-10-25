---
name: ai-roi-business-case
description: "Activate when: user says 'is this AI project worth doing?', 'calculate the ROI of AI', 'how long until this agent pays back?', 'build the AI business case for my boss/investors', 'what does this AI tool really cost us?', or is about to pay for an AI tool/agent or replace a manual workflow with one.
  Do NOT activate when: exploratory personal use with negligible cost; the system is already live and only needs an operating review (use agent-ops-monitoring); the pilot is funded and the question is how to run it to a scale/kill verdict (use ai-pilot-to-scale); the question is general CAC/LTV unit economics, not an AI project (use unit-economics-cac-ltv-payback). More: deciqai.com/s/ai-roi-business-case"
---

# AI ROI Business Case


## Overview

AI business cases are usually inflated the same three ways: they count only "hours saved," they omit the costs that arrive after the subscription (inference, integration, human review, change management), and they assume full adoption on day one. The result is an ROI that looks decisive on the slide and never shows up in the P&L — and, with no pre-agreed kill line, sunk cost carries the project forward.

The core mechanism: **measure the baseline → count only value levers that can be realized → cost everything → discount by the adoption ramp → compute payback → run sensitivity → write the kill line before you start.** ROI = (realizable value − full cost) ÷ full cost, with value always measured against how the work is done *today*.

The NIST AI Risk Management Framework asks for the same thing in its MAP function: document the potential benefits (MAP 3.1) *and* the potential costs, "including non-monetary costs" (MAP 3.2), before deployment. This skill turns that into a one-page table.

Compose with: [unit-economics-cac-ltv-payback](../unit-economics-cac-ltv-payback/SKILL.md) (payback-period conventions) · [premortem](../premortem/SKILL.md) (imagine the failure before funding) · [margin-of-safety](../margin-of-safety/SKILL.md) (discount conservatively) · [sunk-cost-fallacy](../sunk-cost-fallacy/SKILL.md) (why the kill line is written upfront) · [ai-pilot-to-scale](../ai-pilot-to-scale/SKILL.md) (run the funded pilot to a verdict).

## When to Use

- Before buying an AI tool or agent; before using AI to replace or augment a manual workflow
- Asking a boss, partner or investor for AI budget
- A pilot has ended and the decision is scale or kill

**When NOT to use:** personal trials with negligible cost · no measurable workflow (pure creative exploration) · already live and only needs an operating review.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user gives a concrete workflow and numbers → run The Process directly.
- **Coach mode:** user is unfamiliar → one question per step. Each [WAIT] is a hard stop — output only that step's question.

1. **What it is.** "ROI = (value you can actually realize − full cost) ÷ full cost, and value is measured against how the work is done now."
2. **Check fit.** "Is someone doing this workflow today, and can you count how long it takes or how often it goes wrong?"
3. **Elicit the real case.** "Which workflow, who does it, how many times a month, how long each time?"
> **[WAIT — do not advance until user responds]**
4. **Run steps 1–3 together:** fill in the baseline and the full-cost list.
> **[WAIT — do not advance until user responds]**
5. **Name the insight.** Is payback still acceptable in the pessimistic case, and what is the kill line?
> **[WAIT — do not advance until user responds]**

## The Process

**Output:** one-page AI ROI table

1. **Measure the baseline.** Monthly volume, time per instance, fully loaded labor cost, error rate, cycle time — from timing or system records. *Gate: no baseline data → record 2–4 weeks first; stop.*
2. **Pick value levers.** Hours saved · incremental revenue · errors avoided · speed. For each, write the **realization path** (hire fewer, redeploy, take more volume). *Gate: freed time has nowhere to go (no cost cut, no extra output) → count it as zero.*
3. **Cost everything.** License/subscription · inference (estimate tokens/calls by volume) · integration build and maintenance · **human review time** · training and change management · vendor switching cost. *Gate: review time not counted → stop.*
4. **Apply the adoption ramp.** Set adoption by month (pilot → partial → full) and discount value by it. *Gate: 100% adoption in month 1 → redo.*
5. **Compute payback and ROI.** The month cumulative net cash flow turns positive; 12-month ROI.
6. **Run sensitivity.** Pessimistic / base / optimistic on at least adoption rate, inference unit price, and review share. *Gate: pessimistic payback exceeds the acceptable ceiling → shrink scope or don't do it.*
7. **Write the kill line.** In advance: "if metric Y is not met by month X → stop or downgrade," plus who decides.
8. **Stop-rule:** if the value rests mainly on unmeasurable "strategic importance," this method does not apply → run a small, option-style pilot instead.

**Output template:**
`Workflow | Baseline (volume/time/errors) | Lever + realization path | Monthly full cost | Adoption ramp | Payback (pess/base/opt) | 12-mo ROI | Kill line + decider`

*→ Method in Action: [Klarna's AI assistant — the $40M estimate and the quality reversal (2024–2025)](examples/klarna-ai-assistant-2024-2025.md)*

## Applying It Well

1. **Baselines are measured, not remembered.** "About 2 hours" gets timed 10 times first.
2. **Only realizable value counts.** Time saved that neither cuts cost nor raises output is worth zero.
3. **Human review is the most-missed AI cost.** Price it at the real spot-check rate, not the hoped-for one.
4. **Quality is a cost line, not a footnote.** If the AI path lowers quality, the lost revenue or rework belongs in the pessimistic case.
5. **The kill line is written at approval, never at the loss.**

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "AI is cheap, no need to model it in detail" | The subscription is cheap; integration, review and change management are not. |
| [D] "Staff will use the saved time for higher-value work" | No realization path means no value. Write down where the time goes. |
| [D] "Everyone will use it from launch" | Adoption ramps. Full adoption in month 1 is the most common source of inflated ROI. |
| [D] "Let's just start and see how it goes" | No pre-set kill line → sunk cost keeps it running. |
| [D] "One scenario is enough — the base case is realistic" | A single-scenario ROI hides which assumption the decision actually hinges on. |
| [D] "Cost per interaction is the metric" | Cost per interaction ignores whether the interaction resolved the customer's problem at the same quality. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- ROI shown in one scenario only · no human-review cost line · value column says "efficiency gains" with no number · no kill line or no named decider · adoption at 100% from month 1

## Verification

- [ ] Baseline comes from measurement or system records
- [ ] Every value lever has a realization path
- [ ] Full cost includes inference, integration, review and change management
- [ ] Adoption ramps by month
- [ ] Three-scenario sensitivity done
- [ ] Kill line, decider and review date written down

---

*Part of **deciqAI Knowledge Skills** — 253 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/ai-roi-business-case** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/ai-roi-business-case.json*
