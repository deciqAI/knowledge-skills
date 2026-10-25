# Method in Action: ChatGPT Shopping and the Agentic Commerce Protocol (2025–2026)

> *Example for the [agent-ready-product-data](../SKILL.md) skill.*

This is not a single merchant's story. It is the public record of one large AI shopping channel — what OpenAI said its agent reads, what it requires from merchants, and how its checkout layer changed within six months. Walking that record through the Process shows which parts of "agent-ready" are durable and which are volatile. Every fact below comes from OpenAI's own announcements and its published feed specification.

**The launch (September 29, 2025).** OpenAI announced Instant Checkout in ChatGPT, "powered by the Agentic Commerce Protocol, built with Stripe." U.S. users could buy directly from U.S. Etsy sellers in chat, with "over a million Shopify merchants" announced as coming soon. The protocol was open-sourced. OpenAI described its ranking: product results are "organic and unsponsored, ranked purely on relevance," and when several merchants sell the same product, ChatGPT "considers factors like availability, price, quality, whether a merchant is the primary seller, and whether Instant Checkout is enabled."

**The change (March 24, 2026).** OpenAI wrote that "the initial version of Instant Checkout did not offer the level of flexibility that we aspire to provide, so we're allowing merchants to use their own checkout experiences while we focus our efforts on product discovery." In the same post it extended the Agentic Commerce Protocol to discovery — "merchants share product feeds and promotions so their catalogs are fully represented in ChatGPT" — and named Target, Sephora, Nordstrom, Lowe's, Best Buy, The Home Depot and Wayfair as already integrated for discovery. Shopify merchants' product data reaches ChatGPT through Shopify Catalog.

So within six months, the channel's **Bought** layer was redesigned, while its **Seen** and **Understood** layers — the product feed — became the center of the integration.

## Running the Process against the published spec

The feed specification (OpenAI Developers, "Products — Agentic Commerce", read October 2026; the spec is versioned and may have changed since) maps almost line for line onto the Process.

1. **Field audit.** Nine fields are required on every row: `item_id`, `title`, `description`, `url`, `brand`, `seller_name`, `image_url`, `availability`, `price`. The spec says to "use a real brand and seller name, not placeholders" and forbids placeholder strings such as `null`, `unknown` or `n/a` (with `unknown` allowed only where explicitly listed). Optional attributes — `material`, `color`, `size`, `dimensions` with an explicit unit, `weight` with a unit — exist precisely so an agent can compare. *Gate: a row with a missing required field, or a placeholder in it, is not agent-ready.*

2. **Disambiguate variants.** "Submit one row per purchasable item or variant." Each variant gets a distinct `item_id`, a shared `group_id`, and a `variant_dict` of the selected options; "each row carries its own price, availability, URL, and images." IDs must stay stable when price or stock changes, and "never include price in an offer ID." GTINs must be exactly 8, 12, 13 or 14 digits with a valid check digit, and the spec warns not to "invent a value to replace a missing GTIN." *Gate: a dropdown variant with no row of its own fails this step.*

3. **Machine-readable transaction data.** Price must be written as an amount plus ISO 4217 code (`79.99 USD`). The spec states that an omitted `shipping_price` "means unknown, not free shipping," and that sale-window dates "do not schedule price or availability changes" — the merchant must update the feed when prices change. Returns are separate fields (`accepts_returns`, `return_deadline_in_days`, `return_policy` URL). *Gate: feed and page must agree — the spec warns, of conflicting attribute values within a row, that "neither representation reconciles conflicting values for you," and the same logic applies between feed and page.*

4. **Policy and trust pages.** Checkout eligibility is "conditionally required" to include a public `seller_privacy_policy` and `seller_tos` URL. Product and image URLs "must be publicly accessible." A policy behind a login fails this step.

5. **Checkout friction — and its volatility.** In September 2025, enabling Instant Checkout was one of the ranking factors OpenAI listed. By March 2026 merchants were directed back to their own checkout, with ChatGPT apps as the option for deeper native experiences (Walmart was the example named). A merchant who had treated "integrated Instant Checkout" as the finish line had optimized the layer that changed; a merchant who had cleaned fields and variants kept that work. This is why the Process marks the channel checkout as *replaceable*. *Gate: never trade away fraud controls or payment security for a faster integration.*

6. **Test with real agents.** The spec itself concedes that "format guidance is not a guarantee that every invalid value will be rejected at upload," and that eligibility "does not guarantee display." Passing validation is not the same as being Seen, Understood and Bought — only end-to-end runs show that.

7. **Repair and re-test.** The channel's own history argues for a fixed re-test cadence: the integration model changed inside two quarters.

## What the case shows

- **The durable asset is the data, not the integration.** Required fields, one-row-per-variant, unit-bearing attributes and explicit availability served the channel both before and after its checkout change.
- **"Unknown" is a value an agent treats differently from "zero" or "free."** The spec spells this out for shipping, availability and returns; a catalog that leaves these blank, or fills them with placeholders, is ambiguous by construction.
- **The stop-rule applies.** A product that passes every field check and is still not surfaced has left the domain of catalog data; ranking also weighs price, quality and primary-seller status, which no feed field can fix.

Primary sources: OpenAI, "Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol" (September 29, 2025), https://openai.com/index/buy-it-in-chatgpt/ · OpenAI, "Powering Product Discovery in ChatGPT" (March 24, 2026), https://openai.com/index/powering-product-discovery-in-chatgpt/ · OpenAI Developers, "Products — Agentic Commerce" feed specification, https://developers.openai.com/commerce/specs/file-upload/products
