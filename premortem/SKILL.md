---
name: premortem
description: "Activate when: user says 'let's check what could go wrong before we commit', 'I want to stress-test this plan', 'we're about to launch and I'm worried we're missing something', 'premortem', or is about to make a hard-to-reverse decision with a team that has converged on one plan.
  Do NOT activate when: the decision is small and easily reversible (overhead exceeds value); the situation is time-critical and analysis would prevent timely response."
---

# Premortem

## Overview

Before committing to a plan, the team imagines that plan has already failed catastrophically, then works backward to enumerate causes. The retrospective frame ("it failed — what caused it?") surfaces risks the prospective frame ("what could go wrong?") systematically misses. Gary Klein operationalized this in *HBR* (2007), grounded in Mitchell-Russo-Pennington (1989) showing prospective hindsight increases correct failure-mode identification by 30%.

Composes with [`inversion`](../inversion/SKILL.md) (premortem is inversion made operational), [`confirmation-bias`](../confirmation-bias/SKILL.md) (structural counter), [`hindsight-bias`](../hindsight-bias/SKILL.md) (leveraged as a feature), and [`critical-thinking`](../critical-thinking/SKILL.md).

## When to Use

- Before any high-stakes, hard-to-reverse decision (launch, major hire, contract, capital allocation)
- When the team has converged quickly on a single plan with little visible dissent
- When a previous similar effort failed and the team is about to repeat the pattern
- At project milestones to identify emerging failure modes
- Before committing to an AI product launch, model migration, or AI capex/growth spend where model commoditization, inference unit economics, a safety incident, or stretched AI valuations could break the plan within a year

**Not when:** small reversible decision; equivalent rigorous risk analysis already done; Chaotic domain (action before analysis); time-critical where premortem delays response.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete decision → run The Process directly.
- **Coach mode:** user is new → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: imagine the project already failed — the retrospective frame surfaces risks "what could go wrong?" misses.
2. Check fit: if the decision is small and reversible, skip.
3. Elicit the specific decision, team, and imagined failure date.
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time — enforce private generation before group discussion.
> **[WAIT — do not advance until user responds]**
5. Close by naming the insight uncovered and scheduling the re-premortem date.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Frame:** decision/plan, imagined failure date, failure type, participants, facilitator.

**Step 2 — Set up the fiction:** read aloud: *"It is [date]. We executed the plan. It has failed catastrophically. Write down — in silence, 5-10 minutes — the specific reasons why. Be specific. Generate as many as you can."* Enforce: failure is a fact, not a possibility.

**Step 3 — Private silent generation:** each participant writes privately. No discussion. This step is non-negotiable — group discussion first produces conformity, not coverage.

**Step 4 — Consolidate:** round-robin read-out; facilitator captures all without judgment; group into clusters; rate each by probability / severity / detectability.

**Step 5 — Mitigate:** for each high-probability or high-severity cluster: mitigation action · owner · monitoring trigger · escalation threshold.

**Step 6 — Schedule re-premortem:** failure modes shift at each milestone; lock in the next date before leaving the room.

## Output Template

```markdown
# Premortem: <decision>
Imagined failure date: | Failure type: | Facilitator:

| # | Failure mode | Prob | Severity | Detect | Mitigation | Owner | Trigger |
|---|---|---|---|---|---|---|---|

Modified plan — new mitigations added:
Monitoring signals to track:
Pre-committed escalation thresholds:
Re-premortem date:
```

*→ Method in Action: [Klein 2007 and the Mitchell-Russo-Pennington 1989 Foundation](examples/klein-2007-mitchell-russo-pennington-1989-foundation.md)*
*→ 2026 lens: [Back-Casting a Failed AI Agent Startup 12 Months Out (2024–2026)](examples/backcasting-ai-agent-startup-failure-2024-2026.md)*

## Pack: Application Patterns

| Domain | When | Common failure modes |
|---|---|---|
| Product launch | Before public launch | Customer confusion; pricing rejection; competitive response |
| Major hire | Before offer | Cultural mismatch; performance miss; early departure |
| M&A | Before LOI / close | Integration failure; key-person flight; due diligence miss |
| Capital raise | Before launching | Failed close; bad terms; runway miscalculation |
| Technology migration | Before major rewrite | Hidden dependencies; data loss; team burnout |

## Applying It Well

- The grammatical mood is non-negotiable: "it failed — what caused it?" not "what might go wrong?" Enforce the fiction throughout.
- Private silent generation must precede group discussion or you get conformity, not risk coverage.
- The deliverable is the modified plan, not the failure list. Assign owners and triggers before leaving.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We've already done risk analysis" | Risk analysis is prospective; premortem is retrospective. Different frame, different output. |
| [D] "It would demoralize the team" | Empirically the opposite — premortems license dissent and are reported as morale-positive. |
| [D] "We don't have time" | A 60-minute premortem on a 6-month project is 0.07% of project time. |
| [D] "The leader has already committed" | Exactly when premortem is most valuable — public commitment creates the strongest groupthink. |
| [D] "The risks are obvious" | Private generation regularly surfaces risks absent from the consensus risk register. |
| [D] "Premortem is pessimism" | Output is a stronger plan with mitigations — rational confidence-building, not pessimism. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Major decision with little visible dissent; team converged quickly; leader publicly endorsed before stress-testing
- "What could go wrong?" produced only vague concerns; previous similar effort failed; no one tasked with finding flaws

## Verification

- [ ] Fiction set up explicitly (failure as fact, not possibility)
- [ ] Private silent generation preceded group discussion
- [ ] All participants contributed (not just senior voices)
- [ ] Clusters rated for probability, severity, detectability
- [ ] Mitigations assigned with named owner and trigger signal
- [ ] Plan modified to incorporate mitigations (not just discussed)
- [ ] Re-premortem date on the calendar

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/premortem?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=premortem** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
