# Method in Action: Where AI SaaS Funnels Leak (2023–2026)

> *Example for the [aarrr-pirate-metrics](../SKILL.md) skill.*

A pattern-level worked example — not a single company, but the recurring funnel shape observed across the wave of AI-native SaaS products that launched after ChatGPT's release in November 2022. The generative-AI boom pushed a distinctive failure mode to the surface: acquisition became historically *easy* while activation and retention became the real leaks. This example applies the Funnel Audit to that pattern. Where a specific number would be fragile, it is qualified or omitted.

The context in one line (drawn from the 2023–2025 record; the pattern appears to persist but recent periods should be re-checked against current data): after the November 2022 ChatGPT launch, curiosity and press drove enormous top-of-funnel traffic to anything labeled "AI," and by early 2025 the AI-native SaaS category was crowded with near-identical wrapper products competing on the same underlying foundation models. In that environment, *showing up* is cheap and *staying* is hard — the inverse of the classic pre-AI SaaS funnel, where distribution was the scarce resource.

Walk the Funnel Audit (matching the SKILL.md Process steps):

**Step 1 — Define each stage for this specific product.** For a generic AI SaaS assistant:
- **Acquisition** = visitor lands on the site and creates an account (often driven by AI-hype PR, launch-day virality, or a viral demo).
- **Activation** = the user reaches first real value — i.e., they get past the **empty state** and complete one genuinely useful task with the AI (a good draft, a correct answer on *their own* data, a workflow actually finished), not merely "typed one prompt."
- **Retention** = the user returns and uses the product in a later week for real work, *after the novelty of trying an AI toy has worn off*.
- **Referral** = the user shares an output or invites a colleague.
- **Revenue** = the user converts from free trial to a paid subscription.

The single most common definitional error here is calling "signed up and sent one message" *Activation*. That is the end of Acquisition. AI products are unusually vulnerable to this because a first prompt is trivially easy, so the vanity signal looks great while no durable value has been delivered.

**Step 2 — Measure conversion at each stage.** The characteristic AI-SaaS reading:
- Acquisition→Activation: **leaky.** Many curiosity-driven signups hit a blank chat box or empty canvas, don't know what to type, get a generic or hallucinated first result, and never reach first value. This is the **empty-state / first-value** leak.
- Activation→Retention: **the deepest leak.** Even users who got one impressive result often don't come back, because the initial "wow" was novelty, not a solved recurring job. This is the **novelty-decay** leak.
- Retention→Referral and →Revenue: mostly downstream symptoms — thin because too few users retained.

**Step 3 — Compare against domain benchmarks.** By the consumer-freemium and B2B-SaaS packs in this skill, healthy day-30 retention for sticky SaaS is high (B2B 70%+; strong freemium keeps a meaningful engaged core). The widely-discussed concern across 2023–2025 was that many AI-native apps retained *well below* comparable non-AI SaaS — high novelty-driven signups, weak week-4+ engagement. Treat specific retention percentages as directional; the durable, well-reported fact is the *shape*: acquisition strong, activation and retention weak relative to benchmark.

**Step 4 — Identify the load-bearing bottleneck.** Absolute counts mislead here: Acquisition has the biggest number and looks like a triumph. But relative to benchmark, the worst two stages are **Activation (empty-state → first value)** and **Retention (surviving novelty decay)**. Pouring more launch-day traffic into this funnel — the tempting move when AI PR makes acquisition cheap — just fills a leaky bucket faster. The constraint is not "get more signups"; it is "get signups to first value, then to a recurring job."

**Step 5 — Pre-commit one experiment.** Attack Activation first (it gates Retention). Example intervention and pre-committed threshold:
- *Change:* replace the blank empty state with guided templates / example prompts / a one-click "do a real task on sample-or-your data" onboarding, so a new user reaches a genuinely useful first result inside session one.
- *Metric:* Acquisition→Activation conversion (reached first real value).
- *Threshold:* pre-commit a target lift (e.g. +X percentage points) before running it, per [lean-startup](../lean-startup/SKILL.md).
- *Window:* a fixed measurement period (e.g. 4 weeks of new cohorts).

**Step 6 — Re-measure and re-identify.** Once activation improves, the bottleneck **moves to Retention** — and the fix there is different in kind: it requires embedding the product in a recurring job (memory of the user's context, integrations into daily workflow, results that improve with use) so the tool survives after novelty fades. Re-run the audit; do not assume the first fix is the last.

**The non-obvious lesson.** In the pre-AI SaaS era the scarce resource was distribution, so teams instinctively optimized Acquisition. The post-2022 AI wave inverted this: foundation models and hype made Acquisition abundant and near-commoditized (many products wrap the same models), which pushed the true constraint downstream to **Activation and Retention**. A team that reads its own soaring signup chart as success is optimizing the stage that isn't broken. The audit's discipline — *worst conversion relative to benchmark, not the lowest absolute number* — is exactly what stops that mistake. It also reframes the "AI moat" question: durable retention (a solved recurring job, accumulated user context, workflow integration) is the moat, not the model, because the model is the one thing every competitor also has.

*Sources: McClure, Dave. "Startup Metrics for Pirates" — the AARRR framework, first presented in 2007 (Ignite Seattle); the widely-circulated "long version" slide deck cited here is the Startonomics SF (October 2008) edition: https://www.slideshare.net/dmc500hats/startup-metrics-for-pirates-long-version . Goldratt, Eliyahu M. "The Goal" (North River Press, 1984) — Theory of Constraints / bottleneck logic. OpenAI, "Introducing ChatGPT" (Nov 30, 2022): https://openai.com/blog/chatgpt — dates the acquisition-side inflection. Sequoia Capital, "Generative AI: A Creative New World" (2022) and "AI's $600B Question" (David Cahn, 2024): https://www.sequoiacap.com/article/ais-600b-question/ — widely-cited discussion of the AI capex build-out and the gap between AI infrastructure spend and durable end-application revenue/retention. Retention-shape claims are stated qualitatively; specific per-app retention figures are omitted as fragile.*
