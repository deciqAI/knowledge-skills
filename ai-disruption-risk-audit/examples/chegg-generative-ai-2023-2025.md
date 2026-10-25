# Method in Action: Chegg and Generative AI (2023–2025)

> *Example for the [ai-disruption-risk-audit](../SKILL.md) skill.*

A worked example of AI disruption arriving at two different activities of the same business, two years apart — documented in Chegg's own earnings releases and annual report, and in CNBC's market coverage. The audit below is a retrospective reading of the public record through the skill's steps; Chegg did not publish such an audit, and the scores are illustrative of the method, not Chegg's internal figures.

**The first signal (May 1, 2023).** Chegg reported Q1 2023 total net revenues of **$187.6 million, down 7%** year over year, with Subscription Services at **$168.4 million — 90% of revenue** — and 5.1 million subscribers, down 5%. CEO Dan Rosensweig said on the call: "In the first part of the year, we saw no noticeable impact from ChatGPT on our new account growth… However, since March we saw a significant spike in student interest in ChatGPT. We now believe it's having an impact on our new customer growth rate." He added that Chegg continued "to see very strong retention rates." The company gave only next-quarter guidance. On May 2 the stock lost roughly half its value — CNBC reported a **48% plunge** from a prior close of $17.60. A Piper Sandler note quoted by CNBC asked whether AI advances would "democratize their core offering to the extent that their competitive barriers are lowered."

**The second signal (February 24, 2025).** Chegg reported Q4 2024 total net revenues of **$143.5 million, down 24%**, announced a strategic review, and filed a complaint against Google LLC and Alphabet Inc. The release said Chegg "would not need to review strategic alternatives if Google hadn't launched AI Overviews," and that non-subscriber traffic "plummeted to negative 49% in January 2025, down significantly from the modest 8% decline we reported in Q2 2024." The annual report gives the quarterly path: non-subscriber traffic down 8% in Q2 2024, 19% in Q3 and 39% in Q4.

## Running the Process

1. **Break down the value chain.** From the Q1 2023 release: Subscription Services (Chegg Study Pack, Chegg Study, Chegg Writing, Chegg Math, Busuu) at 90% of revenue; Skills and Other (Thinkful, advertising) at the rest. Underneath the subscription line sit distinct activities: **(a)** answering homework questions step by step, **(b)** writing and math tools, **(c)** acquiring new students — in part through search traffic; the 2025 release says AI Overviews were "retaining traffic that historically had come to Chegg, materially impacting our acquisitions" — and **(d)** retaining existing subscribers.

2–3. **Substitutability and cost collapse.** Activity (a) is standardized, digitized and text-in/text-out — the kind of task a general-purpose chatbot performs for free. The company's own words ("significant spike in student interest in ChatGPT") are the test result the skill asks for: customers ran the test themselves. Illustrative scores: substitutability 5, cost collapse 5.

4. **Customer bypass risk.** Switching cost for a student asking a homework question is low, and there is no liability or credential requirement attached to the answer. The record shows the bypass hitting **new customer growth** first while **retention stayed strong** — exactly the pattern in the skill's rationalization table: an existing relationship protected existing accounts, not acquisition. *Gate fires: high substitutability + low switching cost → red zone.*

   The second red zone is the one a product-only audit misses: activity (c), **distribution**. When Google's AI Overviews answered queries on the results page, the channel that delivered prospective students stopped delivering them (-8% → -19% → -39% → -49% non-subscriber traffic). Customers did not have to reject Chegg's product; they never reached it.

5. **Where advantage migrates.** In May 2023 Chegg named its candidates: "our proprietary data, our 150,000+ experts, and our decade-plus years of experience," combined with CheggMate, built with OpenAI. The Process asks two questions of each: *do you own it?* and *can AI reproduce it too?* A library of step-by-step solutions is owned — but if a general model answers the same questions acceptably, it is a red-zone asset, not a migration point. The migration points the record shows mattering were distribution and the customer's starting point for a query — neither of which Chegg controlled.

6. **Decide the action.** The red-zone choices in the skill are retreat (re-price, bundle) or attack (rebuild on AI first, at the lower price). Chegg chose to attack with CheggMate in 2023; by 2025 it was reviewing strategic alternatives. The audit does not judge the decision in hindsight; it shows that the distribution activity needed its own row, owner and 90-day metric from the start — non-subscriber traffic was the leading indicator, and it was falling for three quarters before the strategic review.

7. **Stop-rule and re-score.** The six-month re-score rule fits the record: the product-layer shock (ChatGPT, early 2023) and the distribution-layer shock (AI Overviews, visible in Chegg's reported traffic from Q2 2024) arrived far enough apart that a single audit would have scored the second as green.

## The mapped steps

1. Value chain: Q&A content, tools, acquisition via search traffic, retention
2–3. Q&A content: substitutability and cost collapse at the maximum; customers ran the test
4. Bypass: new-customer growth hit while retention held; distribution became a second red zone
5. Migration points claimed (content, experts) were themselves exposed; distribution was not owned
6. Action: attack (CheggMate) in 2023; strategic review in 2025
7. Re-score: two shocks two years apart — a one-off audit misses the second

**The lesson.** Score the channel that delivers your customers, not only the work you deliver to them. An audit that stops at "can AI do our product?" will catch the first shock and miss the second.

Primary sources: Chegg, "Chegg Announces First Quarter 2023 Earnings" (May 1, 2023), https://investor.chegg.com/Press-Releases/press-release-details/2023/Chegg-Announces-First-Quarter-2023-Earnings/default.aspx · Chegg, "Chegg Reports 2024 Fourth Quarter and Full Year Financial Results" (February 24, 2025), https://investor.chegg.com/Press-Releases/press-release-details/2025/Chegg-Reports-2024-Fourth-Quarter-and-Full-Year-Financial-Results/default.aspx · Chegg, Form 10-K for fiscal year 2024, https://www.sec.gov/Archives/edgar/data/1364954/000136495425000013/chgg-20241231.htm · Ari Levy, "Chegg shares rebound with 17% pop after losing almost half their value on ChatGPT concerns," CNBC, May 3, 2023, https://www.cnbc.com/2023/05/03/chegg-shares-jump-17percent-wednesday-after-dropping-48percent-on-chatgpt-concerns.html
