# Method in Action: The AI Demo-Dopamine Trap — Chasing the Launch Over the Moat (2023–2026)

> *Example for the [hyperbolic-discounting](../SKILL.md) skill.*

The generative-AI boom that began with ChatGPT's late-2022 release created a textbook present-bias environment. A demo that goes viral delivers an *immediate* reward — sign-ups, press, a term sheet, an internal round of applause — while the payoff of durable engineering (rigorous evaluations, reliability infrastructure, data moats, unit-economics discipline) is *delayed* and uncertain. Teams that reliably said they valued long-term defensibility repeatedly chose the fast demo when the moment arrived. That gap between the patient plan and the impatient choice is hyperbolic discounting operating at organizational scale.

This walks the pattern through the skill's own Process. It is a *composite* pattern observed across many companies through the 2023–2025 AI cycle (and continuing into 2026), not a claim about any single named firm.

---

**Step 1 — Identify the reversal.**

- *Intended behavior:* "We'll build a defensible product — proprietary data, hard evals, reliable infra, sound unit economics."
- *Actual behavior:* ship the next demo/model wrapper, chase the launch spike, defer the durable work to "after this round / after this launch."
- *Repetition count:* the deferral repeats every hype cycle — each new model release restarts the "just ship the demo now" impulse.
- *Cost of the gap:* thin wrappers with no moat get compressed the moment a foundation-model vendor ships the same capability natively; reliability debt surfaces as churn and enterprise deals that stall at the pilot stage.

**Step 2 — Map the asymmetry.**

| | Desired (build durable moat) | Undesired (chase the demo) |
|---|---|---|
| Immediate cost | High — slow, unglamorous eval/infra work, no viral moment | Low — a weekend demo can trend |
| Immediate benefit | Low/invisible now | High — attention, sign-ups, fundraising momentum, dopamine |
| Delayed benefit | High — retention, defensibility, pricing power | Low — the spike decays |
| Delayed cost | Low | High — commoditization, churn, "AI feature" absorbed by the platform |

The structure is identical to the gym-membership and retirement-savings cases: the undesired path front-loads reward and back-loads cost, so the present-biased self takes it.

**Step 3 — Diagnose β.**

Unaided success rate is low. The environment supplies maximal near-term reward (funding was abundant and demos were the currency of the era), which is exactly the condition that drives β down and makes internal correction unlikely (β well below 1). When the reward for the impatient choice is this large and this immediate, willpower ("we'll be disciplined this time") is not a reliable corrective — a commitment device is required.

**Step 4 — Choose the device.**

Bind the impatient self at the moment of temptation (the next launch decision):

- A pre-committed **eval gate**: no ship without passing a fixed, written reliability/eval bar — decided *before* the demo exists, when the patient self is in charge.
- A **moat memo requirement**: any new build must state, in writing, what is defensible after a foundation-model vendor ships the same feature; reviewed by someone outside the launch team.
- **Metric pre-registration**: commit in advance to judging the launch on retention and unit economics at 30/60/90 days, not on launch-day sign-up count.

Each satisfies the criteria: binds at the temptation moment, hard to circumvent (external reviewer / written pre-registration), and acceptable to the present-self when chosen calmly ahead of time.

**Step 5 — Install with defaults.**

- Make "durable work is scheduled and protected" the default — reserve engineering capacity for evals/infra *by default*, requiring an explicit opt-out to reallocate it to the next demo.
- Add friction to the undesired path: a launch requires the moat memo and a passing eval gate before it can go out.
- Remove friction from the desired path: standing eval harness, reusable reliability tooling, so the durable work is the path of least resistance.
- Public accountability: the metric pre-registration is shared with the board/investors, so the 90-day judgment is on record.

**Step 6 — Re-check.**

At 30/60/90 days, ask: did the eval gate actually block anything, or was it waved through? Did the moat memo change any decision? If the device was circumvented, it was too weak — re-install a harder gate (e.g., an external reviewer with veto). If retention and unit economics justify the demo-first choices, that is a *revealed preference* worth respecting, not present bias — Step 2 of the skill's fit-check.

---

**Why this is present bias and not a rational update.** The skill warns against firing when a changed plan reflects genuine new information. Choosing speed *is* rational when a real land-grab window exists and being first is defensible. The tell for present bias is the *reversal*: the same team that planned for defensibility abandons it for the near-term spike every cycle, and the deferred durable work never arrives — the repetition, not any single fast decision, is the diagnostic.

The macro backdrop reinforced the incentive. AI infrastructure and capital spending surged across 2023–2025, with the largest US technology companies collectively raising capital-expenditure guidance into the hundreds of billions of dollars annually, and private-market AI valuations reaching levels that widely prompted "bubble" comparisons in mainstream financial commentary by 2024–2025. Abundant, fast capital rewards the demo; it does not, by itself, reward the moat. That is precisely the choice architecture in which a commitment device — not willpower — is the reliable fix.

*Sources: Laibson, D. (1997), "Golden eggs and hyperbolic discounting," Quarterly Journal of Economics 112(2), 443-477 (β-δ present-bias framework). O'Donoghue, T. & Rabin, M. (1999), "Doing it now or later," American Economic Review 89(1), 103-124 (naïve vs sophisticated discounters). On the 2023–2026 AI capex and valuation backdrop, see widely reported quarterly earnings and capital-expenditure disclosures from major US technology firms and contemporaneous coverage in the Financial Times, The Economist, and The Wall Street Journal (2023–2025); figures here are stated in qualified terms because exact totals vary by source and reporting period.*
