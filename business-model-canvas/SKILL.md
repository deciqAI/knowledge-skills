---
name: business-model-canvas
description: >
  Activate when: user says "business model canvas," "BMC," "Osterwalder canvas," "what's our business model," "map this business," or asks to evaluate/design/pivot/compare a business model before raising capital.
  Do NOT activate when: no customer segment exists yet (redirect to first-principles first); or the question is purely operational (which CRM, which feature to ship).
---

# Business Model Canvas

## Overview

A business creates, delivers, and captures value through **nine interlocking blocks** (Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partners, Cost Structure). The canvas maps each block and exposes which claims are *specific enough to be tested* vs. *still wishful thinking*. Introduced by Osterwalder (HEC Lausanne, 2004); popularized in *Business Model Generation* (Wiley, 2010).

**Compose:** [first-principles](../first-principles/SKILL.md) to clarify genuine dependencies · [occams-razor](../occams-razor/SKILL.md) to compare models · [inversion](../inversion/SKILL.md) to find the block whose failure kills the model · [second-order-thinking](../second-order-thinking/SKILL.md) to trace block cascades.

## When to Use

Apply when: designing a new business · evaluating an existing business for block-level risk · considering a pivot · comparing against incumbents · before raising capital · sizing an AI-native model's economics under AI capex / usage-based margins / AI-native competition (does the foundation-model provider's pricing or its own product roadmap sit in your Cost Structure and Key Partners?).

**When NOT to use:** no customer named yet (do first-principles first) · canvas done and nothing validated since · purely operational decision · you will fill it in but never test it.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line what-it-is: nine blocks map how a business creates, delivers, and captures value — so you can see which claims are testable and which are wishful thinking.
2. Check fit against When to Use / When NOT to use. If no customer named, redirect to [first-principles](../first-principles/SKILL.md).
3. Elicit their real business — one specific segment and one specific value prop before opening the other seven blocks.
> **[WAIT — do not advance until user responds]**
4. Walk the nine blocks one at a time in dependency order (Segments → Value Prop → Channels → Relationships → Revenue → Resources → Activities → Partners → Cost). Force specifics.
> **[WAIT — do not advance until user responds]**
5. Close by naming the single block with the most unvalidated assumption and the next-week experiment to test it.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Business Model Canvas Audit** — map all nine blocks, tag each claim, surface the riskiest assumptions, name next-week experiments.

| Step | Block | Key question |
|---|---|---|
| 1 | Customer Segments | Specific who (not "consumers") — multi-sided businesses list each side |
| 2 | Value Propositions | What the customer *gets* in their own units (time/money/anxiety/status) — not features |
| 3 | Channels | Five phases: awareness, evaluation, purchase, delivery, after-sales |
| 4 | Customer Relationships | What relationship does each segment expect? (self-service / personal / community) |
| 5 | Revenue Streams | Model + price + *why they pay* — willingness-to-pay must be testable |
| 6 | Key Resources | Only the small distinctive set that enables the value prop |
| 7 | Key Activities | Only what must be done *distinctively well* to deliver the value prop |
| 8 | Key Partners | Named, with role and replacement risk |
| 9 | Cost Structure | Named drivers, fixed vs. variable; value-driven or cost-driven? |

After mapping: tag every claim VALIDATED/ASSUMED/DEPENDENT · name the 1–2 ASSUMED claims that would kill the business · design the smallest next-week experiment for each.

### Output template

```
# Business Model Canvas Audit: <business name>
| Block | Specifics | Status |
|---|---|---|
| Customer Segments | … | VALIDATED/ASSUMED/DEPENDENT |
| Value Propositions | … | … |
| Channels | awareness/eval/purchase/delivery/after-sales | … |
| Customer Relationships | … | … |
| Revenue Streams | model + price + why they pay | … |
| Key Resources | … | … |
| Key Activities | … | … |
| Key Partners | named + role + replacement risk | … |
| Cost Structure | fixed/variable drivers | … |

Multi-sided check: [list each side's segment + value prop + revenue]
Load-bearing ASSUMED claims: 1. … 2. …
Next-week experiments: To test <claim>: <smallest experiment by <date>>
Comparison to incumbents: [block-by-block diff vs. closest competitor]
```

*→ Method in Action: [Southwest Airlines (1971 → ongoing)](examples/southwest-airlines-1971.md) · [Nespresso's Razor-and-Blades Pivot](examples/nespresso-razor-and-blades-1986.md)*
*→ 2026 lens: [Mapping an AI-Native Startup (2024–2026)](examples/ai-native-startup-2024-2026.md) — usage/outcome revenue, compute as dominant variable cost, the foundation-model provider as both key partner and key risk*

## Industry Canvas Packs

| Domain | Load-bearing block | Typical ASSUMED claim | Common failure |
|---|---|---|---|
| B2B SaaS | Value Propositions | time-to-value short enough to survive the pilot | scaling sales before validating segment fit |
| Two-sided marketplaces | Customer Segments (×2) | cold-start liquidity on the harder side | mapping one side's canvas, skipping the other's Segments/Value Props/Revenue Streams |
| DTC consumer | Channels | CAC below contribution margin at scale | pricing set before any willingness-to-pay evidence; Channels covering purchase but not after-sales |
| Professional services | Key Resources | the specific people who deliver the value prop are retainable and replicable | selling capacity that walks out the door; Cost Structure left as "salaries" without utilization drivers |

*Contribute a pack for your domain — see the template at the repo root.*

## Applying It Well

- **Generic words are theater.** Replace "consumers," "online," "low cost" with specifics before a block counts as filled.
- **The blocks must compose.** A great Value Prop + Channels that can't reach the segment is not a business model.
- **Multi-sided is the rule; the canvas points to experiments.** Platforms have multiple Segments/Props/Revenue Streams — skipping a side breaks the canvas. Surface the 1–2 ASSUMED claims that would kill the business and test them next week.
- **Compare block-by-block to incumbents.** Identical canvas to a competitor = worse-positioned version of theirs.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] **Canvas as decoration** — filled in after strategy is set | Canvas is for *finding* the strategy. Retrofitted = wall poster. |
| [D] **Generic segments** — "consumers," "businesses," "everyone" | Generic segments → generic canvas → untestable claims. |
| [D] **Value Prop = feature list** | Features = what the product does; value prop = what the customer gets in their own units. |
| [D] **Single-sided thinking** in a multi-sided business | Platforms have multiple Segments/Value Props/Revenue Streams — skipping a side breaks the canvas. |
| [D] **Cost Structure left vague** ("low" / "high" without driver names) | "Low cost" without named drivers is a wish, not an answer. |
| [D] **Revenue Streams without willingness-to-pay evidence** | Pricing without evidence is ASSUMED, not validated. |
| [D] **Key blocks as generic lists** · **No experiment plan** | Only distinctive-set items belong; without experiments, the canvas is a hypothesis. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags / Verification

- [ ] Canvas filled *after* strategy was set (decoration) · Segments contain "consumers"/"everyone" · Value Props are a feature list
- [ ] Revenue Streams give price without willingness-to-pay evidence · Key blocks list generic inventory · No multi-sided check on a platform
- [ ] No ASSUMED claims labeled · No next-week experiment named for load-bearing assumptions
- [ ] All nine blocks specific (not generic) · Channels covers all five phases · Each claim tagged VALIDATED/ASSUMED/DEPENDENT
- [ ] Canvas compared block-by-block to at least one incumbent's

---

*Part of **deciqAI Knowledge Skills** — 225 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/business-model-canvas** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
