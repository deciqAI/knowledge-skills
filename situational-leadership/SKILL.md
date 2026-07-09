---
name: situational-leadership
description: "Activate when: user says 'my management style isn't working for this person', 'I don't know how much to delegate', 'my top performer is disengaged', 'my new hire is struggling without guidance', 'should I give him more autonomy?', or asks how to lead/manage a specific person on a specific task.
  Do NOT activate when: the performance issue is an incentive misalignment (reward structure is wrong — use principal-agent instead); the organization is in acute crisis requiring uniform command and all debate is suspended."
---

# Situational Leadership

## Overview

Match your leadership style to each person's development level on each specific task — cycling through four styles (Directing, Coaching, Supporting, Delegating) as competence and commitment evolve. Introduced by Hersey & Blanchard (1969); formalized as SLII by Blanchard, Zigarmi & Zigarmi (1985).

Core diagnostic: instead of "what kind of leader should I be?" ask "what does this person need from me on *this task* right now?" Failure to update style as the person grows is the most common cause of high performers disengaging.

Composes with: [`kotter-change`](../kotter-change/SKILL.md) for org-level transformation (Kotter = org sequence; this = each individual relationship); [`principal-agent`](../principal-agent/SKILL.md) to rule out incentive problems first; [`okr-goal-setting`](../okr-goal-setting/SKILL.md) to set goals (OKR) then govern how to support each person toward them.

## When to Use

- A manager-report relationship has **friction or underperformance** and root cause is undiagnosed
- A **high performer is disengaging** ("I'm being micromanaged", "no room to grow") — signature of D4 receiving S1
- A **new hire or person in a new role** is struggling despite effort — signature of D1/D2 receiving insufficient structure
- A **task or technology change** resets development levels for experienced people
- **AI adoption resets who's the expert** — after rolling out AI coding tools / AI-native workflows amid the 2024–2026 AI capex race, a senior person is D1/D2 on the new tool even while D4 on the core work
- You are making a **delegation decision** for a specific person on a specific task

**When NOT to use:** incentive misalignment (principal-agent problem); acute crisis requiring uniform command; task is too vague to name (diagnosis requires a specific task).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a specific person and task → run The Process directly.
- **Coach mode:** user is unfamiliar or asks "what is situational leadership?" → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: there's no single best management style — what works depends on how much the person knows and how confident/motivated they feel on *this task*. The manager's job is to match style to that, and update as the person grows.
2. Check fit: is there a specific person and specific task where management is stuck? If the issue is incentives not capability, point to principal-agent.
3. Elicit the real case — get the specific task and specific person. Never assess development level for "the employee in general."
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time: start with competence — "Describe 2–3 things this person has done on this task. What was the quality?"
> **[WAIT — do not advance until user responds]**
5. Close by naming the insight: which development level, which style, and one specific behavior the manager should change immediately.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Development Diagnosis**, then select and implement the **Leadership Style**.

1. **Define the task precisely.** State: "[Person] on [specific task]." If the task cannot be named, the diagnosis cannot run.
2. **Assess competence** on this specific task — Knowledge / Skill / Track record. Rate: Low / Medium / High.
3. **Assess commitment** on this specific task — Motivation / Confidence / Engagement. Rate: High / Variable / Low. Do not infer from behavior alone — ask directly.
4. **Determine development level:** D1 = Low competence + High commitment; D2 = Low-medium competence + Low commitment; D3 = Medium-high competence + Variable commitment; D4 = High competence + High commitment. *Stop-rule: ambiguous level → default to lower (more structure).*
5. **Select and implement style:** S1 Directing (D1) — clear steps, specific check-ins, no open-ended "how do you think?"; S2 Coaching (D2) — high directive + high supportive, acknowledge effort + give guidance; S3 Supporting (D3) — ask questions, explore confidence barriers, avoid deciding for them; S4 Delegating (D4) — assign outcomes not methods, check in periodically, express trust through reduced supervision.
6. **Monitor, reassess, shift.** Reassess when new responsibilities arrive, performance drops, or disengagement signals appear. Name style shifts explicitly: "I'm adding more structure on this new task — that's about the task, not my confidence in you."

### Output: Development Diagnosis

