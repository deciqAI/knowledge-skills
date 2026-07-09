# Method in Action: The AI-Era Commons — Open Web, Power, and GPUs (2024–2026)

> *Example for the [tragedy-of-the-commons](../SKILL.md) skill.*

The generative-AI build-out that accelerated through 2024–2025 (and continued into 2026) put three shared resources under simultaneous strain, each closely fitting Hardin's structure: the **open web** (published human content, scraped at scale to train models), **shared electrical grid and power capacity** (drawn on by rapidly growing data centers), and **frontier GPUs / accelerator supply** (a rivalrous input every AI lab competes for). In each, rational individual extraction degrades a resource whose cost of depletion is spread across everyone. This example walks all three through the skill's process, because they illustrate three different Ostrom-audit failure profiles.

**Step 1 — Identify.**

- *Open web.* Shared resource: the corpus of freely published human writing, images, and code. User community: AI labs and crawler operators (extractors) plus the publishers, forums, open-source maintainers, and individual creators who supply the content. Failure mode: the incentive to publish openly erodes as creators see their work absorbed into models that compete with or bypass them, so they paywall, add "no-AI" terms, or stop publishing — degrading the very commons the models depend on. Current rules: `robots.txt` (a voluntary, unenforceable convention from the 1990s), site terms of service, and a wave of crawler-blocking tools and licensing deals negotiated site-by-site.
- *Power/grid.* Shared resource: finite electricity generation and transmission capacity on regional grids. User community: hyperscale data-center operators, other industrial users, and residential ratepayers. Failure mode: concentrated new demand strains interconnection queues and can push costs onto other users. Current rules: utility interconnection processes, tariffs, and grid-operator (e.g., ISO/RTO) planning.
- *GPUs.* Shared resource: the constrained supply of advanced AI accelerators and the leading-edge fab capacity that makes them. User community: AI labs, cloud providers, enterprises, and researchers. Failure mode: supply concentrates with the largest buyers; smaller labs and academics are priced or crowded out. Current rules: vendor allocation, cloud reservation/quota systems, and export controls.

**Step 2 — Verify commons structure.**

- *Open web.* Shared access ✓ (anyone can crawl). Rivalrous — *partially*: the bytes are non-rival (copying costs nothing), but the **incentive to keep supplying new content is rivalrous and depletable**; unrestrained extraction erodes it. Diffuse responsibility ✓ (no crawler bears the cost of a shrinking open web). Hardin pattern ✓ (each lab rationally scrapes maximally; collectively they can starve future training data). Commons — with the nuance that the depletable stock is the *supply incentive*, not the copies.
- *Power.* Shared ✓, rivalrous ✓ (a megawatt drawn is unavailable to others), diffuse responsibility ✓, Hardin pattern ✓. A clean commons.
- *GPUs.* Shared ✓, rivalrous ✓ (a chip allocated to one buyer is unavailable to another), diffuse responsibility ✓, Hardin pattern ✓. A clean commons on a rivalrous private good under scarcity.

**Step 3 — Ostrom audit.**

*Open web:*
- **1 Boundaries — absent/weak.** No enforceable line separates permitted from prohibited use; `robots.txt` is honored voluntarily and inconsistently.
- **2 Congruence — absent.** Those who benefit from extraction (labs) are largely not those who bear the cost (creators); contribution and appropriation are decoupled.
- **3 Collective-choice — weak.** Creators historically had no seat in the rules governing crawling; recourse emerged mostly through lawsuits and one-off licensing deals rather than shared rule-making.
- **4 Monitoring — weak.** It is hard for a publisher to detect which crawler took what, though crawler-identification and analytics tools improved through 2024–2025.
- **5 Graduated sanctions — weak.** Blocking a crawler or suing are blunt, high-cost instruments, not graduated ones.
- **6 Conflict resolution — weak.** Disputes ran through courts (multiple copyright suits against AI developers filed 2023–2025) rather than a low-cost forum.
- **7 Right to organize — emerging.** Publisher coalitions, licensing marketplaces, and proposed provenance/consent standards began forming.
- **8 Nested enterprises — absent.** No layered governance from site to sector to international level.

*Power:* Boundaries and nested enterprises are relatively strong (utilities, grid operators, regulators are layered). Congruence is the pressure point — the concern that data-center demand can shift costs onto other ratepayers. Monitoring and collective-choice run through existing regulatory proceedings, which are slow relative to the pace of demand growth.

*GPUs:* Boundaries exist (allocation is contractual/private). Congruence and collective-choice are weak for smaller actors with no bargaining power; graduated mechanisms (fair-share quotas, reservation tiers, academic set-asides) are the natural design targets.

**Step 4 — Intervene.** For each weak/absent principle, the skill points to institutional design rather than the "privatize or regulate" binary:

- *Open web:* strengthen **boundaries and congruence** with machine-readable consent/provenance standards, licensing marketplaces that route value back to creators (restoring the supply incentive), and coalitions giving creators a collective-choice voice. Pure privatization (everything behind paywalls) would shrink the open web; pure regulation is slow and jurisdiction-bound. Ostrom's lens favors negotiated, layered consent regimes.
- *Power:* strengthen **congruence** via tariff and interconnection design that assigns the cost of new capacity to the demand that causes it, plus co-located or dedicated generation so hyperscale load does not free-ride on shared capacity. This is classic congruence + nested-enterprise work through existing regulators.
- *GPUs:* strengthen **collective-choice and graduated allocation** with reservation tiers, transparent fair-share quotas, and academic/public-interest set-asides (national research compute programs are a nested-enterprise response). Markets clear supply but concentrate it; deliberate set-asides preserve the research commons.

**Step 5 — Monitor.** Track resource health per commons: for the open web, the share of high-value sites blocking or licensing crawlers and any decline in fresh open publication; for power, interconnection-queue times and the ratepayer cost-allocation split; for GPUs, access for non-frontier labs and academics. Review on a fast cycle — this commons is moving far faster than fisheries or grazing land.

The mapped steps:
1. Identify: open web / grid power / GPU supply · extractor labs vs. supplier creators/ratepayers/small labs · eroding supply incentive, cost-shifting, crowd-out · voluntary conventions and private allocation
2. Verify commons structure: power ✓✓✓✓ and GPUs ✓✓✓✓ clean; open web ✓ with the depletable stock being the *incentive to publish*, not the copies
3. Ostrom audit: boundaries and congruence are the recurring gaps across all three
4. Intervene: consent/licensing regimes (web), cost-causer tariffs and dedicated generation (power), fair-share quotas and research set-asides (GPUs) — layered governance over the privatize-or-regulate binary
5. Monitor: fast-cycle metrics on supply health, cost allocation, and access

The operational lesson: the AI build-out did not create new economics — it re-ran Hardin at internet speed across three commons at once. The open-web case sharpens the skill's own boundary condition — a resource can be non-rival in its *copies* yet a genuine commons in its *renewal incentive*, which is exactly the depletable stock Ostrom's design principles exist to protect.

*Sources: Hardin, G. (1968). "The Tragedy of the Commons." Science, 162(3859), 1243–1248. Ostrom, E. (1990). Governing the Commons. Cambridge University Press. Reuters and Associated Press reporting (2023–2025) on copyright litigation between publishers/authors and AI developers, on data-center electricity demand and grid strain, and on advanced-GPU supply constraints and export controls. International Energy Agency, "Electricity 2024: Analysis and Forecast to 2026" and related IEA analyses (through 2025) on data-center and AI electricity demand.*
