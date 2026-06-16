---
name: industry-learning-sprint
description: "Activate when: user is entering an unfamiliar industry and needs a working mental model fast; user says 'I need to understand this sector before a meeting next week'; user is evaluating an acquisition or investment in a domain they don't know; user is preparing for a high-stakes expert conversation with limited time; user needs to produce an investment thesis or market entry recommendation under time pressure. Do NOT activate when: user already has deep domain expertise in the target industry; user needs regulatory or legal precision — engage domain-specific counsel instead."
---

# Industry Learning Sprint

## Overview

A structured 3-step process (financial reports → expert dialogue → unique view) for building a working industry mental model in approximately one week. The sequence is strict: financials before experts, experts before view formation. Financial reports reveal how an industry actually works stripped of marketing narrative; gross margin, capex pattern, and disclosed risk factors encode economic reality.

**Neighbors:** [`probabilistic-thinking`](../../probabilistic-thinking/SKILL.md) (assign confidence intervals before expert conversations) · [`first-principles`](../../first-principles/SKILL.md) (stress-test the view after Step 3) · [`confirmation-bias`](../../confirmation-bias/SKILL.md) (audit Step 3) · [`non-consensus-thinking`](../non-consensus-thinking/SKILL.md) (evaluate if the view is truly non-consensus) · [`narrow-gate-strategy`](../narrow-gate-strategy/SKILL.md) (identify the leverage point for focused entry).

---
## When to Use

**Trigger conditions:** Entering an industry for the first time (investor, founder, executive, advisor) · Evaluating an acquisition or partnership in an unfamiliar sector · Preparing for a high-stakes expert conversation with limited prep time · Producing an investment thesis or market entry recommendation under time pressure.

**When NOT to use:** Deep domain expertise already exists · Timeline under 48 hours (mark output as preliminary) · Industry is primarily informal/unregistered (financial reports will be unrepresentative).

---
## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a concrete industry target → run The Process directly.
- **Coach mode:** user unfamiliar with financial analysis → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. Reframe the goal: "You need one falsifiable hypothesis that would be contested by an insider — not comprehensive understanding."
2. Check fit: confirm this is a new industry entry scenario, not a domain they already know deeply.
3. Elicit their real case: "Which industry, and what decision are you trying to make at the end of this sprint?"
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time with their input: start with financial structure mapping using their named industry.
> **[WAIT — do not advance until user responds]**
5. Close by naming the insight: "Your non-consensus view is [X] — here's why it would be contested by an insider."
> **[WAIT — do not advance until user responds]**

---
## The Process

**Step 1 — Financial Structure Mapping (Day 1–2).** Pull 3–5 years of annual reports for 2–3 leading companies. Do not read analyst commentary first. Extract: **Revenue model** · **Gross margin** (>60% = platform economics; <20% = commodity) · **Capex vs. opex split** (determines moat and entry barrier) · **Customer concentration** (>30% from one customer = disclosed systemic risk) · **Disclosed risk factors** (the most honest document a company publishes — read as a map of industry failure modes). Output: one-page financial structure map.

**Step 2 — Expert Dialogue (Day 3–5).** Conduct 3–5 conversations using the financial structure as your hypothesis base. Target four categories: operators, investors, ex-employees, regulators. Design each conversation as a hypothesis stress-test: "I noticed [X] in the financials — is that because [Y] or [Z]?" Ask: "What does the financial structure not capture?" Output: 3–5 corrections or confirmations + 2–3 structural insights the financials did not reveal.

**Step 3 — Unique View Formation (Day 6–7).** Synthesize into one non-consensus hypothesis: **specific** (name the mechanism), **falsifiable** (state what would prove it wrong), **contested** (a domain expert would disagree). Stop-rule: if you cannot state a contested view, you have summarized, not analyzed. Return to expert corrections: "What do experts believe that I saw evidence against in the financials?"

### Output Template

