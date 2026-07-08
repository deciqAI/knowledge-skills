---
name: mece
description: "Activate when: user says 'decompose this', 'structure this thinking', 'MECE', 'issue tree', 'Minto Pyramid', 'how do we cover all the cases without double-counting', a problem feels too big to think about cleanly, a list of options is messy or overlapping, an analysis keeps going in circles, or a presentation needs to survive hard scrutiny.
  Do NOT activate when: the problem is trivially small (lunch decisions), or the user is in purely creative/generative mode where premature structure would constrain exploration."
---

# MECE (Mutually Exclusive, Collectively Exhaustive)

## Overview

**MECE** is a decomposition principle: break a problem, set of options, or population into sub-groups that are **Mutually Exclusive** (no overlap) and **Collectively Exhaustive** (no gaps) — every relevant item covered exactly once. Operationalized by **Barbara Minto** at McKinsey (1963–1973) in *The Pyramid Principle* (1973; 3rd ed. 2002). The test: sum the pieces back to the whole; if they don't sum cleanly, the decomposition is broken.

**Compose:** use [first-principles](../first-principles/SKILL.md) to reach root variables; [pareto-principle](../pareto-principle/SKILL.md) to find load-bearing branches; [critical-thinking](../critical-thinking/SKILL.md) to test whether categories are the *right* ones; [occams-razor](../occams-razor/SKILL.md) when multiple MECE structures fit — pick the simplest.

## When to Use

- Problem feels **too big to think about cleanly** — surface area is unclear
- **List of options** is messy or overlapping — competing answers that aren't parallel
- Analysis is **going in circles** — same issues reappear because they're not separated
- **Presentation** must convince hard-to-convince listeners
- Team converging on a hypothesis **without considering the full space** of alternatives
- Someone says: *"MECE," "decompose this," "issue tree," "structure this thinking"*

**When NOT to use:** trivially small problem; purely creative/generative mode; genuinely non-decomposable question (some ethical/aesthetic problems resist this); decomposition already known and well-trodden.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: MECE is **breaking a problem into pieces that don't overlap AND don't leave gaps** — every relevant thing is covered exactly once. The check: do the pieces sum back to the whole?
2. Check fit against When to Use / When NOT to use. Trivial problem → redirect. Creative exploration → not yet.
3. Elicit their specific problem to decompose. *"My business has problems"* is too vague; need a concrete question — *"why is our gross margin declining?"*, *"what are the options for resolving this escalation?"* > **[WAIT — do not advance until user responds]**
4. Walk through Level 1 of the decomposition one step at a time, check ME and CE, then Level 2 if needed. > **[WAIT — do not advance until user responds]**
5. Close by naming the load-bearing branch — they leave knowing where to focus, confident nothing important is missing. > **[WAIT — do not advance until user responds]**

## The Process

Run the **MECE Decomposition**: define the whole → propose top split → check ME AND CE → iterate → identify load-bearing branch.

1. **State the whole precisely.** "Our business" is not the whole; "*revenue this fiscal year by customer segment*" is.
2. **Propose a top-level split (2–7 categories).** Common dimensions: customer segment, geography, product line, time period, formula component (revenue = price × volume), life-cycle stage, cause type.
3. **Test Mutual Exclusivity.** For each pair: is there any case that belongs to both? If yes, refine until no item can belong to more than one branch.
4. **Test Collective Exhaustiveness.** What case is *not* covered? Add an explicit "other" or "future" branch if needed.
4a. **Sum-to-whole test.** Do the branches add up to the whole? If not, identify what's missing or double-counted.
5. **Recurse if needed.** Apply MECE to each branch. Stop when each leaf is actionable.
6. **Identify the load-bearing branch.** Per [pareto-principle](../pareto-principle/SKILL.md), one or two branches carry disproportionate weight.
7. **Document the structure.** The issue tree / Minto pyramid diagram is the standard shareable artifact.

### Output: the MECE Decomposition

```markdown
# MECE Decomposition: <whole problem / question>
## The whole: <measurable, bounded subject>
## Top-level split (Level 1): Branch A / Branch B / Branch C / (Other if needed)
## ME test: A ∩ B = ? / A ∩ C = ? (refine until empty)
## CE test: What is missing? / Sum = whole? (yes/no + what's added)
## Sub-decomposition (Level 2, only if needed): A → A1 / A2 ...
## Load-bearing branch: <branch with most insight per effort>
## Action implied: <specific action this decomposition makes obvious>
## Alternative decompositions considered: <why this dimension over others>
```

*→ Method in Action: [Lou Gerstner's IBM Turnaround Decomposition (1993)](examples/lou-gerstner-ibm-turnaround-decomposition-1993.md)*

## Decomposition Packs

Canonical MECE dimensions by domain: **Profit/margin** — Revenue = Price × Volume; Cost = Fixed + Variable. **Customer segmentation** — industry / size / use case / buying mode. **Strategy options** — axis of competition; build/buy/partner; time horizon. **Failure-mode** (see [inversion](../inversion/SKILL.md)) — technical / human / process / environmental.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Applying It Well

- **MECE is the test, not the brainstorm.** Propose first; then check ME AND CE. Most people skip the check.
- **The dimension matters more than the depth.** Wrong Level 1 dimension makes Level 2 useless. Try 2–3 before committing.
- **Sum back to the whole.** If branches don't sum, the decomposition is broken.
- **"Other" is sometimes the right branch.** Forcing named categories creates fake exhaustiveness.
- **Stop when the leaf is actionable.** Decomposing past action is paralysis.

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] **Claiming MECE without testing** | "These are the three options" is not MECE until tested. Run the overlap check AND the gap check. |
| [D] **Overlapping categories** ("Big customers / Important customers") | These overlap. Refine — perhaps by quantitative threshold — until disjoint. |
| [D] **Missing the residual** | Geography split into "North America / Europe / Asia" misses Latin America, Africa, Oceania. Add "Other" explicitly. |
| [D] **Wrong dimension chosen** | Product-line decomposition was MECE but missed the customer-buying-mode dimension that mattered. Try alternatives. |
| [D] **Decomposing trivial problems** | Lunch decisions don't need MECE. Reserve it for problems with large surface area. |
| [D] **Going too deep** | Decomposing past actionable leaves produces complexity without insight. |
| [D] **Fake "Other" branches** | An "Other" capturing > 30% of the whole means the dimension is wrong. Rethink the split. |
| [D] **Not summing back to the whole** | The most reliable MECE test is arithmetic. Skipping it lets broken decompositions look fine. |
| [D] **Treating MECE as the analysis** | MECE produces *the structure*; analysis happens *within* the structure. A MECE diagram with no investigation is wall art. |
| [D] **Single decomposition without alternatives** | Most analytical disagreements are about *which* decomposition. Consider 2–3 dimensions before committing. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- "These are MECE" stated without overlap and gap tests
- An "Other" category capturing > 30% of the whole
- Categories that share obvious cases (e.g., "Big customers" and "Important customers")
- The decomposition was inherited / copied without checking
- The branches don't sum to the original whole
- Only one decomposition dimension was considered
- The decomposition goes 5+ levels deep without action at the leaves

## Verification

- [ ] Whole stated precisely and measurable; top-level dimension named and justified
- [ ] ME explicitly checked between every pair; CE checked (missing-case test)
- [ ] Branches sum back to the whole (arithmetic test)
- [ ] Each leaf is *actionable*; at least one alternative dimension was considered
- [ ] Load-bearing branch identified

---

*Part of **deciqAI Knowledge Skills** — 189 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/mece** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