```
# Development Diagnosis: <person> on <task>
Task: <precisely stated>
Competence: Knowledge / Skill / Track record → Overall: low/medium/high
Commitment: Motivation / Confidence / Engagement → Overall: high/variable/low
  (Assessment method: observation / conversation / inference)
Development level: D1/D2/D3/D4 — reasoning
Style recommendation: S1/S2/S3/S4
Immediate behavior changes: (1) (2) (3)
Reassessment trigger: <signal>
```

*→ Method in Action: [Google's Project Oxygen (2009)](examples/google-project-oxygen-2009.md)*
*→ 2026 lens: [Leading AI-native engineering teams (2024–2026)](examples/leading-ai-native-teams-2024-2026.md)*

## Style Packs

**Engineering teams:** Most common error — treating technical seniority as a proxy for all tasks. A senior engineer may be D4 on Python and D1 on AI deployment. Maintain a task-level development map; separate legacy skills from AI-assisted tasks.

**Startup scaling:** Most dangerous failure — founder default to S4 as company grows, continuing S4 with incoming D1/D2 hires and producing confused new-hire failures. Reverse error: staying S1 with D4 executives who should be released.

## Applying It Well

- Never assess development level globally — always for a specific named task. "She's a D4" is meaningless; "D4 on client management, D1 on data analysis" is actionable.
- Most dangerous mismatch: D4+S1. Symptoms: person stops raising ideas, stops initiating, starts mentioning other opportunities. When shifting S4→S1 on a new task, name the shift explicitly.
- Commitment is harder to assess than competence. Ask: "On a scale of 1–10, how confident do you feel?" The gap between inferred and stated confidence is the coaching starting point.
- Development arc (D1→D4) is not linear in time. Apply the style the current level calls for — don't rush the levels.

*→ Primary sources: [references/sources.md](references/sources.md)*
## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**
| Fake move | Reality |
|---|---|
| [D] "I treat everyone the same — it's fair" | Applying S1 to a D4 and S4 to a D1 simultaneously is uniform — and both are harmful. Fairness means matching the response to the actual need. |
| [D] "He's been here 5 years, so I delegate everything to him" | Tenure is not development level. A 5-year employee on a new task type is D1 on that task. Assign by task, not tenure. |
| [D] "She's technically strong, so she doesn't need much management" | Technical competence is one dimension. A technically strong person who has lost motivation (D3) needs S3, not S4. Ignoring commitment produces the disengaged high performer. |
| [D] "I gave him full autonomy and he failed — he's not as capable as I thought" | This is D1+S4 failure. The error is in the style assignment, not the person's capability. |
| [D] "I can't give her S1 treatment — she'll think I don't trust her" | S1 for a D1 is appropriate support, not distrust. Name the rationale: "You're new to this task; I'll give you structure and pull back as you develop." |
| [D] "We're a high-autonomy culture — everyone operates independently" | Culture-level autonomy doesn't substitute for task-level assessment. High-autonomy culture extends trust to people ready for it — it does not mean ignoring D1 new hires or D3 people needing coaching. |
| [D] "My style is coaching — I do S2 with everyone" | A fixed coaching style is as rigid as any other. D1 needs direction before coaching; D4 needs space, not coaching. |
| [D] "I don't have time for 1:1s — they're not productive" | S2 and S3 require individual conversation to assess commitment and explore barriers. Skipping 1:1s forces drift to uniform S1 or S4 — both produce predictable failure. |
| [D] "The person needs to step up — that's on them" | Prior question: did they have competence and commitment, and did they receive the matching style? Blaming the person before checking style match is diagnostic failure. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Development level was assessed for a person overall, not for a specific task
- Commitment was inferred from behavior without direct conversation
- Manager has not changed style for a long-tenured member even as responsibilities evolved
- High performer is disengaging or citing "no growth opportunities" — likely D4+S1
- New hire is repeatedly failing — likely D1+S4
- Development level not updated after new tasks were assigned

## Verification

- [ ] Task is precisely stated — not "her performance" but "her performance on [specific named task]"
- [ ] Competence assessed on all three dimensions: knowledge, skill, track record
- [ ] Commitment assessed through direct conversation, not only inferred
- [ ] Development level (D1–D4) stated with reasoning, not just the label
- [ ] Leadership style (S1–S4) matched to development level, with three specific behavior changes named
- [ ] Stop-rule applied: ambiguous level defaults to lower (more structure)
- [ ] Reassessment trigger defined

---
*Part of **deciqAI Knowledge Skills** — 189 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/situational-leadership** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
