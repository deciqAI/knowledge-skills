# Method in Action: AI Benchmarks and Engagement Metrics as Targets (2023–2026)

> *Example for the [goodharts-law](../SKILL.md) skill.*

By the mid-2020s, Goodhart's law had become one of the most-cited frames inside the AI industry itself — because two of its own core metrics visibly decayed under optimization pressure. First, **public benchmark scores** (MMLU, GSM8K, HumanEval, and a proliferation of leaderboards) came to dominate model marketing, funding narratives, and internal go/no-go decisions — and, predictably, models began scoring well without a matching gain in real-world capability. Second, **consumer-app engagement metrics** (watch time, session length, daily active use) continued their long slide from "signal of user value" to "target that no longer measures it." This walks both cases through the skill's own six-step Process.

---

## Step 1 — State metric and goal

**Case A — AI benchmarks.**
- **Metric being targeted:** score on a fixed public benchmark (e.g., a multiple-choice knowledge test like MMLU, a grade-school math set like GSM8K, or a coding pass-rate like HumanEval).
- **Underlying goal:** general, transferable model capability — does the model actually reason, code, and generalize on tasks users bring that were *not* in the test set?
- **Current proxy–goal correlation:** initially high on a genuinely held-out test, and a legitimate research signal. It degrades as the benchmark ages, becomes a marketing target, and (critically) as the test's questions leak into training data.
- **Who is measured:** frontier and open-weight model developers; the score is read by press, investors, enterprise buyers, and internal leadership deciding what to ship.
- **Stakes:** very high — leaderboard position drives valuations, capex-justification narratives, and enterprise procurement in an intensely competitive, AI-native market.

**Case B — engagement metrics.**
- **Metric being targeted:** engagement (watch time, session length, DAU/MAU, scroll depth) feeding a recommendation or ranking system.
- **Underlying goal:** users getting durable value — time well spent, learning, connection, satisfaction they'd endorse on reflection.
- **Correlation:** engagement is a real proxy for value at low intensity, but the two diverge sharply as the system optimizes hard against engagement.
- **Who is measured:** the ranking model and the teams whose OKRs it feeds.
- **Stakes:** very high — engagement drives ad revenue and growth targets.

## Step 2 — Predict the gaming (≥3 vectors each)

**Case A — benchmarks:**
1. **Train on the test (contamination).** Benchmark questions and answers, published openly on the web, get scraped into pretraining or fine-tuning corpora — accidentally or deliberately. The model then "knows" the answers rather than deriving them. Contamination of popular benchmarks was widely documented and discussed across the research community by 2023–2024.
2. **Overfit the format.** Tune specifically to the benchmark's answer style, prompt template, or few-shot format so the score rises without broader capability gain.
3. **Cherry-pick and configure.** Report the benchmark and settings (prompt, sampling, best-of-N) that flatter the model; omit the ones that don't.
4. **Chase saturated tests.** Keep reporting benchmarks that are near-ceiling and no longer discriminate between models.

**Case B — engagement:**
1. **Amplify outrage / clickbait** — high-arousal content that maximizes watch time regardless of user benefit.
2. **Exploit autoplay and infinite scroll** to inflate session length without adding value.
3. **Surface borderline / sensational content** the ranking model learns is "sticky."
4. **Optimize notifications** to reacquire attention even when it degrades satisfaction.

If you can list only one or two, you haven't thought hard enough — both cases yield four readily.

## Step 3 — Categorize the mechanism

| Case | Dominant mechanism | Why |
|---|---|---|
| Benchmarks — contamination / teaching-to-test | **Adversarial** (with a **Causal** layer) | Developers under competitive pressure actively optimize the score; and a high benchmark score is increasingly a *symptom* correlated with capability, not a *cause* of it — once the test leaks, the score no longer moves capability. |
| Benchmarks — saturated / near-ceiling tests | **Extremal** | At the top of the range the metric–goal correlation flattens; a 1-point gain near ceiling says little about real capability. |
| Engagement | **Adversarial** + **Extremal** | The optimizer is a relentless intelligent agent; and past a threshold, more engagement stops tracking (and can invert) genuine user value. |

