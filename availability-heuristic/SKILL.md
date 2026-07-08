---
name: availability-heuristic
description: "Activate when: user says 'we keep hearing about X so it must be common', 'that just happened so it's risky', 'the news is full of stories about this', 'I've seen this a lot lately so it's probable', or is making a risk/frequency estimate driven by memorable examples rather than data. Do NOT activate when: the available evidence is genuinely representative of the reference class; the decision warrants heavy precautionary weight on rare but catastrophic/irreversible risks."
---

# Availability Heuristic

## Overview

The **availability heuristic**: people estimate probability by how easily examples come to mind. Vivid, recent, and media-reported events are systematically overestimated; routine, statistical events are underestimated. Five triggers: **recency**, **vividness**, **media coverage**, **personal experience**, **imaginability**. Structural fix: **reference-class forecasting** — answer from base-rate data, not memory.

Composes with [`bayesian-reasoning`](../bayesian-reasoning/SKILL.md), [`probabilistic-thinking`](../probabilistic-thinking/SKILL.md), [`anchoring`](../anchoring/SKILL.md), [`survivorship-bias`](../survivorship-bias/SKILL.md), [`framing-effect`](../framing-effect/SKILL.md).

## When to Use

- Someone estimates probability from memorable examples rather than data
- Risk perception driven by recent news, vivid anecdotes, or media coverage
- Team is preparing for the last disaster rather than the most likely next one
- Investment or resource-allocation decision follows a recent dramatic event
- Medical, legal, or technical decision made by anecdote rather than reference class
- AI capex, AI valuations, or AI-adoption/displacement estimates are driven by a viral demo, a dramatic layoff headline, or a safety scare rather than deployment and labor base rates

**Not when:** available evidence is a representative sample; decision warrants precautionary weight on rare catastrophic risks; no reference-class data exists.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** user has a specific risk or frequency estimate → run The Process directly.
- **Coach mode:** user is new → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. One-line: before trusting an intuitive probability, ask whether it is based on retrieval ease or on a reference class with actual data.
2. Check fit: if recent vivid evidence is also representative, use it; otherwise discount and seek base rates.
3. Elicit their real case — what probability is being claimed, on what basis?
> **[WAIT — do not advance until user responds]**
4. Run The Process one step at a time: reference class → base rate → distortion diagnosis → compare to intuitive estimate.
> **[WAIT — do not advance until user responds]**
5. Close: restate corrected estimate as base-rate + specific adjustment, with the adjustment justified.
> **[WAIT — do not advance until user responds]**

## The Process

**Step 1 — Specify the estimate:** probability/frequency being estimated · current intuitive estimate · basis (memory/news/data) · decision that depends on it.

**Step 2 — Identify the reference class:** population of comparable cases · size · time horizon · inclusion/exclusion criteria. *(Getting this wrong is the main failure mode.)*

**Step 3 — Get the base rate:** actual frequency in the reference class · source · confidence level.

**Step 4 — Diagnose availability distortions:** recency (is the recent rate representative?) · vividness (dramatic vs. routine?) · media coverage (over-reported?) · personal experience (inflated?) · imaginability (easy to picture → feels more probable?).

**Step 5 — Compare:** intuitive estimate vs. base rate. If ratio >2×, availability is doing significant work. Adjust toward base rate; justify any residual deviation.

**Step 6 — Document:** corrected probability · reasoning (base rate × adjustments) · decision implications · calibration log entry.

## Output Template

```
Availability Correction: <event>
Original estimate: <value> | Basis: | Decision:
Reference class: <population, size, time horizon>
Base rate: <frequency> | Source: | Confidence:
Distortions: recency / vividness / media / personal / imaginability
Corrected estimate: <value> | Adjustment rationale:
Decision implications: | Calibration log:
```

*→ Method in Action: [Tversky and Kahneman's 1973 Availability Studies](examples/tversky-and-kahnemans-1973-availability-studies.md) · [Post-9/11 Flight Avoidance and Road Fatalities](examples/post-9-11-flight-avoidance-and-road-fatalities.md)*

*→ 2026 lens: [Vivid AI Stories vs. Base Rates (2023–2026)](examples/ai-vivid-stories-vs-base-rates-2023-2026.md)*

## Pack: Availability Bias Patterns

| Domain | Distortion | Correction |
|---|---|---|
| Personal risk | Overestimate terrorism/plane crashes; underestimate heart disease/car crashes | CDC/BLS mortality statistics |
| Investment | Recent winners feel certain to continue | Long-horizon data; mean reversion priors |
| Hiring | Memorable candidate beats better-qualified one | Structured rubric; reference-class hire data |
| Project planning | Optimism from vivid current plan vs. project-class history | Flyvbjerg reference-class forecasting |
| Medical diagnosis | Recently-seen diagnosis over-weighted | Base-rate-weighted differential diagnosis |
| Strategic planning | Recent competitor event dominates outlook | Multi-year base rates; explicit reference class |

## Applying It Well

- Define the reference class before looking up the base rate. Calibration improves with logged predictions vs. outcomes, not exhortation. Present absolute frequencies (deaths per 100,000), not relative risk.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] "But that just happened!" | Recency aids recall; it doesn't increase future probability. Check the longer reference class. |
| [D] "I've seen this many times" | Easy retrieval ≠ high population frequency. |
| [D] "The news is full of stories about this" | Coverage tracks vividness, not frequency. |
| [D] "I'd remember if it were rare" | You remember dramatic-rare more than statistical-common. |
| [D] "I have personal experience" | Personal examples are a tiny, often unrepresentative sample. |
| [D] "The risk is too vivid to ignore" | Vividness ≠ probability. Compute actual probability; respond proportionally. |
| [D] "We have to prepare for the worst" | Sometimes valid. Often over-preparation for spectacular-low-probability events. |
| [D] "The base rate is irrelevant — this case is different" | Be specific about which factors actually move the estimate. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- Risk estimate made without consulting actual data
- Single-case vivid examples or recent news are the dominant evidence
- Coverage volume treated as evidence of frequency
- Reference class not explicitly identified

## Verification

- [ ] Intuitive estimate stated with confidence level
- [ ] Reference class identified
- [ ] Base rate retrieved from a defensible source
- [ ] Availability distortions (recency, vividness, media, personal experience) considered
- [ ] Corrected estimate documented with reasoning
- [ ] Decision implications computed
- [ ] Estimate logged for later calibration

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/availability-heuristic?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=availability-heuristic** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*