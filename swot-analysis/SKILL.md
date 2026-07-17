---
name: swot-analysis
description: "Activate when: user says 'SWOT', 'our strengths and weaknesses', 'internal/external analysis', 'strategic audit', 'what's our edge', 'competitive threats we face', or is beginning a strategy planning cycle, evaluating market entry, or preparing investor materials. Do NOT activate when: user needs a purely quantitative financial model or precise numerical decision (use financial analysis instead); user wants to map competitive industry structure forces (use Porter's Five Forces instead). More: deciqai.com/s/swot-analysis"
---

# SWOT Analysis

## Overview

SWOT maps internal Strengths/Weaknesses against external Opportunities/Threats, then generates strategies via TOWS cross-matrix (SO/ST/WO/WT). Rooted in Humphrey's SRI research (1960s–70s) and Harvard's "fit" logic — matching internal capability to external environment. The list is setup; strategy comes from the cross-pairs.

Composes with: [`porters-five-forces`](../porters-five-forces/SKILL.md) (before SWOT, to structure O/T); [`bcg-matrix`](../bcg-matrix/SKILL.md) (after, for portfolio allocation); [`ansoff-matrix`](../ansoff-matrix/SKILL.md) (after, to translate SO into growth direction).

## When to Use

Apply when: beginning a strategic planning cycle; evaluating market entry; preparing investor materials; conducting competitive analysis from a rival's perspective; facing a crisis requiring rapid capability/threat mapping; assessing how AI adoption, AI-native competition, or rising AI capex reshapes your strengths, pricing model, and threats.

**When NOT to use:** precise quantitative decisions (SWOT is too subjective); firm-level competitive positioning within known industry structure (use Five Forces or VRIO); specifically which direction to grow (use Ansoff); team cannot agree on what a Strength even is.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete case → run The Process directly.
- **Coach mode:** user is unfamiliar or has no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **One-line:** SWOT forces you to look at your business in four buckets — what you're good at (Strengths), where you're weak (Weaknesses), what the market offers (Opportunities), threats from outside (Threats) — then crosses them to generate strategies.
2. **Check fit** — if user wants industry structure, redirect to Five Forces; if growth direction, redirect to Ansoff.
3. **Elicit the real case** — ask: "Which company or situation are you analyzing, and what decision does this need to support?"
> **[WAIT — do not advance until user responds]**
4. **One step at a time** — walk through Strengths, Weaknesses, Opportunities, Threats, then TOWS, waiting for input before advancing.
> **[WAIT — do not advance until user responds]**
5. **Close by naming the payoff** — "The key thing SWOT just showed you is [the specific S×O match or W×T collision most directly driving your decision]."
> **[WAIT — do not advance until user responds]**

## The Process

Produce a **Strategic Audit** — populated four-quadrant SWOT plus TOWS cross-matrix with actionable strategy options.

**Step 1 — Define unit and purpose:** what entity + what decision. Stop if the unit cannot be bounded with identifiable competitors.
**Step 2 — Strengths (internal+):** comparative capabilities vs. named competitors. 3–5 entries. Regress-test: "Does our competitor also have this?" If yes, it's a market trait, not your advantage.
**Step 3 — Weaknesses (internal−):** internal deficits. Distinguish remediable (12–24 months) vs. structural. 3–5 entries from exit interviews, churn data, cost benchmarks.
**Step 4 — Opportunities (external+):** conditions that exist regardless of whether you are in the market. Use Five Forces for structural discovery. 3–5 entries.
**Step 5 — Threats (external−):** external conditions damaging competitive position. Rate probability and impact. 3–5 entries.
**Step 6 — TOWS cross-matrix:** SO (Strengths → Opportunities); ST (Strengths → Threats); WO (fix Weakness → Opportunity); WT (minimize Weakness×Threat). 1–2 specific, actionable statements per type.
**Step 7 — Prioritize:** score by value, resource, speed to signal. Select top 2–3. Explicitly deprioritize the rest. Set review cadence.

### Output: Strategic Audit

