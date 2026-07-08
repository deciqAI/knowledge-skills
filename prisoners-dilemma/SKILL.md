---
name: prisoners-dilemma
description: "Activate when: user asks 'why does everyone keep doing X when it's obviously bad for all of us', 'how do we get out of this race to the bottom', 'should we trust them not to defect', 'we'd both be better off cooperating but it never happens', 'is this a prisoner's dilemma / Nash equilibrium / tragedy of the commons / race to the bottom'.
  Do NOT activate when: the situation is zero-sum (one side's gain is the other's loss) — use a different game model; or when the parties already have a long-established repeated relationship with observable moves — use repeated-games-reputation instead."
---

# Prisoner's Dilemma

## Overview

Whatever the other party does, **each player is individually better off defecting** — so both defect, and both end up worse than mutual cooperation. This is the structural skeleton beneath price wars, arms races, overfishing, and ad spend spirals. The problem is never character; it is structure. Exhortations to cooperate fail. Change the matrix.

Composes with: [`second-order-thinking`](../second-order-thinking/SKILL.md) for matrix redesign · [`expected-value-and-kelly`](../expected-value-and-kelly/SKILL.md) for probabilistic payoffs · [`repeated-games-reputation`](../repeated-games-reputation/SKILL.md) for the iterated-game case.

## When to Use

- Two or more parties **would each do better cooperating**, but cooperation keeps failing to materialize
- Situation involves **price competition, capacity races, advertising arms races, or commons-style resource depletion**
- You are about to **negotiate or enter a partnership** and want to know whether the structure makes betrayal individually rational
- Someone asks directly about "prisoner's dilemma," "tragedy of the commons," "race to the bottom," or "Nash equilibrium"

**When NOT to use:** zero-sum games · pure coordination problems (Schelling) · long transparent repeated game with established reputations (use [`repeated-games-reputation`](../repeated-games-reputation/SKILL.md)) · low-stakes reversible decisions

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is (≤2 sentences): some situations look like "people being stubborn" but are actually a structural trap — given the rules, defecting is individually rational, and exhorting people to cooperate won't work; you have to change the structure.
2. Check fit against When to Use / When NOT to use. If it's zero-sum or pure coordination, point elsewhere.
3. Elicit their real situation. Get a concrete case (a partnership, a market, a negotiation). > **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time with their input — payoff matrix first, then dominant-strategy reasoning, then escape options. > **[WAIT — do not advance until user responds]**
5. Close by naming the one escape mechanism that fits their situation — repetition, reputation, enforcement, or matrix-change — and why that one rather than the others. > **[WAIT — do not advance until user responds]**

## The Process

Run the **Game Diagnosis**. Diagnose first, then redesign.

1. **State the players and choices.** Who are the parties? What are the two actions each can take? If you cannot reduce the situation to a small number of players and moves, the PD lens probably doesn't fit.
2. **Write the payoff matrix.** Fill in all four cells: (C,C), (C,D), (D,C), (D,D). Use real numbers or ordinal rankings (1st-best through 4th-worst). **The diagnosis requires numbers** — you cannot identify the structure by intuition alone.
3. **Check whether it is a Prisoner's Dilemma.** The defining ordering: **T > R > P > S** (and typically 2R > T + S). If T > R > S > P it is Chicken. If R > T there is no dilemma.
4. **Identify the dominant strategy.** In a true PD, "defect" dominates regardless of what the other player does (T > R; P > S). This is why the trap is structural.
5. **Identify the equilibrium.** Both defect → both get P, even though both prefer R. Nash equilibrium = the trap.
6. **Design the escape.** Four mechanisms: **Repetition** (shadow of the future); **Reputation** (third-party observation); **Enforcement** (contract/law changes payoffs); **Matrix transformation** (vertical integration, side payments, pre-commitment devices).
7. **Pick the right escape and test it.** Each mechanism has costs and prerequisites — diagnose which is *actually available*. Re-draw the post-escape matrix: if defection is still dominant, the escape is theatrical.

### Output: the Game Diagnosis

```
# Game Diagnosis: <situation>
Players: <P1>: C or D | <P2>: C or D
Matrix: (C,C)=R,R  (C,D)=S,T  (D,C)=T,S  (D,D)=P,P  [true PD: T>R>P>S]
Game type: <PD | Chicken | Coordination | Zero-sum | Other>
Dominant strategies / Nash equilibrium / Pareto-optimum / Gap (the trap)
Why "just cooperate" fails: <structural reason>
Escape options — Repetition: <feasible?> | Reputation: <observable to whom?>
  Enforcement: <contract + penalty?> | Matrix transformation: <structural change?>
Recommended escape: <mechanism + why it changes the matrix>
Test: re-draw post-escape matrix — confirm defection is no longer dominant
```

