---
name: repeated-games-reputation
description: "Activate when: user asks how to build trust with a repeat counterparty, whether to retaliate after a partner defected, how to design a reputation system, whether a long-term relationship can survive betrayal, or says 'shadow of the future / tit-for-tat / burn this bridge / they'll remember this / build credibility.' Do NOT activate when: interaction is genuinely one-shot with no third-party observers (use prisoners-dilemma), or situation is zero-sum competition where repetition entrenches rivalry. More: deciqai.com/s/repeated-games-reputation"
---

# Repeated Games & Reputation

## Overview

When parties repeat — or third parties observe — defection costs tomorrow's cooperation, flipping the Prisoner's Dilemma. Axelrod's 1979–1981 tournaments proved cooperation wins empirically; the Folk Theorem (Fudenberg & Maskin 1986) proved it mathematically. This skill diagnoses when cooperation is sustainable (discount factor check), selects the right strategy (TFT vs Generous TFT vs Pavlov), and engineers reputation infrastructure for markets where parties don't repeat directly. Composes with [`prisoners-dilemma`](../prisoners-dilemma/SKILL.md) · [`second-order-thinking`](../second-order-thinking/SKILL.md) · [`signaling-games`](../signaling-games/SKILL.md).

## When to Use

Apply when:
- A relationship is **expected to continue** between the same parties (supplier-buyer, employer-employee, GP-LP, founder-investor, customer-platform)
- Even in a one-shot direct interaction, **third parties observe** the move and adjust their willingness to play with you
- You're designing **a platform or marketplace** that needs strangers to cooperate — reputation infrastructure is the architectural question
- You're trying to **escape a defection trap** and the candidate escape is "repetition" or "reputation"
- A partnership keeps fragmenting — diagnose whether δ is too low or observation is broken
- Trust/safety reputation is shaping who wins **AI adoption and AI-native competition** — where capability converges, a bad launch or safety incident reprices every future round of enterprise adoption (and the AI capex supercycle only lengthens the shadow of the future)

**When NOT to use:**
- Genuinely one-shot with no third-party observability → use [`prisoners-dilemma`](../prisoners-dilemma/SKILL.md)
- Parties are **about to exit** (last round of finite game) — backward induction risk; standard repeated-game logic can fail
- Zero-sum situation — repetition can entrench rivalry rather than dissolve it
- "Repetition" is only nominal — rotating counterparties who don't talk = effectively one-shot

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete repeated/reputational situation → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: one-shot rationality says "defect"; repeated rationality says "cooperate if the future matters enough and your opponent will see your move." This skill works out the math of *enough* and *will see*.
2. Check fit against When to Use / When NOT to use. If genuinely one-shot, redirect to [`prisoners-dilemma`](../prisoners-dilemma/SKILL.md).
3. Elicit their real repeated relationship or reputational concern — never run on a hypothetical when a real one is available.
> **[WAIT — do not advance until user responds]**
4. Walk the Analysis one element at a time: discount factor, observation structure, retaliation feasibility, forgiveness design.
> **[WAIT — do not advance until user responds]**
5. Close by naming the one strategic move (TFT variant, reputational signal, structural change to δ or observation) that fits their situation.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Repeated-Game Analysis** across these steps:

1. **Establish true repetition.** Indefinite/infinite → folk-theorem logic applies. Finite with known endpoint → backward induction risk; add uncertainty or commitment devices.
2. **Estimate δ.** Cooperation threshold: δ ≥ (T − R) / (T − P). Below threshold → change the structure first; no strategy design saves it.
3. **Confirm observability.** Perfect → TFT variants work. Noisy → Generous TFT (cooperate ~1/3 of the time after apparent defection) or Contrite TFT. Pure TFT under noise → recrimination spirals.
4. **Select strategy.** TFT (clean bilateral) · Generous TFT (noisy) · Pavlov (mixed populations) · Grim Trigger (high-stakes, credible threat only) · benchmarks: Always Defect / Always Cooperate.
5. **For reputation infrastructure:** design Observation · Aggregation · Persistence · Manipulation resistance — all four required; missing one breaks the system.
6. **Stress-test endgame.** Mitigations: endpoint uncertainty; legacy concerns; successor obligations; overlapping generations.
7. **Stop-rule:** lifetime cooperative payoff must beat one-shot defection by margin sufficient to absorb noise.

### Output template

```
Repeated-Game Analysis: <situation>
Repetition: <bilateral/reputational> | Horizon: <indefinite/finite-known/finite-unknown>
δ_actual vs δ_required=(T−R)/(T−P): <values> → Cooperation sustainable? <yes/no/borderline>
Observation: <clean/noisy> | Aggregation/Persistence/Manipulation-resistance (if reputational)
Strategy: <TFT/Generous TFT/Pavlov/Grim Trigger> | First move: <> | Retaliation: <> | Forgiveness: <>
Endgame risk: <> | Mitigations: <>
Test: <lifetime payoff vs one-shot defect>
```

