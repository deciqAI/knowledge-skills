---
name: ai-content-factory-brand-consistency
description: "Activate when: user says 'use AI to mass-produce content', 'how do we make AI write like our brand?', 'the AI content got facts wrong', 'how do we keep AI content out of legal trouble?', 'build a content factory', or plans 10+ AI-assisted pieces per week (blog, social, email, product pages) across several writers or agents.
  Do NOT activate when: writing a single one-off piece of copy; brand positioning and target customer are not yet decided (position first); the question is how content drives growth at all (use content-led-growth). More: deciqai.com/s/ai-content-factory-brand-consistency"
---

# AI Content Factory and Brand Consistency


## Overview

AI drives the marginal cost of a draft toward zero, so the bottleneck moves to **consistency, accuracy and compliance**. Volume without gates is brand dilution, factual error and legal exposure, multiplied by output.

The core mechanism: **specify the inputs (a voice spec and a fact base) → generate → pass every piece through risk-tiered gates → feed quality measurements back into the spec.** Humans stop writing first drafts and start guarding gates.

Compose with [content-led-growth](../content-led-growth/SKILL.md) (why content compounds) · [trust-brand-architecture](../trust-brand-architecture/SKILL.md) (what a factual error costs in trust) · [checklist](../checklist/SKILL.md) (the shape of each gate) · [goodharts-law](../goodharts-law/SKILL.md) (don't chase piece count) · [ai-output-verification-trust-tiers](../ai-output-verification-trust-tiers/SKILL.md) (tiering any AI output by error cost).

## When to Use

- Output must rise from a few pieces a month to dozens a week
- Several people or agents write, and tone and claims have started to drift
- Content carries accountable claims: prices, efficacy, comparisons, customer reviews, regulated topics

**When NOT to use:** a single low-risk piece · positioning not yet decided · a strictly regulated industry with a mandatory compliance workflow (this process supplements it, never replaces it).

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete brand and content plan → run The Process directly.
- **Coach mode:** user is unfamiliar → guide one step at a time.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. **What it is:** "First write down how the brand talks and which facts it may state. Then let AI produce at volume, with humans guarding the gates."
2. **Check fit:** "How many pieces a week are you planning? Do any include prices, efficacy, comparisons or reviews?"
3. **Elicit the real case:** "Send 3 pieces that sound most like your brand, and 1 that sounds least like it."
> **[WAIT — do not advance until user responds]**
4. **Run The Process:** "From your samples, here is a draft voice spec — 3 attributes, banned words, good/bad pairs. Correct it."
> **[WAIT — do not advance until user responds]**
5. **Name the insight:** "Consistency comes from a spec and gates, not from a better prompt."

## The Process

**Output:** Content Factory Runbook (voice spec + fact base + gates + cadence + metrics)

1. **Voice spec.** 3–5 tone attributes written as is / is-not pairs, banned words, sentence length, person, and 3 good/bad example pairs. *Gate: two reviewers score the same draft differently → the spec is too vague; rewrite it → stop.*
2. **Fact base (single source of truth).** Product specs, prices, case data, customer-approved quotes — each entry with source, expiry date and owner. *Gate: any number or quote in a draft that is not in the fact base → reject the draft.*
3. **Risk tiers.** Low (opinion, tutorials) · Medium (product descriptions) · High (prices, efficacy, comparisons, reviews and testimonials, legal / health / financial topics). *Gate: no high-risk piece publishes without a line-by-line human check against the fact base.*
4. **Generate → review gates.** AI drafts → automated checks (banned words, fact-base match, links, required AI disclosure) → human spot-check (low) or full review (medium and high). *Gate: any claim that cannot be traced to a source → delete it or rewrite it as a provable statement.*
5. **Style QA.** Sample weekly and score voice fit 1–5; write low-scoring samples back into the spec as bad examples.
6. **Cadence and metrics.** Fix the publishing frequency; track quality (dwell, replies, conversion, corrections issued), not just count. *Gate: correction rate rising for consecutive periods → cut volume and fix the spec first.*
7. **Stop-rule:** no one will own the fact base → halt volume production and publish only low-risk opinion content until someone does.

**Output template:**
`voice spec v_ | fact-base entries / expired | risk-tier rules | gates (auto / human) | cadence | quality metrics | corrections this week | spec revision log`

*→ Method in Action: [CNET's AI-written finance explainers (2022–2023)](examples/cnet-ai-finance-explainers-2023.md)*

## Applying It Well

1. **Specify with examples, not adjectives.** "Professional but friendly" cannot be executed; a good/bad pair can.
2. **The fact base is an asset with a shelf life.** An expired figure is more dangerous than a missing one — set expiry reminders.
3. **"A human edited it" is not a gate.** Review without a source check is reading, not verifying.
4. **Disclose visibly.** Where content was AI-assisted, say so where readers will see it, per the rules that apply where you publish.
5. **Never fabricate reviews, testimonials or case studies.** Treat endorsements and AI disclosure under the rules of the jurisdiction you publish in.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "A good prompt is enough" | A prompt does not replace a fact base and gates; the model still fabricates. |
| [D] "Volume will find the hits" | Low-quality volume dilutes the brand and search trust. |
| [D] "Review is too slow" | Tier by risk. Low-risk pieces get spot-checks; only high-risk pieces are slow. |
| [D] "An editor already looked at every piece" | Looking is not checking. Without a fact-base match, errors pass a human reader. |
| [D] "Errors written by AI aren't ours" | The publisher is responsible for what it publishes. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Publishing numbers with no fact base · counting only pieces published · a voice spec made of adjectives
- Reviews or case studies of unknown origin · no named owner per piece · AI disclosure hidden behind a hover

## Verification

- [ ] Voice spec has good/bad examples, and two reviewers score the same draft the same way
- [ ] Every number and quote traces to a fact-base entry with source and expiry
- [ ] High-risk pieces carry a record of the line-by-line check
- [ ] Metrics include quality and corrections, not only volume

---

*Part of **deciqAI Knowledge Skills** — 253 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/ai-content-factory-brand-consistency** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/ai-content-factory-brand-consistency.json*
