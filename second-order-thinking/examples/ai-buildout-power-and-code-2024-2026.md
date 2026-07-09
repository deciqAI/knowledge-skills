# Method in Action: The AI Buildout — from Capex to the Grid, and from Coding Assistants to Maintenance (2024–2026)

> *Example for the [second-order-thinking](../SKILL.md) skill.*

A worked example in a live, unresolved domain: **technology capex and adoption**. Where Prohibition and Hanoi are closed cases with a known ending, this cascade is still running as of early 2026 — which makes the stop-rule and confidence-decay discipline (steps 3 and 7) load-bearing rather than decorative. Two parallel cascades are traced from one root: (A) AI compute buildout → electricity, and (B) AI coding assistants → the software they help ship.

---

## Cascade A: AI capex → electricity demand → the grid

**1. The decision and its first-order effect.** Through 2024–2025, the major cloud and AI companies committed to a historically large capital-expenditure program: building and filling data centers with AI accelerators to train and serve large models. The first-order, consensus effect is exactly what the buildout is for — more compute capacity, faster model training and inference, and the ability to serve a rapidly growing base of AI users. This part is not controversial; it was the announced goal, and reported aggregate hyperscaler capex rose steeply year over year.

**2. "And then what?" (second order — the actor response).** Compute is not free of physics: accelerators draw power and reject heat. As the fleet grows, data-center electricity demand rises. After roughly a decade of flat U.S. electricity demand, forecasters and grid operators began revising load projections upward, attributing a meaningful share of the new growth to data centers (alongside electrification and manufacturing). The actor here is concrete: utilities and grid operators re-plan capacity around large new interconnection requests, and data-center operators race to secure power.

**3. Continue to third+ order.** Power is a constrained, slow-to-build resource, so the next hop is competition and siting. When large new loads concentrate in particular regions, they compete with existing users for generation and transmission that take years to build. Reported consequences by early 2026 include: multi-year interconnection queues and delayed hookups; operators signing deals directly with generators (including reported interest in nuclear, gas, and restarting or life-extending existing plants) to secure firm power; and rising local political friction over new data-center siting, water use for cooling, and who pays for grid upgrades. Wholesale power prices and capacity-market prices rose in several markets, with data-center demand cited as one contributing factor. **Stop-point: order four.** Whether these costs land on residential ratepayers versus data-center operators, and the net effect on consumer electricity bills, was an open and contested question as of this writing and depends on regulatory decisions not yet made — beyond here the chain becomes forecast, not record.

**4. Sweep all groups, and later in time.** The *builders* (AI/cloud firms) get compute but inherit a new binding constraint — power availability and cost — that some did not price into their original site plans. *Utilities and grid operators* get load growth (revenue) but also planning risk if forecasts overshoot. *Existing ratepayers and local communities* near new sites bear congestion, potential rate pressure, and land/water/noise externalities they did not choose. *Generators* — including nuclear and gas owners — gain a large new creditworthy customer. Later in time: if AI demand growth slows after utilities have committed to long-lived generation and transmission, the stranded-asset risk falls on utilities and ratepayers, not on the AI firms that triggered the buildout.

**5. Reversal check — the payoff.** The first-order framing is "buildout → abundant cheap compute." A second-order reversal for at least one group: **for the AI firms themselves, power became a bottleneck that partly reverses the "just add GPUs" plan** — some capacity sat or risked sitting idle waiting for interconnection, so the constraint moved from chips to electrons. A second reversal candidate: the buildout intended to serve the public with AI can raise the public's electricity costs and slow their local grid, i.e., a benefit to users routed through a cost to the same people as ratepayers. Whether this reversal is *load-bearing* depends on the ratepayer-allocation question in step 3, which is unresolved — so it is flagged, not asserted.

**6. Consensus vs. non-consensus.** By early 2026 the "AI needs a lot of power" observation was itself becoming consensus — so simply repeating it carries no edge (the obvious is priced in). The non-consensus, still-contested questions are the *reversals and second-order allocations*: does power turn out to be the real ceiling on AI scaling; who ultimately pays for the grid; and does demand hold long enough to justify the generation being committed. That is where the analytical premium lives.

**7. Stop-rule and humility.** Grounded through order three on widely reported facts (rising capex, upward load-forecast revisions, interconnection delays, direct power-procurement deals, local siting fights). Order four (final incidence of costs, price effects, stranded-asset risk) is genuinely uncertain and depends on decisions not yet made as of this writing (early 2026) — treated as scenario, not prediction. Confidence decays sharply after order three.

