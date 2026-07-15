---
name: confirmation-bias
description: "Activate when: user says 'we keep finding evidence that supports our view,' 'the team is all aligned on this,' 'I've done the research and it checks out,' or a decision moves forward with only supporting evidence cited. Do NOT activate when: context is explicit advocacy (legal brief, pitch deck) where one-sided argument is the design; or stakes are too low to justify structured disconfirmation."
---

# Confirmation Bias

## Overview

**Confirmation bias** is the systematic tendency to seek, interpret, remember, and weight evidence in ways that support existing beliefs — and to correspondingly miss disconfirming evidence. It is the most-replicated finding in cognitive psychology, documented across cultures, expertise levels, and IQ ranges.

The canonical proof: Wason's 1960 "2-4-6 task" showed ~80% of subjects (including PhD scientists) confidently announced a wrong rule after testing only sequences they expected to confirm — never proposing a sequence designed to refute the hypothesis.

Composes with [`critical-thinking`](../critical-thinking/SKILL.md), [`bayesian-reasoning`](../bayesian-reasoning/SKILL.md), [`abductive-reasoning`](../abductive-reasoning/SKILL.md), and [`metacognition`](../metacognition/SKILL.md).

## When to Use

- A team is converging on a single answer too quickly
- You feel confident about a claim and haven't looked for evidence against it
- Research or due diligence keeps "validating" existing beliefs
- Someone says "cherry-picking," "echo chamber," or "looking for what you want to see"
- A team is committing to an AI thesis (AI capex, AI valuations, or AI adoption) by citing confirming demos and adoption while discounting failed eval results

**Not when:** explicit advocacy context; very low-stakes decision; cost of disconfirmation exceeds value of decision.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-liner: before trusting evidence that supports your view, ask what would have changed your mind — and whether you actually looked for it.
2. Check fit against When to Use / When NOT to use.
3. Elicit the specific claim and evidence cited.
> **[WAIT — do not advance until user responds]**
4. One question at a time: what would falsify this? Did you look for that? What's the strongest counter-evidence? How did you treat it?
> **[WAIT — do not advance until user responds]**
5. Close: name the falsification test + structural countermeasure (Devil's advocate, red team, blind evaluation).
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — State claim:** Claim / Evidence cited / Confidence level.

**Step 2 — Construct falsification:** What observation would falsify this? What would you expect if wrong? Has anyone looked for that? *(If you can't articulate falsification, you have a description, not a hypothesis.)*

**Step 3 — Audit evidence-seeking:** Sources consulted — belief-aligned? Strongest case against sought? Evidence encountered and dismissed?

**Step 4 — Re-evaluate ambiguous evidence:** Of evidence cited, how much is unambiguous vs. ambiguous-read-as-supporting? Does the opposite reading fit equally? *(If yes, it's interpretation, not evidence.)*

**Step 5 — Install structural countermeasure:** Devil's advocate (rotated, mandatory) · Red team · Pre-mortem (Klein 2007) · Blind evaluation · Falsification-first design (three refuting cases before one confirming).

**Step 6 — Establish update conditions:** What would convince me I'm wrong? When will I formally re-examine? Who is empowered to push back?

## Output Template
```
Claim: / Evidence: / Confidence:
Falsification: what would falsify it / has it been tested:
Evidence audit: sources (aligned vs counter) / counter-evidence treatment:
Ambiguous evidence: amount / does opposite reading fit:
Countermeasure: [type] / Owner:
Update conditions: trigger / re-examination date:
```

*→ Method in Action: [Peter Wason's 2-4-6 Task, 1960](examples/peter-wasons-2-4-6-task-1960.md) · [The FBI Mayfield Fingerprint Misidentification, 2004](examples/2004-fbi-mayfield-fingerprint-misidentification.md)*
*→ 2026 lens: [The AI Thesis War (2023–2026)](examples/ai-thesis-confirmation-2023-2026.md)*

## Pack: Confirmation Bias Patterns

| Domain | Common manifestation | Countermeasure |
|---|---|---|
| Product | Building features based on early-adopter feedback only | Cohort retention; non-user interviews |
| Investment | Reading only the bull case for a held position | Pre-commit short thesis; quarterly "kill the position" |
| Hiring | Post-hoc rationalization of intuitive hire | Structured rubric; reference checks before offer |
| Debugging | Looking only where you think the bug is | Bisect elimination; alternative-hypothesis tests |

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "I've been doing this for years; I know" | Experience compounds confirmation bias if not paired with deliberate disconfirmation. |
| [D] "I have an open mind" | Self-report correlates poorly with measured open-mindedness. When did you last change your mind on counter-evidence? |
| [D] "I considered the alternative" | Considering ≠ stress-testing. Did you actively seek evidence the alternative is correct? |
| [D] "The evidence overwhelmingly supports my view" | Overwhelming-feeling evidence is exactly what confirmation bias produces. |
| [D] "I'm a critical thinker / scientist / analyst" | Wason's PhD subjects had the same bias. Structural countermeasures work; personal vigilance does not. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Team converged quickly on a single answer; evidence cited is belief-aligned
- No one tasked with finding flaws; disconfirming evidence dismissed as "biased"
- Hypothesis not stated in falsifiable form; hypothesis-former is also the tester

## Verification

- [ ] Claim stated in falsifiable form; specific falsifying observation named
- [ ] Counter-evidence actively sought (not just acknowledged)
- [ ] Ambiguous evidence re-evaluated against the opposite hypothesis
- [ ] Structural countermeasure installed (not just personal vigilance)
- [ ] Update conditions and re-examination point specified

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/confirmation-bias** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
