# Method in Action: Zappos's Concierge MVP (1999)

> *Example for the [mvp](../SKILL.md) skill.*

A worked example. Not Silicon-Valley myth — primary-source documented in Tony Hsieh's own writings.

In 1999, **Nick Swinmurn** had the idea for **Zappos**: an online shoe store. Conventional wisdom was clear: shoes were a "must touch" purchase; nobody would buy them online without trying them on; building inventory and a fulfillment back-end was a multimillion-dollar bet against this skepticism.

Rather than build the back-end, Swinmurn ran a **concierge MVP**. He went to local San Francisco shoe stores, took photos of shoes on the shelves with permission, posted those photos on a basic website, and — when an order came in — went back to the store, **bought the pair at retail price**, and shipped it to the customer himself. The site looked like a real e-commerce store; the back-end was Swinmurn manually buying and shipping shoes one pair at a time.

The MVP tested **one specific assumption**: *will customers buy shoes online at all, given a credible storefront and a return guarantee* — without committing to inventory, warehousing, supplier relationships, or scaled fulfillment. Each order was unprofitable (Swinmurn paid retail and shipping); that didn't matter. *The MVP existed for learning, not revenue.*

Walk the MVP Design Card on Zappos 1999:

- **Single assumption (Step 1):** *Consumers will purchase shoes online without prior physical try-on, at scale enough to justify building a true e-commerce + supplier back-end.*
- **MVP type (Step 2):** **Concierge**. Manual back-end behind an automated-looking front. The right choice because *the assumption is "will customers buy?"* — no inventory or supplier infrastructure was needed to test that.
- **Why this type (Step 2 rationale):** A smoke test (email capture) would have tested interest, not purchase. A real e-commerce build would have committed millions before testing the demand. Concierge isolates the load-bearing test.
- **Actionable metric (Step 3):** Order count over the first weeks. (Not site traffic; not signups. Actual orders with shipped shoes.)
- **Build time-box (Step 4):** Days, not months. The "build" was a basic website + a manual purchase-and-ship process.
- **Features excluded (Step 5):** Inventory system, supplier integrations, warehouse, automated fulfillment, return logistics platform. All absent.
- **Disposability (Step 6):** The concierge process was always temporary; it was a learning instrument, not the future operation. Once demand validated, Zappos built the real back-end (and eventually became the leader in online footwear, acquired by Amazon in 2009 for $1.2 billion).
- **Validated learning (Step 7):** *Consumers will buy shoes online at scale, given a credible storefront and a generous return policy — even without physical try-on; the load-bearing assumption against e-commerce in this category was wrong.*

The non-obvious feature: Swinmurn's MVP looked nothing like the eventual product (no real inventory, no real supply chain, manual everything) but **tested precisely the right assumption**. A better-engineered MVP — with real inventory in a small SKU range — would have **cost 100× more and tested the same assumption**.

**Sources:** Ries, Eric. *The Lean Startup* (Crown, 2011), pp. 76–81 — the MVP definition and discussion. Verbatim Overview quote is from p. 77. The Zappos concierge MVP is referenced in lean-startup literature and discussed by Hsieh in his own account: Hsieh, Tony. *Delivering Happiness: A Path to Profits, Passion, and Purpose* (Business Plus, 2010), chs. 1–2. Blank, Steve. "An MVP is not a Cheaper Product, It's about Smart Learning." Blog post, July 22, 2013: https://steveblank.com/2013/07/22/an-mvp-is-not-a-cheaper-product-its-about-smart-learning/ (verbatim quoted in Overview). Robinson, Frank — the originator of the term "MVP" at SyncDev, 2001; see SyncDev's history page: https://www.syncdev.com/minimum-viable-product/
