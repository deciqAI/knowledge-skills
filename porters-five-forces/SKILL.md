---
name: porters-five-forces
description: "Activate when: user asks 'is this a good industry to enter?', 'why is our margin so low despite solid execution?', 'what are the barriers to entry here?', 'how much power do our suppliers/buyers have?', 'should we invest in this sector?', or requests a structured competitive/industry analysis.
  Do NOT activate when: the market is a platform or ecosystem (buyer/supplier roles are ambiguous), or the industry is brand-new with no stable competitive structure yet."
---

# Porter's Five Forces

## Overview

Some industries earn 30%+ margins decade after decade; others fail to earn their cost of capital despite intelligent, well-funded firms. The cause is industry structure. Porter's 1979 five forces — new entrants, supplier power, buyer power, substitutes, rivalry — determine long-run profitability. A firm's earnings are the residual after those forces have taken their cut. Strategic goal: **position where the forces are weakest; where possible, change the forces in your favor** through scale, switching costs, differentiation, or vertical integration.

Composes with [`network-effects`](../network-effects/SKILL.md), [`switching-costs`](../switching-costs/SKILL.md), [`signaling-games`](../signaling-games/SKILL.md), [`pmf-crossing-the-chasm`](../pmf-crossing-the-chasm/SKILL.md).

## When to Use

- Entering or exiting an industry; strategic planning; explaining why a business is profitable or unprofitable despite good execution; evaluating an investment in a specific sector
- Someone says: "barriers to entry," "buyer/supplier power," "industry attractiveness," "structural competitiveness"
- Sizing a sector reshaped by AI: "who captures the profit in AI?", "does AI capex / compute supplier power make this industry attractive?", "can we win against AI-native competition or open-weight substitutes?"

**When NOT to use:** dynamic technology disruption; platform/ecosystem markets; very new markets (no stable structure); firm-level analysis (use VRIO instead).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** concrete industry/decision → run The Process directly.
- **Coach mode:** unfamiliar or no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-liner: some industries are structurally profitable, others hostile — five forces determine which, and a firm's earnings are the residual after those forces take their cut.
2. Check fit: dynamic transitions, platforms, very new markets → point elsewhere.
3. Elicit their real industry. > **[WAIT — do not advance until user responds]**
4. Walk through each force one at a time; ask user to score and name the binding force. > **[WAIT — do not advance until user responds]**
5. Close by naming the binding force and the strategic move that shapes it. > **[WAIT — do not advance until user responds]**

## The Process

Run the **Five-Forces Analysis**. Score each force, identify the binding constraint, design the strategic response.

**Step 1 — Define the industry boundary.** The right boundary: the set of competitors directly substitutable from the typical buyer's perspective. Test: if a buyer is *not* considering company X as an alternative, X is in a different industry.

**Step 2 — Score each force (1=weak/favorable, 5=strong/hostile).**
- *New entrants* — capital requirements, scale economies, brand loyalty, switching costs, distribution access, IP/licenses, retaliation
- *Supplier power* — supplier concentration, switching costs, forward-integration threat, input importance
- *Buyer power* — buyer concentration, purchase volume, product standardization, switching costs, backward-integration threat
- *Substitutes* — relative price-performance, buyer propensity to switch, outside-industry alternatives
- *Rivalry* — competitor count, growth rate, fixed costs, differentiation, switching costs, exit barriers

**Step 3 — Identify the binding force.** The five forces don't average. Name the single most binding force.

**Step 4 — Strategic response by binding force.**
- Entrants binding → raise barriers (scale, brand, switching costs, IP)
- Supplier power binding → backward integration, multi-source, alternative supply
- Buyer power binding → differentiate, increase switching costs, fragment buyer base
- Substitutes binding → improve price-performance vs substitutes, or pivot value proposition
- Rivalry binding → consolidate (M&A), differentiate, find defensible niche, or exit

**Step 5 — Validate against industry profitability data.** If predicted and actual ROIC diverge, you missed a force or an enabling factor. Sources: IBISWorld, Damodaran NYU dataset, public company 10-Ks.

### Output: Five-Forces Analysis

```
# Five-Forces Analysis: <industry>
Boundary: <definition> | Substitutable alternatives: <list>
| Force | Score | Key drivers |
|---|---|---|
| New entrants | _ | |
| Supplier power | _ | |
| Buyer power | _ | |
| Substitutes | _ | |
| Rivalry | _ | |
Binding force: <name> — <why>
Strategic response: <specific move>
Validation: predicted ROIC <…> vs actual <…> | gap: <…>
```

*→ Method in Action: [Porter's 1979 HBR Paper and Its Empirical Foundation](examples/porters-1979-hbr-paper-and-its-empirical-foundation.md) · [Porter's US Passenger Airline Analysis](examples/us-passenger-airline-industry-analysis.md)*
*→ 2026 lens: [The AI Foundation-Model Industry Structure (2024–2026)](examples/ai-foundation-model-industry-structure-2024-2026.md)*

## Pack: Five-Forces by Industry Archetype

| Industry | Strongest force | Typical ROIC |
|---|---|---|
| US passenger airlines | Rivalry + buyer power | <5% |
| Pharmaceuticals (branded) | Entry barriers (patents) | 15-25% |
| Enterprise SaaS | Low rivalry + switching costs | 20-35% |
| Restaurants | Rivalry + low entry barriers | 5-10% |
| Search engines | Entry barriers + data moats | >40% |

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Five-forces is static, ignore it" | Refresh every 2-3 years — don't abandon, refresh. |
| [D] Averaging the five scores | The strongest force is the binding constraint; averaging hides it. |
| [D] Industry defined too broadly or too narrowly | Refine until competitors are mutually substitutable from buyers' view. |
| [D] Ignoring dynamic shifts | Re-run when underlying technology or regulation shifts. |
| [D] Strategic response spread across all five forces | Focus on the binding force first; the rest are background. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Forces scored on intuition without evidence | Binding force not named ("moderately attractive" is not a finding)
- Industry boundary set to flatter own position | Substitutes from outside the industry missed
- Strategic response spread across all five forces equally | Snapshot used as static >3-5 years

## Verification

- [ ] Boundary defined and tested against buyer substitution behavior
- [ ] All 5 forces scored 1-5 with specific drivers
- [ ] Single binding force named; strategy targets it specifically
- [ ] Validated against actual industry ROIC data
- [ ] Dynamic shifts noted (technology, regulation)

*→ Primary sources: [references/sources.md](references/sources.md)*

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/porters-five-forces** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
