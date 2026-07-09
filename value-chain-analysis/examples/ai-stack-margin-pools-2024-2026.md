# Method in Action: The AI Value Chain — Where the Margin Pools Sit (2024–2026)

> *Example for the [value-chain-analysis](../SKILL.md) skill.*

The 2024–2025 generative-AI buildout is a rare case where a whole industry's value chain reorganized in real time, with unusually public data (chip vendor filings, hyperscaler capex disclosures, model pricing pages). Applying the framework treats "the AI stack" as one end-to-end chain — silicon → cloud/compute → foundation models → applications — and asks the framework's central question: which activities capture durable margin, and which see their value competed away?

**Step 1 — Map all activities.** The AI stack's primary activities, layer by layer:
- *Inbound Logistics / Procurement (silicon inputs):* advanced-node wafer capacity, almost entirely from TSMC; high-bandwidth memory (HBM) from SK Hynix, Samsung, Micron; advanced packaging (TSMC CoWoS).
- *Operations (chip design + fab):* Nvidia designs GPUs (H100/H200, and the Blackwell generation announced in 2024); TSMC manufactures them. AMD and custom accelerators (Google TPU, Amazon Trainium/Inferentia) are the alternatives.
- *Operations (compute/cloud):* hyperscalers — Microsoft Azure, Amazon AWS, Google Cloud — plus neoclouds (e.g., CoreWeave) build data centers around these chips and rent compute.
- *Operations (foundation models):* labs (OpenAI, Anthropic, Google DeepMind, Meta, and open-weight releases) train frontier models on that compute.
- *Outbound Logistics / Marketing & Sales (applications):* the app layer — Copilot-style assistants, coding tools, and thousands of AI-native startups — packages models for end users via APIs and SaaS.
- *Support:* Technology Development (CUDA and the software ecosystem, model research); Procurement (multi-year power and GPU supply agreements); HR (scarce ML and GPU-systems talent).

Stop rule: "compute" is deliberately split into chip design, fabrication, and cloud operation — they sit at different firms with different economics, so lumping them hides where margin actually accrues.

**Step 2 — Allocate cost / locate the margin.** The framework's cost lens here is really a *margin* lens — follow the dollars:
- *Silicon design (Nvidia):* the standout margin pool. Nvidia's reported gross margins ran in roughly the mid-70s percent range through fiscal 2024–2025, and its data-center revenue grew several-fold year over year as the buildout accelerated (Nvidia 10-K/10-Q filings). This is where an outsized share of the chain's profit pooled.
- *Fabrication (TSMC):* healthy gross margin (reported in the low-to-mid 50s percent range), but far below Nvidia's — TSMC is capital-intensive and shares the value with its design customers.
- *Cloud/compute (hyperscalers):* enormous capital expenditure. Combined 2024–2025 capex guidance across the major hyperscalers ran into the hundreds of billions of dollars annually (company earnings disclosures). Much of that spend flows *through* to Nvidia and TSMC, so a large share of the cloud layer's revenue is a cost pass-through to silicon.
- *Foundation models (labs):* very high training and inference cost; frontier training runs are widely reported to cost from tens of millions into the hundreds of millions of dollars, and inference is an ongoing variable cost.
- *Applications:* low direct compute cost per firm, but that cost is a pass-through to the model API.

Top cost/margin consumers: silicon (Nvidia captures margin) and compute capex (hyperscalers spend it). Value-leakage risk sits at the model and app layers, addressed below.

**Step 3 — Identify differentiation sources (with evidence).** Where does willingness-to-pay actually hold up?
- *CUDA software ecosystem (Nvidia):* the most evidenced durable source. Customers pay a premium for Nvidia hardware substantially because of the mature CUDA/software stack and switching costs, not raw silicon alone — competitors sell capable chips yet Nvidia retained dominant data-center share through 2024–2025. Evidence: sustained price realization and share despite AMD/custom-silicon alternatives.
- *Leading-edge process + packaging (TSMC):* the advanced-node and CoWoS packaging that top accelerators require is concentrated at TSMC; capacity itself was a reported bottleneck through this period. Evidence: customers queue for capacity and pay premium node pricing.
- *Frontier model quality + distribution (labs):* differentiation exists but is contested — capability leads have been narrow and short-lived as competing frontier and open-weight models arrived. Evidence: rapid, repeated leapfrogging on public benchmarks and fast API price cuts.

