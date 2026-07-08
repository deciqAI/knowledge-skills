---
name: bcg-matrix
description: >
  Activate when: user says "portfolio review," "cash cow," "Stars and Dogs," "growth-share matrix,"
  "which business should we fund," or "resource allocation across units"; firm has multiple business
  units competing for shared capital; investor or board discussion needs a visual portfolio health read.
  Do NOT activate when: firm is a single-product startup with no portfolio to balance; user needs
  competitive analysis within one market (use Porter's Five Forces or VRIO instead).
---

# BCG Growth-Share Matrix

## Overview

Maps each business unit on a 2×2 grid of market growth rate vs. relative market share, revealing which units generate cash, which absorb it, and which to invest in, harvest, or exit. Four quadrants: **Stars** (invest), **Cash Cows** (harvest), **Question Marks** (binary decide), **Dogs** (exit or hold minimally). Rests on two empirical anchors: experience curve (high share = lowest cost) and industry life cycle (high growth demands reinvestment; maturity throws off cash).

Composes with: [`porters-five-forces`](../porters-five-forces/SKILL.md) to define industry boundary first · [`swot-analysis`](../swot-analysis/SKILL.md) for internal-capability depth · [`ansoff-matrix`](../ansoff-matrix/SKILL.md) to set growth direction for units worth investing in.

## When to Use

- Firm operates **≥ 3 distinct business units** competing for a shared capital pool
- Annual **strategy or budget reviews** need a forcing function for prioritization
- **PE/VC portfolio** requires a quick health-read across holdings; M&A teams assessing retain vs. divest

**When NOT to use:** single-product startup · highly interdependent units where divesting a Dog may destroy a Cash Cow · market in technology transition with unreliable growth data · firm-level competitive analysis within one market

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has specific BU data → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. BCG shows which businesses fund others, which burn cash, and which need a decision — using two numbers: market growth rate and your share relative to your biggest competitor.
2. Check fit: does the user have multiple distinct units? If single-product, redirect to Ansoff or Five Forces.
3. Ask: "Which business units are you trying to prioritize?"
> **[WAIT — do not advance until user responds]**
4. Walk through unit definition, data collection, quadrant plotting, trend analysis, and strategy assignment one step at a time.
> **[WAIT — do not advance until user responds]**
5. Close: "The key thing BCG just revealed is [which unit is your implicit funder and which is consuming it without a clear path to self-sufficiency]."
> **[WAIT — do not advance until user responds]**

## The Process

Produce a **Portfolio Map** — quadrant assignments, trend arrows, and resource-allocation recommendations per SBU.

**Step 1 — Define SBUs.** Must: serve an identifiable customer group, have identifiable competitors, be manageable with resource independence. Stop rule: if you cannot name the primary competitor, the boundary is wrong.

**Step 2 — Market growth rate.** 2–3 years external data; calculate CAGR. Dividing line: **10%** (raise to 20–30% for AI/clean-tech). Never use own revenue growth as a proxy.

**Step 3 — Relative market share.** Own share ÷ largest competitor's share. >1.0 = leader; <1.0 = follower.

**Step 4 — Plot.** X-axis: relative share (log, right = high); Y-axis: growth (linear, up = high); bubble size = revenue. Assign quadrant.

**Step 5 — Trend arrows.** 2-year trajectory per SBU. Trend often matters more than current position.

**Step 6 — Strategy.** Star: invest aggressively. Cash Cow: extract surplus; minimize capex. Question Mark: binary — upgrade to Star OR exit by a named date. Dog: harvest/exit; hold only if synergy is named and quantified.

### Output Template

```
BCG Portfolio Map: <company> | Threshold: <X>% | Date: <date>
SBU | Growth | Rel.Share | Quadrant | Revenue | Profitable?
Trend: <SBU> moving <from> → <to> — reason: <…>
Cash generators: <list> | Cash absorbers: <list> | Balance: <surplus/deficit>
Strategy: <SBU A>: invest/harvest/exit by <date>
Key decision: <what the analysis forces>
```

*→ Method in Action: [Procter & Gamble's Brand Portfolio Restructuring (2012–2016)](examples/procter-gamble-brand-portfolio-restructuring-2012-2016.md) · [GE's "Fix, Sell, or Close" Pruning (1981–1995)](examples/general-electric-fix-sell-or-close-portfolio-pruning-1981-1995.md)*

## Portfolio Packs

| Industry | Share proxy | Growth proxy | Dog trap | Star misread |
|---|---|---|---|---|
| Consumer packaged goods | Nielsen/IRI retail share | Category CAGR | Legacy brand in declining format | Tiny-base subcategory inflating growth rate |
| Enterprise SaaS | ARR share vs. ICP rivals | Gartner/IDC forecast | Feature-complete product commoditizing | VC competitor's discount-driven "growth" |
| AI products (2024+) | Monthly active API users vs. nearest rival | Segment TAM growth | Model-wrapper with no defensible moat | Benchmark-topping product with no enterprise path |
| Retail/e-commerce | GMV share | Segment GMV CAGR | Category with free platform substitute | High-growth vertical with dominant incumbent |

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] Using absolute share instead of relative share | A 25%-share firm facing a 40% rival is a follower. Absolute share hides competitive position. |
| [D] Defining market too broadly to manufacture high relative share | Calling a niche player in "enterprise software" a leader obscures the actual threat. |
| [D] Labeling every Dog as "strategic" to avoid exit | Synergy must be quantifiable — name the mechanism and the dollar amount. |
| [D] Treating the matrix as a one-time exercise | Growth rates and positions shift. Refresh annually at minimum. |
| [D] Assuming every Question Mark deserves investment | Correct default is a defined decision deadline. Most Question Marks should be exited. |
| [D] Using BCG to justify a decision already made | If unit definitions are chosen after quadrant destinations are known, the analysis is reverse-engineered. |
| [D] Applying experience-curve assumption to software or platforms | High share does not mechanically produce low costs in knowledge-intensive businesses. |
| [D] Treating all Cash Cows as permanent | Cows can become Dogs. Maintain a deterioration watch with leading indicators. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Market boundary defined after desired quadrant assignment is known · relative share uses own revenue not competitor's share · all Question Marks described as "likely Stars" with no exit criteria · no trend arrows · Dogs retained with unquantified synergy · Cash Cows don't cover Stars + Question Mark investment needs · matrix used as a slide with no reallocation following

## Verification

- [ ] Each SBU passes the standalone-manager test (identifiable market, rivals, separable P&L)
- [ ] Relative share = own share ÷ largest competitor's share (not absolute share)
- [ ] Market growth from external data, not own revenue growth
- [ ] 2-year trend arrows plotted for each SBU
- [ ] Cash Cow generation quantified against Star + Question Mark investment needs
- [ ] Each Dog has an exit plan or a named, quantified synergy
- [ ] Each Question Mark has a decision deadline with invest-or-exit criteria
- [ ] Refresh cadence scheduled (state the date)

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/bcg-matrix** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
