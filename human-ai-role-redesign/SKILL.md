---
name: human-ai-role-redesign
description: "Activate when: user says 'what does this role do once the agent takes over?', 'how should KPIs change after AI goes live?', 'what new skills do our people need?', 'how do we tell the team about AI replacing work?', 'rewrite the job description for AI', or an agent has already taken over part of a role's tasks.
  Do NOT activate when: it has not yet been decided which tasks go to the agent (run a task-delegability assessment first); the question is purely a headcount-reduction cost calculation; the change itself needs leading across the organization (use kotter-change). More: deciqai.com/s/human-ai-role-redesign"
---

# Human–AI Role Redesign

## Overview

When an agent takes over part of a job, the job does not disappear — a bundle of tasks changes hands. If the role, KPIs, skills, and incentives stay as they were, the old scorecard keeps rewarding people for the work the agent now does. People then compete with the agent, route around it, or quietly rebuild the old process in the shadows.

Core mechanism: **a role is a set of tasks; once an agent takes some of them, rewrite the role, KPIs, skills, and incentives around the remaining tasks plus the new human duties.** The research base: technology substitutes for tasks, not whole occupations (Autor, Levy & Murnane 2003); generative AI lifts novices most (Brynjolfsson, Li & Raymond 2023: +14% average, +34% for novice and low-skilled agents); AI's capability frontier is jagged, and relying on it outside the frontier degrades quality (Dell'Acqua et al. 2023: subjects using AI on a task outside the frontier were 19% less likely to produce a correct solution).

The new human duties fall into four categories: **judgment** (decisions outside the agent's boundary) · **exception handling** · **relationships** · **supervising the agent**.

Compose with [okr-goal-setting](../okr-goal-setting/SKILL.md) (writing the new KPIs) · [incentive-design](../incentive-design/SKILL.md) (what the new scorecard actually rewards) · [kotter-change](../kotter-change/SKILL.md) (change communication).

## When to Use

- An agent has taken over ≥20% of a role's working hours
- Staff resist the agent, quietly bypass it, or output has not risen with the tooling
- Hiring plans need job descriptions rewritten for the current state of AI

**When NOT to use:** the delegation map (which tasks go to the agent) is not done · duties are defined by regulation · the agent is still in a one-off trial.

## Coaching Novices (Adaptive Front Door)

**Engine mode:** user has a role and a delegation map → run The Process directly.
**Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What-it-is:** "AI takes tasks, not jobs — so the job has to be rewritten around what's left and what's new."
2. **Check fit:** "How much of this role's time has the agent already taken over?"
3. **Elicit the real case:** "Name the role, list its current tasks, and give the share of hours each one takes."
> **[WAIT — do not advance until user responds]**
4. **Run The Process:** "Mark each task: goes to the agent, human–AI collaboration, or stays human."
> **[WAIT — do not advance until user responds]**
5. **Name the insight:** "State the new role definition, the new KPI, and the first skill gap."

## The Process

**Output:** New role card (duties + KPIs + skills + incentives + communication plan)

1. **Decompose into tasks.** List every task in the role with its share of hours. *Gate: shares sum to <90% → complete the list before continuing.*
2. **Assign each task a destination.** From the delegation map: fully delegable (agent runs it, human spot-checks) → agent; partially delegable (agent drafts, human approves) → human–AI collaboration; not delegated → stays human.
3. **Write the new human duties.** Judgment (decisions outside the agent's boundary) · exception handling · customer and partner relationships · supervising the agent (sampling, correcting, feeding back rules). *Gate: supervision has no named owner → stop.*
4. **Rewrite the KPIs.** Move from throughput to outcome + quality + exception resolution time + agent-correction rate. *Gate: an old volume KPI is still live → stop; it will fight the new incentives.*
5. **Close skill gaps and retrain.** List the new skills (prompting and evaluating outputs, exception judgment, data checking); set format, duration, and a pass criterion.
6. **Align incentives.** State where freed hours go (higher-value work, more accounts), and set an explicit rule — or equivalent arrangement — that using the agent does not cut pay.
7. **Communicate the change.** Lead with why, what stays the same, and each person's path; run a trial period with a feedback channel.
8. **Stop-rule:** freed hours have no higher-value destination → escalate to the business level to decide headcount, then re-run this process.

**Output template:**
`role | task → destination (hours %) | new duty + owner | new KPIs | skill gap + training + pass criterion | incentive rule | communication date | review date`

*→ Method in Action: [Klarna's AI assistant and the return of human service (2024–2025)](examples/klarna-ai-assistant-customer-service-2024-2025.md)*

## Role Packs

Typical patterns (tasks the agent takes / human duties that grow / KPI to retire → replace / dominant failure):
- **Customer support:** routine tickets / complex, emotional, escalated cases + agent QA / tickets per hour → resolution quality + escalation time / cost as the only scorecard.
- **Sales development:** list building, first-touch emails / discovery calls, qualification judgment / emails sent → qualified pipeline / volume KPI rewards spam.
- **Finance operations:** categorization, reconciliation drafts / exceptions, sign-off, client advice / items processed → error rate + close time / nobody owns the agent's misclassifications.

## Applying It Well

1. **Change the KPIs before the agent goes live.** Under the old metrics, resisting the tool is the rational move.
2. **Supervision is a formal duty.** Put it in the job description and in the hours — never "do it when you have a minute."
3. **Design separately for novices and veterans.** Novices gain fastest but need guarding against over-reliance; veterans' value shifts to judgment and coaching.
4. **Map the frontier before assigning tasks.** Where the agent is outside its competence, a human who defers to it does worse than a human working alone.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "The tool is live; the role will adapt on its own" | With unchanged incentives people route around the tool or pull tasks back. |
| [D] "Someone will supervise the agent along the way" | Supervision with no owner is no supervision. |
| [D] "If we don't mention AI, people won't worry" | Silence is read as the prelude to layoffs. |
| [D] "Send out a tutorial and call it training" | Training with no pass criterion does not change behavior. |
| [D] "Cost per contact is down, so the redesign worked" | Cost alone hides quality loss. Klarna's CEO said cost had been "a too predominant evaluation factor" and the result was "lower quality." |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- KPIs still count volume · no owner for agent corrections · no stated destination for freed hours · staff running shadow processes on the side

## Verification

- [ ] Task list covers ≥90% of hours
- [ ] Every new duty has an owner and allocated hours
- [ ] New KPIs have replaced the old ones and each person has been told
- [ ] Training has a pass criterion; communication and review dates are in the calendar

---

*Part of **deciqAI Knowledge Skills** — 253 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/human-ai-role-redesign** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/human-ai-role-redesign.json*