*→ Method in Action: [Flood, Dresher, and Tucker — RAND, 1950](examples/flood-dresher-tucker-rand-1950.md) · [Live and Let Live in the WWI Trenches](examples/live-and-let-live-wwi-trenches.md)*

## Pack: Recognizing PD Patterns in the Wild

- **Pricing / oligopoly:** price wars, capacity races → vertical differentiation or consolidation. See [`pricing-strategy`](../pricing-strategy/SKILL.md).
- **Partnerships / JVs:** effort underprovision, IP withholding, joint spend free-riding → vesting, milestones, audit, or integration.
- **Commons / externalities:** tragedy of the commons, antibiotic overuse, ad spend wars → privatization, regulation, or community governance (Ostrom 1990).
- **Labor / recruiting:** salary escalation, counter-offer cycles → pre-committed comp ladders (salary-band collusion = antitrust risk).
- **Internal coalitions:** resource hoarding, founder-investor info asymmetry → centralization or pre-committed reporting cadence.

## Applying It Well

- Write the matrix before diagnosing — PD-reasoning without numbers is wishful thinking.
- Distinguish game type first: PD ≠ Chicken ≠ Coordination ≠ Zero-sum.
- Test escape by re-drawing the post-escape matrix. If defection is still dominant, the escape is theater.
- In repeated settings, invoke [`repeated-games-reputation`](../repeated-games-reputation/SKILL.md).

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "They wouldn't be so stupid as to defect — it would hurt them too" | In a true PD, defection is *not* stupid; it is **individually rational**. If you are surprised when they defect, you misdiagnosed the game or refused to write the matrix. |
| [D] "We just need to build trust" | Trust without a matrix change is theater. In a one-shot PD, trust is exactly what the matrix punishes. Identify the mechanism, then confirm the matrix changed. |
| [D] Calling every conflict a "prisoner's dilemma" | Many conflicts aren't. Zero-sum, coordination, and Chicken games all have different structures and different fixes. Write the matrix first; check T > R > P > S. |
| [D] Treating "they cheated us" as evidence of bad character rather than bad structure | If the structure punishes cooperation, defection is *what the structure produces*. Character matters at the margin; structure dominates. |
| [D] "We have a contract, so we've solved it" | A contract without enforceability is a piece of paper. Test: does defecting now trigger penalties that turn T negative? If not, the contract is rhetoric. |
| [D] "Cooperation always pays in the long run" | Only if the game is genuinely repeated indefinitely with the same parties and observable moves. In a one-shot PD, cooperation does not pay — the matrix ensures it. |
| [D] Confusing PD with Chicken (T > R > S > P) | In Chicken, mutual defection is the *worst* outcome. In PD it is second-worst. The escape mechanisms differ fundamentally. |
| [D] "We tried cooperating and they defected, so cooperation doesn't work" | One round of data is not a verdict. The escape is structural, not based on whether one prior counterpart cooperated. |
| [D] Skipping the matrix and arguing about feelings | The PD lens *only* works if you write the matrix. Even ordinal rankings are enough to diagnose. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- No payoff matrix was written (even ordinal rankings count)
- Recommendation is "just cooperate" with no mechanism making cooperation individually rational
- PD was diagnosed without confirming T > R > P > S
- Proposed escape not tested by re-drawing the post-escape matrix
- Parties assumed irrational rather than rational-and-trapped
- One-shot vs. repeated distinction ignored (different equilibria, different escapes)

## Verification

- [ ] Matrix written with at least ordinal payoffs; PD ordering T > R > P > S confirmed (or ruled out)
- [ ] Dominant strategy and Nash equilibrium stated; gap to Pareto-optimum named (the trap)
- [ ] At least three escape mechanisms considered and matched to the specific situation
- [ ] Recommended escape tested by re-drawing the post-escape matrix — defection no longer dominant
- [ ] One-shot vs. repeated distinction made; if repeated, [`repeated-games-reputation`](../repeated-games-reputation/SKILL.md) invoked
- [ ] "This party defected" (data point) distinguished from "the structure rewards defection" (actionable layer)

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/prisoners-dilemma?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=prisoners-dilemma** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
