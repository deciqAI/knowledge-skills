# Method in Action: Vivid AI Stories vs. Base Rates (2023–2026)

> *Example for the [availability-heuristic](../SKILL.md) skill.*

Between the launch of ChatGPT in late 2022 and 2026, public and boardroom estimates of AI's risks and opportunities were shaped less by aggregate data than by a handful of unforgettable stories: a viral demo that looked like magic, a dramatic "AI replaced our whole team" layoff headline, a safety scare that dominated a news cycle. Each is recent, vivid, heavily covered, and easy to picture — all five availability triggers firing at once. The pattern is the skill's core failure mode at population scale: a memorable single case substitutes for the reference class, and both opportunity and risk estimates get pulled off their base rates. Running the Process makes the distortion legible.

**Step 1 — Specify the estimate.** Three intuitive claims circulating in 2023–2026, each driven by a memorable example rather than data:
- *Opportunity:* "A demo went viral / one competitor shipped an impressive feature, so we'll get comparable results fast if we adopt now." Basis: the demo, not deployment outcomes.
- *Risk (jobs):* "A company just cut a large share of a function and credited AI, so my role/team is about to be automated." Basis: one dramatic layoff headline.
- *Risk (safety):* "A safety scare made the news, so catastrophic AI harm is imminent and probable." Basis: one news cycle.
Decisions at stake: whether to greenlight an AI rollout, how much to fear displacement, and how much precautionary weight to assign to AI-safety tail risk.

**Step 2 — Identify the reference class.** For each claim the relevant population is *not* the single vivid case:
- Opportunity: the full population of enterprise AI pilots and deployments, including the many that stall before production — not the one polished demo.
- Jobs: economy-wide employment and task-exposure data across occupations over years — not one announced headcount cut.
- Safety: the record of documented, materialized AI harms across deployed systems — kept distinct from speculative tail risk, which the skill's boundary treats separately.
Getting this wrong — reasoning from a reference class of one — is the central error in each case.

**Step 3 — Get the base rate.** The aggregate pictures, as of early 2026, told a more muted story than the headlines:
- Adoption/opportunity: surveys such as those in Stanford HAI's *AI Index* and McKinsey's annual "State of AI" reported that while a large and rising share of organizations were *using* generative AI in at least one function, the share reporting material, bottom-line financial impact was far smaller — many pilots did not translate into measured ROI. The viral demo is a poor predictor of realized deployment value.
- Jobs: through 2023–2025, most large-scale labor statistics and studies (e.g., the ILO and OECD work on generative-AI exposure) framed the near-term effect as *task augmentation and exposure* rather than wholesale occupation elimination, and aggregate unemployment did not show an AI-driven displacement shock over this window. "AI-attributed" layoff announcements were a small and often reclassified slice of total workforce reductions.
- Safety: over the same window the well-documented, materialized harms were concentrated in mundane categories — hallucinated/incorrect outputs, bias, privacy and data leakage, fraud and deepfake-enabled scams — not the catastrophic scenarios that drove the scariest coverage.

**Step 4 — Diagnose availability distortions.**
- *Recency:* a demo, layoff, or scare that "just happened" was treated as the new steady state.
- *Vividness & imaginability:* a magical demo and an "AI took the jobs" headline are dramatic and easy to picture; a stalled pilot or a slow augmentation of tasks is routine and statistical, so it is under-retrieved.
- *Media coverage:* coverage volume tracks drama, not frequency — spectacular demos and dread-laden safety stories are over-reported relative to the modal outcome (a pilot that quietly underperforms).
- *Personal experience:* a single striking interaction with a model ("it wrote my code / it hallucinated a court case") gets generalized into a population frequency.
- *Affect/dread:* as with post-9/11 "dread risk," the safety scare's emotional charge inflates its perceived probability independent of any base-rate change.

**Step 5 — Compare.** In each case the intuitive estimate and the base rate diverge by more than 2×, so availability is doing significant work:
- The demo-to-value gap: enthusiasm keyed to a viral demo, base rate keyed to the minority of deployments showing measured impact — a large overestimate of near-term opportunity.
- The layoff signal: one attributed cut treated as an economy-wide trend, versus aggregate data showing augmentation-dominant, slow displacement — an overestimate of imminent personal risk.
- The safety scare: one news cycle treated as evidence that catastrophic harm is probable now, versus a documented-harm record dominated by mundane failure modes — a misallocation between speculative tail risk and the risks actually materializing.
Adjust each toward its base rate; justify residual deviation with case-specific factors (e.g., your firm's data readiness for the opportunity case) rather than the vividness of the anchor story.

**Step 6 — Document.** The correction: size AI opportunity from deployment-outcome base rates, not demos; size displacement risk from task-exposure and labor data, not attributed-layoff headlines; and separate *documented, materialized* AI harms (govern these now) from *speculative catastrophic* harms (the skill's boundary permits precautionary weight here, but on its own explicit ledger — not smuggled in via a vivid news cycle). Log each prediction against outcomes to build calibration.

Note the boundary the skill draws. Availability correction does **not** mean dismissing AI risk or opportunity — it means estimating both from the reference class instead of the most memorable instance. For genuinely rare-but-catastrophic AI-safety tail risks, precautionary weight can be warranted; the discipline is to assign that weight explicitly and quantitatively, not to let a single dramatic story stand in for a base rate it never measured.

The mapped steps:

1. Specify the estimate: viral demo → "fast results"; one layoff → "my job is next"; one scare → "catastrophe is imminent" — each from a memorable case, not data
2. Reference class: all enterprise deployments; economy-wide task-exposure data; the record of materialized AI harms — not the single vivid instance
3. Base rate: adoption high but measured ROI far narrower; near-term labor effect augmentation-dominant; documented harms mostly mundane (errors, bias, fraud/deepfakes)
4. Distortions: recency, vividness, imaginability, saturation coverage, one-off personal experience, and dread-affect
5. Compare: intuition vs. base rate diverges >2× on opportunity, jobs, and safety; adjust toward base rates
6. Document: separate materialized from speculative risk; forecast from deployment/labor data; log for calibration

*Sources: Tversky, A., & Kahneman, D. (1973), "Availability: A heuristic for judging frequency and probability," Cognitive Psychology 5(2); Stanford HAI, AI Index Report (2024 and 2025 editions), https://hai.stanford.edu/ai-index ; McKinsey & Company, "The state of AI" annual global surveys (2024, 2025), https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai ; OECD Employment Outlook (2023) on AI and the labour market, https://www.oecd.org/ ; International Labour Organization, "Generative AI and Jobs" (2023), https://www.ilo.org/ . Figures described qualitatively; consult the cited reports for exact, as-of-publication numbers.*
