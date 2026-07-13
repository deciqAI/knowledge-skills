---
name: comparative-advantage
description: "Activate when: user says 'should I do this myself or delegate,' 'I'm the best at X so I should do it,' 'should we outsource or build in-house,' 'how should we divide work on the team,' 'is it worth hiring someone for this.' Do NOT activate when: the situation is genuinely single-task with no trade-off; the user is asking about competitive strategy between companies (use Porter's Five Forces instead)."
---

# Comparative Advantage

## Overview

Mutually beneficial specialization depends on *relative* productivity, not absolute. Even if you are better than everyone else at every task, you gain by focusing on tasks where your opportunity-cost ratio is lowest and delegating the rest. The right question is not "am I better at X than them?" but "am I better at X *relative to Y* compared to how they are?"

Proved by David Ricardo (1817); called "the only proposition in economics that is both true and non-obvious" by Paul Samuelson (1969).

Composes with [`opportunity-cost`](../opportunity-cost/SKILL.md), [`pareto-principle`](../pareto-principle/SKILL.md), [`circle-of-competence`](../circle-of-competence/SKILL.md), [`theory-of-constraints`](../theory-of-constraints/SKILL.md).

## When to Use

- Founder time allocation across activities; team division of labor
- Build vs. buy / in-house vs. outsource decisions
- M&A decisions; international operations / supply chain design (e.g. AI-chip re-shoring, chip export controls, semiconductor vertical integration)
- Personal career or skill specialization decisions

**Not when:** situation is genuinely single-task (no B to trade off); transaction costs swamp any gains; alternative producer's capacity is fully constrained.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete allocation decision → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: the right test is not "am I better than them at this?" but "am I better at this *relative* to what else I could be doing?"
2. Check fit: if single-task or transaction costs very high, analysis adds limited value.
3. Elicit the case: what are you considering doing? What else could you do with the time? Who else could do it?
> **[WAIT — do not advance until user responds]**
4. One question at a time: what's your opportunity cost of the focal task? What's the alternative producer's OC? Where do ratios diverge? Are transaction costs material?
> **[WAIT — do not advance until user responds]**
5. Close: specialization recommendation + transaction-cost caveat + monitoring plan.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Producers and tasks:** name Producer 1, Producer 2, Task A, Task B, time horizon.

**Step 2 — Productivity:** estimate value-per-hour (or units/time) for each producer at each task.

**Step 3 — Opportunity-cost ratios:** Producer 1's OC of Task A = Task B output forgone per unit of Task A. Repeat for Producer 2. Lower OC = comparative advantage in that task.

**Step 4 — Specialization:** each producer focuses on their comparative-advantage task. Total output rises.

**Step 5 — Transaction costs:** add coordination, communication, quality-risk, and information-asymmetry costs. If net benefit positive: specialize. If net negative: produce in-house.

**Step 6 — Implement and monitor:** document arrangement, set quality monitoring, schedule re-evaluation as productivity ratios or transaction costs shift.

## Output Template

```markdown
# Comparative-Advantage Analysis: <decision>
Producers: P1 = ___ | P2 = ___   Tasks: A = ___ | B = ___
OC of Task A — P1: ___ | P2: ___   → CA in A: P___ | CA in B: P___
Transaction costs: coordination ___ | quality risk ___ | net ___
Recommendation: P1 specializes in ___ | P2 specializes in ___
Caveats / re-eval trigger: ___
```

*→ Method in Action: [Ricardo 1817 England-Portugal + Modern Applications](examples/ricardo-1817-england-portugal-modern-applications.md) · [Samuelson's Lawyer and Typist](examples/samuelson-lawyer-typist-delegation.md)*
*→ 2026 lens: [The AI-chip supply chain — ASML, TSMC, Nvidia (2024–2026)](examples/ai-chip-supply-chain-2024-2026.md)*

## Pack: Application Patterns

| Decision | Absolute-advantage trap | Comparative-advantage answer |
|---|---|---|
| Founder time | "I'm best at everything" | Specialize in 2-3 highest-leverage activities; delegate the rest |
| Senior engineer | "I should code everything" | Architect, mentor, hard problems; delegate routine tasks |
| Manufacturing | "We could build our own factory" | Outsource to specialist; focus on design/marketing/sales |
| Customer support | "I know the product best" | Hire CS specialists; handle only strategic relationships yourself |

## Applying It Well

- Compute opportunity-cost *ratios*, not absolute productivity
- Transaction costs are real — factor coordination, communication, quality-monitoring
- Revisit as productivity ratios shift or transaction costs change

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "I'm best at this, so I should do it" | Right question is OC ratio. You can be best at it and still not be the one who should do it. |
| [D] "I can do it faster than they can" | An hour spent doing it is an hour not spent on higher-OC work. Calculus often favors delegation. |
| [D] "Quality will drop if I delegate" | Compute: does the quality drop outweigh the OC gain from focusing on higher-CA activities? Often no. |
| [D] "Outsourcing is risky" | Transaction costs and quality risk are part of the calculus — compute them, don't assume. |
| [D] "Comparative advantage is academic; real life is different" | The framework underpins modern supply chains, team specialization, and founder time-allocation. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Founder doing many tasks personally despite team members who could do them
- "I'm best at X" used to justify allocation instead of OC analysis
- Outsourcing decisions based on absolute productivity rather than opportunity cost
- Transaction costs ignored entirely or used as a blanket excuse

## Verification

- [ ] Both producers and both tasks explicitly specified
- [ ] Productivity or value-per-hour estimated for each combination
- [ ] Opportunity-cost ratios computed; comparative-advantage assignment determined
- [ ] Transaction costs considered; net benefit computed
- [ ] Decision documented; re-evaluation conditions specified

---

*Part of **deciqAI Knowledge Skills** — 225 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/comparative-advantage** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
