# Method in Action: The AI Capex Boom as a Reinforcing Loop Meeting Its Balancing Limits (2024–2026)

> *Example for the [feedback-loops](../SKILL.md) skill.*

Between 2024 and 2026, the largest US technology companies — Microsoft, Alphabet, Amazon, and Meta, joined by chipmaker Nvidia and a wave of AI-native startups led by OpenAI and Anthropic — poured historic sums into AI data-center capacity. Reported annual capital expenditure at the four "hyperscaler" cloud providers rose from roughly $150 billion in 2023 toward figures widely reported in the several-hundred-billion range for 2025, with further increases guided for 2026. The dominant narrative through most of this period was pure reinforcing-loop optimism: spend more, get better models, unlock more demand, justify spending still more.

This example runs the **Feedback-Loop Diagnosis** on that dynamic. The point is not to predict the exact top of the cycle — the skill explicitly warns against extrapolating a feedback system's recent trend — but to show why a runaway reinforcing loop with long build delays is structurally set up to overshoot, and where the balancing loops that eventually check it actually live.

## 1. Name system + variable of interest

**System:** the AI compute build-out — the interconnected market of AI model developers, cloud infrastructure providers, chip suppliers, and the enterprises and consumers buying AI products.

**Variable of interest:** installed AI compute capacity (roughly, GPU-equivalents in service), and the capital-expenditure *rate* funding its growth. The two are not the same thing, which matters at step 7.

## 2. List drivers and outputs

- **Drivers that raise capex:** expected demand for AI products; belief that model quality scales with compute (the "scaling laws" thesis); competitive fear of being left behind; cheap capital and strong balance sheets; falling cost-per-token making new use cases viable.
- **What capex changes in turn:** more installed compute → larger/better-trained models → more capable AI products → (claimed) more end-user demand → more revenue and more investor conviction → still more capex. Capex also drives up demand for chips, electrical power, and data-center real estate.

## 3. Identify loops

- **R1 (the flywheel):** capex → compute → better models → more demand → more revenue/conviction → more capex. This is the loop everyone was pitching.
- **R2 (capital-markets amplifier):** rising AI revenue and rising valuations → cheaper capital and investor pressure to spend → more capex → more revenue expectation. A financial reinforcing loop stacked on top of the physical one.
- **B1 (physical limits):** more capex → more compute demanded → scarce inputs (advanced-packaging capacity, high-bandwidth memory, electrical power, grid interconnects) → input prices/lead-times rise → effective cost of adding capacity rises → capex growth checked.
- **B2 (unit economics / return on capital):** more capex → more depreciation and more capacity chasing revenue → if AI revenue does not grow fast enough, return on invested capital falls → investors demand discipline → capex growth checked.
- **B3 (competition / commoditization):** more players building comparable frontier models → price competition on tokens and rapid capability convergence → margin per unit of compute compressed → weaker justification for the next capex increment.

## 4. Classify each loop (R or B)

- **R1** and **R2:** count the signs around each chain — all links are "more → more," an even number (zero) of negative signs. **Reinforcing.**
- **B1, B2, B3:** each contains an odd number of sign-flips (more capex eventually produces a *reduction* in the incentive to add the next unit — via higher input cost, lower ROIC, or compressed margin). **Balancing.**

## 5. Locate delays

Delays are where intuition fails, and this system is unusually delay-heavy:

- **Data-center and power build-out:** commonly reported at multiple years from decision to energized capacity; grid interconnection and new generation can take longer still. This is the critical delay — commitments made in 2024–2025 come online well afterward.
- **Chip supply, especially advanced packaging (e.g. TSMC CoWoS) and high-bandwidth memory:** roughly a year-plus to expand, and a known bottleneck reported through 2024–2025.
- **Demand/monetization realization:** the lag between shipping a more capable model and enterprises actually rearchitecting workflows to generate durable revenue — plausibly quarters to years.
- **ROIC signal:** depreciation on today's capex shows up in financial statements over subsequent years, so the return-on-capital feedback (B2) arrives *late* relative to the spending decision.

Every one of the balancing loops acts with a long delay. That is the setup for overshoot.

## 6. Identify dominant loop

Through 2024 into 2025, **R1 and R2 dominated**: capacity, valuations, and capex all compounded, which is the signature of a reinforcing loop in its growth phase. The balancing loops were present but *not yet binding* — their long delays meant their corrective force had not arrived. This is exactly the regime where operators are most tempted to extrapolate, because the only loop currently visible is the one pushing up.

## 7. Map stocks and flows

- **Stocks (accumulations):** installed compute capacity; data centers under construction; committed-but-not-yet-delivered chip orders; accumulated depreciation; investor conviction.
- **Flows (rates):** the capex *rate*; the rate of new capacity energized; the rate of AI revenue booked.

The stock-vs-flow distinction is the trap here. A very high capex *flow* does not mean capacity is adequate *now* — because of the multi-year build delay, today's flow is filling a stock that arrives years later. Symmetrically, when demand signals soften, the capex flow can be cut quickly, but the stock of half-built data centers and in-flight chip orders keeps arriving — the supply line, in Sterman's sense, that operators chronically underweight.

## 8. Predict behavior pattern