---

## Cascade B: AI coding assistants → more code shipped → more to maintain and secure

**1. First-order effect.** AI coding assistants (chat-based and IDE-integrated) were adopted widely by developers across 2023–2025. The first-order, consensus effect: individual coding tasks get faster — boilerplate, scaffolding, tests, and routine functions are produced with far less typing. Surveyed developer adoption of AI tools rose to a large majority by 2024–2025.

**2. Second order (actor response).** Faster generation lowers the marginal cost of *producing* code. Rational teams respond by shipping more code and attempting more changes per unit time. But code is a liability as much as an asset: every line shipped must be read, reviewed, maintained, secured, and eventually changed. So more code produced means more code to *own*.

**3. Third+ order.** Two documented pressures emerge. (a) **Review and maintenance surface:** the bottleneck shifts from writing to reviewing and integrating; reviewers must vet more, sometimes unfamiliar, generated code. (b) **Security and correctness surface:** studies and practitioner reports have found AI-generated code can reproduce insecure patterns or subtly wrong logic, and that developers sometimes over-trust plausible-looking output. Larger volume × constant defect-rate = more absolute defects and a larger attack surface, plus supply-chain risks from AI-suggested or hallucinated dependencies. **Stop-point: order three** — net long-run effect on total system quality is still being measured and is confounded by tooling improvements.

**4. Sweep all groups, and later in time.** *Individual developers* feel faster now. *Reviewers and senior engineers* absorb the shifted load. *Security teams* inherit a larger surface. *The organization*, later in time, carries the maintenance and technical-debt tail of a larger codebase written partly by a tool the original author did not fully scrutinize. Users bear any escaped defects.

**5. Reversal check.** First-order: "assistants make us faster." Reversal candidate: **if the added review, debugging, and maintenance burden grows faster than the writing time saved, net delivery velocity can fall even as typing speed rises** — the classic "optimization moves the bottleneck" pattern. Whether this reversal dominates is team- and task-dependent and not settled; flagged, not asserted.

**6. Consensus check.** "AI makes coding faster" is the consensus first-level take. The second-order insight the crowd underweights: *writing was rarely the bottleneck; understanding, reviewing, and maintaining were.* An intervention that accelerates the cheap step and enlarges the expensive step can net out worse — so measure end-to-end delivery and defect escape, not keystrokes saved.

**7. Stop-rule.** Grounded through order three on reported adoption levels and documented security/review concerns. The net productivity verdict is genuinely unsettled as of early 2026; stop before claiming a system-wide sign.

---

## The mapped steps (both cascades)

1. **Decision + first-order effect:** (A) AI capex → more compute; (B) coding assistants → faster code production — consensus, correct in isolation.
2. **Second order (actor response):** (A) rising data-center electricity demand → utilities re-plan; (B) lower cost of producing code → teams ship more code to own.
3. **Third+ order (equilibrium):** (A) power competition, interconnection queues, direct generation deals, siting politics; (B) shifted bottleneck to review + enlarged security/maintenance surface.
4. **All-groups sweep:** (A) builders, utilities, ratepayers, communities, generators — with later-in-time stranded-asset risk; (B) developers, reviewers, security teams, the org's future maintenance tail, end users.
5. **Reversal:** (A) power becomes the ceiling on "just add GPUs," and user benefit can route through ratepayer cost; (B) accelerating the cheap step (writing) can enlarge the expensive step (review/maintenance) and net-slow delivery ← the payoff, both flagged as load-bearing-only-if the unresolved allocation/velocity questions resolve that way.
6. **Consensus check:** "AI needs power" and "AI speeds coding" are now consensus and priced in; the edge is in the second-order allocations and reversals the crowd skips.
7. **Stop-rule:** both grounded to order three; order four is scenario, not prediction; confidence decays by hop.

*Sources: International Energy Agency, *Electricity 2024* and subsequent electricity/data-center analyses (iea.org) on data-center electricity demand growth; U.S. Energy Information Administration electricity data and outlooks (eia.gov) on U.S. load growth after a flat decade; Stack Overflow Developer Survey 2024 (survey.stackoverflow.co) on majority developer adoption of AI tools; GitHub research and blog posts on Copilot usage and productivity (github.blog); and widely reported 2024–2025 coverage of hyperscaler AI capex, data-center power-procurement deals, interconnection delays, and local siting disputes. Figures are directional and reported as of early 2026; final cost incidence and net-productivity effects were unresolved at the time of writing.*