**Step 4 — Compare to key competitor(s) at each layer.**
- *Silicon:* Nvidia vs. AMD and custom accelerators (Google TPU, Amazon Trainium). Rivals price lower and hyperscalers build in-house to escape Nvidia margin — but Nvidia's software lock-in kept it structurally ahead through 2025. Nvidia: higher price, higher margin; rivals: lower cost-to-buyer, weaker ecosystem.
- *Fab:* TSMC vs. Samsung Foundry and Intel Foundry — TSMC held a leading-edge yield/capacity advantage for the accelerators that matter.
- *Cloud:* Azure/AWS/Google Cloud compete on GPU availability and price; neoclouds undercut on raw GPU rental. Compute is trending toward commoditization — comparable cost, thin differentiation beyond availability and integration.
- *Models:* frontier labs vs. each other and vs. open-weight models. This is the most competed layer — differentiation erodes fastest.

**Step 5 — Map linkages.** The most powerful dynamics are linkages, not single activities:
- *CUDA (Technology Development) × GPU sales (Operations):* the classic value-chain linkage — investment in the software ecosystem lets the hardware command premium price and raises switching costs. This linkage, not the transistor, is Nvidia's moat.
- *Capex (cloud Operations) × silicon Procurement:* hyperscaler AI capex is largely a *pass-through* to Nvidia/TSMC. So the layer spending the most does not capture the most — a textbook illustration that the activity with the highest spend is often not where margin sits.
- *Model quality (labs) × app distribution:* app-layer differentiation depends on an input (the model) it does not control and that keeps getting cheaper and more capable — value flows to whichever layer holds the scarce, non-substitutable position.

**Step 6 — Activity-level strategy.** Reading the chain through the framework's disposition table:

| Layer | Disposition | Why |
|---|---|---|
| Silicon design + software ecosystem (Nvidia/CUDA) | Invest, internalize, protect | High-value, differentiation source, hard to replicate — the durable margin pool |
| Leading-edge fab + packaging (TSMC) | Strategic bottleneck — fix or secure | Scarce capacity gates the whole chain; capital-intensive |
| Cloud/compute | Accept as linked cost; differentiate on integration | Trending to commodity; much revenue is silicon pass-through |
| Foundation models | Contested — protect via distribution, data, and cost, not capability alone | Capability leads are narrow and short-lived |
| Applications | Differentiate on workflow, proprietary data, distribution | Compute is a pass-through input the layer cannot control |

**Payoff.** The framework predicts the pattern observed through 2024–2025: the largest *spend* (hyperscaler capex) and the loudest *narrative* (foundation models) were **not** where durable margin sat. Margin pooled at the scarce, hard-to-replicate, switching-cost-protected positions — Nvidia's chip-plus-CUDA linkage and TSMC's leading-edge capacity — while compute commoditized and model capability was competed away at speed. Where value gets competed away is exactly where no activity holds a scarce, non-substitutable position.

*Sources: Nvidia Corp. SEC filings (Form 10-K FY2024 and FY2025, and quarterly 10-Q reports), https://investor.nvidia.com; TSMC investor relations and financial reports, https://investor.tsmc.com; Microsoft, Amazon, and Alphabet quarterly earnings disclosures on 2024–2025 capital expenditure (company investor-relations sites and SEC filings); Porter, M.E. (1985), Competitive Advantage, Chapter 2. Specific figures are stated in reported/approximate ranges; exact quarterly values should be confirmed against the primary filings.*