| Section | Contents |
|---|---|
| Financial Structure Map | Revenue model, gross margin, capex/opex, customer concentration, top 3 risk factors — each with source |
| Expert Dialogue Corrections | Hypothesis confirmed / corrected, source (name, role, date); plus 3 structural insights not in financials |
| Unique View | Specific falsifiable hypothesis · evidence base (financial finding + expert correction + tension) · falsifier · confidence |
| Known Gaps | What was not covered and what would change the view |

*→ Method in Action: [Graham's Analysis of Northern Pipeline (1926)](examples/grahams-analysis-of-northern-pipeline-1926.md)*

---
## Domain Packs

**Pharma / Biotech:** Diagnostic: R&D-to-revenue ratio (>25% = pipeline-dependent), gross margin by product line, patent expiry schedule. Best experts: clinical scientists, formulary managers, ex-FDA reviewers. Reject: "Strong pipeline = strong future."

**Logistics / Freight:** Diagnostic: operating ratio (<85% = healthy), fuel cost sensitivity, top-10 shipper concentration. Best experts: freight brokers, dispatch supervisors, shippers' logistics managers.

*Contribution invitation: submit domain packs via the deciqAI repository.*

---
## Applying It Well

- **Sequence strictly** — financials before experts; experts before view formation.
- **Read primary documents** — annual reports and earnings transcripts, not analyst summaries.
- **Design expert conversations as hypothesis tests** — specific financial questions yield 10x more signal than "What should I know?"
- **Target four expert categories** — operators, investors, ex-employees, regulators each have a structurally different view.
- **Apply the stop-rule** — "Would a domain expert be surprised by this?" If no, revise.
- **Document known gaps** — prevents overconfidence.

*→ Primary sources: [references/sources.md](references/sources.md)*

---
## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "I've read five analyst reports." | Five consensus documents give higher-confidence consensus, not independent analysis. |
| [D] "I talked to insiders for hours." | Without a financial hypothesis base, expert talk produces orientation, not stress-testing. |
| [D] "My view is that this is a great industry." | That is the marketing narrative. A view names the structural mechanism most people are wrong about. |
| [D] "I don't know how to read financials." | The sprint requires only four numbers: revenue model, gross margin, capex/opex, customer concentration. |
| [D] "All the experts agree, so the view is right." | Expert consensus is what the sprint is designed to think against. |
| [D] "I need much more research before forming a view." | More research without a view target produces information, not insight. Commit at Day 7. |
| [D] "My unique view might be wrong." | Specify what would falsify it. Being wrong about a falsifiable view beats vaguely right about consensus. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

---
## Red Flags

- No view that would be contested by a domain expert — produced a summary, not an analysis.
- Expert conversations conducted before reading financial reports — sequence reversed.
- Financial structure map missing gross margin — the most diagnostic number omitted.
- Sprint took more than two weeks — time pressure is a design feature, not a bug.
- Unique view is not falsifiable — it is an opinion, not a hypothesis.
- Only one expert category consulted — one-dimensional model.
- Sprint conducted entirely from secondary sources — primary documents and expert dialogue skipped.

---
## Verification

- [ ] Annual reports for 2–3 leading companies (3+ years) read as primary sources.
- [ ] Financial structure map contains all four dimensions: revenue model, gross margin, capex/opex, customer concentration.
- [ ] Expert conversations designed as hypothesis stress-tests with specific financial hypotheses as agenda.
- [ ] At least 3 distinct expert categories consulted (operators, investors, ex-employees, regulators).
- [ ] Unique view is specific, falsifiable, and would be contested by at least one domain expert.
- [ ] Stop-rule applied: "Would an insider be surprised by this?" — if no, view was revised.
- [ ] Known gaps explicitly documented. Sprint completed within approximately one week.

---
*Part of **deciqAI Knowledge Skills** — 163 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/industry-learning-sprint?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=industry-learning-sprint** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
