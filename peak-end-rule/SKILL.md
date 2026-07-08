---
name: peak-end-rule
description: "Activate when: user says 'how will they remember this,' 'experience design,' 'journey design,' 'memorable moment,' 'end-of-experience,' or 'our NPS is lower than expected'; when designing or auditing a multi-stage customer or user journey; when a competitor with similar quality earns higher recommendation rates.
  Do NOT activate when: the interaction is instantaneous with no temporal sequence (single API call, one-tap action); or when total real-time utility matters more than retrospective memory (welfare assessments, health measurements)."
---

# Peak-End Rule

## Overview

People remember experiences not by averaging all moments but by sampling two: the peak (highest emotional intensity) and the end. Everything in between — including duration — is largely discarded. This is the *peak-end rule*, from Kahneman et al. (1993) and Redelmeier & Kahneman (1996).

Global evaluation ≈ (peak intensity + end intensity) / 2. Experience design is not an averaging problem — it is a peak-and-ending problem.

**Neighbor skills:** Use after [aarrr-pirate-metrics](../aarrr-pirate-metrics/SKILL.md) to place the peak in the right lifecycle stage; use [anchoring](../anchoring/SKILL.md) to set expectation baselines peaks must exceed; pair with [nudge-theory](../nudge-theory/SKILL.md) to smooth the path to the peak and ending; use [probabilistic-thinking](../probabilistic-thinking/SKILL.md) before designing peaks to estimate expected effect size.

## When to Use

Apply when:
- Designing or auditing a multi-stage experience with a clear start and end (onboarding, service encounter, event, medical visit)
- NPS or satisfaction scores are lower than expected given average perceived quality
- A competitor with similar objective quality consistently earns higher recommendation rates
- Allocating limited resources across experience stages and need to know where to concentrate

**When NOT to use:** purely instantaneous interactions with no duration; real-time performance optimization (not retrospective rating); welfare/health assessments where experienced utility — not memory — is the correct measure; one-time required events with no competitive alternative.

## Coaching Novices (Adaptive Front Door)

- **Engine mode:** concrete journey to audit → run The Process directly.
- **Coach mode:** unfamiliar or no concrete case → guide step by step.

In Coach mode, respond one step at a time. Each [WAIT] is a hard stop — output only that step's question, then stop.

1. What-it-is: people remember by their strongest moment and how it ended — the middle barely matters.
2. Check fit: instantaneous interaction or real-time utility goal → redirect.
3. Elicit their real journey — get actual stages and where emotion rises and falls.
> **[WAIT — do not advance until user responds]**
4. Walk through emotion map; identify current peak and ending; ask what "better" looks like for those two points only.
> **[WAIT — do not advance until user responds]**
5. Name the one change most likely to move NPS/return rate and the metric to confirm it.
> **[WAIT — do not advance until user responds]**

## The Process

Run the **Peak-End Audit**. Emotion map first, then peak and ending diagnosis, then redesign.

**Stop-rule:** If you cannot map the experience into a temporal sequence of stages with varying emotional intensity, the peak-end rule does not apply.

1. **Map the experience timeline.** List every significant stage in chronological order. Estimate emotional intensity (-5 to +5) per stage. Note where intensity spikes, dips, and what the emotional state is at the last touchpoint.
2. **Identify the current peak.** Highest intensity stage — positive or negative. Document: is it designed or accidental? Positive or negative? Strategically placed?
3. **Identify the current ending.** Emotional state at the last touchpoint. Flag if it is neutral/procedural (checkout confirmation, invoice, exit survey).
4. **Diagnose the gaps.** Peak gap: strong enough and positive? Ending gap: warm and memorable? Negative peak risk: any negative stage overwhelming the positive peak?
5. **Design the peak intervention.** One moment exceeding expectation *significantly*. Intensity correlates with surprise gap (actual minus expected), not absolute quality. Specify: what moment, what "exceeding expectation" means, estimated cost vs. expected lift.
6. **Design the ending intervention.** Highest-ROI optimization. Principles: (a) make the person feel *remembered*; (b) leave a tangible memory artifact; (c) point forward, not backward.

