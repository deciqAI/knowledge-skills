# Method in Action: Where the AI Race Is Zero-Sum and Where It Isn't (2024–2026)

> *Example for the [zero-sum-game](../SKILL.md) skill.*

By 2024–2026 the dominant framing of the AI boom was a single "race" — one leaderboard, one winner, everyone else loses. That framing quietly bundles together resources with very different structures. Some inputs to AI are genuinely fixed in the near term and therefore zero-sum; the output — AI-driven productivity — is not. Treating the whole thing as one zero-sum contest is exactly the diagnosis error this skill is built to catch: it pushes firms toward pure capture (outbid rivals, hoard talent, block competitors) when part of the game rewards expansion (build the market, enlarge supply, complement rather than substitute).

The point of the diagnosis is that "the AI race" is not one game — it is a **mixed** game, and you have to name the resource before you know which move applies.

Running the Diagnosis:

**Step 1 (define the contested resource).** Split "AI competition" into its distinct contested resources rather than treating it as one blob:
- *Near-term advanced-chip and high-bandwidth-memory (HBM) supply* — the units of leading-edge accelerators and the HBM stacks they require, buildable only through a small number of suppliers with long lead times.
- *Top-tier AI research talent* — the small pool of people who have actually trained frontier systems.
- *AI-driven productivity / the value AI creates for end users* — the output the whole boom is ostensibly about.

Each is a nameable, distinct unit. That is the precondition for a real diagnosis; "who wins AI" is not a resource.

**Step 2 (test fixity) — run separately per resource:**
- *Chips/HBM, near term:* **fixed.** Leading-edge fabrication and advanced-memory capacity cannot be expanded on a quarterly horizon — it is gated by a handful of suppliers and multi-year fab and packaging build-outs. Within a given year, one buyer's allocation is largely another's shortfall. **Zero-sum (near term).**
- *Top talent, near term:* **fixed.** The pool of people who have led frontier training runs is small and slow to grow. A senior hire at one lab is, for that cycle, a hire the rival did not get. **Zero-sum (near term).**
- *AI productivity / end-user value:* **not fixed.** Cooperation and innovation expand it — better models, cheaper inference, and new applications enlarge total value created rather than merely reallocating it. One firm shipping a useful AI product does not consume the possibility of another firm shipping one. **Non-zero-sum.**
- *Time dimension:* the fixity of chips and talent is a **near-term** property. Over a multi-year horizon, supply responds — new fab and advanced-packaging capacity comes online and the trained-talent pool grows — so even these resources become less zero-sum the longer the horizon.

**Step 3 (check for zero-sum bias).** The popular "one race, one winner" frame shows all three bias markers on the *productivity* dimension:
- *Countability:* leaderboard ranks, benchmark scores, model-release dates, and capex figures are countable and salient, so attention anchors on the visibly rankable inputs and treats the diffuse, expandable productivity pie as if it were another leaderboard.
- *Relative-position anchoring:* "we must be #1 or we lose" fixates on rank rather than on absolute value created — a firm can rank second and still capture a growing absolute business if the pie is expanding.
- *Comparative-advantage blindness:* the frame ignores that different players can specialize (chips, cloud, foundation models, applications, tooling) and gain jointly, treating any rival's success as one's own loss.

So the diagnosis splits: **bias is present on the productivity dimension, absent on the chip and talent dimensions** — those really are fixed near-term.

**Step 4 (confirmed-zero-sum branch → minimax) for chips and talent, near term.** Where the resource is genuinely fixed, capture logic is correct, not a bias. For scarce near-term compute the rational move is to secure allocation against the worst case — long-term supply commitments, pre-purchase and reserved capacity, supplier diversification, and vertical moves toward custom silicon so a rival's buying spree cannot starve you. For scarce talent, competitive retention and acquisition are appropriate. This is the minimax posture: choose the strategy that protects your floor against a rival who is trying to lock up the same fixed pool. Cooperation here does not create a bigger pool this year, so "let's not compete" would be a strategic error on this dimension.

**Step 5 (confirmed-non-zero-sum branch → design for surplus) for the productivity pie.** On the output dimension the correct move is expansion, not capture. The surplus is the value AI creates that no single firm captures under pure rivalry — new categories of application, workflows automated, users served. The **mechanisms** to capture it are concrete and already visible in this period: open ecosystems and platforms (API access, model marketplaces, developer tooling), interoperability and shared standards, and complement strategies (a cloud provider and a model lab enlarging each other's markets rather than only fighting for rank). *Stop-rule check:* this is not wishful cooperation talk — the pie-growth mechanism is nameable (falling inference cost and new applications enlarging total AI usage), so the non-zero-sum diagnosis holds rather than reverting to capture.

**Step 6 (state the time horizon).** State both frames explicitly. *Near term:* chips/HBM and top talent are fixed → zero-sum → capture and minimax are correct on those inputs. *Longer term:* supply and the talent pool respond, and the productivity pie keeps growing → the game shifts toward non-zero-sum → the firms that also invested in market-expanding, complement-building strategy win the larger absolute prize. Mistaking the near-term fixed inputs for a permanently fixed *whole* is the error: it justifies burning resources purely to deny rivals while under-investing in the expansion that determines the long-run size of the business.

The mapped steps:
1. Contested resource: split into near-term chips/HBM, top talent, and AI productivity — three different units, not one "race"
2. Fixity test: chips fixed (near term), talent fixed (near term), productivity not fixed; all soften over a longer horizon
3. Bias audit: countability, relative-position, and comparative-advantage blindness all present on the productivity dimension; absent on the fixed-input dimensions
4. Zero-sum branch: secure fixed compute and talent via supply commitments and retention — minimax capture is correct there
5. Non-zero-sum branch: expand the productivity pie via platforms, interoperability, and complement strategies — surplus with a named mechanism
6. Horizon: zero-sum near term on inputs, non-zero-sum longer term and on output — state both, and don't let the first justify neglecting the second

**Diagnosis: Mixed** — genuinely zero-sum on near-term compute and talent, non-zero-sum on the AI-productivity pie. The strategic failure mode of the era is applying a single frame to a mixed game.

*Sources: Von Neumann, J. & Morgenstern, O. (1944), Theory of Games and Economic Behavior, Princeton University Press (definition of zero-sum games and the minimax result); Meegan, D.V. (2010), "Zero-Sum Bias: Perceived Competition Despite Unlimited Resources," Frontiers in Psychology, 1:191 (empirical basis for zero-sum bias). The 2024–2026 characterization of constrained leading-edge AI accelerator and high-bandwidth-memory supply, and of a small frontier-talent pool, reflects widely reported industry conditions during that period; specific allocation figures are omitted deliberately.*