*→ Method in Action: [Robert Axelrod's Computer Tournament, 1979–1981](examples/robert-axelrod-computer-tournament-1979-1981.md)*
*→ 2026 lens: [Trust Reputation as Strategy in the AI Race (2024–2026)](examples/ai-trust-reputation-enterprise-adoption-2024-2026.md)*

## Pack: Reputation Infrastructure Patterns

Six documented patterns (observation mechanism → known failure mode):
eBay/Airbnb (post-transaction ratings → 5-star inflation) · FICO (payment history → thin-file bias) · GitHub (commit history → popularity ≠ quality) · B2B scorecards (procurement records → approved-list lock-in) · Professional reputation (peer review + regulatory filings → old-boys' network slow to update) · Sovereign credit (macro indicators → rating-agency capture)

## Applying It Well

Diagnose δ first — wrong discount factor invalidates everything downstream. In noisy environments (most real ones), add forgiveness. Never confuse bilateral repetition (TFT) with third-party reputation markets (requires infrastructure). Legibility is a strategic asset: a simple strategy your counterparty can model beats a clever one they cannot.

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "We have a long relationship, so they won't defect" | The relationship's *length* doesn't matter; the **shadow of the future** does. If their discount factor is low (they're about to retire, the firm is being sold, they have alternative partners lined up), past relationship duration provides no protection. Run the δ check, not the nostalgia check. |
| [D] "Reputation will discipline them" | Only if the reputation system has all four pieces (observation, aggregation, persistence, manipulation resistance) and is actually consulted. Many "reputation matters" claims are wishful — the system is broken on one of the four pieces. |
| [D] Applying TFT in a noisy environment without forgiveness | Pure TFT under noise enters mutual-recrimination death spirals. If observation has error, use Generous TFT, Contrite TFT, or Pavlov. Recommending TFT without checking noise level is a documented failure. |
| [D] Using cooperation-by-default in a known finite-endpoint game | Backward induction: last round → defect dominates; second-to-last → both know this and defect; unraveling cascades to round one. Add uncertainty about endpoint or commitment devices. |
| [D] "Always-defect can't beat TFT, so cooperation is automatic" | Always-defect can't beat TFT head-to-head, but can dominate in a population without retaliators. Tournament context matters — don't generalize from two-player simulation to a marketplace with unknown counterparties. |
| [D] Designing a reputation system without manipulation resistance | A gameable system creates worse outcomes than no system, because the gamed signal substitutes for direct due diligence. Test every reputation system against adversarial gaming before deployment. |
| [D] Confusing repeated game with reputation game | Repeated: same parties, bilateral, direct observation. Reputation: changing parties, third-party observation, requires infrastructure. Many "reputation will solve it" arguments fail because that infrastructure doesn't exist. |
| [D] "TFT is the winning strategy, period" | TFT won clean-observation tournaments. Under noise, Generous TFT and Pavlov outperform it. Strategy is environment-conditional: δ, noise, population mix, and horizon all matter. |
| [D] Adding excessive forgiveness "to be nice" | Over-forgiving strategies lose to exploiters. All four properties required: nice + retaliatory + forgiving + clear. Niceness without retaliation is exploited; the data is clear. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- "Build trust" recommended without specifying which mechanism creates it
- δ check skipped (no estimate vs (T−R)/(T−P) threshold)
- TFT recommended in noisy observation environment
- Backward-induction risk ignored in finite-endpoint game
- Reputation system proposed missing any of the four mechanisms
- Strategy chosen for fairness rather than what wins the actual tournament
- Bilateral repetition confused with third-party reputation market

## Verification

- [ ] Repetition structure diagnosed (indefinite/finite-known/finite-unknown; bilateral/reputational)
- [ ] δ estimated and compared to (T−R)/(T−P) threshold
- [ ] Observation noise assessed; forgiveness added if non-trivial
- [ ] Strategy matched to specific environment (not off-the-shelf)
- [ ] If reputation-based, all four infrastructure components specified
- [ ] Endgame dynamics considered; mitigations named if known endpoint
- [ ] Lifetime payoff beats one-shot defection by noise-absorbing margin
- [ ] Alternative strategies compared and rejected with reasons

*→ Primary sources: [references/sources.md](references/sources.md)*

---

*Part of **deciqAI Knowledge Skills** — 228 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/repeated-games-reputation** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/repeated-games-reputation.json*
