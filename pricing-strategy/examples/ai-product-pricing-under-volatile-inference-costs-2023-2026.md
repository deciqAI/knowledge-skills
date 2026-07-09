# Method in Action: Pricing an AI Product Under Volatile Inference Costs (2023–2026)

> *Example for the [pricing-strategy](../SKILL.md) skill.*

Where the De Beers case shows the framework executed deliberately and Qwikster shows it failing all at once, this case shows the framework applied to a *moving* cost base — the defining pricing problem of the 2023–2026 generative-AI wave. The distinctive feature: the input cost (model inference) is not fixed, and it moves in *both* directions with each model release — capability jumps up while per-token prices fall — so a price set against today's cost can be stranded within a quarter.

This is a synthesized worked example built on well-documented public facts about the period. Treat the specific vendor list-price movements below as illustrative of a widely-reported direction, not as exact quotes for any single day.

**The setup.** You sell an AI product — say, an AI coding assistant or a document-analysis tool — built on a frontier model API. Two forces move underneath your pricing at once:

1. **Per-token API prices fell sharply and repeatedly across the period.** OpenAI, Anthropic, and Google all cut token prices and shipped cheaper "mini/flash/haiku"-class models multiple times between 2023 and 2025. As a widely-reported directional fact, the cost of a given level of capability fell by roughly an order of magnitude over the period.
2. **Capability jumped with each release**, so customers expected *more* per dollar even as your unit cost fell — and heavy users could burn far more tokens than the average, making a flat seat price dangerous.

The result is a gross-margin trap: **a flat, seat-based subscription set against average usage bleeds margin on power users**, precisely the users an AI product attracts. This is not hypothetical — it became visible publicly in 2024–2025 when several usage-heavy AI products (notably in the coding-assistant category) publicly revised plans, added usage caps, or moved toward metered/credit models after heavy users ran costs above subscription revenue.

Now run the **Pricing Audit**.

**1. Articulate value to the customer in customer units.** Not "our model is smart" but the customer's own metric. For an AI coding assistant: *"merges ~4 more PRs per engineer per week"* or *"cuts ~6 engineer-hours/week of boilerplate."* At a loaded engineer cost, six hours a week is worth thousands of dollars per seat per month — an order of magnitude above any plausible inference cost. **The key move: value is anchored to the customer's labor cost, not to your token cost.** This is what lets you hold price while your input cost collapses.

**2. Estimate WTP per segment.** The segments diverge hard here:
- **Individual/prosumer:** low WTP, high price-sensitivity, benchmarks against a ~$20/month consumer-chatbot reference point (ChatGPT Plus / Claude Pro / Gemini list prices clustered near $20/month across the period — a durable, widely-known anchor).
- **Team/SMB:** moderate WTP, values seat simplicity and predictable bills.
- **Enterprise:** high WTP, values security, admin controls, and outcome guarantees — and, critically, has *high usage variance*. Measure via paid pilots (most reliable for B2B), not surveys. Enterprise WTP for a real workflow outcome is often 5–10× the prosumer tier for the same underlying model.

**3. Choose an anchor.** The trap is anchoring to the model API's per-token price — that number is falling and would drag your whole structure down with it. **Anchor instead to the value metric: the cost of the labor or the outcome you replace.** "This replaces ~6 engineer-hours/week" anchors to a large, *rising* number (wages), not a shrinking one (tokens). Enterprise tier anchors high on outcome + security and lifts the structure.

**4. Design the tier structure — and pick the pricing *model*, not just the number.** This is where the AI case departs from classic SaaS. Three archetypes, each protecting margin differently:
- **Seat-based (flat per user):** simplest to sell, predictable for the buyer — but *unprotected* against usage variance. A single power user can invert the unit economics. Safe only where usage is naturally bounded or a hard cap is attached.
- **Usage/metered (per token, per credit, per action):** margin-protecting by construction — cost passes through to price, so falling token prices become *your* margin gain or a competitive price cut you choose to make. Downside: unpredictable bills scare buyers and suppress adoption.
- **Outcome-based (per resolved ticket, per merged PR, per successful task):** captures the most value and aligns price to the customer's metric — but requires you to bear the inference cost per outcome, so it only works once your cost *per successful outcome* is stable and well below the outcome's value.

