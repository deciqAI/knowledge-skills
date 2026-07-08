# Method in Action: AI and Venture Returns Concentration (2023–2026)

> *Example for the [power-law-distribution](../SKILL.md) skill.*

Between 2023 and early 2026, the economic value created by the generative-AI wave concentrated into an extraordinarily thin tail: a handful of frontier model labs (most prominently OpenAI and Anthropic) plus the dominant AI-compute supplier, Nvidia, captured a wildly disproportionate share of the value, funding, and market-cap gains. This is a textbook power-law distribution unfolding in real time — and it is exactly the kind of domain where averaging ("the average AI startup," "the average enterprise-software return") produces systematically wrong decisions. Below the case is run through this skill's six-step Process.

## Step 1 — Identify the distribution

**What is distributed?** Value capture across the AI/compute value chain — split into three overlapping layers:

- **Compute / chips:** revenue and margin across GPU and accelerator vendors.
- **Frontier model labs:** funding raised and revenue across foundation-model companies.
- **Public-market gains:** the share of major-index appreciation attributable to a small set of AI-exposed mega-caps.

**Preliminary hypothesis:** power-law, not Gaussian. The prior from venture and technology-platform markets (this skill's [base case](pareto-1896-mandelbrot-1963-and-vc-return-data.md)) is strongly power-law, and winner-take-most dynamics (network effects, economies of scale in compute, data moats) push AI even further into the tail.

## Step 2 — Check power-law indicators

The upper-tail-dominates signature is visible in every layer:

- **Chips:** Nvidia's data-center segment revenue grew several-fold year-over-year through fiscal 2024–2025 on AI demand, and Nvidia became the first company to reach an approximately $3 trillion market capitalization in June 2024 (briefly the world's most valuable public company). No competitor captured a comparable share of AI-accelerator value in the same window. Top-1 share of the accelerator profit pool is extreme.
- **Model labs:** funding clustered violently. Microsoft committed a reported ~$10 billion to OpenAI in January 2023; Amazon committed up to $4 billion to Anthropic (announced September 2023, expanded in 2024), and Google also invested in Anthropic. The largest few labs absorbed the overwhelming majority of foundation-model capital while many smaller "GPT-wrapper" startups raised comparatively little and some folded.
- **Public markets:** the group popularly dubbed the "Magnificent Seven" (Nvidia, Microsoft, Apple, Alphabet, Amazon, Meta, Tesla) accounted for a large majority of the S&P 500's gain in 2023, per widely reported index-attribution analyses.

**Mean-to-median ratio:** very high — the mean AI-company outcome is pulled far above the median by a few enormous winners; the median AI startup's outcome is modest or negative. **Long right tail:** yes. **Log-log linearity:** consistent with the venture-return distribution this sits inside.

## Step 3 — Estimate tail exponent (if data available)

Precise α for the 2023–2026 AI cohort is not yet cleanly estimable (the outcomes are still maturing and the data is private). But the parent distribution — venture returns — is characterized in the empirical literature as roughly α ≈ 2 or lower, i.e. in or near the **infinite-variance** regime, where a single outlier can dominate the entire sample mean. The underlying return data is starkly skewed (see the [Correlation Ventures data](pareto-1896-mandelbrot-1963-and-vc-return-data.md): a small top fraction of financings returned >50×, and roughly 65% returned less than invested capital). AI, if anything, concentrates harder than the base venture case. **Practical implication:** treat the sample mean as unstable and outlier-driven; do not plan off it.

## Step 4 — List Gaussian errors being made

Common mistakes observed during this period:

1. **"The average AI startup will…"** — averaging across a cohort whose mean is defined by two or three companies. The median AI application startup faces thin margins, model-provider dependency, and commoditization.
2. **Diversifying to "average into the AI theme."** Spreading capital evenly across many AI names treats the payoff as symmetric; in a power law, equal-weighting the tail is what captures return, but equal-weighting the *body* mostly buys the losers.
3. **Assuming compute margins normalize smoothly.** Modeling Nvidia's position as a mean-reverting cyclical rather than a tail-dominant platform underweighted both the upside and the fragility (see Step 6).
4. **Pricing the concentration risk as low-probability.** The January 2025 DeepSeek market reaction — a Chinese lab's efficient open model triggering a sharp single-day sell-off in AI-exposed stocks (Nvidia's market cap fell by a historically large one-day dollar amount) — is a tail event of exactly the kind Gaussian volatility models under-price.

## Step 5 — Redesign for power-law structure

- **Maximize shots at the tail, then concentrate.** In AI venture, the correct posture is broad access to genuine frontier bets plus fast concentration of capital and support into the emerging winner — not even spreading across the body of me-too startups.
- **Own the tail-capturing layer, not the commoditizing one.** Value concentrated in scarce compute and frontier models; the application body faced margin compression. Position where the power law pays.
- **Size tail risk with extreme-value thinking, not std-dev.** The dominance of a single supplier (Nvidia) and a few labs is itself a concentration risk: US export-control rounds on advanced AI chips to China (successively tightened from October 2022 onward), supply constraints, and efficiency shocks like DeepSeek are fat-tail events. Model them as scenarios, not as ±1σ moves.
- **Watch the moat's foundations.** Nvidia's CUDA software ecosystem, TSMC's advanced-node manufacturing (including the Arizona fabs ramping under the CHIPS Act), and frontier-lab capital access are the structural reasons the tail stays thin — and the specific things whose erosion would redistribute the distribution.

## Step 6 — Define monitoring triggers

- **Track top-N share, not the average.** Monitor the revenue/margin share of the top-1 accelerator vendor and top-few labs, and the index-gain share of the mega-cap AI group — not "average AI valuation."
- **Distribution-shift signals:** a credible efficiency or open-weights shock (DeepSeek was the first big one) that cuts the compute needed per unit of capability; a viable CUDA alternative gaining real adoption; export-control or supply changes reshaping who can access frontier compute; a frontier lab losing capability leadership. Any of these would flatten the tail.
- **Review cadence:** re-estimate the top-N shares each earnings cycle; treat a sustained decline in top-1 compute share as the trigger to revisit the whole thesis.

## Takeaway

The 2023–2026 AI wave is a live, high-stakes demonstration of the skill's core claim: in a power-law domain, the mean is a mirage. Capital, revenue, and market-cap gains concentrated into a tail of a few companies. Decisions built on "the average AI company" or on Gaussian volatility models (which mispriced the DeepSeek shock) were systematically wrong; decisions built on maximizing tail access, owning the scarce layer, and scenario-sizing concentration risk were right.

*Sources: Nvidia investor relations quarterly results and press releases (fiscal 2024–2025 data-center revenue; ~$3T market cap, June 2024). Microsoft, "Microsoft and OpenAI extend partnership" (Jan 23, 2023). Amazon, "Amazon and Anthropic announce strategic collaboration" (Sep 25, 2023) and 2024 expansion announcement. U.S. Bureau of Industry and Security advanced-computing/semiconductor export-control rules (Oct 7, 2022, and subsequent updates). Reuters and Bloomberg reporting on the Jan 27, 2025 DeepSeek-driven AI-stock sell-off and Nvidia's record single-day market-cap decline. Widely reported S&P 500 2023 index-attribution analyses of the "Magnificent Seven." TSMC Arizona / U.S. CHIPS and Science Act (2022) fab announcements. Correlation Ventures venture-return dataset (2014), as in the base example.*
