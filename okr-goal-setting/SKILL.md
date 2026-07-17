---
name: okr-goal-setting
description: "Activate when: user says 'set OKRs', 'write objectives and key results', 'our goals aren't measurable', 'teams are hitting targets but the business isn't moving', 'we need stretch goals', 'align teams around quarterly goals', or mentions Doerr / Measure What Matters.
  Do NOT activate when: the team is under ~10 people with informal alignment that works fine; output is genuinely uncertain (deep R&D, research labs) making 'achieve X by Q3' structurally impossible. More: deciqai.com/s/okr-goal-setting"
---

# OKRs (Objectives and Key Results)

## Overview

OKRs separate ambition from measurement: an **Objective** is qualitative and aspirational; **Key Results** (3-5) are quantitative outcomes proving the objective was reached. KRs must be *outcomes*, not activities. Calibration rule: 70% achievement is success — routine 100% means goals were sandbagged. Developed by Andy Grove at Intel (1971); introduced to Google by John Doerr (1999).

Composes with [`north-star-metric`](../north-star-metric/SKILL.md), [`first-principles`](../first-principles/SKILL.md), [`metacognition`](../metacognition/SKILL.md), [`mece`](../mece/SKILL.md).

## When to Use

- Team goals are vague, unmeasurable, or just "complete project X" lists
- Teams hitting all goals but the business isn't moving (sandbagging signal)
- Cross-team work failing due to private, conflicting goals; or a new company needs goal infrastructure
- Setting OKRs on AI features and the draft KR is "ship AI" / "increase AI usage" (vanity/Goodhart metric — replace with outcome KRs)

**Not when:** under ~10 people with sufficient informal alignment; inherently uncertain output (research labs); leadership will punish 70% achievement.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user unfamiliar or no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. OKRs separate the inspirational *what we're trying to be* (Objective) from the measurable *how we'll know* (3-5 Key Results) — aiming for 70% so goals stretch beyond what's safe.
2. Check fit: under 10 people / uncertain output / leadership punishes 70% → not the right time.
3. Elicit the actual goal the team is trying to set.
> **[WAIT — do not advance until user responds]**
4. Ask one question at a time: what's the outcome? What would prove it happened? Activity or outcome? Would 70% be a real win?
> **[WAIT — do not advance until user responds]**
5. Close: one well-formed Objective and 3 Key Results, plus the cadence to revisit them.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Write the Objective.** Qualitative, aspirational, time-bounded, one sentence. Test: "If achieved, would this objectively matter to the business?"

**Step 2 — Write 3-5 Key Results.** Quantitative outcomes (not activities), time-bounded, 70%-success-calibrated. "Ship v2.0" = activity (wrong). "Reach 100k WAU on v2.0 within 30 days" = outcome (right). If all KRs happen and the Objective is not achieved, the KRs are wrong — iterate.

**Step 3 — Calibrate ambition.** >85% probability per KR → sandbagged, stretch it. <30% → unreasonable, compress. Target: 50-70% probability.

**Step 4 — Cascade and align.** Company OKRs first → Team OKRs derived from company → Individual OKRs (optional). Cross-team dependencies must appear explicitly in both teams' OKRs.

**Step 5 — Run the quarterly cycle.** Week 1: set. Mid-quarter: score 0.0–1.0. Final week: scoring + retrospective. Carryover: carry, drop, or rewrite.

**Step 6 — Score honestly.** Each KR scored 0.0–1.0, reported transparently. Scoring is NOT performance evaluation. Sandbagged 1.0s are worse than stretched 0.6s.

## Output: Quarterly OKR Sheet

```
# OKR: Q[X] [Year] — [Team]
## Objective 1: <qualitative, ambitious>
- KR1: [start] → [target] (actual: [x], score: [0.0-1.0])
- KR2: ...  KR3: ...
## Dependencies: depends on / others depend on us for
## Confidence: start / mid-quarter / end actual
```

*→ Method in Action: [Andy Grove at Intel, 1971; John Doerr at Google, 1999](examples/andy-grove-at-intel-1971-john-doerr-at-google-1999.md) · [Bono's ONE Campaign](examples/bono-one-campaign-2002-2018.md)*

*→ 2026 lens: [OKRs in an AI-native org (2024–2026)](examples/ai-native-org-okrs-2024-2026.md)*

## Pack: OKR Patterns

| Domain | Good KR (outcome) | Bad KR (activity) |
|---|---|---|
| Engineering | "Reduce P0 incidents from 4/qtr to 1" | "Implement new deployment pipeline" |
| Sales | "Close 15 new accounts at >$50k ACV" | "Hire 3 mid-market AEs" |
| Product | "Increase day-7 retention from 22% to 40%" | "Launch new onboarding flow" |
| Marketing | "Reach 50k organic blog visits/mo" | "Publish 10 blog posts" |

## Applying It Well

Limit ruthlessly: ≤2 Objectives per team, ≤5 KRs each. Celebrate 70% explicitly — punishing it destroys stretch. Decouple scores from comp/performance reviews. Require cross-team OKRs to reference each other.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Ship feature X" as a KR | Activity, not outcome. What change in the world does shipping X cause? That's the KR. |
| [D] All KRs hit at 100% | Sandbagged. Recalibrate next quarter. |
| [D] 30% achievement is normal | Goals unreasonable. Target is 60-80%. Recalibrate. |
| [D] 20 KRs across 5 Objectives | Lack of focus. Cut to 1-2 Objectives, 3-5 KRs each. |
| [D] OKRs tied to performance evaluation | Couples stretch with punishment; sandbagging becomes rational. Decouple. |
| [D] Quarterly OKRs match what you'd have done anyway | Then they're a to-do list. The KR must change what the team chooses to do. |
| [D] No scoring at quarter end | Skipping retrospective destroys the learning loop. Score every KR. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- KRs that are activities ("ship," "launch," "hire," "complete") — 100% achievement every quarter
- More than 5 Objectives or 5 KRs per Objective — OKRs invisible across teams
- OKR scores tied to compensation — no quarterly retrospective

## Verification

- [ ] Each Objective: qualitative, ambitious, one sentence
- [ ] Each KR: quantitative, outcome-focused, time-bounded, genuinely stretching (70% target)
- [ ] Cross-team dependencies explicit; OKRs visible org-wide
- [ ] Quarterly cadence established; scoring honest and decoupled from performance reviews

---

*Part of **deciqAI Knowledge Skills** — 228 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/okr-goal-setting** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/okr-goal-setting.json*
