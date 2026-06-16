---
name: principal-agent
description: "Activate when: someone asks why an employee, executive, contractor, board member, or fund manager isn't acting in the org's interest; a compensation or incentive structure is being designed; outsourcing or partnership terms are being negotiated; someone says 'agency cost,' 'moral hazard,' 'skin in the game,' or 'incentive misalignment.'
  Do NOT activate when: parties have fully aligned interests and fully observable behavior; the cost of designing a contract exceeds any misalignment (trivial-stakes interactions)."
---

# Principal–Agent Problem

## Overview

One party (the **principal**) delegates to another (the **agent**) whose interests differ and whose actions can't be fully observed — producing **agency cost**: monitoring spend + agent bonding spend + residual loss. Formalized by Jensen & Meckling (1976). Structure produces the behavior, not character — so the fix is structural.

Composes with [`signaling-games`](../signaling-games/SKILL.md), [`repeated-games-reputation`](../repeated-games-reputation/SKILL.md), [`prisoners-dilemma`](../prisoners-dilemma/SKILL.md), and [`okr-goal-setting`](../okr-goal-setting/SKILL.md).

## When to Use

- Board reviewing executive compensation; outsourcing or contractor decisions
- Employees/executives behaving in ways that puzzle leadership
- New joint venture, LP-GP fund, or platform marketplace being structured
- Someone says "agency cost," "moral hazard," "skin in the game," "fiduciary duty"

**Not when:** fully aligned interests + fully observable behavior; contract design cost exceeds the agency cost it would prevent.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** concrete case → run The Process directly.
- **Coach mode:** unfamiliar or no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-liner: when one party delegates to another whose interests differ and actions are unobservable, the agent will systematically act in ways the principal didn't want — cure is structure, not character.
2. Check fit: fully aligned + fully observable → no agency problem.
3. Elicit their specific relationship — who is principal, who is agent, what does each really want?
> **[WAIT — do not advance until user responds]**
4. Probe: what can the principal not observe? which misalignment dominates (effort / risk / time horizon / info asymmetry / multitasking)?
> **[WAIT — do not advance until user responds]**
5. Close: name the specific misalignment and one structural lever (incentive, observability, or selection).
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Identify structure**
Principal / Agent / What principal wants / What agent would do absent intervention / What principal cannot observe.

**Step 2 — Diagnose misalignment**
1-3 dominant types: effort · risk · time horizon · info asymmetry · adverse selection · moral hazard · multitasking · hidden self-dealing.

**Step 3 — Estimate agency cost**
Monitoring cost + bonding cost + residual loss = total. Order-of-magnitude is enough.

**Step 4 — Design alignment mechanisms**
(a) Incentives: equity, performance bonuses, carried interest, profit-sharing, skin in the game.
(b) Observability: audits, reporting, independent verification, public reputation systems.
(c) Selection: reference checks, work samples, trial periods, self-selection through contract design.

**Step 5 — Trade off** — optimum minimizes the *sum* of all three costs, not any single one.

**Step 6 — Accept residual cost** — quantify it, decide if acceptable, build into forecasts.

## Output: Principal-Agent Analysis

```markdown
# Principal-Agent Analysis: <relationship>
- Principal: / Agent: / Delegated task: / What principal cannot observe:
- Primary misalignment(s): / Estimated agency cost:
- Incentive mechanism: / Observability mechanism: / Selection mechanism:
- Residual cost: <amount> — Acceptable?: <yes/no>
- What changes about how we structure this:
```

*→ Method in Action: [Jensen-Meckling 1976 and the Enron Collapse, 2001](examples/jensen-meckling-1976-and-the-enron-collapse-2001.md)*

## Pack: Common Patterns (see also full table in examples)

Shareholders ↔ CEO (stock gaming) · Investors ↔ Fund manager (AUM vs returns) · Company ↔ Sales reps (discount-to-close) · Patient ↔ Doctor (procedure-volume billing) · Client ↔ Attorney (hourly billing) · Platform ↔ Users (rent extraction).

## Applying It Well

- Use multiple mechanisms: incentives + observability + selection. Mono-mechanism designs are brittle.
- Agency problems compose multiplicatively across levels — analyze each boundary separately.
- Most dangerous relationships are the unrecognized ones (framed "fiduciary" when the structure says otherwise).

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We just need to hire good people" | Structure produces behavior; good people in bad structures behave badly. |
| [D] "Our agent has skin in the game" (small stake) | Size matters — 1% equity barely shifts behavior. |
| [D] "We trust them" | Trust without structural alignment is the bonding mechanism the structure exploits. |
| [D] "We have an oversight committee" | Captured or info-starved boards don't constrain agents. Enron's board met regularly. |
| [D] "Long-term incentives align them" | Most "long-term" plans vest at 3-4 years — short relative to many decision horizons. |
| [D] "Performance metrics solve agency" | Agent optimizes the metric; principal's real interest decays (Goodhart's law). |
| [D] "This is a fiduciary relationship" | Legal duty adds recourse after the fact; structural alignment still needs designing. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- P-A relationship exists but not named or analyzed; compensation purely fixed for an outcome-sensitive role
- Observability poor — agent's behavior cannot be measured
- "We trust them" used as substitute for structural alignment
- Board or audit body captured by the agents it supposedly oversees

## Verification

- [ ] Principal and agent explicitly named
- [ ] What principal cannot observe is stated
- [ ] Specific misalignment(s) diagnosed
- [ ] Agency cost estimated (order-of-magnitude is enough)
- [ ] At least one mechanism in each of incentive, observability, selection
- [ ] Trade-offs across mechanisms acknowledged
- [ ] Residual cost accepted explicitly, not assumed away
- [ ] Exit mechanism for the principal preserved

---

*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/principal-agent?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=principal-agent** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
