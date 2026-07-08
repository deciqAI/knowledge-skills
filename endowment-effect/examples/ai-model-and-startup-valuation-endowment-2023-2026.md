# Method in Action: The In-House Model Trap and Founder Valuation in the AI Cycle (2023–2026)

> *Example for the [endowment-effect](../SKILL.md) skill.*

The 2023–2026 generative-AI boom created two textbook endowment-effect situations that recurred across the industry:

1. **The in-house model trap.** Engineering teams that had trained their own model, curated their own dataset, or written their own inference/orchestration codebase systematically resisted switching to a stronger external foundation model — even when the external option was cheaper, more capable, and faster to ship on. They coded "abandoning what we built" as a loss.
2. **Founder valuation inflation.** As the funding cycle cooled from its 2021 peak and a wave of AI acquisitions, "acqui-hires," and quiet wind-downs occurred through 2023–2025, many founders anchored on the valuation they had internalized as *theirs* — often the last private round's paper mark — while acquirers and the public markets modeled from current fundamentals.

Both are the same bias running in two arenas: ownership inflates subjective value, and giving up the owned thing registers as a ~2× loss. Below, both are walked through this skill's Process.

---

## Case A — The in-house model / dataset / codebase

### S1 — Ownership
- **Who owns it:** an internal ML/engineering team.
- **What:** a self-trained model (or fine-tune), a hand-curated proprietary dataset, and a bespoke inference/orchestration stack.
- **How long:** typically 12–36 months of accumulated work by 2024–2025.
- **Customization level:** very high. The team built it, tuned it, and shaped their identity around it. High customization is precisely the condition under which the endowment effect (and its "IKEA effect" variant — valuing what you assembled yourself) is strongest.

### S2 — Gap
- **Owner's value:** "our model is a core asset / our moat."
- **Market reference:** by 2024–2025, leading external foundation models were widely reported to match or exceed most in-house models on general capability, and per-token API prices for frontier-class models fell sharply over the period as competition intensified.
- **Gap:** the team's internal valuation of "our model as differentiator" often exceeded the market reality that the same or better capability was purchasable off-the-shelf.
- **External comps:** public model benchmarks and rapidly falling API pricing provided an unusually *salient* neutral reference — which, per the theory, is exactly what weakens the endowment effect once you actually look at it.

### S3 — Attribute the gap
- **Info asymmetry portion:** real but limited — the team genuinely knew their domain data and edge cases better than an external vendor.
- **Legitimate-feature portion:** real in narrow cases — privacy/data-residency constraints, latency, or a truly proprietary dataset can justify keeping in-house work.
- **Endowment portion:** large. "We built it, so it must be worth keeping" is the IKEA-effect rationalization listed in this skill's own Common Rationalizations table.
- **Loss-framing language:** watch for "we'd be throwing away two years of work" (sunk cost + endowment) and "we can't just depend on a vendor."

### S4 — Direction: **Counteract**
The decision here is to *counteract* the team's own endowment, not to leverage a buyer's. The neutral-reference move: evaluate the in-house asset **as if it were being acquired today**. Ask the test question from the skill: *would you pay to build this from scratch right now, given current external options — or would you buy the external model?* Reframe from "keep vs. kill our model" (loss framing) to "which capability, in-house or external, best serves the roadmap" (exchange framing).

### S5 — Bridge
- **Reference anchor:** put current public benchmarks and current API prices on the table before the "build vs. buy" debate, not after.
- **Structural bridge:** rather than a binary keep/kill, adopt a hybrid — external foundation model for general capability, in-house effort reserved only for the genuinely proprietary layer (your data, your fine-tune, your domain evals). This converts "giving up our model" into "redeploying our best work where it uniquely wins."
- **Framing:** frame retained in-house work as *chosen* differentiation, not as *defended* endowment.

### S6 — Close
- Endowment premium isolated from the genuine info-asymmetry and constraint-driven reasons to stay in-house. ✅
- Bridge (hybrid architecture) tested against the team's real loss threshold — they keep ownership of the layer that actually differentiates. ✅
- Ethical/quality check: decision driven by roadmap value, not by attachment. ✅

---

## Case B — Founder valuation in M&A / wind-down talks

### S1 — Ownership
- **Who owns it:** the founder(s).
- **What:** the company they built — team, product, IP.
- **How long:** often several years.
- **Customization level:** maximal. Nothing triggers the endowment effect more than something you created and identify with.

### S2 — Gap
- **Owner's value:** frequently anchored to the last private round's post-money valuation — a paper mark set in a different (often 2021-era) market.
- **Market reference:** acquirer models and, for later-stage comparables, public-market multiples — which compressed materially from the 2021 peak.
- **Gap:** the founder's asking value often sat well above the acquirer's model — illustratively on the order of 2–3× — in the same direction as the ~2× endowment ratio this skill documents (real-world M&A gaps are widened further by stale paper marks and market compression, so they can run above the lab figure).

### S3 — Attribute the gap
- **Info asymmetry:** the founder genuinely knows the pipeline and roadmap better — real, but rarely explains a 2–3× gap.
- **Legitimate portion:** disagreement about growth trajectory is legitimate and is exactly what an earnout is built to resolve.
- **Endowment portion:** large. "The buyer just doesn't understand the value" and "I've put too much into this to sell for that" are both in the skill's rationalization table.

### S4 — Direction: **Counteract**
Introduce a neutral reference — recent comparable-transaction multiples and current public multiples — *before* the founder states a number, to reduce self-anchoring on the stale paper mark.

### S5 — Bridge
- **Reference anchor:** current comparable M&A multiples, not the last round.
- **Earnout:** tie a portion of consideration to post-close performance. If the company performs as the founder believes, the earnout pays their number; if not, the acquirer paid market value. This is the canonical structural bridge for founder endowment.
- **Framing:** convert "I'm giving up my company for less than it's worth" into "I receive full value *if* it performs as I expect."

### S6 — Close
- Endowment premium separated from legitimate trajectory disagreement. ✅
- Earnout bridge tested against the founder's loss threshold. ✅
- Where no bridge closes the gap, the honest read is that the residual is endowment, not a market error. ✅

---

## The one-line takeaway

In both arenas the failure mode is identical: *we built it, so it must be worth more than the market says.* The fix is identical too — put the salient neutral reference (benchmarks and API prices; comparable multiples) on the table early, and use a structural bridge (hybrid architecture; earnout) instead of arguing about the number. The endowment effect is weakest exactly when a live, credible reference price is visible — so make it visible first.

*Sources: Kahneman, Knetsch & Thaler (1990), "Experimental Tests of the Endowment Effect and the Coase Theorem," Journal of Political Economy 98(6) — the 2× owner/non-owner ratio and the neutral-reference-price condition. Thaler (1980), "Toward a Positive Theory of Consumer Choice," JEBO 1(1) — the endowment effect and the build/own attachment. The 2023–2026 dynamics (falling foundation-model API prices, in-house vs. external "build vs. buy" pressure, the funding-market reset from the 2021 peak, and the wave of AI acquisitions/acqui-hires/wind-downs) are widely and durably reported industry trends; specific figures are omitted here in favor of the direction of the trend, which is well documented across mainstream technology and financial press through early 2026.*
