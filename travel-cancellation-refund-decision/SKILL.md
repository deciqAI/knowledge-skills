---
name: travel-cancellation-refund-decision
description: "Activate when: a client needs to cancel/change; deciding refund vs credit vs insurance claim; comparing supplier penalties; 'what's my best move to recover the most?'. Do NOT activate when: fully refundable booking, no decision needed."
---

# Travel Advisor — Cancellation & Refund Decision

> **Industry front door for [decision-tree](../decision-tree/SKILL.md).** Adds domain triggers, example, packs only. Parent Process unchanged.

**Activate when:** a client needs to cancel/change; deciding refund vs credit vs insurance claim; comparing supplier penalties; "what's my best move to recover the most?"
**Do NOT activate when:** fully refundable booking, no decision needed.

## Why this variant
The parent [decision-tree](../decision-tree/SKILL.md) maps sequential choices with payoffs and probabilities. Cancellation recovery is a decision tree: supplier refund vs future credit vs insurance claim vs card dispute, each with a probability of success and a net recovery.

## Domain inputs → parent's Process
Nodes and payoffs:
- Supplier policy branch: refundable window? penalty tier? credit vs cash.
- Insurance branch: is the reason a covered peril? claim probability × payout.
- Card/chargeback branch: supplier default only; success probability.
- Roll back expected recovery; pick the branch with best net-of-effort value; sequence claims (don't forfeit one by taking another).

## Worked example
Non-refundable tour, client has covered medical reason, trip in 20 days.
→ Tree: supplier gives 25% credit; insurance covers ~90% cash if documented. EV strongly favors the insurance path — but preserve supplier credit as fallback and don't accept a waiver that voids the claim. Sequence matters.

## Compliance anchors
- Present options neutrally; disclose that you don't adjudicate insurance claims; document the advice given (E&O).

## Packs
- **Solo:** standard recovery decision card by supplier type.
- **Agency:** insurer-specific covered-peril quick reference.

## Red flags
- Accepting a supplier credit that voids an insurance claim.
- Advising a claim outcome you can't guarantee.
- No documentation of options presented.

## Verification
- [ ] All recovery branches enumerated with rough odds
- [ ] Expected net recovery compared
- [ ] Claim sequence preserves fallbacks
- [ ] Advice + client choice documented

---
Part of **deciqAI Knowledge Skills**. Core method: [decision-tree](../decision-tree/SKILL.md).
