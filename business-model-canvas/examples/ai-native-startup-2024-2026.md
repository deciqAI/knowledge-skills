# Method in Action: Mapping an AI-Native Startup (2024–2026)

> *Example for the [business-model-canvas](../SKILL.md) skill.*

The 2024–2026 wave of AI-native startups — companies whose core product is a wrapper of value around a third-party foundation model (coding assistants, support-automation agents, drafting and research copilots) — breaks two habits the canvas was built to expose. First, revenue is often **usage- or outcome-based**, not a flat SaaS seat, so the Revenue Streams block and the Cost Structure block move *together* with volume. Second, the dominant variable cost is **inference compute**, and the supplier of that compute is frequently the *same* firm whose model the product depends on — so a single named entity sits in both Key Partners and, inverted, in the Cost Structure and the competitive threat. The canvas is useful here precisely because it forces those couplings onto one page.

This maps a *representative composite* AI-native startup, not a specific company's internal numbers — the point is the block structure, which was widely reported across the sector through 2024–2025.

**1. Customer Segments.** Not "businesses that want AI." A named wedge: e.g., mid-market engineering teams (20–200 developers) who already pay for developer tooling, or B2B support organizations with high ticket volume. Multi-sided is usually *not* the trap here — most of these are single-sided B2B — but the real segment risk is that the buyer (a VP) and the user (an individual dev or agent) differ, so awareness and value must land on both.

**2. Value Propositions.** Stated in the customer's own units: "resolve X% of support tickets without a human," "cut time-to-first-draft from hours to minutes," "close tickets at $Y instead of $Z of loaded human cost." The temptation is to list model capabilities ("powered by a frontier LLM," "128k context"). Those are features. What the customer *gets* is displaced labor cost, latency, or throughput — the value prop must be in those units or it is untestable.