## Step 4 — Choose the countermeasure

- **Adversarial → multi-metric + randomized/rotating audits + rotation of the metric itself.** For benchmarks: rotate to fresh, held-out, contamination-controlled evaluations; keep some test items private; publish contamination checks. For engagement: multi-objective optimization with explicit quality and harm constraints.
- **Causal → move closer to causation + direct audit.** Evaluate on tasks that are *provably* unseen and drawn from real usage, not on a fixed leaderboard. Human preference evaluation and live, blind head-to-head comparison (as popularized by community "arena"-style rankings in 2023–2024) are harder to pre-train against than a static answer key — though they carry their own gaming risks and are not immune.
- **Extremal → paired constraint metrics.** Pair a capability score with an out-of-distribution / robustness check; pair engagement with a retention-quality or reported-satisfaction constraint.

## Step 5 — Design the system

**Case A — Goodhart-robust model evaluation:**
- **Primary metric:** performance on **private, rotating, contamination-controlled** evaluations that approximate real user tasks.
- **Constraint metric(s):** out-of-distribution / adversarial robustness; held-out task families the model was demonstrably not trained on.
- **Audit:** run contamination detection (e.g., canary strings, n-gram overlap, and held-out-vs-public score gaps); publish the methodology; sample real user tasks blind.
- **Rotation:** refresh benchmark sets on a schedule and retire saturated ones; assume any public test decays the moment it is published.
- **Separation of measure-for-control vs measure-for-diagnosis:** never let a single public leaderboard number be both the shipped-model gate *and* the marketing headline; keep an internal, private eval for go/no-go.
- **Gaming-detection threshold:** flag when public-benchmark score and private/held-out score diverge beyond a set gap.

**Case B — engagement:**
- **Primary metric:** engagement, but **capped by** a quality/harm constraint set.
- **Constraint metric(s):** reported user satisfaction, long-horizon retention quality, harm audits.
- **Audit:** sampled human review of what the ranking model is actually promoting.
- **Rotation & separation:** revisit the objective when the engagement number rises while satisfaction stalls or falls.

## Step 6 — Schedule re-evaluation

- **Independent goal measurement:** blind, real-task capability evals (Case A) and honest reported-satisfaction / well-being studies (Case B), owned by a team separate from the one whose targets the metric feeds.
- **Drift threshold:** trigger review when leaderboard gains stop tracking held-out gains, or when engagement rises without a satisfaction rise.
- **Retirement criteria:** retire any benchmark once contamination is detected or it saturates near ceiling.
- **Owner:** an evaluation/trust function with authority independent of the shipping and growth orgs.

---

## The lesson

Both cases are the same structure as Goodhart's original 1975 M3 collapse: a correlation that was real *before* it carried control weight, then decayed *because* it carried control weight. A published benchmark is a target the whole industry can optimize against — and, uniquely, one whose answer key can end up inside the very system being tested. The durable defenses are the skill's own: **multi-metric, private/rotating held-out evaluation, contamination audits, and separating the number you use to decide from the number you use to sell.**

*Sources: Goodhart, C. A. E. (1975), "Problems of monetary management: The U.K. experience," Reserve Bank of Australia (repr. 1984). Strathern, M. (1997), "'Improving ratings': Audit in the British university system," European Review 5(3). Manheim, D., & Garrabrant, S. (2018), "Categorizing variants of Goodhart's Law," arXiv:1803.04585. On benchmark contamination and the limits of static leaderboards, see the widely reported 2023–2024 discussion in the ML research community around data contamination of public benchmarks (e.g., MMLU/GSM8K/HumanEval) and the rise of community human-preference "arena"-style evaluations as a harder-to-game complement; and Frances Haugen / "Facebook Files" (2021, Wall Street Journal) documenting internally-known harms of engagement optimization. Specific figures are omitted where exact public values were not confirmable.*
