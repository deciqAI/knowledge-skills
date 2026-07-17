---
name: freight-lane-pricing-decision
description: "Activate when: a freight broker must quote a lane and decide accept/counter/pass on a load or carrier rate; 'what should I quote', 'is this rate any good', margin vs win-probability on a lane. Do NOT activate when: a contracted rate already governs the lane (no decision). More: deciqai.com/s/freight-lane-pricing-decision"
---

# Freight Broker — Lane Pricing & Load Decision

> **Industry front door for [decision-tree](../decision-tree/SKILL.md).** Adds domain triggers, example, packs. Parent Process unchanged.

**Activate when:** quoting a shipper; deciding whether to accept a carrier's rate; spot vs contract; a tight-margin load; reposition/deadhead trade-offs.
**Do NOT activate when:** a locked contract rate applies.

## Why this variant
The parent [decision-tree](../decision-tree/SKILL.md) maps branching choices with payoffs and probabilities. A load quote is a decision tree: quote high (higher margin, lower win) vs low (win, thin margin) vs pass — against carrier cost, market rate, and relationship value.

## Domain inputs → the tree
- Branch on: market lane rate (DAT/Truckstop benchmarks), carrier cost to cover, shipper relationship value, reposition/deadhead, timing/urgency.
- Roll back expected value: margin × win-probability, plus relationship option value for key shippers.
- Decide accept / counter / pass; protect against covering below carrier cost.

## Worked example
Shipper offers $1,800; market ~$2,100; a carrier will haul for $1,650.
→ Tree: covering at $1,650 nets $150 — thin but the shipper is a top-5 account (relationship value). Counter to $1,950 first; if declined, take it to hold the account; pass only if no carrier covers profitably.

## Packs
- **Solo broker**: quick margin × win-rate card per lane.
- **Brokerage**: benchmark-fed pricing rules; minimum-margin floors.

## Red flags
- Quoting off gut, not the market benchmark.
- Covering below carrier cost to "win."
- Ignoring reposition/deadhead in true cost.

## Verification
- [ ] Market benchmark pulled for the lane
- [ ] Carrier cost-to-cover known
- [ ] Margin × win-probability compared across accept/counter/pass
- [ ] Relationship/option value weighed for key accounts

---
*Part of **deciqAI Knowledge Skills** — 228 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/freight-lane-pricing-decision** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/freight-lane-pricing-decision.json*