**3. Channels.** Awareness through developer communities, content, and marketplace listings (the model provider's app store or a cloud marketplace); evaluation through a free tier or trial where the product's *own* inference cost is being spent on an unpaid user; purchase self-serve or sales-assisted; delivery via API/SaaS; after-sales through support and, critically, **usage monitoring** — because in a usage-billed model the channel must keep showing the customer the value that justifies a variable bill.

**4. Customer Relationships.** Largely self-service and product-led for the wedge, shifting to personal/enterprise-success motions upmarket. A subtle relationship risk: outcome-based pricing makes the vendor and customer partly *aligned on the customer's success*, which is a relationship asset — but disputes over "did the agent actually resolve it" are a relationship liability.

**5. Revenue Streams.** The load-bearing 2024–2026 shift. Models seen across the sector: per-seat (legacy SaaS carryover), usage/consumption (per token, per API call, per message), and **outcome-based** (per resolved ticket, per successful action). *Why they pay* is the displaced cost from block 2. The trap: **gross margin is not fixed.** In classic SaaS, cost of revenue is near-zero at the margin; here every unit of usage triggers a real inference bill, so a heavy user can be unprofitable at a flat price. Willingness-to-pay must be tested against *realized* cost-to-serve, not list price.

**6. Key Resources.** The genuinely distinctive set is thin and worth naming honestly: proprietary data/feedback loops (customer interactions that fine-tune or route better over time), workflow integrations and the resulting switching cost, brand/distribution — and *access to compute capacity and model quality on acceptable terms*. The base model itself is usually **not** a distinctive resource, because a competitor can call the same API.

**7. Key Activities.** What must be done distinctively well: prompt/agent orchestration and evaluation, guardrails and reliability, the integration surface into the customer's systems, and **inference cost engineering** — caching, routing to smaller models, batching — because unit economics live here. Training a foundation model is *not* on this list for most of these companies; that is deliberately outsourced.

**8. Key Partners.** The foundation-model provider is the marquee named partner — it supplies the model *and* often the compute, may provide distribution (marketplace, co-selling), and sets pricing that flows straight into block 9. Replacement risk cuts both ways: multi-model abstraction lowers dependence, but true switching still costs re-evaluation, re-tuning, and quality regressions. Other partners: the underlying cloud/GPU provider, and any data or systems-of-record integrations.

**9. Cost Structure.** Value-driven at the top of funnel but with an unusually large **variable** component: inference compute per unit of usage is the dominant marginal cost, alongside R&D salaries (largely fixed) and go-to-market. This is the block that most distinguishes an AI-native model from classic SaaS — and it is coupled to block 8, since the partner sets the input price, and to block 5, since revenue and this cost scale together.

**Audit — tag and stress the claims.**

- **VALIDATED (sector-wide, by 2025):** demand for usage- and outcome-based AI products exists; enterprises will run paid pilots.
- **Load-bearing ASSUMED claim 1 — gross margin at scale.** That realized cost-to-serve (inference) stays comfortably below price as usage grows and as power users cluster. This is the claim most likely to kill the business, and it is *testable now*: instrument per-customer cost-to-serve and compute true gross margin per cohort, not blended.
- **Load-bearing ASSUMED claim 2 — the foundation-model partner is a partner, not a competitor.** Inversion (which block's failure kills the model?) points straight here: the same provider can raise API prices, deprecate the model version the product is tuned against, or ship a first-party product into the same use case. This is the AI-native version of "platform risk."

**Next-week experiments.**
- To test margin: pull last 30 days of usage logs, compute inference cost per paying account, rank by margin, and identify the unprofitable tail — before raising, not after.
- To test partner risk: price a full migration to a second model provider (eval + re-tuning + regression), and read the provider's published deprecation and pricing-change policies to bound the exposure.

**Comparison to the incumbent (classic B2B SaaS).** Block-by-block, the AI-native canvas is *not* a strictly better SaaS canvas — it trades SaaS's near-zero marginal cost for a real variable inference cost (blocks 5 + 9 coupled), and it trades "we own the core IP" for "our core capability is rented from a partner who may compete" (blocks 6 + 8). An AI-native model with the *same* value prop as an incumbent but this cost structure is a *worse-positioned* version unless a distinctive Key Resource (data loop, workflow lock-in) or a genuinely cheaper cost-to-serve makes it defensible.

The mapped steps:
1. Customer Segments: a named B2B wedge, with buyer ≠ user flagged
2. Value Propositions: displaced labor cost / latency / throughput in customer units — not model features
3. Channels: five phases, with trials spending real inference on unpaid users and after-sales usage monitoring
4. Customer Relationships: product-led → enterprise success; outcome pricing as both alignment asset and dispute liability
5. Revenue Streams: seat vs. usage vs. outcome — margin is variable, WTP tested against realized cost-to-serve
6. Key Resources: data loop, integrations/switching cost, brand, compute access — the base model is *not* distinctive
7. Key Activities: orchestration, evaluation, reliability, inference cost engineering — not model training
8. Key Partners: foundation-model provider named, with dual role (supplier + potential competitor) and real replacement cost
9. Cost Structure: large variable inference component coupled to blocks 5 and 8
10. Audit: load-bearing ASSUMED claims (gross margin at scale; partner-not-competitor) tested by per-cohort cost-to-serve and a costed second-provider migration

*Sources: Osterwalder, Alexander & Pigneur, Yves (2010). *Business Model Generation*. Wiley — the canvas framework. Sector structure (usage/outcome-based pricing, inference as dominant variable cost, foundation-model provider as key partner and platform risk) is widely and durably documented across 2024–2025 industry and investor commentary, e.g. Andreessen Horowitz, "Navigating the High Cost of AI Compute" (a16z.com, 2023) and a16z's ongoing writing on AI-native margins and app-layer economics; and OpenAI's and Anthropic's published API pricing and model-deprecation policies (platform.openai.com; docs.anthropic.com). Figures in this example are illustrative placeholders (X%, $Y), not reported values.*
