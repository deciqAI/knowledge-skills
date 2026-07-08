---
name: zero-sum-game
description: "Activate when: someone asks 'are we fighting over a fixed pie?', 'should we cooperate or compete?', 'is the market growing or are we just stealing share?', uses phrases like 'winner-take-all', 'race to the bottom', or 'your gain is my loss', or needs to check whether a negotiation/market/policy situation is truly zero-sum before designing strategy.
  Do NOT activate when: the situation is already confirmed zero-sum (chess, derivatives, fixed-license auctions) and diagnosis is complete — go straight to minimax; or the question is already framed at the equilibrium level — use nash-equilibrium directly."
---

# Zero-Sum Game

## Overview

Zero-sum means total value is fixed — one player's gain is another's exact loss. Most real-world competition is NOT zero-sum: the pie can grow, shrink, or be split in many ways. Misdiagnosis sends strategy in the wrong direction from step one. The most consequential error is **zero-sum bias**: the tendency to perceive non-zero-sum situations as zero-sum.

Neighbor skills: use [`prisoners-dilemma`](../prisoners-dilemma/SKILL.md) when confirmed non-zero-sum but cooperation keeps failing. Use [`strategic-commitment`](../strategic-commitment/SKILL.md) when genuinely zero-sum and you need credible deterrence. Use [`nash-equilibrium`](../nash-equilibrium/SKILL.md) for the equilibrium solution in confirmed zero-sum settings.

## When to Use

Apply this skill when: entering a competitive situation before determining whether total value is fixed; someone proposes a negotiation assuming "what I gain, you lose"; a market entry hinges on whether total market size is fixed; a policy analysis needs to assess whether an intervention redistributes or creates welfare; someone uses zero-sum language ("winner-take-all", "race to the bottom", "fixed pie").

**When NOT to use:** already confirmed zero-sum — go straight to minimax; clear cooperative surplus with no competitive distribution problem; stakes trivial and reversible; question already at equilibrium level — use [`nash-equilibrium`](../nash-equilibrium/SKILL.md) directly.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **One-line what-it-is.** Zero-sum: total value fixed — if I get more, you get less by exactly the same amount. Most real-world competition is NOT zero-sum. The diagnosis changes everything about strategy.
2. **Check fit.** Is the resource at stake genuinely fixed? If the total can change through cooperation, innovation, or trade, it is likely non-zero-sum.
3. **Elicit the real case.** Get the specific situation — which market, which negotiation, which policy.
> **[WAIT — do not advance until user responds]**
4. **One step at a time.** Walk through the Diagnosis one question per turn. Start with: "What exactly is being contested — and is the total amount of it fixed?"
> **[WAIT — do not advance until user responds]**
5. **Close by naming the payoff.** State whether zero-sum or not, and what that means for strategy — cooperate/expand vs. minimax/capture.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Zero-Sum Diagnosis**. Five gates; confirm or rule out at each one.

1. **Define the contested resource.** State precisely what is being competed over (market share, license, price spread, votes, contract). If you cannot name a concrete unit being divided, the zero-sum frame likely does not apply.
2. **Test fixity.** Can *innovation/technology* expand the total? Can *cooperation* create additional value? Can *time* change the total? If any answer is "yes," the situation is non-zero-sum in that dimension.
3. **Check for zero-sum bias.** Are you perceiving zero-sum because the resource is countable? Anchored on relative position over absolute gains? Ignoring comparative advantage? If expansion is feasible, you are in the wrong game.
4. **If confirmed zero-sum: apply minimax.** Enumerate strategies and worst-case payoffs; choose the strategy maximizing your minimum; consider mixed strategies to prevent exploitation.
5. **If confirmed non-zero-sum: design for cooperative surplus.** Quantify value neither party gets under pure competition. Specify the mechanism (contract, JV, standard, platform) to capture it. **Stop-rule:** if you cannot identify a concrete pie-growth mechanism, revert to zero-sum analysis.
6. **State the time horizon.** Many situations are zero-sum short-term and non-zero-sum long-term. State both frames explicitly.

### Output template

