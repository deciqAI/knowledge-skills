---
name: ai-pilot-to-scale
description: "Activate when: user says 'our AI pilot is done but nobody uses it', 'the demo was great, how do we roll it out?', 'how do we get this POC into daily operations?', 'should we scale or kill this pilot?', 'the pilot keeps getting extended', or is about to launch an AI/agent pilot.
  Do NOT activate when: still deciding whether to build, buy or partner for the capability (use build-buy-partner-ai); deciding whether the project is worth funding at all (use ai-roi-business-case); pure model selection or prompt/parameter tuning; an explicitly labeled learning experiment with no commitment to go live. More: deciqai.com/s/ai-pilot-to-scale"
---

# AI Pilot to Scale


## Overview

Most AI pilots do not fail on the model. They fail on the organization: the tool sits outside the systems people already use, nobody on the business side owns the result, and the success metric is chosen after the fact — so any outcome can be narrated as progress and the pilot is extended indefinitely. That state has a name: **pilot purgatory**. Gartner predicted in July 2024 that at least 30% of generative AI projects would be abandoned after proof of concept by the end of 2025, citing poor data quality, inadequate risk controls, escalating costs or unclear business value.

The core mechanism: **before the pilot starts, lock a narrow workflow, a measured baseline, written success and kill criteria, a business owner, and a scale/kill date** — then decide on that date against what was written, not against what the demo felt like.

This is the same discipline Google's *Rules of Machine Learning* opens with ("First, design and implement metrics") and Anthropic's agent guidance states for autonomy ("finding the simplest solution possible, and only increasing complexity when needed"): measure first, earn autonomy in stages.

Compose with: [agent-delegability-assessment](../agent-delegability-assessment/SKILL.md) (staged delegation of autonomy) · [theory-of-constraints](../theory-of-constraints/SKILL.md) (pick the bottleneck workflow as the pilot target) · [premortem](../premortem/SKILL.md) (stress-test before scaling) · [kotter-change](../kotter-change/SKILL.md) (adoption is a change program) · [ai-roi-business-case](../ai-roi-business-case/SKILL.md) (the money case behind the scale decision) · [build-buy-partner-ai](../build-buy-partner-ai/SKILL.md) (the sourcing decision that precedes the pilot).

## When to Use

- Before starting any AI or agent pilot
- A pilot has run past ~8 weeks with no scale/kill verdict
- The demo was praised, but frontline staff have not changed how they work
- Leadership asks "should we roll this out company-wide?"

**When NOT to use:** pure learning exploration, explicitly labeled and not promised to go live · no solution chosen yet (use [build-buy-partner-ai](../build-buy-partner-ai/SKILL.md)) · the workflow itself is being retired.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete pilot → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What it is.** "Before the pilot starts, write down what success looks like, who owns it, and the date you decide to scale or kill."
2. **Check fit.** "Does this pilot have a specific business workflow and a business owner?"
3. **Elicit the real case.** "Name the workflow, how it's done today, its weekly volume, and the number you want to improve."
> **[WAIT — do not advance until user responds]**
4. **Run The Process.** Measure the baseline together and write the success and kill criteria.
> **[WAIT — do not advance until user responds]**
5. **Name the insight.** The user states the scale/kill date and the number that decides it.
> **[WAIT — do not advance until user responds]**

## The Process

**Output:** Pilot Charter + Scale/Kill Decision Record

1. **Pick one narrow workflow.** One workflow, one team, high frequency, value measurable — prefer the bottleneck. *Gate: scope spans more than 2 departments → narrow it.*
2. **Measure the baseline.** At least 2 weeks of real data: cycle time, cost, error rate, throughput. *Gate: no baseline → do not launch.*
3. **Write success criteria in advance.** Hard numbers and a date — e.g. "handling time down 40%, error rate not up, verdict at week 8." Write the kill conditions at the same time. *Gate: the business owner signs the criteria; they cannot be changed after launch.*
4. **Name the owner.** One business owner (not IT, not the vendor) is accountable for the result and has authority to change the workflow.
5. **Integrate into existing systems.** Run it inside the tools people already use (CRM, inbox, ticketing), not in a new window. *Gate: staff must copy-paste between tools → build the integration first.*
6. **Grant autonomy in stages.** L1 suggest → L2 approve-then-act → L3 act-then-report. Each step up requires hitting a pre-set error threshold.
7. **Decide on the date.** Against the written criteria, pick one: **Scale** (replicate to an adjacent workflow/team) · **Revise** (allowed once, time-boxed) · **Kill** (record why).
8. **Stop-rule:** criteria missed at the deadline and no concrete fix identified → kill; move the resources to the next workflow.

**Output template:**
`Workflow | Baseline (time/cost/error) | Success criteria + kill conditions | Owner | Integration point | Autonomy stage + threshold | Decision date | Verdict (scale/revise/kill) + evidence`

*→ Method in Action: [Generative AI at Work — a staggered support-desk rollout (2020–2021)](examples/generative-ai-at-work-support-rollout-2020-2021.md)*

## Applying It Well

1. **Criteria before technology.** Sign the success criteria first, then pick the model.
2. **Usage is the first signal.** If the frontline does not use it, do not scale it, however good the dashboard looks.
3. **"Revise" is granted once.** Repeated extensions are the entrance to purgatory.
4. **Scale to the adjacent workflow, not the whole company.** Each replication is a new narrow pilot with its own baseline.
5. **Look for uneven effects.** An average gain can hide a segment where the tool makes work worse; check before widening scope.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Let's get it running and define metrics later" | Metrics chosen after the fact can always be read as success — that is having no standard. |
| [D] "One more month and it'll be there" | An extension without a new fix only postpones the kill. |
| [D] "IT owns it" | The result lands on the business side, so the owner must sit on the business side. |
| [D] "The demo was great — roll it out company-wide" | Scaling before a narrow workflow is proven multiplies the failure surface. |
| [D] "People will learn to use the new tool" | A separate window with copy-paste is friction that adoption numbers will expose; integrate first. |
| [D] "It's only suggesting, so we can skip the error threshold" | The threshold is what earns the next autonomy stage; without it, promotion is a guess. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- No baseline · no decision date · owner is IT or the vendor · staff copy-paste into a new window · pilot past its deadline with no verdict · success criteria edited after launch

## Verification

- [ ] Baseline is ≥ 2 weeks of real data, not estimates
- [ ] Success criteria and kill conditions signed by the business owner before launch
- [ ] Tool runs inside existing systems
- [ ] Autonomy stage and its promotion threshold written down
- [ ] Verdict (scale/revise/kill) issued on the date and archived with evidence

---

*Part of **deciqAI Knowledge Skills** — 253 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/ai-pilot-to-scale** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/ai-pilot-to-scale.json*
