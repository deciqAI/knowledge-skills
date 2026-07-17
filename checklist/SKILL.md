---
name: checklist
description: "Activate when: user says 'let's make sure we don't skip anything', 'we need a pre-flight', 'build me a checklist for X', 'we keep missing steps in our deployment / close / launch', 'Gawande / Pronovost / checklist manifesto'. Do NOT activate when: the task is simple and one-off with no recurrence; the user is asking for a to-do list or project plan (not a must-not-skip operational gate). More: deciqai.com/s/checklist"
---

# Checklist

## Overview

A **checklist** is a short written list of must-not-skip steps for a complex repeated operation. It externalizes working memory — which fails under load, ego, time pressure, and fatigue — so attention stays on the situation rather than step recall. Boeing 1935 → Pronovost ICU 2001 → WHO Surgical 2008: each produced 36-47% reductions in major adverse events at near-zero cost.

Composes with [`metacognition`](../metacognition/SKILL.md), [`confirmation-bias`](../confirmation-bias/SKILL.md), [`cognitive-load-theory`](../cognitive-load-theory/SKILL.md), [`premortem`](../premortem/SKILL.md), [`inversion`](../inversion/SKILL.md).

## When to Use

- High-stakes repeated operations (deployments, launches, M&A close, hiring decisions, financial close)
- Multiple steps where skipping one costs far more than running the checklist
- Multi-person operations where coordination must be consistent
- New team members joining a critical workflow

**Not when:** operation is simple/one-off; no recurring pattern exists; checklist culture creates false confidence (mechanical checking without thought).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a specific operation → run The Process directly.
- **Coach mode:** user is new to the framework → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: for any complex repeated operation, a 6-10 item checklist outperforms expert memory under load — it externalizes the steps that fail systematically.
2. Check fit: repeated + high-stakes + consequential errors = checklist candidate. Simple or one-off = skip.
3. Elicit their real case: what operation, where does it fail, what near-misses have occurred?

> **[WAIT — do not advance until user responds]**

4. Run The Process one step at a time with their input: what items must never be skipped? DO-CONFIRM or READ-DO? who runs it and when?

> **[WAIT — do not advance until user responds]**

5. Close: present drafted checklist + format + workflow integration, name the key reliability insight they uncovered.

> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Identify the operation:** operation name, frequency, stakes of errors, current failure modes, near-miss history.

**Step 2 — List 15-25 candidate items:** steps that have been skipped, steps that prevent major errors, coordination steps, bias-catching steps, reversibility checkpoints.

**Step 3 — Cut to 6-10:** keep only items that are critical, easily missed by skilled operators, and verifiable (yes/no signal). Longer lists get truncated in use.

**Step 4 — Choose format:** READ-DO (read → act → next item; use for novices, novel procedures, multi-person coordination) vs DO-CONFIRM (pause → confirm all done; use for skilled experts where flow matters).

**Step 5 — Embed in workflow:** define trigger, owner, consequence of skipping, and cultural reinforcement (leadership models it, peers enforce it).

**Step 6 — Iterate:** after each near-miss, check if an item would have caught it and add it. Quarterly review: remove stale items, add new failure modes.

## Output: Checklist Design

```
# Checklist: <operation>
Format: DO-CONFIRM / READ-DO | Trigger: | Owner:
Items (6-10):
1.   2.   3.   4.   5.   6.
Consequence of skipping:
Near-miss tracking:  Quarterly review owner:
```

*→ Method in Action: [B-17 1935 + Pronovost ICU + WHO Surgical](examples/b-17-1935-pronovost-icu-who-surgical.md) · [Van Halen's Brown M&M Rider Clause](examples/van-halen-brown-mms-rider-clause.md)*

## Pack: Domain Patterns

| Domain | Gate | Checklist focus |
|---|---|---|
| Aviation | Pre-flight | Systems, fuel, weather, navigation, crew brief |
| Surgery / ICU | Pre-incision / central-line | Patient identity, site, antibiotics, hand hygiene, drapes |
| Software | Pre-deploy | Tests pass, monitoring, rollback ready, comms sent |
| Investment | Pre-decision | Bias check, valuation, management, structural risks |
| M&A / Hiring | Pre-close / pre-offer | Due diligence complete, financing committed, rubric coverage |

## Applying It Well

- 6-10 items is the empirical optimum; cut ruthlessly — longer lists get skipped.
- Match format (DO-CONFIRM vs READ-DO) to the natural rhythm of the work.
- Cultural commitment is load-bearing: consistent use and genuine attention, not mechanical checking.
- Iterate after every near-miss; the list must evolve with real failure patterns.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "I know what I'm doing; I don't need a checklist" | Expert intuition fails under load. B-17's pilot was one of the most experienced of his era. |
| [D] "Checklists slow us down" | Slightly — but prevent rework and catastrophes. Net benefit overwhelmingly positive. |
| [D] "Checklists are for amateurs" | Lufthansa pilots, neurosurgeons, and top investors all use them. |
| [D] "We have one but no one uses it" | Value comes from consistent use. Culture and workflow integration are part of the discipline. |
| [D] "More items = better" | False. >10 items get truncated. Aim for the critical few. |
| [D] "We tried one and it didn't help" | Likely wrong design (too long, wrong format, misaligned with workflow). Iterate. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Complex repeated high-stakes operation has no checklist; or checklist exists but seniors skip it
- 20+ items and users are truncating it; or near-misses are not updating it
- Items run mechanically without genuine attention; no one owns maintenance

## Verification

- [ ] Operation identified, failure modes documented, near-miss history noted
- [ ] 6-10 items, each critical, easily missed, and verifiable (yes/no signal)
- [ ] Format (DO-CONFIRM or READ-DO) matches operation pace and expertise level
- [ ] Embedded with clear trigger, owner, consequence of skipping, cultural reinforcement
- [ ] Near-miss tracking and quarterly review scheduled

---

*Part of **deciqAI Knowledge Skills** — 228 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/checklist** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/checklist.json*
