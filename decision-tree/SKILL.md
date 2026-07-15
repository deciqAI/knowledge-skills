---
name: decision-tree
description: "Activate when: user says 'help me choose between two options with different risks', 'I need to map out what could happen if we go with X', 'we have a sequential decision — first we do A then depending on results we do B', 'what is the expected value of this investment given uncertain demand'. Do NOT activate when: the decision is a one-shot choice with no sequential stages (use simple EV instead); probabilities cannot be estimated even roughly and uncertainty is too deep to quantify."
---

# Decision Tree

## Overview

A **decision tree** maps a multi-stage decision: decision nodes (squares) for choices you control, chance nodes (circles) for outcomes you don't, probabilities on every branch, payoffs at the leaves — then rollback right-to-left to get expected value at the root. First systematized by John F. Magee (HBR, 1964); formalized by Howard Raiffa (1968). Its biggest value: converting "I feel we should expand" into "what probability do you assign to high demand?" — making every assumption explicit and contestable.

Composes with [`expected-value-and-kelly`](../expected-value-and-kelly/SKILL.md) (EV scaffold + bet sizing), [`probabilistic-thinking`](../probabilistic-thinking/SKILL.md) (calibration per node), [`inversion`](../inversion/SKILL.md) (rollback = working outcomes backward), [`mece`](../mece/SKILL.md) (branches must be MECE so probabilities sum to 1.0).

## When to Use

- Decision has sequential stages (decide → learn → decide again)
- Outcomes uncertain; probabilities can be estimated (even roughly)
- Payoffs quantifiable (NPV, revenue, cost, lives saved)
- Multiple stakeholders need a shared visual model to align on assumptions
- Sizing a big irreversible bet under AI uncertainty — build vs. buy vs. wait on AI capex, a fab investment, or committing while AI adoption / AI valuations are unproven

**Not when:** one-shot choice with no stages; probabilities unestimable; payoffs purely qualitative; branch set too large (use scenario planning instead).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete multi-stage decision → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **One-line:** a decision tree converts "I feel" into "what probability do you assign?" — making assumptions explicit so they can be argued about.
2. **Check fit.** Sequential stages? Uncertain outcomes? Quantifiable payoffs? If yes to all three, a tree applies.
3. **Elicit their real case.** What's the initial choice? What uncertain outcomes follow? What payoffs result?
> **[WAIT — do not advance until user responds]**
4. **Run The Process one step at a time** with their input — draw structure, assign probabilities, assign payoffs, roll back.
> **[WAIT — do not advance until user responds]**
5. **Close** by naming the insight: the threshold at which the recommendation flips, and whether to gather more data.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Root:** Define the decision (options, timeline, decision-maker). Draw a square; each option is a branch.

**Step 2 — Chance nodes:** For each branch, identify uncertain events → draw circles. Branches at each circle must be MECE; probabilities must sum to 1.0.

**Step 3 — Probabilities:** Assign a number (0.0–1.0) + documented basis to every branch. Reject "50/50" without justification.

**Step 4 — Payoffs:** Assign consistent-unit payoffs (NPV, revenue, etc.) to every terminal leaf.

**Step 5 — Rollback:** Right to left — EV at each circle = Σ(p × value). At each square, keep highest EV branch; mark losers //.

**Step 6 — Sensitivity + stop-rule:** Find the probability threshold where the optimal choice switches. Compute EVPI = EV(perfect info) − EV(best decision now). If EVPI < cost of data: decide now. If EVPI > cost: gather data first. Stop refining when the leading option's EV advantage exceeds the value of further analysis.

## Output Template
```
Decision Tree: <topic>
Options: A / B  |  Timeline:
Tree: [node-by-node description]
Probabilities: Node | Branch | p | Basis
Payoffs: Path | Value | Unit
Rollback: Option A EV= / Option B EV= / Optimal=
Sensitivity: flips when p([key branch]) > [threshold]  |  EVPI=
Recommendation: [option] — holds if [condition]; flips if [condition]
```

*→ Method in Action: [Magee 1964 — Chemical Plant Investment (HBR)](examples/magee-1964-chemical-plant-investment-hbr.md) · [Eisenhower's D-Day Weather Decision](examples/eisenhower-1944-d-day-weather-decision.md)*
*→ 2026 lens: [A Chipmaker's Leading-Edge Fab Investment Under AI Uncertainty (2024–2026)](examples/chipmaker-leading-edge-fab-investment-2024-2026.md)*

## Pack: Decision Tree by Domain

| Domain | Root Decision | Key Uncertainty | Payoff | Watch For |
|---|---|---|---|---|
| Capital investment | Large vs. small plant | Demand scenarios | NPV | Overconfident demand p |
| R&D portfolio | Fund vs. kill | Technical success; adoption | Revenue × p | Ignoring base-rate failure |
| Litigation | Settle vs. litigate | Win/lose; damages | Expected settlement | Anchoring on best case |
| Product launch | Now vs. delay | Market reception; competitor | Revenue per scenario | Missing competitor-first branch |
| M&A | Acquire vs. pass | Integration; synergy | Post-acquisition EV | Paying for performance peak |

## Applying It Well

- Draw before calculating — structure surfaces hidden assumptions
- Assign probabilities before revealing your preferred option
- Run sensitivity before concluding; find the switchover threshold and EVPI
- Audit missing branches explicitly: "what did we leave out?"

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Rationalization (Fake Move) | Reality |
|---|---|
| [D] "This is strategic — we don't need numbers." | Without numbers the tree is just a picture. Force strategic disagreements to become numerical ones. |
| [D] "We can't estimate probabilities." | Even rough estimates beat implicit zero/one assumptions. Every un-numbered branch already has an implicit probability. |
| [D] "The tree chose A — we're done." | Holds only at assigned probabilities. Sensitivity analysis is mandatory before concluding. |
| [D] "We enumerated all branches." | Trees are always simplifications. Ask explicitly: what branches are missing? |
| [D] "It's 50/50 — we just don't know." | 50/50 is a claim requiring justification. What base rate supports it? |
| [D] "My gut says B even though the tree says A." | Gut = implicit tree with different probabilities. Find which number your gut is using and put it in. |
| [D] "The tree gave a recommendation — it must be right." | GIGO: garbage probabilities produce garbage recommendations. Calibrate inputs first. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Probabilities verbal only — no numbers written | Chance-node probabilities don't sum to 1.0
- No sensitivity analysis performed | Terminal payoffs in mixed units across branches
- Probabilities assigned post-hoc to justify a pre-decided conclusion | No missing-branch audit

## Verification

- [ ] Root decision defined; all options enumerated
- [ ] All chance nodes MECE; probabilities sum to 1.0 at each node
- [ ] Every probability has documented basis
- [ ] All terminal payoffs in same unit and discount rate
- [ ] Rollback verified numerically at every node
- [ ] Sensitivity complete — switchover threshold identified
- [ ] EVPI calculated; data-gathering decision made
- [ ] Missing-branch audit performed; recommendation states conditions it holds and flips
---
*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/decision-tree** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