**Output template — Peak-End Audit:** Timeline table (Stage | Description | Intensity -5 to +5 | Notes) → Current Peak (stage / intensity / positive or negative / designed or accidental) → Current Ending (stage / intensity / warm–neutral–cold–procedural) → Gap Diagnosis (peak gap | ending gap | negative peak risk) → Peak Intervention (stage / change / mechanism / cost) → Ending Intervention (change / personalization / memory artifact / forward orientation) → Verification Metrics (NPS or return rate | baseline | target | timeline).

*→ Method in Action: [Redelmeier and Kahneman — Colonoscopy Study (1996)](examples/redelmeier-and-kahneman-colonoscopy-study-1996.md)*

## Experience Design Packs

Domain substance varies; the audit runs identically everywhere.

- **SaaS onboarding:** peak = Aha moment; ending = activation final screen. Fix: delay complexity until after peak; replace "setup complete" with personalized progress preview.
- **Hospitality:** peak = unexpected service moment; ending = checkout. Fix: handwritten note, small gift, staff escort to door.
- **Healthcare:** primary risk = negative peak from procedure. Fix: warm "you did well" close; printed care plan as memory artifact.
- **B2B services:** peak = project delivery; ending = invoice. Fix: retrospective framing the client's success, not the deliverable.

## Applying It Well

- Ending = highest-ROI optimization; audit what literally the last thing a person sees/hears/feels is.
- Peaks require exceeding expectation — design for the *surprise gap*, not just quality level.
- Duration neglect = resource allocation insight: don't over-invest in the middle at peak/ending's expense.
- Negative peaks compete with positive peaks — address them first.
- Personalization amplifies both peak and ending intensity. Do not pre-announce the peak.

*→ Primary sources: [references/sources.md](references/sources.md)*

## Common Rationalizations

**[D] = designed upfront | [O] = observed in real use. [O] entries are more valuable.**

| Fake move | Reality |
|---|---|
| [D] **"We improved average satisfaction, so the experience is better."** | Average = experiencing self. NPS = remembering self. Improved average with unchanged ending may produce no NPS movement. |
| [D] **"Quality is high throughout, so peak-end doesn't apply."** | Uniform quality without variance produces no memorable peak. Even excellent experiences need a designed one. |
| [D] **"We improved the ending by adding a thank-you email."** | An automated email isn't an ending experience. The ending is the last direct emotional touchpoint — inbox email has near-zero peak-end value. |
| [D] **"Duration doesn't matter — extend the bad part as long as it ends well."** | Duration neglect is directional, not a hack. Extended negatives with a good ending still underperform shorter ones with the same ending. |
| [D] **"We averaged step-by-step ratings."** | Measures experienced utility, not remembered utility. NPS and return behavior are remembered-utility outcomes; they diverge substantially. |
| [D] **"Our peak is at the beginning."** | Beginning peaks drive acquisition; delivery peaks drive retention and NPS. Beginning peaks decay with expectation reset. |
| [D] **"We can't change the checkout/invoice ending."** | That moment is most amenable to low-cost redesign. A personal message on an invoice is trivially cheap with high expected impact. |
| [D] **"Peaks are expensive."** | The most powerful peaks are low-cost high-personalization: a handwritten note, a remembered detail. Surprise drives intensity, not cost. |
| *→ Add [O] entries here after each real use — paste the actual failure pattern* | *What went wrong and why* |

## Red Flags

- NPS targets set without identifying which stage is being redesigned
- "Peak" = the entire experience rather than a specific moment
- Ending touchpoint is an automated system message with no emotional content
- Budget allocated uniformly across all stages
- Negative peak risk stages not addressed before positive peak investment
- User research measures step-by-step ratings only — no retrospective global measure
- Peak announced in advance — eliminating the surprise gap

## Verification

- [ ] Timeline mapped with emotional intensity estimated per stage
- [ ] Current peak identified — positive/negative, designed/accidental
- [ ] Current ending assessed — warm / neutral / cold / procedural
- [ ] Negative peak risks identified before positive peak investment
- [ ] Peak intervention targets *exceeding expectation* at a specific moment
- [ ] Ending intervention has personalization element, memory artifact, and forward orientation
- [ ] Retrospective verification metric (NPS, return rate) defined with baseline and target

---

*Part of **deciqAI Knowledge Skills** — 164 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/skills/peak-end-rule?utm_source=skill&utm_medium=oss&utm_campaign=knowledge-skills&utm_content=peak-end-rule** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*
