---
name: deliberate-practice
description: "Activate when: user says 'I've been doing this for years but I'm not getting better'; someone suspects a skill plateau despite continued effort; designing a learning program for a high-performance outcome; an organization reports high training hours but low skill transfer.
  Do NOT activate when: goal is execution of existing skills rather than acquiring new ones (use deep-work instead); there is no identifiable expert performance benchmark to target."
---

# Deliberate Practice

## Overview

Most people confuse repetition with learning — they accumulate years of experience and plateau. Once an activity becomes automatic, executing it no longer builds new neural architecture. Ericsson, Krampe & Tesch-Römer (1993) showed the predictive variable is not hours of doing but hours of *specifically deliberate practice* — targeted, uncomfortable, feedback-rich repetition designed to build mental representations.

**Cross-skill composition:** Use [`feedback-loops`](../feedback-loops/SKILL.md) first (audit your error signal); then [`metacognition`](../metacognition/SKILL.md) (surface your current representation gap); use instead of [`deep-work`](../deep-work/SKILL.md) when acquiring skills, not producing output; use alongside [`cognitive-evolution-stages`](../cognitive-evolution-stages/SKILL.md) for stage-aware practice design.

---

## When to Use

**Trigger:** plateau despite experience; designing high-performance learning program; training hours high but skill transfer low; evaluating whether practice is building capability or maintaining it; skill atrophy or deskilling as AI copilots absorb the routine reps (AI adoption, AI hype, "will AI make me worse at my craft").
**When NOT:** goal is execution not acquisition (use deep-work); no expert benchmark exists; bottleneck is motivational not representational.

---

## Coaching Novices (Adaptive Front Door)

**Engine mode:** user has a concrete case → run The Process directly.
**Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. Ask the plateau question: "When you practice X, what does it feel like after 15 minutes — harder, the same, or easier?" Comfort/easy = automatic = not building representations.
2. Find the expert performance structure: "Who is world-class at X? What do they perceive in the first 3 seconds that you don't?" This locates the mental representation gap.
3. Identify the discomfort zone: "What part of practicing X makes you most want to stop?" That is almost always where the gap lives.
> **[WAIT — do not advance until user responds]**
4. Design the smallest feedback loop: "How would you know within 60 seconds whether a move was correct?" Latency over 24h kills representation-building.
> **[WAIT — do not advance until user responds]**
5. Set the repetition target and stop-rule: "How many reps of this specific discomfort can you sustain before concentration drops?" (1–4 hours/day is Ericsson's ceiling.)
> **[WAIT — do not advance until user responds]**

---

## The Process

**Step 1 — Define the sub-skill with precision.** Not "get better at X" — specify the exact representational gap (e.g., "detect when counterpart shifts from positional to interest-based").
**Step 2 — Find or construct the feedback mechanism.** Latency >24h breaks action-result association. Expert feedback > peer one level above > simulation with ground truth.
**Step 3 — Diagnose the mental representation gap.** Ask: "What does an expert *see* here that I don't?" Not what they do — the doing follows from the seeing.
**Step 4 — Design the repetition targeting the gap.** Must trigger the sub-skill, produce in-session feedback, and be executable at dozens–hundreds of reps per session.
**Step 5 — Track representation progress, not output.** Output metrics lag by weeks. Track: "Am I perceiving X earlier than before?"
**Step 6 — Apply the stop-rule.** Comfort = automaticity maintenance. Redesign to a harder sub-skill. End session when concentration drops.

### Output: Practice Design Artifact

```
Target sub-skill (precise): [specific representational gap]
Expert mental representation: [what expert perceives that I currently don't]
Current representation gap: [specific failure mode]
Feedback — Source / Latency / Reliability:
Repetition — Exercise / Volume / Duration / Frequency:
Progress indicator (representation-level, not output): [what I will perceive by Week N]
Stop-rule triggers: comfortable → redesign; concentration drops → end; latency >24h → redesign
```

*→ Method in Action: [Berlin Violin Study (1991–1993)](examples/berlin-violin-study-1991-1993.md) · [Franklin's Spectator Method](examples/franklin-spectator-writing-method.md)*
*→ 2026 lens: [Keeping Skill Alive When AI Does the Reps (2024–2026)](examples/skill-atrophy-when-ai-does-the-reps-2024-2026.md)*

---

## Practice Design Domain Packs

**Medicine/Surgery:** sub-skill: laparoscopic tissue manipulation; feedback: simulator + debrief within 1h; rationalization to reject: "I'll improve with more cases."
**Writing:** sub-skill: eliminate nominalization in first-draft prose; feedback: rewrite published paragraphs vs original; rationalization: "I write every day."
**Investment:** sub-skill: identify customer concentration risk from footnotes in 20 min; feedback: 50-case retrospective library with outcomes.

Contribute packs via the deciqAI repo — requires sub-skill, expert representation, feedback latency, and common rationalization.

---

## Applying It Well

- Target representations, not outcomes — ask "What does the expert *perceive* that I don't?"
- Make feedback faster — redesign question: "How do I get a reliable signal within 60 seconds?"
- Comfort signals time to redesign, not celebrate.
- 1–4 genuine hours/day is Ericsson's hard ceiling; volume in degraded concentration reinforces errors.
- Require expert think-alouds or annotated examples — you cannot design practice you cannot see.

*→ Primary sources: [references/sources.md](references/sources.md)*

---

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "I've been doing this for 10 years." | Duration is not deliberate practice. Years in automaticity = maintenance, not development. |
| [D] "I practice every day." | Comfortable daily repetition is automaticity reinforcement, not representation-building. |
| [D] "More cases/reps will help." | Only if structured to exceed current capability with rapid feedback. Otherwise more reps deepen the rut. |
| [D] "I can give myself feedback." | Self-feedback confirms what you already believe. External feedback from someone who sees the expert standard is required. |
| [D] "The discomfort means I'm doing it wrong." | Discomfort is the signal you are in deliberate practice. Comfort means automaticity. |
| [D] "My metrics are going up." | Output lags representation by weeks and is confounded by external factors. |
| *→ Add [O] entries after each real use — paste the actual failure pattern* | *What went wrong and why* |

---

## Red Flags / Verification

- Sessions feel comfortable — automaticity has absorbed the activity.
- Feedback latency measured in days — action-result association cannot form.
- Practitioner describes what expert *does* but not what they *perceive* — no representational target.
- Practice volume cited as expertise without verifying hours were deliberate.
- [ ] Sub-skill = specific representational gap; feedback latency <24h; expert representation identified.
- [ ] Reps: dozens per session; stop-rule applied; progress tracked at representation level not output level.

---

*Part of **deciqAI Knowledge Skills** — 223 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/deliberate-practice** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
