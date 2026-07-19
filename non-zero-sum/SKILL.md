---
name: non-zero-sum
description: "Activate when: someone says 'this is win-lose,' 'we can't both win,' 'what's in it for them to cooperate,' 'is there a deal here,' or 'how do we get past this standoff'; a negotiation or conflict feels deadlocked; you're designing a platform, contract, or institution that needs to align competing parties.
  Do NOT activate when: the resource pool is genuinely fixed and one-shot with no side effects (true zero-sum); the conflict is identity- or values-based with no concrete trade that creates net value. More: deciqai.com/s/non-zero-sum"
---

# Non-Zero-Sum

## Overview

A non-zero-sum interaction is one where mutual gain (or mutual loss) is possible — the parties' outcomes do not simply cancel each other out. Most real-world conflicts and negotiations are not zero-sum, but *feel* zero-sum because we focus on the visible resource rather than underlying interests. Robert Axelrod's computer tournament showed cooperation can emerge without central authority when interactions repeat and the future is valued. Robert Wright extended this: the arc of history is driven by accumulating non-zero-sum arrangements — specialization, trade, institutions.

**Compose with neighbors:** Use [prisoners-dilemma](../prisoners-dilemma/SKILL.md) to model the payoff structure first. Use [repeated-games-reputation](../repeated-games-reputation/SKILL.md) when the key variable is whether interaction repeats. Use [nash-equilibrium](../nash-equilibrium/SKILL.md) to find whether a stable cooperative outcome exists.

## When to Use

- A negotiation or conflict is deadlocked in zero-sum framing — each side treating every gain as the other's loss
- You want to find latent cooperative value in an adversarial relationship
- Designing an institution, platform, or contract to align incentives for competing parties
- Someone says: *"this is win-lose," "we can't both win," "what's in it for them," "could we cooperate instead of compete?"*
- A market is framed as winner-take-all — *"AI will take all the jobs / margin," "the AI capex will only pay off for the platform," "AI-native startups will crush incumbents (or vice versa)"* — and you need to test whether the layers can grow together instead

**When NOT to use:**
- Genuinely fixed-pool, one-shot interaction with no side effects — non-zero-sum framing is wishful, not analytical
- Interests are fundamentally incompatible (ideological, identity-based) with no concrete trade creating net value
- The real constraint is power asymmetry → use [batna-zopa](../batna-zopa/SKILL.md) instead

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a specific standoff or competitive dynamic → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: non-zero-sum means both parties can gain — or both can lose — from an interaction. Most conflicts feel zero-sum but aren't.
2. Check fit against When to Use / When NOT to use — if genuinely zero-sum, redirect to zero-sum negotiation strategy.
3. Elicit their specific standoff or competitive dynamic. "How do I negotiate better?" is not workable; a concrete situation is. > **[WAIT — do not advance until user responds]**
4. Walk through the payoff structure, shadow of the future, and cooperation structure steps one at a time with their input. > **[WAIT — do not advance until user responds]**
5. Close by naming the specific non-zero-sum mechanism that creates cooperative potential — the concrete thing both parties gain by cooperating that neither gets by fighting. > **[WAIT — do not advance until user responds]**

## The Process

Five steps producing a **Non-Zero-Sum Analysis**. **Stop rule:** If Step 2 reveals a genuinely zero-sum payoff structure, stop and shift to zero-sum strategy.

1. **Map positions vs. underlying interests.** Positions are often zero-sum; interests often are not. A wage negotiation (zero-sum on money) may be non-zero-sum on scheduling, job security, and productivity bonuses.
2. **Construct the payoff matrix.** Is total value fixed (zero-sum) or variable (non-zero-sum)? Identify mutual-defection outcomes, mutual-cooperation outcomes, and the temptation payoff. If mutual cooperation produces more total value, the interaction is non-zero-sum.
3. **Assess the shadow of the future.** Will parties interact again? How much value is in future vs. this one interaction? Are there reputational effects that make defection costly beyond this round?
4. **Identify the cooperation mechanism.** (a) direct reciprocity (Tit-for-Tat); (b) reputation (third parties reward cooperators); (c) institution (contract or platform that makes defection costly); (d) reframing (make mutual gain visible). Match mechanism to relationship structure.
5. **Design the first move.** Cooperative enough to invite reciprocation; clear enough that defection is unambiguous; resilient enough to survive one defection without collapsing.

