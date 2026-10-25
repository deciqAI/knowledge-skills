---
name: aeo-answer-engine-optimization
description: "Activate when: user says 'win the featured snippet', 'get the voice assistant to read our answer', 'AEO', 'answer engine optimization', 'structure our FAQ', asks 'how do we get our answer shown directly?', or needs to restructure content so a single passage can be lifted as the one direct answer to a question.
  Do NOT activate when: the goal is overall brand share in AI recommendations (use geo-generative-engine-optimization); the work is purely technical site SEO; the question has no definite answer (opinion or highly case-specific). More: deciqai.com/s/aeo-answer-engine-optimization"
---

# Answer Engine Optimization (AEO)

## Overview

Answer engines — featured snippets, "People Also Ask" boxes, voice assistants, AI answer panels — lift **one passage** and present it as the answer. The page whose passage answers the question first, shortest and most accurately is the one that gets lifted. A correct answer buried in paragraph six of a long article loses to a mediocre answer sitting directly under the question.

Core mechanism: **map real questions → put an answer-first passage directly under each question → add a definition block and structured data that match the visible page**, so a machine can extract the answer without reading the whole page. Keep three goals distinct: SEO gets a page into the results list; AEO gets one passage selected as the direct answer; generative-engine optimization gets the brand mentioned and cited by generative AI. They share inputs but are measured differently.

Without the method, teams write long "authoritative" pages, bolt on schema markup and wait — then find a competitor's one-sentence definition being read aloud instead. Google's own documentation is explicit that a page cannot mark itself as a featured snippet; its systems decide which passage is useful ([sources](references/sources.md)).

Compose with [geo-generative-engine-optimization](../geo-generative-engine-optimization/SKILL.md) (the brand-citation layer) · [jobs-to-be-done](../jobs-to-be-done/SKILL.md) (questions come from real jobs customers are trying to get done) · [landing-page-conversion](../landing-page-conversion/SKILL.md) (what happens after the click) · [content-led-growth](../content-led-growth/SKILL.md) (the content program the answers live in).

## When to Use

- The target question has a definite answer (definition, steps, number, comparison) but your page's answer is buried mid-article
- Customers repeatedly ask the same question (support tickets, sales calls) and the website has no direct answer to it
- A voice assistant or AI answer box is quoting a competitor's definition of a term you own
- Rewriting a FAQ, glossary or help center so individual entries can be lifted out of context

**When NOT to use:** opinion-type or strongly case-specific questions · the underlying content is not yet accurate · trying to use schema to describe content that is not on the page.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has specific pages and a question list → run The Process directly.
- **Coach mode:** user is unfamiliar → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What it is.** "Answer engines lift one passage. Put the answer in the first sentence under the question."
2. **Check fit.** "Does your target question have a clear, verifiable answer?" Opinion question → wrong tool.
3. **Elicit the real case.** "List the 5 questions customers ask most, and the page that currently answers each."
> **[WAIT — do not advance until user responds]**
4. **Run The Process.** Pick one question; rewrite it as "question heading + answer-first passage of roughly 40–60 words + expansion", and show before/after.
> **[WAIT — do not advance until user responds]**
5. **Name the insight.** "Selection comes from structure and accuracy, not length."

## The Process

**Output:** Question map + rewritten pages + selection tracking log

1. **Map the questions.** Collect from support tickets, sales-call notes, search queries and "People Also Ask" boxes. Classify by intent: what-is / how-to / how-much / which-is-better. *Gate: every question has a real source → otherwise delete it.*
2. **One question, one anchor.** Use the user's own wording as the H2/H3 heading. One primary question per page, or one tight FAQ group. *Gate: heading matches how users actually phrase it → otherwise rewrite.*
3. **Answer first.** The first paragraph under the heading answers directly (conclusion first, conditions after; roughly 40–60 words is a common working length, not a published rule). Steps as a numbered list, comparisons as a table, numbers with units and an as-of date. *Gate: reading only the first paragraph yields the answer → otherwise rewrite.*
4. **Definition block.** On term pages, give a one-sentence "X is …" definition plus its scope. *Gate: the definition contains no marketing adjectives → otherwise strip them.*
5. **Structured data.** Add schema types (Article, QAPage, Speakable where relevant) only for what the page visibly says. Do not promise rich results: Google stopped showing HowTo rich results in 2023, restricted FAQ rich results to authoritative government and health sites in August 2023, and announced FAQ rich results would stop appearing from May 2026. Schema still helps machines understand the page; it does not guarantee display. Check the current status of any rich-result type against Google's live documentation before relying on it. *Gate: schema content matches visible page content → otherwise remove it.*
6. **Track.** Log whether the target question's featured snippet / AI answer cites you and which passage; re-check in 4–8 weeks.
7. **Stop-rule:** the answer is accurate and well-structured and still not selected → the bottleneck is authority and third-party corroboration, not structure. Stop editing the passage and work on authority (see [geo-generative-engine-optimization](../geo-generative-engine-optimization/SKILL.md)).

**Output template:**
`Question | Source | Intent | Target page/anchor | Answer-first passage (≤60 words) | Schema type | Currently selected source | Re-check date | Result`

*→ Method in Action: [Google's featured-snippet failures and the FAQ/HowTo rich-result rollback (2017–2026)](examples/google-featured-snippets-and-faq-rollback-2017-2026.md)*

## Applying It Well

1. **One passage answers one question.** Conditions and exceptions go in the second paragraph.
2. **The answer must stand alone.** The machine will lift it out of context; it must be true and complete without the paragraph before it.
3. **Match the asker's phrasing, not your taxonomy.** Engines match questions to passages; a passage that answers a near-neighbor question gets a near-neighbor slot or none.
4. **Date your numbers and refresh them.** Stale answers get replaced.
5. **Structure cannot rescue weak authority.** Engines weigh source authoritativeness, especially on sensitive or fringe queries.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Adding FAQ schema is enough" | Schema does not guarantee display, and Google has withdrawn FAQ and HowTo rich results. The answer structure on the page is the foundation. |
| [D] "Long-form is more authoritative" | An answer buried mid-article is not lifted. Answer first, then expand. |
| [D] "AEO is the same as GEO" | AEO competes for one answer passage; GEO competes for brand mentions and citations. Different metrics, different work. |
| [D] "We'll write the questions ourselves" | Self-invented questions drift from how users ask; they fail to match. |
| [D] "We were picked once, so we're done" | Selection is re-decided continuously; competitors and dated numbers displace you. Keep the re-check date. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Headings are slogans, not questions · first paragraph is preamble, not the answer · schema describes content not on the page · no tracking log · rich-result claims copied from an old blog post

## Verification

- [ ] Every question has a real source (ticket, call, query, PAA)
- [ ] Every anchor's first paragraph answers its question on its own
- [ ] Schema matches visible content; rich-result status checked against Google's current docs
- [ ] AEO / GEO / SEO goals and metrics stated separately
- [ ] Re-check date scheduled in the tracking log

---

*Part of **deciqAI Knowledge Skills** — 253 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/aeo-answer-engine-optimization** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/aeo-answer-engine-optimization.json*
