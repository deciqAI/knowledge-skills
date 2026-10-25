---
name: agent-ops-monitoring
description: "Activate when: user says 'how do we watch the agent after launch', 'AI output quality is getting worse', 'inference spend suddenly jumped', 'the agent broke something, how do we roll back', 'we need an AI ops weekly review', or an AI agent is already in production handling real business.
  Do NOT activate when: the project is still at the business-case stage (use ai-roi-business-case); usage is one-off and manual with no ongoing traffic. More: deciqai.com/s/agent-ops-monitoring"
---

# Agent Ops Monitoring

## Overview

An agent that is live without logs, quality metrics or alerts fails quietly. Output quality drifts after a prompt tweak or a vendor model update, spend creeps up, and when something goes wrong nobody can reconstruct what the agent saw, called or said. Most bad outputs are never reported. Customers just leave.

Core mechanism: **log every run → define quality metrics and sample for human review → alert on drift and cost → have incident handling and rollback ready → route risky cases to a human queue → review weekly.** It is site reliability engineering (SRE) practice adapted to systems whose failures are often *plausible-looking* rather than crashes. Google's SRE book frames monitoring as answering "what's broken, and why?". For an LLM agent, "broken" includes a confident wrong answer that returns HTTP 200.

The hardest lesson is that pre-launch checks are not monitoring. Offline evaluations and small A/B tests can all look good while real-world behavior goes wrong. OpenAI's April 2025 GPT-4o rollback is a documented case ([example](examples/openai-gpt-4o-sycophancy-rollback-2025.md)).

Compose with [checklist](../checklist/SKILL.md) (the incident-response checklist) · [premortem](../premortem/SKILL.md) (imagine failure modes before launch) · [ai-output-verification-trust-tiers](../ai-output-verification-trust-tiers/SKILL.md) (which outputs go to the human review queue) · [agent-delegability-assessment](../agent-delegability-assessment/SKILL.md) (autonomy levels the monitoring data promotes or demotes) · [goodharts-law](../goodharts-law/SKILL.md) (a proxy metric that looks good is not the goal).

## When to Use

- An agent handles customers, orders, finance or external communication
- Before and after switching models, editing prompts or adding tools
- Spend or complaints show an anomaly
- Building the recurring AI-operations review

**When NOT to use:** occasional personal use · experiments with no ongoing traffic · not yet launched (design the logging, but the full loop starts at launch).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user already has an agent running → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What it is.** "You can't manage what you can't see. Every run must leave a trace, be sampleable, and be reversible."
2. **Check fit.** "Is the agent already handling real business, with steady daily traffic?"
3. **Elicit the real case.** "What does the agent do, how many runs a day, and what's the most expensive thing it could get wrong?"
> **[WAIT — do not advance until user responds]**
4. **Run The Process.** Steps 1–2 with the user: list the fields to log and 3 quality metrics.
> **[WAIT — do not advance until user responds]**
5. **Name the insight.** "Next time it goes wrong, how many minutes until you can locate the cause and roll back?"
> **[WAIT — do not advance until user responds]**

## The Process

**Output:** One-page Agent Ops Runbook

1. **Define logged fields.** Per run: trace ID · input · output · tool calls with arguments and results · model and prompt version · tokens/cost · latency · final status. Redact sensitive fields. The OpenTelemetry GenAI semantic conventions give standard names for model, token-usage and tool-call attributes. *Gate: a single run cannot be reproduced from its trace → stop and fix logging first.*
2. **Define quality metrics.** Task success rate · human edit/reject rate · complaint/escalation rate · tool-call failure rate. Randomly sample a fixed share of runs each week for scored human review. *Gate: a metric cannot be computed from the logs → stop.*
3. **Set alerts.** Quality drift (metric departs from the trailing 4-week baseline) · cost (per-run and daily totals over threshold) · error rate · latency. Each alert has a named recipient. *Gate: an alert with no recipient does not count as set.*
4. **Incident handling and rollback.** Classify severity (customer- or money-affecting is highest) → pause or degrade to human handling → roll back to the previous model/prompt version → notify affected parties → run a blameless postmortem. *Gate: no one-step rollback to a previous version exists → stop and build version control first.*
5. **Human-in-the-loop queue.** Low-confidence, high-risk and novel inputs go to a human queue with a handling time limit and a backlog cap.
6. **Weekly review.** Metric trends · sampling findings · alerts and incidents · cost · this week's changes · next week's actions and owners.
7. **Stop-rule:** if the agent only produces low-risk drafts that can be redone at any time, compress to steps 1 and 6.

**Output template:**
`Logged fields | Quality metrics + sample rate | Alerts (condition/threshold/recipient) | Severity levels + rollback steps | Human-queue rules + time limit | Weekly review agenda`

*→ Method in Action: [OpenAI's GPT-4o sycophancy rollback (April–May 2025)](examples/openai-gpt-4o-sycophancy-rollback-2025.md)*

## Applying It Well

1. **Version everything.** Model, prompt, tool definitions. Any change is a release with a version number.
2. **Sample randomly, not only what was complained about.** Complaints are a biased, lagging sample.
3. **Sample more heavily for a week after every change.** Most drift arrives with a change, including a vendor's change you did not make.
4. **Set cost alerts on both per-run and daily totals.** A runaway loop shows in one, a traffic spike in the other.
5. **Treat qualitative "feels off" signals as data.** When reviewers' judgment conflicts with green metrics, the metric may be blind to the failure.
6. **No thresholds from memory.** Thresholds come from each workload's own baseline. Do not import someone else's numbers.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "No complaints means no problem" | Most errors are never reported; they show up as churn. |
| [D] "Logs are too big to store" | Store full text on a sample and metadata on everything. An incident with no logs costs more. |
| [D] "The model vendor guarantees quality" | A vendor's model update can drift *your* quality too. Pin versions and re-test. |
| [D] "We'll figure out rollback if something happens" | Building rollback during an incident is the slowest path. |
| [D] "Evals and the A/B test passed, so we're safe" | OpenAI's April 2025 update passed offline evals and A/B tests and was still rolled back within days. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- No prompt/model version numbers · only averages, never distributions · human queue with no backlog cap · weekly review cancelled repeatedly · changes shipped without notice because they seemed "small"

## Verification

- [ ] Any run can be reproduced from its trace
- [ ] Quality metrics and sampling rate are defined and actually being computed
- [ ] Every alert has a threshold and a recipient
- [ ] Rollback has been rehearsed at least once
- [ ] Human queue has a time limit
- [ ] Weekly review has minutes and an owner

---

*Part of **deciqAI Knowledge Skills** — 253 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/agent-ops-monitoring** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/agent-ops-monitoring.json*
