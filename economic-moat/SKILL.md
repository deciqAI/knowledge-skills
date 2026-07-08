---
name: economic-moat
description: "Activate when: user asks 'does this business have a moat', 'what stops competitors from copying us', 'how defensible is this company', 'is this advantage durable', evaluating a company for investment or acquisition, designing startup strategy for long-term defensibility, reviewing an investor pitch's competitive-advantage claims.
  Do NOT activate when: time horizon is under 1 year (moat is multi-year); question is about immediate execution tactics or a single-quarter decision."
---

# Economic Moat

## Overview

An **economic moat** is the durable, structural competitive advantage that protects a business's returns on capital from being competed away. Popularized by Warren Buffett (1986 Berkshire letter); codified into five sources: intangible assets, switching costs, network effects, cost advantages, efficient scale. Greenwald's test: if you cannot name a specific mechanism that would cost a well-funded rival years and tens of millions to overcome, you have execution — not a moat.

Composes with [`network-effects`](../network-effects/SKILL.md) and [`switching-costs`](../switching-costs/SKILL.md) (two moat sources, deeper treatment), [`porters-five-forces`](../porters-five-forces/SKILL.md) (industry-level; moat is company-level), [`margin-of-safety`](../margin-of-safety/SKILL.md) (wide moat × discount price = Buffett formula), [`lindy-effect`](../lindy-effect/SKILL.md) (long survivors demonstrate moat durability).

## When to Use

- Evaluating an investment, competitor, acquisition, or startup strategy for long-term defensibility
- Founder-board planning or investor pitch review around "what stops competitors"
- Someone says "moat," "defensibility," "competitive advantage," or "what stops competitors"
- Assessing durability amid the AI build-out — AI capex, chip export controls, "is the AI boom a bubble," or which infrastructure players (e.g. Nvidia/CUDA, TSMC) keep their returns

**Not when:** short time horizon; commoditized market (confirms "no moat"); question is immediate execution.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a specific business → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: a moat is a structural barrier — not great product or great team — that rivals can't easily replicate.
2. Check fit: is the time horizon multi-year? Is this an investment, strategy, or acquisition decision?
3. Elicit: what's the business and what is the claimed defensibility?
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time with their input.
> **[WAIT — do not advance until user responds]**
5. Close: name moat width, trajectory, and operational implication.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Frame:** Business · Industry · Time horizon · Claimed advantage · Financial signal (ROIC, gross margin, retention, pricing power).

**Step 2 — Test 5 sources** (present / absent / partial for each):
1. Intangible assets — brand, patents, regulatory license. Can a rival replicate in 5 years?
2. Switching costs — financial, time, data, integration, contractual. Dollar/hour cost to switch?
3. Network effects — user-to-user, two-sided, data flywheel. Past critical mass?
4. Cost advantages — scale, unique resource, proprietary process, location. Durable if rival scales?
5. Efficient scale — market too small to attract new entrants. Would structure tolerate entry?

**Step 3 — Greenwald structural test:** For each "present" source, articulate the mechanism in one sentence. "Great product / great team / first mover" do NOT pass. No articulable mechanism = no moat.

**Step 4 — Trajectory:** Widening / holding / narrowing? Evidence: ROIC trend, market-share trend, competitive-intensity trend over 3-5 years. Static wide-moat + narrowing trajectory = dangerous.

**Step 5 — Smart-attacker test:** Most-credible attack · Cost ($ + time) · P(success). >$100M + >5 years = wide. <$10M + <2 years = narrow or absent.
**Step 6 — Synthesize:** Moat width (wide / narrow / none) · Primary source(s) · Trajectory · Duration of above-competitive returns · Operational implication.

## Output

```markdown
# Moat Analysis: <business>
Business / Industry / Time horizon / Claimed advantage / Financial signal
Five-source table: Source | Present | Structural mechanism | Evidence
Trajectory: widening / holding / narrowing — drivers
Smart attacker: attack / cost + time / P(success)
Assessment: width / primary source(s) / duration / operational implication
```

*→ Method in Action: [Buffett's See's Candies, 1972-present](examples/buffetts-sees-candies-1972-present.md) · [Kodak's Film Moat Erosion, 1975-2012](examples/kodaks-film-moat-erosion-1975-2012.md)*
*→ 2026 lens: [Nvidia's CUDA & TSMC's process — the two deepest AI-supply-chain moats (2024–2026)](examples/nvidia-cuda-tsmc-ai-moats-2024-2026.md)*
## Pack: Moat Source Patterns

| Source | Canonical example | Key signal | Common failure |
|---|---|---|---|
| Brand (intangible) | Coca-Cola, See's | Pricing power without volume loss | Brand awareness ≠ pricing power |
| Switching costs | Enterprise software, CRM | High migration cost / data lock-in | Customer rebellion if abused |
| Network effects | Social networks, marketplaces | Value-per-user grows with scale | Multi-homing erodes moat |
| Cost advantage (scale) | Walmart, Costco | Lower unit cost at same quality | New scale-competitor enters |
| Efficient scale | Regional cement, niche industrials | Few profitable competitors | Market expansion changes calculus |

*→ Primary sources: [references/sources.md](references/sources.md)*
## Applying It Well

- Demand structural specificity — "great product / great team" never pass Greenwald.
- Evaluate trajectory first. Wide-but-narrowing (Kodak, Blockbuster) > narrow-but-widening in danger.
- Startups: identify which moat the model can credibly produce by year 5-10; invest in it deliberately.

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Our team is the moat" | Not a moat. Talent is hired away. What structural barrier does the team create? |
| [D] "Our product is so good, that's our moat" | Product quality is execution. Rivals catch up. Moat must be structural beyond product. |
| [D] "We're first to market" | Usually temporary (Friendster → Facebook; Yahoo → Google). |
| [D] "Our customers love us" | NPS ≠ moat. What prevents switching when a rival appears? |
| [D] "We have network effects" | "We have growth" ≠ network effects. Does each new user demonstrably raise value for existing users via a specific mechanism? |
| [D] "Our brand is strong" | Brand pricing power is the moat. Brand awareness is not. |
| [D] "Our IP / patents protect us" | Most patents are easier to design around than presumed; patent life is finite. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Claimed moat fails Greenwald test; trajectory narrowing but analysis focuses on static width
- Business model has no moat-building mechanism — only execution advantage
- Smart-attacker test yields credible <$10M, <2-year attack
- Technology or regulatory shift reshaping market in ways static analysis misses
- Moat depends on a single key person rather than structural mechanisms

## Verification

- [ ] All five sources tested; each "present" source has a structural mechanism (Greenwald)
- [ ] Trajectory assessed with evidence (ROIC, market share, competitive intensity)
- [ ] Smart-attacker test run with specific attack paths and cost estimate
- [ ] Moat width stated (wide / narrow / none) with estimated duration
- [ ] Operational implication stated; if startup, moat-building plan for years 1-5 articulated

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/economic-moat?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=economic-moat** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
