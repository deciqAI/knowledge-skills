# Method in Action: GEO-bench — the Visibility Experiments That Named the Field (2023–2024)

> *Example for the [geo-generative-engine-optimization](../SKILL.md) skill.*

In November 2023 a team from Princeton University and IIT Delhi (Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan, Deshpande) posted "GEO: Generative Engine Optimization" to arXiv; it was published at KDD 2024. It is the first public, controlled test of the question this skill answers: *what makes a source more likely to be used and cited in a generative engine's answer?* It is a research experiment, not a brand campaign, so it exercises some steps of the Process rigorously and does not test others. Both are worth seeing.

Source: Aggarwal et al., arXiv:2311.09735, https://arxiv.org/abs/2311.09735 (full text: https://arxiv.org/html/2311.09735). All figures below are from the paper.

## Running the steps

**1. Build the prompt panel.** The authors built **GEO-bench: 10,000 queries** from nine sources, split 8K / 1K / 1K for train, validation, and test. They kept a realistic intent mix — **80% informational, 10% transactional, 10% navigational** — and augmented each query with the text of the top 5 Google results as the candidate sources. *Gate check:* the panel was drawn largely from existing query datasets rather than invented slogans, which is the point of the gate — measure against how people actually ask.

**2. Measure the baseline.** They defined two visibility metrics: **Position-Adjusted Word Count** (how much of the answer is attributed to a source, discounted by position) and **Subjective Impression** (seven sub-dimensions, including relevance, influence, uniqueness, and click likelihood, judged by a model). Because generation is stochastic, they **sampled 5 responses at temperature 0.7** and ran experiments on **five random seeds**, reporting averages. *Gate check:* this is the "≥3 runs per prompt" rule done properly. A single answer would have told them nothing.

**3. Fix the entity.** *Not tested.* The paper modifies page text only; it does not vary brand naming, structured data, or cross-site consistency. That step of the Process rests on the engines' own documentation (Google's structured-data and AI-features guidance; Schema.org `sameAs`), not on this experiment.

**4. Create citable facts.** This is where the experiment is decisive. Of nine rewriting methods, the three that add verifiable material won on Position-Adjusted Word Count, against an unoptimized baseline of **19.5**:

| Method | Score |
|---|---|
| Quotation Addition | 27.8 |
| Statistics Addition | 25.9 |
| Cite Sources | 24.9 |
| No optimization (baseline) | 19.5 |
| **Keyword Stuffing** | **17.8** |

The headline: "GEO can boost visibility by up to 40%." And the classic SEO move — stuffing query keywords into the page — scored *below* doing nothing. That is the "just publish more keyword content" rationalization, refuted with a control group.

**5. Earn third-party corroboration.** Partially tested. "Cite Sources" and "Quotation Addition" add citations and quotations *from credible sources* to the page. The study cannot measure off-site reputation, but it does show that tying claims to external authority is what the engine rewards. The equity result is the one to remember: Cite Sources raised visibility **115.1% for sites ranked fifth** in search results, while the **top-ranked site lost 30.3%** on average. Retrieval rank alone does not decide who is cited, which is why a lower-ranked brand with better-sourced facts can win the answer.

**6. Cover the buyer prompts.** The authors found method effectiveness varied by domain and query type (e.g. Cite Sources helps most on factual questions; an authoritative style helps on debate-style ones). The practical reading: write the answer page for the *kind* of prompt the buyer asks, not one template for all.

**7. Re-test.** The authors re-ran the methods on a deployed engine, **Perplexity.ai**, on a 200-query subset, and report "visibility improvements up to 37%." The result held outside the lab setup, though more weakly — the reason the Process re-tests on live assistants rather than trusting one environment.

## What the case shows, and what it doesn't

- **Shows:** measuring visibility needs a fixed panel and repeated sampling; facts, quotations, and citations raise citation share; keyword stuffing does not; lower-ranked sources can gain the most.
- **Does not show:** anything about entity consistency, review-site presence, or crawler access. The core experiments used GPT-3.5-turbo as the generator, and engines have changed since. Treat the numbers as evidence of *direction*, not as a forecast for your brand — the reason step 7 exists.

## The mapped steps

1. **Panel:** 10K queries, realistic intent mix, drawn mostly from existing query sources.
2. **Baseline:** two visibility metrics; 5 samples × 5 seeds.
3. **Entity:** not tested — rely on engine documentation.
4. **Facts:** quotations 27.8 / statistics 25.9 / citations 24.9 vs baseline 19.5; keyword stuffing 17.8.
5. **Corroboration:** citing credible sources helped most for lower-ranked sites (+115.1% at rank 5).
6. **Coverage:** effectiveness varies by domain and query type.
7. **Re-test:** confirmed on Perplexity.ai, up to 37%.