The resolution many teams were visibly moving toward through 2024–2025 (and the direction the market appeared to be settling into): a **hybrid** — a seat/subscription base for predictability, **plus** metered usage above an included allowance (credits), **with** an enterprise outcome-priced or committed-spend tier on top. Starter makes Pro affordable; metered overage protects margin on power users; the enterprise tier anchors and captures top WTP. Anthropic, OpenAI, and Google themselves ship exactly this shape at the API layer: flat consumer subscription, metered per-token API, plus enterprise/committed plans.

**5. Frame for loss aversion.** "Included allowance, then $X per additional 1,000 actions" frames overage as an add-on rather than a penalty. Annual commit framed as "save ~20% vs monthly" beats "monthly costs more." For enterprise, frame against the cost of *not* automating (the labor bill that keeps recurring) — the strongest AI-era frame because that cost is large and rising while your delivery cost falls.

**6. Stress-test the anchor.** Show the structure to 5–10 target buyers in each segment. The specific AI-era question to test: *"Does the metered component make the bill feel unpredictable enough to block the purchase?"* If yes for a segment, convert that segment to a higher flat tier with a generous-but-capped allowance and keep pure metering for the segments that tolerate it (usually enterprise with committed spend).

**7. Run a 60-day measurement — and add a margin-specific gauge.** Beyond conversion, upgrade rate, and discount-request frequency, the AI product must track **gross margin per active user and cost-per-outcome by cohort**, because the input cost is moving. The re-evaluation trigger is not just the calendar: **re-run the audit on every material model-price or model-capability release**, because each release changes both your cost floor and your customers' reference point. A price set against Q1's model economics can be wrong by Q3.

### The mapped steps

1. **Value in customer units:** labor/outcome replaced (e.g. ~6 engineer-hours/week), anchored to *rising* wages, not *falling* token cost.
2. **Segment WTP:** prosumer (~$20/mo reference point) ≪ team ≪ enterprise; enterprise 5–10× and high usage variance; measure via paid pilots.
3. **Anchor:** the value metric (cost of labor/outcome replaced), never the per-token API price.
4. **Structure:** hybrid — flat base + metered overage above an allowance + enterprise outcome/committed tier; choose seat vs. metered vs. outcome by *usage variance* and *cost-per-outcome stability*.
5. **Loss-aversion framing:** included allowance + annual-save framing; enterprise framed against the recurring, rising cost of *not* automating.
6. **Anchor stress test:** test bill-unpredictability per segment; flatten (capped allowance) where metering blocks the sale.
7. **Measurement:** add gross-margin-per-user and cost-per-outcome by cohort; re-run the audit on every material model price/capability release, not on a fixed 12-month cycle.

**The framework's lesson for the AI era:** when your input cost is volatile and falling, the mistake is to anchor price to that input. Anchor to the customer's value metric (which rises), let a metered component pass through usage variance so power users can't invert your margins, and treat each model release as a scheduled trigger to re-run the audit. Falling inference cost then becomes a lever you control — margin expansion, a chosen price cut, or a richer included allowance — rather than a race to the bottom you're dragged into by competitors pricing off the same collapsing token cost.

*Sources: OpenAI, Anthropic, and Google published API price lists and model-release announcements, 2023–2025 (repeated per-token price cuts and cheaper "mini/flash/haiku"-class models are documented across their pricing pages and release posts). Consumer subscription reference points (ChatGPT Plus, Claude Pro, Gemini Advanced) clustered near $20/month per each vendor's public pricing. Loss-aversion and reference-point mechanics: Kahneman & Tversky, "Prospect Theory," *Econometrica* 47(2), 1979. The public shift of usage-heavy AI products toward usage caps and metered/credit models in 2024–2025 was widely reported in the technology press. Specific per-vendor price figures should be confirmed against current published pricing pages before quoting.*
