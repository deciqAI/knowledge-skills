---
name: theory-of-constraints
description: "Activate when: user says 'everyone is working hard but results are flat', 'where is our bottleneck', 'we keep adding capacity but throughput doesn't improve', 'backlog piling up at one stage', 'Goldratt / TOC / Five Focusing Steps', or is designing a process-improvement initiative and wants to know where to invest.
  Do NOT activate when: the system is single-step with no dependencies; the constraint is purely demand-side and supply-side analysis is irrelevant."
---

# Theory of Constraints

## Overview

**Theory of Constraints (TOC)** — Eliyahu Goldratt, 1984: throughput of any multi-step system is determined by its single bottleneck. Improving any other step produces no system-level gain. The Five Focusing Steps (Identify → Exploit → Subordinate → Elevate → Repeat) are the operational discipline.

Composes with [`pareto-principle`](../pareto-principle/SKILL.md) (TOC = Pareto applied to throughput), [`feedback-loops`](../feedback-loops/SKILL.md), [`first-principles`](../first-principles/SKILL.md), and [`mvp`](../mvp/SKILL.md) (MVP design = TOC applied to validated learning).

## When to Use

- System is producing less than desired throughput; "everyone is working hard" but results don't match effort
- Management improvement initiative or capacity investment is being planned
- Backlog or inventory accumulates at a specific step; local improvements don't translate system-wide
- Someone says "bottleneck," "throughput," "Goldratt," or "Theory of Constraints"

**Not when:** single-step system; purely demand-side constraint; problem is strategic/psychological, not operational.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete throughput problem → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: throughput is set by the slowest step — find it, fix it, ignore the rest until a new bottleneck emerges.
2. Check fit: single-step system or demand-side constraint → TOC doesn't apply.
3. Elicit their real case: what's the system? desired throughput? where does work-in-process pile up?
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time: constraint? exploiting it? subordinating everything else? elevate?
> **[WAIT — do not advance until user responds]**
5. Close by naming the constraint, action plan, and re-identification schedule.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Identify:** map all steps with capacity; find where WIP accumulates — that's the constraint.
**Step 2 — Exploit:** max output from the constraint with no new investment (eliminate idle time, defects, distractions at that step).
**Step 3 — Subordinate:** pace all other steps to the constraint's rate. Upstream: don't over-produce. Downstream: don't block. Retire local efficiency metrics that incentivize over-production.
**Step 4 — Elevate:** if still binding after Steps 2-3, add capacity at the constraint (equipment, people, redesign). Highest ROI investment in the system.
**Step 5 — Repeat:** bottleneck has moved. Return to Step 1.

## Output: TOC Analysis
```
# TOC Analysis: <system>
## System map — steps, capacity per step, actual throughput, where WIP accumulates
## Constraint — bottleneck step + evidence (WIP buildup, idle downstream, output rate match)
## Exploit — changes to maximize current constraint output (no new investment)
## Subordinate — upstream rate limits, downstream coordination, metric changes, buffer plan
## Elevate — capacity investment at constraint, cost/benefit
## Re-identification — what to monitor, likely next constraint, re-apply schedule
```

*→ Method in Action: [Goldratt's The Goal (1984) and TOC's Lineage](examples/goldratts-the-goal-1984-and-tocs-lineage.md)*

## Pack: TOC by Domain

| Domain | Typical constraint | Common error | TOC fix |
|---|---|---|---|
| Manufacturing | Specific machine/workstation | Optimizing all stations | Subordinate rest to bottleneck |
| Software dev | Code review, QA, or deploy | Push devs to write faster | Limit WIP to constraint's rate |
| Sales funnel | Specific conversion step | Add more top-of-funnel leads | Fix conversion at the bottleneck |
| Hospital ops | OR scheduling or discharge | Add beds | Find true bottleneck (often discharge) |
| Project mgmt | Critical task or shared resource | Per-task safety padding | Critical chain; project-level buffer |

## Applying It Well

- Identify the constraint with *evidence*, not intuition.
- Exploit and subordinate before elevating — most constraints yield without capital.
- Retire local efficiency metrics at non-constraints; they systematically mislead.
- Re-run Five Focusing Steps after every improvement — the constraint will move.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We need to fix all the problems" | Fix the constraint only. Non-constraint improvements produce no system gain. |
| [D] "Everyone needs to work hard" | Max output at non-constraints creates inventory, not throughput. |
| [D] "100% utilization everywhere" | Mathematically false with variability. Non-constraints need slack. |
| [D] "Local efficiency = global efficiency" | False in any multi-step system. |
| [D] "We don't have a constraint" | Finite throughput = constraint exists. Find it. |
| [D] "More technology will solve it" | Only if it addresses the constraint. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Diagnosis for throughput shortfall is "everyone needs to work harder"
- Capacity investment spread across multiple steps without constraint identification
- Inventory visibly accumulates in front of one step; no one flags it
- Local productivity metrics tracked without aggregation to system throughput
- Previous TOC gains have decayed (new constraint unmanaged)

## Verification

- [ ] System map drawn with capacity at each step
- [ ] Constraint identified with evidence (not intuition)
- [ ] Five Focusing Steps applied in order (exploit before elevate)
- [ ] Non-constraint metrics that contradict system throughput retired
- [ ] Next constraint identified after improvement; re-application scheduled

---

*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/theory-of-constraints?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=theory-of-constraints** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
