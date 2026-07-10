# Method in Action: The AI Hot Streak — Viral Quarters, Fund Streaks, and Benchmark Spikes (2023–2026)

> *Example for the [regression-to-the-mean](../SKILL.md) skill.*

Between 2023 and 2026, the generative-AI boom produced a steady stream of extreme single-period observations: an app that went viral in one quarter, a venture fund riding a hot streak, a model that spiked to the top of one benchmark leaderboard. The temptation in each case is identical — extrapolate the outlier run into a permanent trend and act on it (raise at the peak valuation, pour capital into the "proven" fund, declare a model the new state of the art). Regression to the mean is the default explanation the excitement crowds out.

This example walks the AI hot-streak pattern through the skill's six Process steps. Rather than lean on one fragile figure, it treats three recurring, well-documented AI-era patterns as instances of the same statistical structure.

## 1. Identify the extreme observation

Three archetypal extreme observations from the 2023–2026 window:

- **The viral quarter.** A consumer AI app posts an explosive stretch — ChatGPT's launch in late 2022 famously reached an enormous user base faster than prior consumer software, and a wave of AI-wrapper apps subsequently posted breakout months of downloads and revenue. The extreme value is a single period (a quarter, a launch window) of growth or engagement far above the app's own baseline.
- **The fund's hot streak.** A venture or hedge fund posts a standout period of returns during the AI run-up, often concentrated in a handful of AI bets. The extreme value is one fund's short-window performance ranking near the top of its peer set.
- **The benchmark spike.** A newly released model tops a specific leaderboard — a coding benchmark, a math eval, a chatbot arena — by a notable margin at release. The extreme value is one score on one benchmark at one point in time.

In all three, the subject is a noisy performer, the value is extreme relative to its own history and its peers, and the "intervention" that observers want to credit is some narrative of durable superiority: better product, better fund, better model.

## 2. Identify the retest

The retest is simply the next comparable measurement period:

- **Viral app → next quarter's retention and growth.** Many breakout AI apps saw growth decelerate and retention settle well below launch-window peaks as novelty faded — a widely observed pattern for consumer apps generally, and repeatedly reported for AI-wrapper products in 2023–2025.
- **Hot fund → next period's returns.** The fund's subsequent-period performance, and its ranking relative to peers.
- **Spiking model → the next benchmark, or the same benchmark once competitors respond.** Across the 2023–2025 window, frontier leaderboards changed hands frequently; a model at the top at release was often surpassed within months, and margins on any single eval tended to compress as rivals shipped.

In each case, the retest tends to land closer to the relevant average than the extreme observation did. That directional move toward the mean is exactly what the skill predicts.

## 3. Estimate expected regression

The skill's rule of thumb: `regression ≈ (1 − reliability) × distance from mean`. The lower the reliability (the higher the noise share) of a single-period measurement, the more regression to expect.

- **Viral quarter:** low reliability. A launch quarter is dominated by one-time novelty, press cycles, and curiosity traffic — a large transient noise component. Distance from the app's own steady-state baseline is huge. Expected regression is large: most of the launch spike should be presumed non-repeating until proven otherwise.
- **Fund hot streak:** short-window fund returns are notoriously low-reliability signals. A few concentrated bets in one hot sector inflate a short-window number; the skill's `stock fund` row in the Pack table flags exactly this — a hot year regularly underperforms the next. Expected regression is substantial.
- **Benchmark spike:** a single eval is a noisy proxy for general capability — vulnerable to benchmark-specific tuning, prompt sensitivity, and (documented in the period) train/test contamination concerns. Expected regression on *that specific number*, and on the ranking, is meaningful.

The honest move is to state the expected regression *before* crediting any durable-superiority story.

## 4. Compare to control

The control question: how did comparable, untreated peers move over the same window?

- If **most** breakout consumer apps decelerate after a launch quarter, then a given AI app's deceleration is the baseline, not evidence its product "cooled off" for idiosyncratic reasons.
- If **most** top-decile funds in one period fail to stay top-decile the next, then a hot AI fund reverting is the peer baseline, not proof the manager lost their touch.
- If **most** benchmark leaders get surpassed within months as competitors ship, then one model losing its #1 spot is the field baseline, not a sign it "got worse."

Intervention effect = the subject's change minus the peer-group change. In the AI hot-streak cases, once you subtract the peer-group regression baseline, the residual "durable edge" is usually far smaller than the launch-day narrative implied — and sometimes indistinguishable from zero.

## 5. Calibrate the causal claim

Now separate signal from noise for each:

- **Viral quarter:** How much of the launch spike exceeds what pure novelty-driven regression predicts? The durable signal is *retained* users and *repeat* revenue after novelty decays — not the peak. Calibrate the valuation and the growth trend to the post-decay baseline, with wide confidence bands.
- **Fund hot streak:** Does the fund's edge persist across multiple periods and diversified bets, or is it one hot sector in one window? A durable edge shows up over a multi-year track record (the skill's prescribed `5-year track record`), not one AI-fueled quarter.
- **Benchmark spike:** Does the model lead across many independent evals and real user tasks, or spike on one? A durable capability signal is broad, replicated superiority — not a single leaderboard peak that inverts when the next model ships.

In every case, the calibrated claim is narrower than the hype: "extreme single-period observation, expect reversion toward the mean, durable edge unproven pending multi-period / multi-benchmark confirmation."

## 6. Adjust action

- **Do not extrapolate the outlier run into a permanent trend.** Model the app's trajectory off its post-novelty baseline, not its launch spike, before committing capital or headcount at a peak valuation.
- **Credit the fund's "skill" only across a long window and diversified bets** — not one hot AI quarter. Chasing last period's top fund is a documented way to buy the peak and hold through the reversion.
- **Judge models on broad, replicated, contamination-resistant evaluation and real-task performance**, not one leaderboard number at release. Treat a single benchmark spike as a hypothesis, not a coronation.
- **Build the control in upfront.** For any AI bet justified by a breakout number, write down the peer-group baseline and the expected regression *first*, then invest only in the residual edge that survives.

The 2023–2026 AI cycle did not repeal statistics. Viral quarters, hot streaks, and benchmark spikes are, structurally, the flight instructor's cadet who nailed one maneuver: praise the peak all you like — the next attempt still regresses. The discipline is to size your commitment to the durable signal, not the noise-inflated extreme.

*Sources: Kahneman, D. (2011), *Thinking, Fast and Slow*, Ch. 17 (regression to the mean; the framework applied here). Galton, F. (1886), "Regression towards Mediocrity in Hereditary Stature," *Journal of the Anthropological Institute*, 15, 246–263 (origin of the concept). On the AI-era patterns: ChatGPT's rapid post-launch user growth was widely reported (e.g., Reuters/UBS coverage, early 2023); the frequent turnover of frontier-model benchmark leaders and concerns about benchmark contamination/overfitting were widely documented across 2023–2025 (e.g., LMSYS Chatbot Arena leaderboard dynamics; academic work on benchmark data contamination). Consumer-app novelty decay and the non-persistence of short-window fund performance are long-established, well-documented general patterns (see SPIVA persistence studies). Specific figures for individual apps/funds/models are deliberately omitted where they cannot be verified precisely.*
