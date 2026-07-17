---
name: ria-position-sizing-kelly
description: "Activate when: sizing a single-name or thematic position; a client with concentrated stock; setting max-position/rebalancing bands; 'how much of the portfolio should this be?'. Do NOT activate when: broad index allocation already governed by the IPS. More: deciqai.com/s/ria-position-sizing-kelly"
---

# RIA — Position Sizing & Concentration Discipline

> **Industry front door for [expected-value-and-kelly](../expected-value-and-kelly/SKILL.md).** Adds domain triggers, example, packs only. Parent Process unchanged.
> **Not investment advice.** Educational framework; apply within IPS and suitability.

**Activate when:** sizing a single-name or thematic position; a client with concentrated stock; setting max-position/rebalancing bands; "how much of the portfolio should this be?"
**Do NOT activate when:** broad index allocation already governed by the IPS.

## Why this variant
The parent [expected-value-and-kelly](../expected-value-and-kelly/SKILL.md) sizes repeated positive-edge bets to maximize long-run growth without ruin. For an RIA, the discipline is inverted toward **survival**: fractional-Kelly thinking caps concentration so no single position can impair the client's plan.

## Domain inputs → parent's Process
- Establish the edge is real and repeatable before sizing anything.
- Use **fractional Kelly** (e.g. ¼–½) — full Kelly is too volatile for client capital.
- Bound by IPS max-position and drawdown tolerance; the *smaller* of Kelly-implied and IPS cap wins.
- Treat concentrated legacy stock as an over-sized position to unwind on a tax-aware schedule.

## Worked example
Client insists on a 25% single-stock position.
→ Even a generous edge under fractional Kelly rarely justifies 25% of a household's net worth; ruin risk dominates. Frame the trade-off, cap per IPS, and set a diversification glide-path (tax-aware). Documented as a suitability decision.

## Packs
- **Solo:** max-position + rebalancing-band rules in the IPS.
- **Advisory:** concentrated-stock unwind playbook (tax-aware).

## Red flags
- Sizing to full Kelly / conviction with client capital.
- Concentration exceeding IPS caps "because it's been working."
- No ruin/drawdown check.

## Verification
- [ ] Edge validated before sizing
- [ ] Fractional Kelly, bounded by IPS cap (smaller wins)
- [ ] Drawdown/ruin tolerance respected
- [ ] Concentration decisions documented for suitability

---
Part of **deciqAI Knowledge Skills**. Core method: [expected-value-and-kelly](../expected-value-and-kelly/SKILL.md).

---

*Part of **deciqAI Knowledge Skills** — 228 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/ria-position-sizing-kelly** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/ria-position-sizing-kelly.json*
