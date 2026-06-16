---
name: dunning-kruger
description: "Activate when: someone says 'how hard could it be' about an unfamiliar domain; a novice dismisses expert opinion or says 'I could do that'; someone's self-assessed confidence seems disconnected from their actual track record; a hiring or promotion decision is driven by self-presentation; feedback loops are absent and someone is operating on gut confidence alone. Do NOT activate when: the person is a known expert with an established external track record; the confidence claim is in a domain with tight, recent feedback loops that already calibrate performance."
---

# Dunning-Kruger Effect

## Overview

The **Dunning-Kruger effect** is the systematic self-assessment asymmetry demonstrated by Kruger & Dunning (1999): bottom-quartile performers overestimate rank by ~50 percentile points; top-quartile performers underestimate by ~5 points. Mechanism: the cognitive skills needed to *perform* a task are the same ones needed to *evaluate* performance — so novices lack the metacognition to see their own gap. The corrective is external measurement and feedback, not internal vigilance.

Composes with [`metacognition`](../metacognition/SKILL.md), [`probabilistic-thinking`](../probabilistic-thinking/SKILL.md), [`critical-thinking`](../critical-thinking/SKILL.md), and [`confirmation-bias`](../confirmation-bias/SKILL.md).

## When to Use

- A novice is expressing high confidence or dismissing expert opinion ("I could do that better")
- Hiring/promotion decisions are based on candidate self-assessment
- "How hard could it be?" asked about a domain the asker hasn't worked in
- Feedback loops are absent; self-assessment is contradicted by external data and rejected
- Someone mentions "overconfident," "doesn't know what they don't know," or "imposter syndrome" (the inverse)

**Not when:** person is a known expert with an external track record; domain has tight, recent feedback loops that already calibrate performance; high-confidence claim is self-deprecating (actual metacognition signal).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user brings a specific confidence claim → diagnose directly.
- **Coach mode:** user unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **One-line:** confidence is not a proxy for competence unless the person has metacognitive feedback — check against external data.
2. **Check fit.** If external performance data exists and the person can see it, the bias may already be corrected. If unsure, ask: *"Are you diagnosing a specific claim, or learning the framework?"*
3. **Elicit the specific claim and basis for confidence.** What is being claimed? Self-assessment, external metrics, peer comparison, formal evaluation?
> **[WAIT — do not advance until user responds]**
4. **One question at a time:** what would they accept as evidence they were wrong? How much feedback have they received? Bottom, middle, or top of comparable performers by an external measure?
> **[WAIT — do not advance until user responds]**
5. **Close:** name an external feedback mechanism (calibration test, peer review, blind evaluation) + a re-measurement schedule.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — State the claim:** Domain · verbatim claim · self-assessed percentile · basis for assessment · stakes.

**Step 2 — Test metacognitive prerequisite:** Can the person evaluate others' performance in this domain? Have they received external feedback? Can they articulate what failure looks like?

**Step 3 — Get external data:** Objective metrics · blind peer comparison · expert evaluation · track record · calibration test (predict score → take test → compare).

**Step 4 — Diagnose quartile pattern:** Bottom+high → novice overconfidence · Top+low → impostor · Top+high → calibrated expertise · Middle+accurate → no intervention.

**Step 5 — Design intervention:** Calibration test / blind peer comparison / structured rubric eval / training+feedback / real-stakes performance test.

**Step 6 — Re-measure:** Baseline → 30/90/180-day schedule → define what change indicates genuine improvement.

## Output Template

```
Dunning-Kruger Diagnosis: <person/domain>
Claim: domain | self-assessed percentile | basis | stakes
Metacognitive test: evaluates others (Y/N) | external feedback (Y/N) | articulates failure (Y/N)
External data: metrics | peer rank | expert eval | track record
Quartile diagnosis: self=X | external=Y | gap=Z pts | pattern=<novice-OC/calibrated/impostor/mid-OK>
Intervention: <method> | Owner: | Re-measure:
```

*→ Method in Action: [Kruger and Dunning's 1999 Cornell Studies](examples/kruger-and-dunnings-1999-cornell-studies.md)*

## Pack: Common Novice Overestimation Patterns

| Domain | Overconfidence signal | Countermeasure |
|---|---|---|
| Programming | "I could build this in a weekend" | Code test; pair programming |
| Investing | "I beat the market last year" | Risk-adjusted return vs benchmark, multi-year |
| Hiring | "I can tell in 5 minutes" | Structured rubric; predictive validity tracking |
| Medical | "I researched online; I know what I have" | Diagnostic test; second opinion |

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "I'm confident, therefore I know what I'm doing" | Confidence in novices is the *signature* of the effect. The metacognitive resources that would correct it are absent. |
| [D] "I've been doing this for years" | Years without feedback produce confident incompetence, not expertise. |
| [D] "I read three books on this" | Reading is exposure, not skill. Self-assessment after reading is consistently inflated. |
| [D] "My peers tell me I'm good" | Peers in your cohort have similar skill distributions; cross-cohort expert eval is more diagnostic. |
| [D] "How hard could it be?" | Applied to an untried domain, reliably precedes falsified overconfidence. |
| [D] "I can self-evaluate" | Kruger-Dunning: you cannot self-evaluate without the underlying skill. External measurement required. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Little measurable track record + strong domain confidence
- Refusal to engage with measurement ("metrics don't capture what I do")
- Dismissal of expert input as "overcomplicated" or "out of touch"
- High self-assessment with absent feedback loops
- Recurring confident claims followed by quiet retractions or excuses

## Verification

- [ ] Confidence claim specified with domain and measurable performance dimension
- [ ] External performance data gathered (or absence noted)
- [ ] Metacognitive prerequisite tested (can person evaluate others' performance?)
- [ ] Four-quartile diagnosis completed
- [ ] Feedback intervention chosen and re-measurement scheduled
- [ ] Rejection of external data documented as a Dunning-Kruger signal

---

*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/dunning-kruger?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=dunning-kruger** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