### Output: Non-Zero-Sum Analysis

```
# Non-Zero-Sum Analysis: <interaction>
## Positions vs. Interests
| Party | Stated position | Underlying interests |
| A | <...> | <...> |
| B | <...> | <...> |
## Payoff Matrix
| | B cooperates | B defects |
| A cooperates | Both gain: <...> | A loses, B gains: <...> |
| A defects | A gains, B loses: <...> | Both lose: <...> |
Non-zero-sum gap: <cooperation dividend>
## Shadow of the Future: <Strong / Moderate / Weak> — <rationale>
## Cooperation Mechanism: <reciprocity / reputation / institution / reframing> — <rationale>
## First Move: <action> | Defection signal: <...> | Recovery path: <...>
```

*→ Method in Action: [Axelrod's Computer Tournament (1980)](examples/axelrods-computer-tournament-1980.md)*
*→ 2026 lens: [The AI Ecosystem — Positive-Sum vs. "AI Eats Everything" (2024–2026)](examples/ai-ecosystem-value-creation-2024-2026.md)*

## Cooperation Packs

- **Business negotiations:** Buyer/seller zero-sum on price; non-zero-sum on volume, reliability, and timing. Mechanisms: long-term contracts, quality bonuses, co-investment.
- **Platform / ecosystem:** Platform wants revenue; developers want distribution. Mechanism: tiered fees decreasing with scale (App Store / Stripe Connect logic).
- **International trade:** Positions conflict on surplus; interests align on market access and supply chain resilience. Mechanism: WTO rules, bilateral reciprocity, supply chain interdependence.

## Applying It Well

- **Map interests before concluding zero-sum** — positions are almost always more zero-sum than underlying interests.
- **Shadow of the future is the master variable** — assess repeat interaction before designing any mechanism.
- **Tit-for-Tat requires unambiguous defection detection** — define what constitutes defection before committing to reciprocity.
- **Forgiveness is structurally required** — Grim Trigger is not evolutionarily stable; build recovery paths in.
- **Institutions change payoff matrices** — if trust is insufficient, a contract is more reliable than repeat-interaction dynamics alone.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] **"This is zero-sum — nothing to cooperate on."** | Map interests vs. positions first. Money may be zero-sum; timing, quality, risk, and relationship usually are not. |
| [D] **Cooperation impossible because of lack of trust.** | Trust is not a prerequisite — payoff structure and shadow of the future are. Axelrod's tournament showed cooperation among purely self-interested strategies with no trust or communication. |
| [D] **Designing cooperation mechanisms for one-shot interactions.** | All reciprocity/reputation mechanisms require repeated interactions. One-shot contexts need external enforcement or one-shot interest alignment. |
| [D] **Assuming identifying non-zero-sum structure is sufficient.** | Structure is necessary but not sufficient — shadow of future must be strong, defection detectable, mechanism designed. |
| [D] **Using Tit-for-Tat where defection is ambiguous.** | Produces retaliatory spirals from misinterpretation. Use Generous Tit-for-Tat in ambiguous contexts. |
| [D] **Treating non-zero-sum as a negotiation trick.** | Requires honest interest-mapping of both parties. Tactical framing without it produces deals that collapse. |
| [D] **Conflating non-zero-sum potential with guaranteed mutual benefit.** | Mutual gain is *possible* — not automatic. Capturing the dividend requires coordination or institutional design. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Zero-sum declared from positions alone, interests not mapped
- Cooperation mechanism designed for a one-shot interaction
- Shadow of the future not assessed before choosing reciprocity
- Defection is ambiguous — Tit-for-Tat will misfire
- No recovery path after first defection; cooperation assumed to follow automatically from structure alone

## Verification

- [ ] Positions vs. interests mapped for both parties
- [ ] Payoff matrix: does mutual cooperation produce more total value than mutual defection?
- [ ] Non-zero-sum gap (cooperation dividend) quantified or ranked
- [ ] Shadow of the future assessed
- [ ] Cooperation mechanism matched to relationship structure
- [ ] Defection detection criteria defined; recovery path designed

---
*Part of **deciqAI Knowledge Skills** — 233 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/non-zero-sum** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/non-zero-sum.json*