```
# Strategic Audit: <company / unit / decision> | Date: <date>  Next review: <trigger>
## Strengths (S1–S3): <specific, comparative> — source: <…>
## Weaknesses (W1–W3): <specific; remediable/structural> — source: <…>
## Opportunities (O1–O3): <external condition> — evidence: <…>
## Threats (T1–T3): <specific; probability H/M/L; impact H/M/L>
## TOWS: SO S_×O_ <action> | ST S_×T_ <action> | WO W_×O_ <action> | WT W_×T_ <action>
## Priority (top 2–3): <strategy + rationale>
## Not prioritizing: <deprioritized strategies and why>
```

*→ Method in Action: [Netflix's 2010–2013 Strategic Pivot](examples/netflix-2010-2013-strategic-pivot.md) · [LEGO's 2003–2005 Turnaround](examples/lego-2003-2005-turnaround.md)*
*→ 2026 lens: [Incumbent Seat-Based SaaS vs. the AI Agent Shift (2024–2026)](examples/seat-based-saas-ai-transition-2024-2026.md) — AI as Opportunity and Threat at once*

## SWOT Packs

**Tech startups:** "Our UX is better" needs retention/NPS data. "AI market growing" = Opportunity for all players, not your Strength. Incumbent's 90-day copy speed = most underweighted Threat.

**Enterprise B2B:** "Sales cycle is 9 months" = Weakness, not Threat. Existing relationships × regulatory complexity driving out rivals = underexploited SO combo.

## Applying It Well

- Always run TOWS — the list is setup, strategy comes from cross-pairs
- Strengths must be comparative vs. named competitors; Opportunities must be external
- Check WO strategies: if fixing the Weakness takes longer than the Opportunity window, the strategy is not viable

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] Listing "our culture is strong" as a Strength | Culture is not a Strength unless it creates measurable outcomes competitors cannot replicate (lower attrition, faster iteration, etc.). |
| [D] Mixing Opportunities (external) with Strengths (internal) | "AI is transforming our industry" is an Opportunity for all competitors. "We have an AI team with 3 published LLM papers" is a Strength. |
| [D] Listing 20+ entries per quadrant | A SWOT with 30 items has no priorities. Force 3–5 per quadrant to identify what is most significant. |
| [D] Stopping at the list — no TOWS cross-analysis | The list is the setup. Strategy emerges from cross-pairs. SWOT without TOWS is diagnosis without treatment. |
| [D] Treating internal Weaknesses and external Threats as equivalent | Weaknesses → address with resource investment or process change. Threats → address through strategic positioning. Different tools, different timelines. |
| [D] Running SWOT on the whole company when the decision is unit-specific | Company-level SWOT is often too diffuse. Define the smallest unit for which the decision is being made. |
| [D] Using last year's SWOT without updating for market events | A Threat rated M/H last year may be H/H this quarter. SWOT is a living document, not an annual ritual. |
| [D] Listing Weaknesses only from management's self-assessment | Exit interviews, churn feedback, and win/loss data surface Weaknesses internal teams rationalize away. |
| [D] Declaring a WO strategy without quantifying the Opportunity window | If fixing the Weakness takes 18 months but the window closes in 12, the WO strategy is not viable. |
| [D] Using the same competitive framing every year | SWOT should surface new entrants, substitutes, and regulatory changes that upend last year's framing. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Strengths and Opportunities appear in the same quadrant (internal/external distinction collapsed)
- Every Strength stated as a superlative ("best-in-class") without comparative evidence
- No TOWS cross-analysis — deliverable ends at the four-quadrant list
- Weaknesses euphemized ("areas for improvement") rather than named precisely
- Threats listed with no probability or impact assessment
- SWOT assembled by executive team alone without customer data or competitive intelligence
- No explicit deprioritization — every TOWS strategy pursued simultaneously

## Verification

- [ ] Analysis unit defined (company? product? geography? decision?)
- [ ] Each Strength stated as comparative advantage vs. named competitor on measurable dimension
- [ ] Each Opportunity genuinely external — exists regardless of whether this firm is in the market
- [ ] Each Threat has probability and impact rating
- [ ] TOWS cross-matrix produced with at least one specific, actionable strategy per type
- [ ] WO strategies checked against Opportunity window duration vs. time-to-fix-Weakness
- [ ] Top 2–3 strategies selected with explicit deprioritization of the rest
- [ ] Review cadence set (date or trigger event)

---

*Part of **deciqAI Knowledge Skills** — 228 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/swot-analysis** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/swot-analysis.json*
