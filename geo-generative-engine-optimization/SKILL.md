---
name: geo-generative-engine-optimization
description: "Activate when: user says 'get ChatGPT / Perplexity to recommend us', 'AI answers never mention our brand', 'GEO', 'generative engine optimization', 'AI search visibility', asks 'how do AI assistants describe our product?', or wants to raise how often a brand is mentioned and cited in generative-AI answers.
  Do NOT activate when: the goal is only classic keyword ranking (plain SEO); the goal is only winning a single featured snippet or voice answer (answer-engine optimization); the product has no verifiable public facts to state yet. More: deciqai.com/s/geo-generative-engine-optimization"
---

# Generative Engine Optimization (GEO)

## Overview

Buyers increasingly ask an AI assistant "what should I use for X?" instead of scanning ten blue links. The assistant can only recommend brands it can **recognize, verify, and cite**. A brand that is ambiguous, unsourced, or absent from the third-party pages the engine retrieves is either left out of the candidate set or described wrongly — stale prices, the wrong category, a competitor named in its place.

Core mechanism: **a clear entity + citable facts + independent corroboration → the engine is more likely to mention and cite you when it retrieves and generates.** The term and the first visibility metrics come from Aggarwal et al. (KDD 2024), who found that adding citations, quotations, and statistics to source content raised visibility in generative answers by up to 40%, while classic keyword stuffing did not help.

Compose with [social-proof](../social-proof/SKILL.md) (third-party corroboration is the heaviest signal) · [positioning-obviously-awesome](../positioning-obviously-awesome/SKILL.md) (you cannot make an engine state a positioning you have not defined) · [content-led-growth](../content-led-growth/SKILL.md) (the pages that answer buyer prompts).

## When to Use

- You run 5–10 buyer-style prompts through AI assistants and your brand is missing or misdescribed
- A new product or category is launching and the engines need to learn who you are, who it is for, and how it differs
- Competitors are recommended repeatedly while you are absent from the review sites and directories the engines cite

**When NOT to use:** only local or keyword ranking matters · there is no public, verifiable information about the product · a regulated claim has not yet cleared compliance review — clear it before publishing.

## Coaching Novices (Adaptive Front Door)

**Engine mode:** user names a brand and a target buyer → run The Process directly.
**Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What-it-is:** "AI assistants only recommend brands they can recognize and back up with a source they trust."
2. **Check fit:** "Do your buyers ask an AI assistant before they buy? If not, work another channel first."
3. **Elicit the real case:** "What is your brand, your category, your target buyer — and three questions, in the buyer's own words, they would type into an AI assistant?"
> **[WAIT — do not advance until user responds]**
4. **Run The Process:** "Here is a baseline on those prompts: mention rate, citation of your pages, and accuracy of the description."
> **[WAIT — do not advance until user responds]**
5. **Name the insight:** "Your gap is in entity, facts, corroboration, or content coverage — and this is the one to fix first."

## The Process

**Output:** GEO baseline + fix list + re-test share

1. **Build the prompt panel.** 20–50 prompts in buyer language (category recommendations, comparisons, alternatives, problem-solving), run across 3–4 assistants. *Gate: prompts come from real customer language (interviews, tickets, search terms), not self-written slogans → otherwise stop.*
2. **Measure the baseline.** For each prompt record: mentioned or not, position, whether your own page is cited, whether the description is accurate, and which third-party sources are cited. Answers are stochastic, so report proportions across runs. *Gate: ≥3 runs per prompt → otherwise draw no conclusion.*
3. **Fix the entity.** One brand name, one category, one positioning line — identical on the website, LinkedIn, directories, Wikidata. Add Organization/Product structured data with `sameAs` links to those profiles. Treat this as identity hygiene, not an AI switch: Google states no special markup is required for its AI features. *Gate: name and category match everywhere → otherwise fix first.*
4. **Create citable facts.** Each core page carries extractable fact blocks: specs, price range, who it is for, comparison table, method and data sources. *Gate: every fact is externally verifiable and there is no unsupported "first" or "best" → otherwise delete it.*
5. **Earn third-party corroboration.** Inventory the sources the engines actually cite (review sites, directories, communities, press) and pursue genuine listings and reviews. No paid fake reviews, no astroturfed posts. *Gate: corroboration comes from an independent third party → otherwise it does not count.*
6. **Cover the buyer prompts.** For each panel prompt where you are absent, publish a direct-answer page (comparison, alternatives, use case, pricing). Confirm `robots.txt` is not blocking the AI search crawlers you want to be retrieved by (e.g. OpenAI's OAI-SearchBot controls inclusion in ChatGPT search answers).
7. **Re-test and iterate.** After 4–8 weeks re-run the same panel and compare share.
8. **Stop-rule:** share has not moved and steps 3–5 are complete → return to step 1 and check whether the prompts really represent your buyers.

**Output template:**
`prompt | assistant | mention rate | position | cites us? | description accurate? | third-party sources cited | gap (entity/facts/corroboration/content) | fix | owner | re-test date`

*→ Method in Action: [GEO-bench — the Princeton / IIT Delhi visibility experiments (2023–2024)](examples/geo-bench-visibility-experiments-2023.md)*

## GEO Packs

Domain patterns (typical buyer prompt / facts that get cited / corroboration that counts / dominant failure):
- **B2B SaaS:** "best X for Y-size team" / pricing tiers, integrations, comparison tables / review platforms and analyst lists / stale pricing in AI answers.
- **Consumer e-commerce:** "best X under $N" / specs, price, availability / independent reviews and retailer listings / a competitor named as the default.
- **Local and professional services:** "who should I hire for X near Y" / service area, credentials, hours / directories and community threads / inconsistent name or address across listings.
- **Regulated categories (health, finance):** "is X safe / right for me" / approved claims only / authoritative third parties / unapproved claims repeated by the engine.

## Applying It Well

1. **Share is a proportion, not a screenshot.** Run the same prompt several times and compare assistants before claiming anything.
2. **Fix "described wrong" before chasing "mentioned more."** A wrong description does more damage than absence.
3. **Third-party corroboration carries the most weight.** Your own pages supply the verifiable raw facts; independent sources make them believable.
4. **Facts beat keywords.** In the GEO-bench experiments, statistics, quotations, and citations raised visibility; keyword stuffing scored below the unoptimized baseline.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Our SEO is strong, so GEO takes care of itself" | Ranking high is not the same as being cited; engines weigh entity consistency and third-party corroboration. |
| [D] "I asked ChatGPT once and we showed up" | A single answer is a random draw. You need a panel and proportions across runs. |
| [D] "Just publish lots of AI-generated articles" | Bulk content with no new facts is rarely cited and dilutes credibility. |
| [D] "Say we're the industry leader" | Unverifiable claims are not reliably cited and carry compliance risk. |
| [D] "Block every AI crawler to protect our content" | Blocking a search crawler can remove you from that assistant's answers. Decide crawler by crawler. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- No fixed prompt panel; progress reported by screenshot · brand name or category differs across channels · all corroboration is self-published or paid placement · changes shipped with no re-test

## Verification

- [ ] Prompt panel built from real buyer language, ≥3 runs per prompt
- [ ] Baseline table has mention, citation, and accuracy columns
- [ ] Entity data consistent across platforms; structured data live
- [ ] Every published fact externally verifiable
- [ ] Re-test date scheduled

---

*Part of **deciqAI Knowledge Skills** — 253 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/geo-generative-engine-optimization** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/geo-generative-engine-optimization.json*