```
Zero-Sum Diagnosis: <situation>
Contested resource: <unit being divided>
Fixity test: innovation <yes/no> | cooperation <yes/no> | time <short/long>
Bias audit: countability <present/absent> | relative-position <yes/no> | comparative-advantage ignored <yes/no>
Diagnosis: <Zero-Sum | Constant-Sum | Non-Zero-Sum | Mixed> — confidence <high/medium>
If zero-sum → minimax choice: <strategy> | mixed-strategy consideration: <if any>
If non-zero-sum → surplus: <size> | mechanism: <type> | structure: <contract/JV/platform>
Strategic recommendation: <one paragraph>
```

*→ Method in Action: [Von Neumann and the Foundation of Zero-Sum Analysis — RAND, 1944–1950](examples/von-neumann-rand-1944-1950.md) · [The Smoot-Hawley Tariff (1930–1934)](examples/smoot-hawley-tariff-1930.md)*

## Game-Type Packs

- **Financial Derivatives:** Zero-sum by contract — every dollar the long gains, the short loses. Minimax applies; cooperation with counterparties is structurally impossible.
- **Market Share Competition:** Constant-sum short-term; non-zero-sum long-term (category growth, platform effects). Treating long-term markets as zero-sum causes destructive price wars.
- **Licensing/Spectrum Auctions:** Zero-sum by design — fixed license count. Firms that bid cooperatively lose to rivals who bid to win.
- **Trade and International Economics:** Non-zero-sum — comparative advantage produces mutual gains. "Trade deficits = losses" is an analytical error.

## Applying It Well

- Always state the contested resource precisely before diagnosing — "competition" is not a resource.
- Confirm the time horizon: the same situation can be zero-sum this quarter and non-zero-sum over three years.
- Non-zero-sum surplus must be *captured*, not just identified — without a credible mechanism it stays theoretical.
- Zero-sum bias is strongest when resources are countable and socially salient (share rankings, polls). Build in a deliberate check before decisions driven by competitive intel.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Our market share went down, so we lost" | Share and value captured differ. If total market grew 50% and share fell 30%→25%, absolute revenue grew. |
| [D] "Trade deficits mean we're losing" | Deficits in goods are offset by export of financial claims. Comparative advantage shows both parties gain. |
| [D] "They won the contract, so we lost it" | One award is zero-sum among bidders. Total industry contracting volume is usually not fixed. |
| [D] "We should cooperate — there's value to be created" | Only correct if non-zero-sum. In genuine zero-sum settings, "cooperation" is illegal or a strategic error. |
| [D] "It's just market share — zero-sum by definition" | Market share is a ratio. The denominator is not fixed unless you freeze the time horizon. |
| [D] "They made money, so we left money on the table" | In non-zero-sum negotiation both parties can gain. Counterparty's gain implies your loss only if truly zero-sum. |
| [D] "Race to the bottom on price — classic zero-sum" | Zero-sum on margin within a fixed pool, but non-zero-sum if lower prices expand total demand. |
| [D] "My industry experience says it's zero-sum" | Intuitions fail at inflection points. Run diagnosis from first principles on the current structure. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Contested resource never explicitly named or tested for fixity
- "Zero-sum" concluded because competition *feels* intense, not from resource structure
- Non-zero-sum used to justify cooperation without identifying a concrete surplus-capture mechanism
- Time horizon not specified — "zero-sum" treated as time-invariant
- Zero-sum bias not audited (countability, relative position, comparative advantage)
- Minimax applied to a non-zero-sum situation; or cooperation proposed in a genuinely zero-sum situation

## Verification

- [ ] Contested resource named precisely with the specific unit being divided
- [ ] Fixity test run on all three dimensions: technology, cooperation, time horizon
- [ ] Zero-sum bias audited: countability, relative-position anchoring, comparative-advantage blindness
- [ ] Diagnosis states game type with reasoning; time horizon specified for both short and long term
- [ ] If zero-sum: minimax strategy identified including mixed-strategy consideration
- [ ] If non-zero-sum: surplus estimated, mechanism named, structural capture mechanism proposed
- [ ] Stop-rule applied: non-zero-sum confirmed by identifiable mechanism, not assumed from desire to cooperate

---

*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/zero-sum-game?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=zero-sum-game** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