A strong reinforcing loop (R1+R2) plus delayed balancing loops (B1/B2/B3) is the textbook recipe for **overshoot-and-correct**, not smooth convergence. The reinforcing loop drives capacity and spending past the level that steady-state demand can profitably support; because the balancing signals (ROIC, margin compression, digestion of capacity) arrive only after a delay, the correction is not felt until significant over-commitment already exists. The likely pattern is: rapid compounding growth → a period where capacity outruns monetized demand → a sharp deceleration or cut in capex growth once the return signal finally lands → possible oscillation (a "digestion" pause) before a more sustainable trajectory. This is the same structure as a capacity-cycle bullwhip in commodities or semiconductors, not a permanent exponential.

If instead AI monetization keeps pace with capacity in real time, R1 would remain genuinely self-sustaining and the balancing loops would bite gently — an S-curve rather than an overshoot. Which of these occurs depends on the *relative timing* of the demand delay versus the build delay, which is precisely what cannot be reliably extrapolated from 2024–2025 data alone.

## 9. Find leverage (Meadows hierarchy)

- **Lowest (parameters):** tweaking a single quarter's capex number — noise against a structurally-driven cycle.
- **Higher (structure / delays):** shortening the build delay (modular data centers, pre-secured power, second-sourcing packaging and memory) genuinely damps the overshoot, because overshoot is *caused* by the delay. Reducing the delay is real leverage.
- **Higher still (the balancing loops):** enforcing an ROIC discipline *before* the lagged financial signal arrives — i.e., importing the balancing loop earlier so it acts on the decision rather than years later — is what separates operators who overshoot from those who don't.
- **Highest (goal / paradigm):** the paradigm that "compute is the constraint and more compute always wins" is itself the driver of R1. If the binding constraint shifts to power, data quality, or monetized demand, the whole loop reorganizes. Questioning that paradigm is the highest-leverage move — and the hardest for a committed incumbent to make.

## 10. Stress-test against system response

The balancing loops *will fight back*: if a player keeps pushing capex past what returns support, ROIC compression and margin erosion are the system restoring equilibrium, not bad luck. **Backfire risk of pushing R1 harder:** you accelerate into the overshoot and own more stranded capacity when the delay-lagged correction lands. **Backfire risk of cutting too hard on an early false signal:** you starve a genuinely reinforcing flywheel and cede position to a competitor whose R1 keeps compounding — the classic danger of misreading a temporary balancing wobble as the end of growth.

**Falsifier:** if AI revenue growth durably keeps pace with installed capacity — ROIC holding or rising as capex compounds, with no digestion pause — then the balancing loops are weaker than diagnosed and R1 is closer to genuinely self-sustaining. Conversely, a sharp, industry-wide capex-growth deceleration following a period of visibly under-utilized capacity would confirm the delayed-overshoot structure.

---

### Output: Feedback-Loop Diagnosis

```
System / variable: AI compute build-out / installed capacity + capex rate
Loops: R1 capex→compute→better models→demand→revenue→capex; R2 revenue/valuation→cheap capital→capex;
       B1 capex→input scarcity (power/packaging/HBM)→cost↑→capex checked;
       B2 capex→depreciation + capacity→ROIC↓ if demand lags→discipline→capex checked;
       B3 more builders→price/capability convergence→margin↓→weaker next increment
Delays: data-center + power build-out (multi-year, critical); chip/packaging (~1yr+);
        monetization (quarters–years); ROIC signal (lagged into later statements)
Dominant loop: R1+R2 through 2024–2025 (compounding capacity, valuations, capex) — balancing loops not yet binding due to delay
Stocks: installed compute, data centers under construction, in-flight chip orders, depreciation, conviction
Flows: capex rate, capacity-energized rate, AI-revenue rate  (high flow ≠ adequate stock now, due to build delay)
Predicted behavior without intervention: overshoot-and-correct / capacity-cycle bullwhip, not smooth exponential;
        possible digestion pause before sustainable path
Leverage (Meadows): lowest = one quarter's capex figure; higher = shorten build delay + import ROIC discipline early;
        highest = question the "more compute always wins" paradigm
Intervention: pre-secure power + second-source packaging/memory (shorten delay) | System response: damps overshoot |
        Backfire risk: over-push R1 → stranded capacity; over-cut on false signal → cede flywheel to a rival
Falsifier: ROIC holds/rises as capex compounds with no digestion pause ⇒ R1 genuinely self-sustaining, diagnosis wrong
```

The AI capex boom is one of the clearest live instances of the skill's core warning: a reinforcing loop in its growth phase looks like destiny, but its balancing limits — power, packaging and memory supply, return on capital, and competitive commoditization — are real and merely *delayed*. Long build delays don't remove the balancing loops; they defer them, and deferred correction is what turns growth into overshoot. Treating the 2024–2025 trend line as an extrapolable baseline is exactly the mistake the Beer Game punishes.

*Sources: Hyperscaler capital-expenditure figures and 2026 guidance as reported in the companies' quarterly earnings releases and calls (Microsoft, Alphabet, Amazon, Meta, 2023–2025) and contemporaneous coverage in the Financial Times, Reuters, and The Wall Street Journal. Advanced-packaging (TSMC CoWoS) and high-bandwidth-memory supply constraints as reported by TSMC and in trade/industry coverage, 2024–2025. Data-center power and grid-interconnection lead times per the International Energy Agency, "Electricity 2024" and subsequent IEA data-centre analysis. Feedback-loop structure (reinforcing/balancing, delay-driven overshoot, Meadows leverage hierarchy) per Meadows (1999, 2008) and Sterman (1989, 2000); see [../references/sources.md](../references/sources.md). Specific figures are approximate and directional; exact totals vary by source and definition.*
