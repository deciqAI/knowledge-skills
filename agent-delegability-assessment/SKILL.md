---
name: agent-delegability-assessment
description: "Activate when: user says 'which work can we hand to an AI agent', 'how far can this process be automated', 'does the agent need human approval', 'how much permission should the agent get', asks 'can the agent just do this on its own?', or is preparing to let an agent take over a business process.
  Do NOT activate when: the question is only which AI tool to buy (use build-buy-partner-ai); the process is not yet defined and is done differently every time. More: deciqai.com/s/agent-delegability-assessment"
---

# Agent Delegability Assessment

## Overview

Teams usually decide how much to hand to an agent by watching a demo. The demo shows what the model *can* do. It says nothing about what a mistake *costs* or whether anyone will notice one. The two failure modes look opposite and are equally expensive. If every output gets a human review, the time savings vanish and reviewers become rubber stamps. If full autonomy comes on day one, one irreversible error (a wrong payment, a wrong email to a customer, a wrong policy answer) wipes out the gains.

Core mechanism: **score each task on six dimensions, map it to one of four autonomy levels, and attach an approval gate to each level.** The cost of error and the ability to verify set the level, not model capability. The four levels: **L1 Suggest** (agent drafts, human does) · **L2 Approve-then-act** · **L3 Act-then-report** · **L4 Autonomous with spot checks**.

The roots are human-factors research. Parasuraman, Sheridan & Wickens (2000) showed automation is not all-or-nothing: it comes in levels, and the right level is chosen by the consequences of failure. Bainbridge's "Ironies of Automation" (1983) adds the warning this skill builds in: once humans step out of the loop, their ability to supervise decays, so even L4 needs scheduled human contact.

Compose with [sop-systemization](../sop-systemization/SKILL.md) (write the procedure before delegating it) · [agent-ops-monitoring](../agent-ops-monitoring/SKILL.md) (the logs and alerts that earn a promotion) · [principal-agent](../principal-agent/SKILL.md) (the delegate's objectives differ from yours) · [human-ai-role-redesign](../human-ai-role-redesign/SKILL.md) (what the humans do once tasks move) · [ai-pilot-to-scale](../ai-pilot-to-scale/SKILL.md) (promotion from pilot to production) · [premortem](../premortem/SKILL.md) (imagine the irreversible failure first).

## When to Use

- Listing a role's or department's processes and deciding which go to an agent
- Setting permissions and approval points before a new agent goes live
- Re-grading an agent after it made a mistake
- An agent is about to talk to customers, move money, send external messages or delete data

**When NOT to use:** the process is undocumented and varies every time · the step is legally required to have a human signature (only L1/L2 are available) · one-off tasks.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a task list → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What it is.** "How much you can delegate depends on how costly a mistake is, whether it can be undone, and whether someone can check it quickly."
2. **Check fit.** "Does this task happen at least a few times a week, done roughly the same way each time?"
3. **Elicit the real case.** "List 3–10 specific tasks you want to hand to an agent."
> **[WAIT — do not advance until user responds]**
4. **Run The Process.** Score the first task on the six dimensions with the user.
> **[WAIT — do not advance until user responds]**
5. **Name the insight.** State that task's level, its approval gate, and what would earn a promotion.

## The Process

**Output:** Delegation Map (task × level × gate × promotion/demotion rules)

1. **Decompose.** Break work down to "one input → one output" tasks. *Gate: input and output cannot be stated → run [sop-systemization](../sop-systemization/SKILL.md) first.*
2. **Score six dimensions (1–5).** Frequency · rule clarity · cost of error · reversibility · data access (can the agent lawfully read what it needs) · verifiability (can a human judge right/wrong in about a minute). Also record the **exception rate (%)**, measured, not guessed.
3. **Assign a level.** Apply caps in this order:
   - High cost of error **and** irreversible → max L2
   - Low verifiability → max L2, regardless of other scores
   - Exception rate > 20% → max L2; split the exception path out as its own task
   - High frequency + clear rules + reversible + easy to verify → start at L3
   - L4 only by promotion from a stable L3 that meets its error-rate target
   *Gate: data access insufficient → do not delegate; fix permissions first.*
4. **Attach gates.** For each level write: who approves, what they approve, the time limit, the amount/scope cap, and the action log.
5. **Set promotion and demotion rules.** Pre-set an error-rate threshold and an observation window. Crossing the threshold demotes the task one level automatically.
6. **Stop-rule:** the task's value is below the cost of approval and supervision → keep it manual or delete the task.

**Output template:**
`Task | Freq | Rules | Error cost | Reversible | Data | Verifiable | Exception % | Level | Approver + cap | Log | Promote when | Demote when`

*→ Method in Action: [Moffatt v. Air Canada — a customer-facing chatbot at the wrong autonomy level (2022–2024)](examples/moffatt-v-air-canada-chatbot-2024.md)*

## Applying It Well

1. **Start low; promote on data.** A level is earned through logged performance, not granted after a demo.
2. **Gate irreversible actions separately.** Payments, external sends, policy commitments and deletions get human confirmation or a hard cap, whatever the task's overall level.
3. **Score verifiability from the recipient's side.** If the person receiving the output cannot tell it is wrong, and nobody internal checks it before it lands, verifiability is low.
4. **Keep the human's hand in.** Schedule spot checks even at L4. Supervision skill decays when unused (Bainbridge).
5. **Delegating the work does not delegate the accountability.** The business answers for what its agent says and does.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "The model is strong — go fully automatic" | The level is set by error cost and verifiability, not by demo quality. |
| [D] "Review every output — safest" | Review cost eats the gains, and approvers soon rubber-stamp. A 100% approval rate is a signal, not a comfort. |
| [D] "Exceptions are rare, ignore them" | An unmeasured "rare" is often 20%+. Measure first, then decide. |
| [D] "We'll deal with errors when they happen" | Irreversible actions have no "later." Gates must exist beforehand. |
| [D] "The agent is a separate thing; its mistakes aren't ours" | A tribunal rejected exactly this argument in *Moffatt v. Air Canada* (2024): the chatbot "is still just a part of Air Canada's website." |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- No action log · payments or external sends with no amount/scope cap · no demotion rule · approval rate stuck at 100% with no spot checks · level justified by "it worked in the demo"

## Verification

- [ ] Every task has all six scores plus a measured exception rate, each with its basis
- [ ] Every irreversible action has a gate and a cap
- [ ] Promotion/demotion thresholds and observation windows are written down
- [ ] Delegation Map has a named owner and is archived

---

*Part of **deciqAI Knowledge Skills** — 253 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/agent-delegability-assessment** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/agent-delegability-assessment.json*
