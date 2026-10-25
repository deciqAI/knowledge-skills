# Sources — agent-ready-product-data

> *Primary sources for the [agent-ready-product-data](../SKILL.md) skill.*

## Data standards the field audit checks against

- **Google Merchant Center Help.** "Product data specification." **Primary source for required product attributes, identifiers and variant handling in a major shopping feed.** https://support.google.com/merchants/answer/7052112
- **Google Search Central.** "Product (Product, Review, Offer) structured data." **Primary source for on-page structured data for products, offers, shipping and returns.** https://developers.google.com/search/docs/appearance/structured-data/product
- **Schema.org vocabulary.** `Product` https://schema.org/Product · `Offer` https://schema.org/Offer · `OfferShippingDetails` https://schema.org/OfferShippingDetails · `MerchantReturnPolicy` https://schema.org/MerchantReturnPolicy. **Primary definitions of the types named in Step 3.**
- **GS1.** "Global Trade Item Number (GTIN)." **Primary source for the GTIN identifier standard (Step 1).** https://www.gs1.org/standards/id-keys/gtin

## Agent channel and protocol (worked example)

- **OpenAI** (September 29, 2025). "Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol." **Primary source for the launch, the Etsy/Shopify merchant scope, the open-sourcing of the protocol, and the ranking factors quoted in the example.** https://openai.com/index/buy-it-in-chatgpt/
- **OpenAI** (March 24, 2026). "Powering Product Discovery in ChatGPT." **Primary source for the move to merchants' own checkout, the extension of the protocol to discovery, and the retailers named as integrated.** https://openai.com/index/powering-product-discovery-in-chatgpt/
- **OpenAI Developers.** "Products — Agentic Commerce" (product feed specification; read October 2026). **Primary source for the required fields, variant rules, money format, shipping/returns semantics and checkout policy fields quoted in the example.** https://developers.openai.com/commerce/specs/file-upload/products
- **Agentic Commerce Protocol** — project site and open specification repository. **Primary source for the protocol itself.** https://www.agenticcommerce.dev/ · https://github.com/agentic-commerce-protocol/agentic-commerce-protocol

## What is NOT cited and why

- The **Seen → Understood → Bought** funnel and the agent-testing method (3+ agents, ≥3 runs per layer, 4-week re-test) are a deciqAI practice synthesis, not a published framework.
- **No agent-shopping conversion statistics are cited.** None we could verify from a primary source; third-party estimates are omitted rather than repeated.
- Secondary reports on how many merchants went live on Instant Checkout before March 2026 are **not** used; OpenAI's own post states the reason for the change, and that is what the example relies on.
- Agent checkout protocols are evolving quickly. Check the channel's current documentation before integrating; the feed specification quoted in the example is versioned.
