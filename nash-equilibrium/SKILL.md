---
name: nash-equilibrium
description: "Activate when: user asks 'what will they do if we do X', 'how will competitors react to our pricing', 'how do I design this auction or mechanism', 'we keep ending up in a bad outcome even though everyone prefers better', or is analyzing a strategic situation with multiple rational counterparties (pricing, negotiation, M&A, regulation, platform launch). Do NOT activate when: the decision is essentially solo with no strategic counterparty; the counterparty is clearly irrational or acting on emotion rather than self-interest."
---

# Nash Equilibrium

## Overview

A **Nash equilibrium** is a stable point in multi-player interaction: a combination of strategies where no player can improve their payoff by unilaterally changing their own strategy, given others hold theirs fixed. Key properties: (1) best-response logic — the equilibrium is a fixed point of mutual best-responses; (2) equilibria can be Pareto-suboptimal (prisoner's dilemma); (3) multiple equilibria are common; (4) equilibrium does not predict the path to get there.

Composes with [`prisoners-dilemma`](../prisoners-dilemma/SKILL.md), [`repeated-games-reputation`](../repeated-games-reputation/SKILL.md), [`signaling-games`](../signaling-games/SKILL.md), [`pricing-strategy`](../pricing-strategy/SKILL.md), and [`batna-zopa`](../batna-zopa/SKILL.md).

## When to Use

- Designing pricing in a competitive market with rational rivals
- Negotiating with a sophisticated counterparty; modeling regulatory or legislative outcomes
- Evaluating M&A or partnership decisions where multiple parties react strategically
- Designing auctions, marketplaces, or platform mechanisms

**Not when:** the situation is essentially solo; the counterparty is not rational; modeling cost exceeds the decision's value.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: find the point in a multi-player situation where no one has incentive to deviate from their strategy.
2. Check fit: no rational counterparty? Nash adds less value than other frameworks.
3. Elicit their real case: who are the players, what can each do, what does each gain or lose?
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time with their input.
> **[WAIT — do not advance until user responds]**
5. Close by naming the equilibrium and recommended action; if equilibrium is bad, name a redesign option.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Specify the game:** Players · Actions per player · Payoff matrix or game tree · Information structure (full vs. private) · Sequential or simultaneous.

**Step 2 — Best-response analysis:** For each player, find the optimal action given each combination of others' strategies. The combination where everyone is best-responding is a Nash equilibrium.

**Step 3 — Identify all equilibria:** Pure-strategy (deterministic) and mixed-strategy (randomized). If multiple equilibria, identify the most plausible focal point.

**Step 4 — Evaluate quality:** Pareto-optimal? If not, what better collective outcome does the structure prevent?

**Step 5 — Act or redesign:** Play equilibrium strategy if acceptable. If bad: change rules, add repeated interaction, change payoffs, add transparency — or walk away.

**Step 6 — Plan counterparty response:** What do others do once you act? Contingency if they deviate from equilibrium.

## Output Template

```markdown
# Nash Analysis: <situation>
Players / Actions / Payoffs / Info structure / Sequential or simultaneous
Best-response analysis (per player) →
Equilibria found: <strategy combination + payoffs>
Pareto-optimal? (Y/N) | If N: better outcome + why game doesn't produce it
Decision: my action | Game redesign considered
Counterparty response plan: expected action | contingency if they deviate
```

*→ Method in Action: [Nash 1950-51 and the FCC Auctions 1994](examples/nash-1950-51-and-the-fcc-auctions-1994.md) · [Penalty Kicks and the Minimax Test](examples/penalty-kicks-professionals-play-minimax.md)*

## Pack: Application Patterns

| Domain | Typical equilibrium | Common pitfall |
|---|---|---|
| Pricing in oligopoly | Cournot markup or Bertrand marginal-cost | Assuming price-cuts go unanswered |
| Auction bidding | Bid to value (English) or shaded bid (sealed) | Ignoring winner's curse in common-value auctions |
| Platform launch | Multiple equilibria; focal point determines winner | Treating launch as solo, not a coordination game |
| M&A bidding | Strategic incumbent often overpays | Failing to model how target plays bidders against each other |
| Cartel formation | Cooperation possible if discount rate is low | Underestimating defection incentives and detection lag |

## Applying It Well

Model the game explicitly before acting. Equilibrium is not optimum — if the equilibrium is bad, redesign the game (add repetition, change payoffs, build trust). When multiple equilibria exist, use focal points or commitment devices to coordinate on the one you want.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We'll just do the right thing; no need for game theory" | The right thing depends on what others do. Without modeling reactions, you'll be surprised. |
| [D] "Game theory is too abstract for real decisions" | The 1994 FCC auction raised $617M using Nash modeling. Auction design, antitrust, military strategy are operational applications. |
| [D] "Counterparties aren't rational; theory doesn't apply" | They're often more rational than assumed. Use Nash as a baseline and adjust for behavioral deviations. |
| [D] "Multiple equilibria mean Nash isn't useful here" | Multiple equilibria mean selection matters more — use focal points, communication, commitment devices. |
| [D] "First mover always wins" | Often false. Equilibrium analysis tells you when first move helps and when it hurts. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Making a strategic decision without modeling how counterparties will respond
- Assuming counterparties will react the way you'd react (mirror-imaging)
- The equilibrium is bad and you haven't considered redesigning the game
- Playing a repeated game using single-round logic
- Multiple equilibria exist and you haven't considered which will emerge

## Verification

- [ ] Players, actions, and payoffs explicitly specified
- [ ] Best-response analysis performed for each player
- [ ] Nash equilibria identified; Pareto-optimality evaluated
- [ ] If multiple equilibria, equilibrium-selection considered
- [ ] If equilibrium is bad, game-redesign options considered
- [ ] Counterparty response plan exists for equilibrium play and deviation

---

*Part of **deciqAI Knowledge Skills** — 189 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/nash-equilibrium** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
