---
name: realtor-price-reduction-decision
description: "Activate when: a listing isn't selling and the agent must decide list price or a price reduction; 'should we drop the price', 'how much and when', days-on-market rising, showings without offers. Do NOT activate when: the property is priced right and getting offers (no decision)."
---

# Real Estate — Pricing & Price-Reduction Decision

> **Industry front door for [decision-tree](../../deciqai-knowledge-skills/decision-tree/SKILL.md).** Adds domain triggers, example, packs. Parent Process unchanged.
> **Not appraisal advice.**

**Activate when:** setting a list price; a listing stalls (DOM up, showings without offers); deciding reduction timing/size; managing seller expectations.
**Do NOT activate when:** priced correctly with active offers.

## Why this variant
The parent [decision-tree] maps sequential choices under uncertainty. Pricing and reductions are a decision tree: hold vs reduce, by how much, when — against showing/offer feedback, carrying cost, and market trend, rolling back to expected net proceeds and time-to-sell.

## Domain inputs → the tree
- Read the signals: showings-to-offer ratio, DOM vs market median, feedback themes, comparable adjustments.
- Branch: hold (if fresh/undersampled), small reduction (nudge into a search bracket), meaningful reduction (reset if far off).
- Value the branches by expected net proceeds × probability × carrying cost of extra DOM. *Gate: reductions below a portal price bracket (e.g. $505k→$499k) capture a new buyer pool — size to brackets, not round guesses.*

## Worked example
30 showings, no offers, DOM 2× median, feedback "overpriced vs the one down the street."
→ Tree: this is a pricing (not marketing/condition) problem; a token cut won't fix a bracket miss. Reduce into the correct search bracket in one decisive move; slow drip prolongs DOM and signals weakness.

## Packs
- **Solo agent**: showings-to-offer + DOM decision card; bracket-aware reduction sizing.
- **Team**: weekly stale-listing review triggering the decision.

## Red flags
- Blaming marketing when the data says price.
- Tiny drip reductions that prolong DOM.
- Reductions not aligned to portal search brackets.

## Verification
- [ ] Showing/offer + DOM signals reviewed vs comps
- [ ] Problem diagnosed (price vs condition vs marketing)
- [ ] Reduction sized to search brackets, not round numbers
- [ ] Expected net proceeds vs carrying cost weighed

---
Part of **deciqAI Knowledge Skills**. Core method: [decision-tree](../../deciqai-knowledge-skills/decision-tree/SKILL.md).
