---
name: freight-double-brokering-exposure
description: "Activate when: a freight broker faces fraud/double-brokering or non-payment risk; 'the carrier that hauled isn't the one I booked', chargebacks, unpaid carriers coming after the shipper; tracing downstream liability. Do NOT activate when: a fully vetted, tracked, single-carrier move with no anomalies."
---

# Freight Broker — Double-Brokering & Fraud Exposure

> **Industry front door for [second-order-thinking](../second-order-thinking/SKILL.md).** Adds domain triggers, example, packs. Parent Process unchanged.
> **Not legal advice.**

**Activate when:** a suspiciously cheap carrier; identity/equipment mismatch at pickup; a carrier you never booked demands payment; cargo goes missing; scaling carrier onboarding.
**Do NOT activate when:** vetted, tracked, single-carrier move with clean signals.

## Why this variant
The parent [second-order-thinking] traces consequences others miss. Double-brokering is a second-order trap: booking a cheap "carrier" who secretly re-brokers to a real hauler → you pay the fraudster, the real carrier goes unpaid and pursues the shipper → cargo claims, lost account, liability cascade.

## Domain inputs → the cascade
- 1st: attractive low rate, load "covered."
- 2nd: the entity hauling ≠ the entity booked; real carrier unpaid; fraudster disappears with the payment.
- 3rd: unpaid carrier files against the shipper/broker bond; cargo claim; shipper churn; bond/insurance exposure.
- Parties: broker, shipper, real carrier, surety.

## Worked example
Booked "ABC Logistics" (new authority, gmail) at a low rate; at delivery the BOL shows a different carrier.
→ Second-order: ABC re-brokered; when you pay ABC, the real carrier chases the shipper. Mitigate now: verify hauling carrier = booked carrier, require tracking, hold payment on mismatch, and file the fraud.

## Compliance anchors
- Consent-to-re-broker rules; broker surety bond exposure; carrier vetting duty (pairs with freight-carrier-vetting-checklist).

## Packs
- **Solo broker**: fraud-signal watchlist + payment-hold rule on mismatch.
- **Brokerage**: automated identity re-verify at pickup; anomaly alerts.

## Red flags
- Rate far below market; brand-new authority; VoIP/gmail; hauling entity ≠ booked; pressure to pay fast.

## Verification
- [ ] Hauling carrier confirmed = booked carrier
- [ ] Tracking required and active
- [ ] Payment held on any identity/equipment mismatch
- [ ] Fraud reported; bond/insurance exposure assessed

---
Part of **deciqAI Knowledge Skills**. Core method: [second-order-thinking](../second-order-thinking/SKILL.md).
