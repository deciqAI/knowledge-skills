# Method in Action: Klarna's AI Assistant — The $40M Estimate and the Quality Reversal (2024–2025)

> *Example for the [ai-roi-business-case](../SKILL.md) skill.*

Klarna's customer-service assistant is the most widely quoted public AI business case of the period, and it is unusual in that the company published its headline numbers. Fifteen months later the CEO publicly said the evaluation had leaned too hard on cost. Both statements are on the record, which makes it a clean test of the ROI table: what the published case contained, and which line of the table the reversal came from.

**The published case (February 27, 2024).** Klarna announced that its OpenAI-powered assistant, live globally for one month, had:

- had **2.3 million conversations — two-thirds of Klarna's customer service chats**
- done "the equivalent work of **700 full-time agents**"
- been "on par with human agents in regard to customer satisfaction score"
- produced "a **25% drop in repeat inquiries**"
- cut time to resolve errands to "**less than 2 mins compared to 11 mins previously**"
- run in 23 markets, 24/7, in more than 35 languages
- been "estimated to drive a **$40 million USD in profit** improvement to Klarna in 2024"

The release also noted that "customers can still choose to interact with live agents if they'd prefer."

**The reversal (May 2025).** In a Bloomberg interview, CEO Sebastian Siemiatkowski said: "As cost unfortunately seems to have been a too predominant evaluation factor when organizing this, what you end up having is lower quality," and that it is "so critical that you are clear to your customer that there will be always a human if you want." Klarna began recruiting human customer-service staff again, piloting a flexible remote setup; in a clarification added to Fortune's report, Klarna said it remained "very much still AI-first."

Now run the **ROI table** against the public record.

**1. Baseline.** Present, and stated: 11 minutes to resolve an errand before, a measurable repeat-inquiry rate, a customer-satisfaction score for human agents. **Pass** — the published case had a real before-state to compare against.

**2. Value levers + realization path.** Two levers are visible: speed (11 → under 2 minutes) and labor (700 FTE-equivalent). The release does not say how the 700-FTE equivalence would be realized — fewer contracted agents, slower hiring, or redeployment. The $40M figure is labeled an *estimate* for the year. **Not auditable from the release:** the realization path for the largest lever is not published.

**3. Full cost.** The release reports no costs: no inference spend, integration work, review effort or change management. That is normal for a press release — but a business case that looked like this internally would fail the gate ("review time not counted → stop"). **Cannot be verified; the public number is a gross-value estimate, not ROI.**

**4. Adoption ramp.** Unusually, adoption was fast and measured: two-thirds of chats in month one. The ramp gate exists to stop *assumed* full adoption; here adoption was observed. **Pass** — and a reminder that the ramp step uses data when data exists.

**5. Payback and ROI.** Not computable from public data, because step 3 is missing. The $40M estimate is a profit-improvement figure, not a payback period.

**6. Sensitivity — where the case broke.** The table requires a pessimistic scenario on the drivers that matter. The quantity that later moved was **quality**: the CEO's own diagnosis was that cost dominated the evaluation and "what you end up having is lower quality." In the table's terms, quality had been treated as a constraint already satisfied ("on par" CSAT at month one) rather than as a variable with a pessimistic case. A downside scenario asking "what if resolution quality or customer trust erodes as volume shifts to the bot?" — and pricing the cost of rehiring and of lost customer trust — is exactly what step 6 is for. **This is the line the reversal came from.**

**7. Kill line / guardrail.** The public record shows no pre-stated threshold, though the release preserved a human option. The May 2025 correction — guaranteeing that a human is always available — works as a guardrail added after the fact. Written at approval, it would have been a kill-or-downgrade condition: "if quality metric Y falls below X, route Z% of contacts back to humans."

### The mapped steps

1. **Baseline:** 11 min resolution, repeat-inquiry rate, human CSAT — present
2. **Levers:** speed + 700-FTE labor equivalence; realization path for labor not published
3. **Full cost:** not published — the $40M is gross estimated value, not ROI
4. **Adoption ramp:** observed, two-thirds of chats in month one
5. **Payback / ROI:** not computable from the public record
6. **Sensitivity:** quality had no pessimistic case → the eventual failure mode (CEO, May 2025)
7. **Kill line:** none stated publicly; "always a human" guardrail added afterwards

**The lesson.** The published case was strong on the steps that make a slide convincing — baseline, speed and adoption — and silent on the steps that make an ROI survive: full cost, realization path and a pessimistic scenario on quality. The reversal did not come from inference pricing or adoption; it came from the variable that had been treated as settled. Put quality in the sensitivity table, and write the guardrail before launch.

*Primary sources: Klarna press release, "Klarna AI assistant handles two-thirds of customer service chats in its first month," February 27, 2024, https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ · Bloomberg, "Klarna Slows AI-Driven Job Cuts With Call for Real People," May 8, 2025, https://www.bloomberg.com/news/articles/2025-05-08/klarna-turns-from-ai-to-real-person-customer-service (paywalled; quotes corroborated by Fortune, May 9, 2025, https://fortune.com/2025/05/09/klarna-ai-humans-return-on-investment/). Klarna's internal cost data is not public; no cost or ROI figure is inferred here.*
