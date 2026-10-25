# Sources — geo-generative-engine-optimization

> *Primary sources for the [geo-generative-engine-optimization](../SKILL.md) skill.*

- **Aggarwal, P., Murahari, V., Rajpurohit, T., Kalyan, A., Narasimhan, K., & Deshpande, A.** "GEO: Generative Engine Optimization." arXiv:2311.09735 (2023); *Proceedings of KDD 2024*. **Origin of the term "GEO" and of the visibility metrics** (Position-Adjusted Word Count, Subjective Impression); GEO-bench (10K queries); "up to 40%" visibility gains from citations, quotations, and statistics; keyword stuffing below baseline; 5 samples at temperature 0.7 over five seeds; +115.1% for rank-5 sites with Cite Sources; Perplexity.ai validation (up to 37%). https://arxiv.org/abs/2311.09735 · full text https://arxiv.org/html/2311.09735
- **Google Search Central.** "AI features and your website." **Primary source that Google requires no special markup or files for AI Overviews / AI Mode** ("There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary"); standard crawlability and content-quality guidance applies. https://developers.google.com/search/docs/appearance/ai-features
- **Google Search Central.** "Introduction to structured data markup in Google Search." **Structured data gives Google "explicit clues about the meaning of a page"** — the basis for step 3's entity hygiene. https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- **Schema.org.** `Organization` type and inherited `sameAs` property ("URL of a reference Web page that unambiguously indicates the item's identity", e.g. Wikipedia, Wikidata, official website). https://schema.org/Organization
- **OpenAI.** "Overview of OpenAI Crawlers." **Primary source for crawler-level control**: sites opted out of OAI-SearchBot "will not be shown in ChatGPT search answers"; GPTBot governs training use separately. https://developers.openai.com/api/docs/bots
- **Wikidata.** Public, linked entity knowledge base referenced in step 3. https://www.wikidata.org/

## What is NOT cited and why

- The prompt-panel design (20–50 buyer prompts, 3–4 assistants, ≥3 runs), the four-way gap taxonomy (entity / facts / corroboration / content), and the 4–8-week re-test interval are **deciqAI practice synthesis**, not a published standard. The ≥3-runs gate is motivated by the stochastic sampling the GEO paper itself controls for.
- No AI-assistant market-share or referral-traffic statistics are cited; such figures move quickly and are mostly vendor-reported.
