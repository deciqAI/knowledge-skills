---
name: build-buy-partner-ai
description: "Activate when: user says 'should we build this AI feature or buy it?', 'should we develop our own agent?', 'which AI vendor should we partner with?', 'build vs buy', 'should we train our own model?', 'the vendor raised prices / changed terms — do we switch?', or is about to sign an annual AI contract, hire an ML team, or commit to a platform for an AI capability.
  Do NOT activate when: trying a free tool that can be dropped any time; a personal productivity tool unrelated to business outcomes; the solution is already chosen and the question is how to run the pilot to a verdict (use ai-pilot-to-scale); the question is general lock-in economics, not an AI sourcing decision (use switching-costs). More: deciqai.com/s/build-buy-partner-ai"
---

# Build / Buy / Partner (AI Capabilities)


## Overview

The core mechanism: **build only the layer that differentiates you *and* depends on data only you hold; buy or partner for everything else — and put maintenance and model-replacement cost on the ledger before comparing.**

Two failure modes recur. Teams build generic capabilities (support chatbots, OCR, transcription) in-house and turn them into a liability. Or they outsource the part that actually differentiates them, and data and customer relationships end up locked inside a vendor. AI sharpens both: foundation models are superseded quickly, so an in-house "lead" can be erased by the next general-purpose model or a vendor's native feature; and ML systems carry hidden maintenance costs far larger than the initial build (Sculley et al., NeurIPS 2015: "it is common to incur massive ongoing maintenance costs in real-world ML systems").

The differentiation test is Prahalad & Hamel's core-competence logic (*HBR*, 1990) applied to AI; the lock-in test is Shapiro & Varian's switching-cost analysis (*Information Rules*, 1998).

Compose with: [switching-costs](../switching-costs/SKILL.md) (lock-in assessment) · [premortem](../premortem/SKILL.md) (stress-test before signing) · [theory-of-constraints](../theory-of-constraints/SKILL.md) (confirm this is the bottleneck first) · [proprietary-data-moat](../proprietary-data-moat/SKILL.md) (is the "unique data" actually a moat?) · [ai-pilot-to-scale](../ai-pilot-to-scale/SKILL.md) (run the chosen option as a gated pilot).

## When to Use

- Before committing engineering headcount, an annual contract, or a data migration to an AI capability
- After a vendor raises prices, changes terms, or is acquired — re-evaluate
- The team wants to "train our own model," or sales is pushing an "all-in-one platform"

**When NOT to use:** low monthly fee, cancel any time · capability unrelated to business outcomes · regulation already mandates the solution.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete capability and candidate options → run The Process directly.
- **Coach mode:** user is unfamiliar → one step at a time. Each [WAIT] is a hard stop — output only that step's question.

1. **What it is.** "Build only the layer that makes customers choose you; buy or partner for the rest."
2. **Check fit.** "Can you exit this commitment within a month at low cost? If yes, you don't need this."
3. **Elicit the real case.** "Which capability, serving which workflow, and what are the candidate options?"
> **[WAIT — do not advance until user responds]**
4. **Run steps 1–3:** the differentiation test and data/IP control.
> **[WAIT — do not advance until user responds]**
5. **Name the insight.** The user states the verdict (build/buy/partner) and the re-evaluation trigger.
> **[WAIT — do not advance until user responds]**

## The Process

**Output:** Decision matrix + chosen option + exit plan

1. **Define the capability.** Write the capability, the workflow it serves, and the success metric (e.g. first-response time on tickets). *Gate: no metric → stop; set a baseline first via [ai-pilot-to-scale](../ai-pilot-to-scale/SKILL.md).*
2. **Differentiation test.** Ask: if a competitor used the same off-the-shelf tool, would customers notice a difference? No → default to buy. *Gate: keep "build" on the table only if the answer is yes **and** the difference comes from your proprietary data or process.*
3. **Data & IP control.** List the data that flows in and what each contract says about training use, retention, deletion and export. *Gate: core customer data would be used for training, or cannot be exported → that option is out.*
4. **Time to value.** Estimate weeks to first usable output per option. If build takes more than ~3× as long as buy, the differentiation value must cover the gap.
5. **Three-year TCO.** License/usage fees + integration + maintenance headcount + evaluation + **rework when the underlying model is replaced** + exit/migration cost. *Gate: maintenance and model replacement not costed → no comparison allowed.*
6. **Lock-in & vendor risk.** Switching cost, single-vendor dependency, vendor viability and roadmap, SLA. Require exportable formats and a model-swappable interface.
7. **Score the matrix and choose.** Weighted dimensions (differentiation, control, time, cost, lock-in, risk); write the exit plan and the re-evaluation triggers.
8. **Stop-rule:** if the capability has not yet been shown to create value, run a minimal *buy* pilot first, then return to step 2.

**Output template:**
`Capability | Metric | Differentiated? (yes/no + evidence) | Data terms | Weeks to value | 3-yr TCO (build/buy/partner) | Lock-in score | Choice | Exit plan | Re-evaluation trigger`

*→ Method in Action: [BloombergGPT and the general-purpose models (2023)](examples/bloomberggpt-build-vs-general-models-2023.md)*

## Applying It Well

1. **Buy by default; build carries the burden of proof.** Evidence of differentiation is customer behavior, not team interest.
2. **Partner = shared data or revenue in exchange for capability.** Write data ownership and post-termination handling into the contract first.
3. **Treat the model as a replaceable part.** Build or buy, keep your own evaluation set and an abstraction layer, so swapping models does not mean rewriting the business logic.
4. **Re-run on every major model release.** A build decision is a bet that the gap between your model and the next general one stays open; check it when the general one moves.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "Building is cheaper — it's just one engineer" | Maintenance, evaluation and model replacement are the bulk of the cost; one engineer is a single point of failure. |
| [D] "This vendor is cheapest — sign three years now" | Low price often comes with high switching cost; check export and termination terms first. |
| [D] "Our data is unique" | Test whether the proprietary data actually improves outcomes; otherwise it is sentiment. |
| [D] "The vendor's roadmap will cover our needs" | A roadmap is not a contract. Evaluate what ships today. |
| [D] "A domain-specific model will always beat a general one in our domain" | General models improve on their own schedule; the gap must be re-measured, not assumed. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Decision made with no three-year TCO · data-training clauses unread · the reason to build is "technically interesting" · no exit plan · no owned evaluation set to compare options

## Verification

- [ ] Differentiation test backed by customer-side evidence
- [ ] TCO includes maintenance, evaluation, model replacement and exit cost
- [ ] Data training/retention/export terms checked clause by clause
- [ ] Matrix scores and weights archived; re-evaluation triggers written (incl. major model releases)

---

*Part of **deciqAI Knowledge Skills** — 253 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/build-buy-partner-ai** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/build-buy-partner-ai.json*
