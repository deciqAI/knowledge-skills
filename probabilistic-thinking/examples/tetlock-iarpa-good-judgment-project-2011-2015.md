# Method in Action: Tetlock, IARPA, and the Good Judgment Project (2011–2015)

> *Example for the [probabilistic-thinking](../SKILL.md) skill.*

A worked example. Not pundit theater — peer-reviewed and US-funded.

In 2010, the **Intelligence Advanced Research Projects Activity (IARPA)**, a research arm of the U.S. Office of the Director of National Intelligence, commissioned a four-year, large-scale geopolitical forecasting tournament under its **Aggregative Contingent Estimation (ACE)** program. The objective was concrete: improve how well the U.S. intelligence community can forecast world events. Five university-led research teams competed; the winner was the **Good Judgment Project**, run by **Philip Tetlock** and **Barbara Mellers** at the University of Pennsylvania.

The project recruited several thousand volunteer forecasters and asked them to assign numerical probabilities to hundreds of specific, time-bounded geopolitical questions ("Will Greece exit the eurozone by date X?"; "Will Bashar al-Assad remain in power as of date Y?"). Forecasters could update their estimates as evidence emerged. Each forecast was scored after resolution against a strict accuracy metric (the Brier score).

The findings — published in peer-reviewed papers and synthesized in Tetlock & Gardner's 2015 book *Superforecasting* — were stark:

- **Top 2% of forecasters ("superforecasters")** beat the average forecaster by ~60% on Brier accuracy, and **outperformed intelligence community analysts with classified access by approximately 30%**, using only public information (Tetlock & Mellers, multiple papers; *Superforecasting* ch. 4).
- Superforecasters were not domain experts. They were **ordinary people** — a retired pharmacist, a software engineer, a homemaker — who had been trained on probabilistic reasoning skills.
- **The skills that distinguished them were teachable**: anchoring on base rates, decomposing questions, updating incrementally with new evidence, *avoiding* both over- and under-reaction to news, taking outside views seriously.
- A short training intervention (≈ 60 minutes) on the CHAMP method (Compare, Historical perspective, Average, Mathematics, Probability) **improved accuracy by 10%** in the average forecaster (Mellers et al., *Psychological Science*, 2014).

Walk through the Probability Estimate applied to one Good Judgment question — *"Will the Greek government default on the IMF before 2016-06-30?"* — as superforecasters approached it:

- **Question (Step 1):** Specific, time-bounded, resolution criteria unambiguous. ✓
- **Base rate (Step 2):** Historical Greek default frequencies on IMF over the prior decade; Eurozone sovereign-default frequency. Anchored around a small but non-zero number.
- **Evidence (Step 3):** Bailout-talks status, deposit flight from Greek banks, ECB liquidity stance, German political signals — each a signal in a direction with a strength.
- **Bayesian update (Step 4):** Each piece of news shifted the estimate, but typically by less than novice forecasters shifted. Superforecasters' characteristic move was *smaller updates more frequently* — they avoided both the journalistic over-reaction and the ostrich-style under-reaction.
- **Estimate (Step 5):** A point estimate with a confidence range, updated as evidence arrived. (Superforecasters typically gave probabilities like "37%" rather than "around a third.")
- **Most-informative next evidence (Step 6):** Often a specific date — IMF-payment-due dates, ECB meetings, election dates — at which a binary signal would arrive.
- **Calibration (Step 7):** Every forecast was Brier-scored after resolution. The discipline of *being scored* was itself part of what produced calibrated forecasters.

The framework's payoff is not "predict the future" — it is **producing forecasts you can be measurably wrong about**, so that you can become measurably better.

**Sources:** Tetlock, Philip E. & Gardner, Dan. ***Superforecasting: The Art and Science of Prediction***. Crown, 2015 — the primary popular account, written by the project's principal investigator. Mellers, Barbara et al. **"Psychological Strategies for Winning a Geopolitical Forecasting Tournament."** *Psychological Science*, Vol. 25, No. 5 (May 2014), pp. 1106–1115 — peer-reviewed evidence on the CHAMP training intervention. https://journals.sagepub.com/doi/10.1177/0956797614524255 . Tetlock, Philip E. ***Expert Political Judgment: How Good Is It? How Can We Know?*** Princeton, 2005; revised 2017 — the earlier, foundational work on expert prediction accuracy. IARPA Aggregative Contingent Estimation (ACE) program: https://www.iarpa.gov/research-programs/ace . Good Judgment Inc. (the post-project commercial successor) maintains active forecasting tournaments: https://goodjudgment.com .
