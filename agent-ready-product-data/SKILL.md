---
name: agent-ready-product-data
description: "Activate when: user says 'make our products buyable by AI shopping agents', 'is our product data agent-ready?', 'agentic commerce', 'the agent failed to place the order', asks 'why doesn't ChatGPT / a shopping agent recommend or buy our products?', is preparing a product feed for an AI assistant or an agent checkout protocol, or wants a catalog that AI agents can read, compare and purchase from.
  Do NOT activate when: the goal is only how often the brand is mentioned inside AI answers (use geo-generative-engine-optimization); there is no online purchase channel; the business is offline-only or quote-based B2B; the category may not legally be sold through automated channels. More: deciqai.com/s/agent-ready-product-data"
---

# Agent-Ready Product Data


## Overview

An AI shopping agent does not respond to photography, mood or persuasive copy. It reads **structured attributes, unambiguous variants, and machine-readable price, stock, shipping and returns**. What it cannot parse, it skips; what it parses wrongly, it buys wrongly — and the merchant pays for the return and the complaint.

The core mechanism: **the agent funnel is Seen (retrieved) → Understood (attributes and variants are unambiguous) → Bought (price, stock, policies and checkout have no blockers), and each layer is measured and repaired separately.** A product that is perfectly described but invisible, or visible but uncheckoutable, loses the sale to the competitor whose data is more complete.

Compose with [geo-generative-engine-optimization](../geo-generative-engine-optimization/SKILL.md) (getting recommended) · [checklist](../checklist/SKILL.md) (field completeness as a hard checklist) · [theory-of-constraints](../theory-of-constraints/SKILL.md) (fix the narrowest funnel layer first).

## When to Use

- Products appear in AI answers, but with stale information, the wrong variant, or the wrong price
- Test orders through an agent stall at variant selection, shipping cost, forced login or a CAPTCHA
- Preparing to submit a product feed, adopt an agent checkout protocol, or list in a platform catalog read by AI assistants

**When NOT to use:** no online transaction · products require a custom quote · categories where regulation bars automated sale · the problem is brand mentions, not catalog data.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has concrete SKUs and a channel → run The Process directly.
- **Coach mode:** user is unfamiliar → guide one step at a time.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What it is:** "An agent only trusts fields it can parse. One missing field can cost one order."
2. **Check fit:** "Can a customer buy your product online, directly, without a quote?"
3. **Elicit the real case:** "Pick 3 best-selling SKUs. Send the product-page links and the attributes you most want an agent to understand."
> **[WAIT — do not advance until user responds]**
4. **Run The Process:** "Run an agent through find → compare → add to cart → checkout on each SKU and record every point where it stalls."
> **[WAIT — do not advance until user responds]**
5. **Name the insight:** "Your loss sits in one layer — Seen, Understood or Bought. Fix that layer first."

## The Process

**Output:** SKU field audit + measured agent funnel + repair list

1. **Field audit.** For every SKU: title, brand, GTIN/MPN, category, material, dimensions, compatibility, intended user. Check against the target channel's published feed specification and schema.org `Product`. *Gate: required-field missing rate is zero → otherwise fill fields first.*
2. **Disambiguate variants.** Every color / size / bundle is its own identifiable variant with its own ID, price, stock status and image; attribute names and values are standardized, with units. *Gate: any single variant can be located uniquely → otherwise split it.*
3. **Machine-readable transaction data.** Price (with currency and promotion window), availability, shipping cost and time, and return policy are expressed in the feed and in structured data (`Offer`, `OfferShippingDetails`, `MerchantReturnPolicy`), and match the page. *Gate: feed, schema and page agree → otherwise regenerate all three from one source of truth.*
4. **Policy and trust pages.** Returns, warranty, privacy, terms and contact pages are public, crawlable, explicit, and need no login.
5. **Cut checkout friction.** Allow guest checkout and standard payment methods; remove forced registration and unnecessary verification; evaluate the agent checkout path the channel or protocol offers, and treat it as replaceable — channel checkout models change. *Gate: never bypass fraud controls or payment security for speed.*
6. **Test with real agents.** Use 3+ shopping agents or assistants, prompted the way buyers prompt, through the full flow. For each SKU record: Seen? Understood (attributes and price correct)? Bought? *Gate: ≥3 runs per layer → otherwise no conclusion.*
7. **Repair and re-test.** Fix the layer with the largest loss first; re-test in 4 weeks.
8. **Stop-rule:** data is complete and the product is still not Seen → the problem is no longer catalog data; move to brand and third-party evidence work ([geo-generative-engine-optimization](../geo-generative-engine-optimization/SKILL.md)).

**Output template:**
`SKU | missing fields | variant issues | price/stock/shipping/returns consistent? | Seen rate | Understood rate | Bought rate | blocker | fix | re-test date`

*→ Method in Action: [ChatGPT shopping and the Agentic Commerce Protocol (2025–2026)](examples/chatgpt-shopping-agentic-commerce-protocol-2025-2026.md)*

## Applying It Well

1. **One source of truth.** Generate page, feed and schema from the same record so they cannot drift apart.
2. **Write attributes for machines.** Standard units and enumerated values, not "extra large" or "slimming".
3. **Unknown is not zero.** Omit a value you do not know rather than filling a placeholder; an omitted shipping charge reads as unknown, not free.
4. **Test beats inference.** Re-run the agent flow after every catalog or site change.
5. **Separate the durable layers from the volatile one.** Clean attributes and variants serve every channel; a specific checkout integration may be withdrawn.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "If a human can read the page, that's enough" | Agents parse fields; they do not read marketing copy or text baked into images. |
| [D] "Variants live in one dropdown on one page" | A variant without its own ID, price and stock is a variant the agent will pick wrongly. |
| [D] "Shipping is calculated at checkout" | An unknowable total pushes the agent toward a competitor whose total is transparent. |
| [D] "We installed a schema plugin, so we're done" | Plugins routinely miss fields or disagree with the page. Audit and test. |
| [D] "We integrated the channel's checkout, so we're agent-ready" | Checkout is the most volatile layer. If attributes and variants are weak, the product is still not Understood. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- No GTIN/MPN · feed price differs from page price · return policy behind a login · forced account creation at checkout
- Placeholder values ("n/a", "unknown") in required fields · variants sharing one ID · never tested with a real agent

## Verification

- [ ] Required-field missing rate is zero
- [ ] Every variant is uniquely locatable (own ID, price, stock, image)
- [ ] Feed, structured data and page agree on price, stock, shipping and returns
- [ ] Seen / Understood / Bought rates measured with ≥3 runs per layer
- [ ] Re-test date scheduled

---

*Part of **deciqAI Knowledge Skills** — 253 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/agent-ready-product-data** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/agent-ready-product-data.json*
