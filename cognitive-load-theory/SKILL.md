---
name: cognitive-load-theory
description: "Activate when: someone says 'this is too much to take in at once', 'learners aren't getting it despite good material', 'our onboarding is overwhelming new hires', 'why does this tutorial confuse people', 'how do I design training that actually works', 'this documentation is hard to follow', 'cognitive load', 'working memory'.
  Do NOT activate when: the audience is already expert (expertise-reversal applies — novice techniques frustrate experts); the bottleneck is motivational rather than cognitive. More: deciqai.com/s/cognitive-load-theory"
---

# Cognitive Load Theory

## Overview

Working memory holds ~4 chunks of novel information — a hard limit. Instruction that exceeds it produces no learning regardless of effort. CLT (Sweller 1988) identifies three load types: **intrinsic** (task complexity), **extraneous** (poor presentation), **germane** (schema-building effort). Target: minimize extraneous, manage intrinsic by sequencing low-to-high element-interactivity, maximize germane.

Composes with [`metacognition`](../metacognition/SKILL.md) (learners aware of limits pace themselves), [`deep-work`](../deep-work/SKILL.md) (same working-memory conditions), and `api-and-interface-design` (UX design = instructional design).

## When to Use

- Designing training, documentation, onboarding, or instructional material
- Learners aren't understanding despite good intent and reasonable material
- Diagnosing why a course / tutorial / interface is underperforming
- Someone says "cognitive load," "working memory," "too much at once," "this is overwhelming"

**Not when:** audience is already expert (expertise-reversal); bottleneck is motivational not cognitive.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete design problem → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **One-line:** when learners aren't getting it, check if working-memory load exceeds capacity — the fix is usually to reduce extraneous load, not add more explanation.
2. **Check fit.** If audience is expert, novice-friendly CLT techniques may backfire (expertise-reversal).
3. **Elicit the specific failure.** Who's learning what, where stuck, what's the current instruction?
> **[WAIT — do not advance until user responds]**
4. **Diagnose load types** one question at a time: intrinsic too high? Extraneous load sources? Expertise match?
> **[WAIT — do not advance until user responds]**
5. **Close:** redesigned instruction with specific CLT effects applied + test with target learners.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Diagnose:** Who is learning (expertise level) · What · Where stuck · Current instruction format · Overload signals (frustration, drop-off, error patterns).

**Step 2 — Identify load types:** Intrinsic (element interactivity, 1-5) · Extraneous sources (split attention / redundancy / wrong modality / irrelevant info / confusing notation) · Germane opportunity.

**Step 3 — Reduce extraneous load:** Split-attention → integrate diagram + label · Redundancy → cut duplicated text · Modality → narration over diagram, not text + text · Irrelevant → cut.

**Step 4 — Match expertise:** Novice: worked examples + heavy scaffolding · Intermediate: partial solutions + faded scaffolding · Expert: free problem-solving (CLT scaffolding now hurts — expertise reversal).

**Step 5 — Maximize germane load:** Sequence concrete→abstract · Use contrast to force schema-building · Pose questions before answers · Variable practice (same deep structure, different surface).

**Step 6 — Test and iterate:** Comprehension test with target learner (not designer) · Measure time-to-mastery · Track error patterns · Cut more extraneous load if struggle persists.

## Output Template

```markdown
# CLT-Informed Design: <instruction>
Learner (expertise): | Material: | Stuck point: | Overload signals:
Intrinsic load (1-5): | Extraneous sources: | Germane opportunity:
CLT effects applied: | Expertise match (novice/intermediate/expert):
Test plan: target learner · comprehension test · iteration trigger · owner
```

*→ Method in Action: [Sweller 1988 and the Development of CLT](examples/sweller-1988-and-the-development-of-clt.md)*

## Pack: CLT Application Patterns

| Domain | High-extraneous mistake | CLT fix |
|---|---|---|
| Software docs | Long prose separated from code | Integrate code + commentary; dual-modality |
| Onboarding | "Read these 12 documents" | Worked example: walk through 1 real task end-to-end |
| Training videos | Talking head + bullet slides | Diagram + narration; cut redundant text |
| User interfaces | Many simultaneous options | Progressive disclosure; group related items |
| Code review | Many unrelated changes in one PR | Split PRs by concern; one change at a time |

## Applying It Well

- The right response to "they're not learning" is usually to *cut* extraneous load, not add more content.
- Instructional design matters more than subject-matter expertise — a CLT-aware non-expert beats an oblivious expert.
- Expertise-reversal is real: differentiate instruction for novices vs. experts; one-size-fits-all hurts one group.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Smart people can handle it" | Working memory is hard-capped at ~4 chunks regardless of intelligence. |
| [D] "More information is better" | False above capacity threshold — additional content above the limit produces no learning. |
| [D] "We can't cut anything — it's all important" | Redundancy effect: cutting duplicated content improves comprehension. |
| [D] "Discovery learning is more engaging" | Often true, but empirically poor for novices — imposes high extraneous load. Scaffold first. |
| [D] "Worked examples are passive" | Sweller 1988: worked examples produce *more* learning than unaided problem-solving for novices. |
| [D] "Add another diagram to clarify" | If it duplicates existing content, redundancy effect makes things worse. Replace, don't add. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Learners abandon training/docs at the same point repeatedly
- "It's just complex" explains high failure rates without examining presentation
- Instruction untested with target audience before deployment
- Highly expert author unaware of expertise-reversal
- Diagram and its explanation physically separated

## Verification

- [ ] Intrinsic, extraneous, and germane load identified separately
- [ ] At least one CLT effect (split-attention, redundancy, modality) applied
- [ ] Expertise level specified and instruction matched to it
- [ ] Tested with target learners (not self-reviewed)
- [ ] Comprehension or completion metrics measured

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/cognitive-load-theory** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/cognitive-load-theory.json*
