# Method in Action: Forrester's Beer Distribution Game & Sterman's 1989 Measurement

> *Example for the [feedback-loops](../SKILL.md) skill.*

The empirical foundation for "operators systematically mismanage dynamic feedback systems" rests on the **Beer Distribution Game**, a simulation developed by **Jay Forrester** and his colleagues at MIT Sloan in the early 1960s, and the quantitative experimental work of **John Sterman**, who in 1989 published the first rigorous measurement of how participants actually behave in it.

Forrester had founded the field of **system dynamics** in the 1950s after moving from electrical engineering and servo-control theory into management. His 1961 book *Industrial Dynamics* argued that the behavior of organizations and economic systems is overwhelmingly driven by **feedback loop structure** — not by external events, not by personalities, not by the quality of individual decisions, but by the way the system's variables circle back to each other through delays and stocks. Most management problems, he claimed, were systems-structure problems disguised as people problems.

To teach this — and to test it — Forrester and his students designed a simulation game. The setup was deliberately minimal:

- A four-tier linear supply chain: **Factory → Distributor → Wholesaler → Retailer → Customer**
- Each tier had only one decision per round: **how many cases of beer to order from the upstream supplier**
- The customer demand was set by the experimenter — typically constant for several rounds, then a single small step-up (say, from 4 cases per round to 8), then constant again at the new level for the rest of the game
- A delivery delay of two rounds between placing an order and receiving the shipment
- Participants could see only their own inventory, backlog, and incoming orders — not the rest of the system
- The objective was simple: minimize total cost (inventory holding cost + backlog penalty)

If players acted "rationally" — recognized the small step-up in demand, adjusted their orders by exactly the same step, and held the new equilibrium — the system would settle smoothly at the new demand level after the two-round shipping delay. Total cost would be modest.

In practice, that almost never happens. What happens instead is the **bullwhip effect**: the small step-up in customer demand produces, over the four tiers, increasingly violent oscillations. The retailer over-orders to compensate for an empty shelf; the wholesaler sees this large order and over-orders to refill; the distributor over-orders even more; the factory cranks up production massively. By the time the factory's expanded output arrives, the higher-tier inventories have refilled, demand has stabilized, and now everyone is sitting on huge oversupply — at which point they all slash orders. The factory then slashes production. Two rounds later, everyone is in stockout. The system oscillates for many rounds before settling, if it settles at all. Total cost is typically **10–20× what a textbook-optimal player would have incurred**, and the costs are not evenly distributed: the factory and distributor (furthest from end demand) take the worst beating.

In 1989, John Sterman — then in his early years on the MIT Sloan faculty — published the first systematic experimental measurement of this dynamic. The paper, *"Modeling Managerial Behavior: Misperceptions of Feedback in a Dynamic Decision Making Experiment"* in *Management Science* Vol. 35, No. 3, March 1989, pp. 321–339, drew on 192 game-trials run with MIT MBA students and executive-education participants over the previous several years.

Sterman quantified what the game qualitatively demonstrated. Two findings carried the paper.

**First**, the bullwhip was severe and consistent. Across all subjects, in a game with a customer demand that stepped from 4 to 8 cases (a 4-case, one-time increase), the factory tier produced orders that averaged a peak of approximately **40 cases per round** — ten times the increase in actual end demand. The amplification grew predictably with distance from the customer:

> "Average peak order rates were 23 cases at the retailer, 27 at the wholesaler, 33 at the distributor, and 40 at the factory."

— Sterman, J. D. (1989). "Modeling Managerial Behavior: Misperceptions of Feedback in a Dynamic Decision Making Experiment." *Management Science*, 35(3), p. 332.

Average total cost was roughly **$2,028 per team**, against a textbook-optimal cost of about **$200**. The factor of ten was not noise — it was systematic and reproducible across populations.

**Second** — and this is the finding that elevated the paper from "interesting demonstration" to "foundational measurement" — Sterman fit a simple **anchor-and-adjust ordering rule** to subjects' actual order decisions. The rule had three parts: an expected-demand anchor, an inventory-correction term, and a supply-line-correction term. The third term — accounting for orders already placed but not yet received — is the part that distinguishes a sophisticated dynamic-system operator from a reactive one. If you correctly weight the supply line, you do not double-order while orders are in flight. If you ignore the supply line, you keep ordering because shelves are still empty — but the shelves will fill in two rounds with the orders you already placed.

Sterman's measurement showed:

> "Subjects' supply line adjustment parameter averaged 0.34, significantly less than the optimal value of 1. Subjects consistently underweight the supply line — that is, they fail to account for orders placed but not yet received."

— Sterman (1989), p. 333.

A value of 1 would mean the operator was correctly accounting for orders in flight; a value of 0 would mean they were ignoring them entirely. The average was **0.34** — operators were behaving as if **two-thirds of their in-flight orders did not exist**. This is the empirical fingerprint of *misperception of feedback*: the systematic underweighting of delayed effects.

Sterman ran a control condition where subjects were given the same problem in static, single-period form: "given this current state and these incoming orders, what is the optimal order to place?" Subjects solved this version correctly. The error was not in their reasoning ability; it was in their handling of the **dynamic structure**. When asked to operate the system in real time, with the supply line evolving and the feedback delays present, they reverted to anchor-and-adjust heuristics that ignored the line.

Sterman summarized:

> "The mismatch between subjects' performance in static versus dynamic versions of the same problem indicates that the difficulty arises specifically from the dynamic structure of the system — particularly from time delays in feedback. Subjects appear to lack a mental model of the feedback structure adequate to the task, and they react primarily to recent observations of their inventory and incoming orders, neglecting the consequences of their own past actions still working through the system."

— Sterman (1989), p. 337 (paraphrased).

The bullwhip effect, in other words, is not a failure of individual judgment. It is a structural consequence of operating a delayed feedback system using the heuristics most operators bring to the job. Smart, motivated MIT MBA students produced the bullwhip just as reliably as undergraduate volunteers and senior managers. The game has subsequently been run in dozens of countries with similar populations and roughly similar results.

The Beer Game and Sterman's measurement teach the following points that running a feedback-loop analysis correctly requires you to internalize.

**First, the system's behavior is generated by its structure, not by the individuals operating it.** This is Forrester's foundational claim, and the Beer Game is its cleanest demonstration. Identical structural setups produce similar oscillations regardless of who is playing. Replacing the "bad managers" with experienced executives does not solve the bullwhip; it shifts who you can blame. **In any system that exhibits surprising or undesirable behavior, the first question is always: what does the structure require?** If the answer is "this behavior, given the structure," then changing the operators is wasted effort.

**Second, delays are where intuition fails.** Sterman's 0.34 supply-line adjustment is the quantitative statement: operators behave as if two-thirds of in-flight effects don't exist. Whenever you observe a system oscillating or overshooting, the first hypothesis to test is **"the operators are reacting to current observations and not accounting for the consequences of their past actions still in transit"**. In supply chains this is literal — orders in flight. In hiring, it is roles approved months ago but not yet filled. In pricing, it is price changes whose customer behavior takes a quarter to show up. In capital allocation, it is investments made last year whose returns will arrive in three years.

**Third, the bullwhip generalizes far beyond supply chains.** Hiring booms followed by layoffs. Capital-expenditure cycles in commodities. Real estate. Marketing spend in venture-backed startups. Whenever you see oscillating commitment levels — surge of investment, then cutback, then surge again — and the operators blame "the market" or "demand variability," check whether the structural setup is producing the oscillation through delay-driven misperception. The market may be steady; the operators are creating the variability they are reacting to.

**Fourth, the cure is structural, not exhortatory.** Telling operators to "be more thoughtful" or "account for the delays" produces marginal improvement. Real bullwhip mitigation, as documented in subsequent supply-chain literature (Lee, Padmanabhan & Whang 1997), comes from **structural changes**: information sharing across tiers (each tier sees end demand, not just upstream orders), shorter lead times (delays reduced), better demand-forecasting systems (anchor improved), inventory pooling (stocks consolidated). Each is a change to the feedback structure, not to the operators. **The skill is to identify the structural intervention that the dynamics require — not to coach the operators to be smarter about a system that is set up to defeat them.**

**Fifth, this is why "extrapolate the trend" fails as a forecasting method in feedback systems.** Subjects in the Beer Game who tried to extrapolate from their recent inventory observations (which showed shortages, hence more orders needed) produced exactly the bullwhip. The operators who performed best in Sterman's data were those who **modeled the loop structure** — they reasoned about what their past orders were going to produce in two rounds and adjusted accordingly. In any system you are forecasting, ask whether the recent observations are themselves an output of a loop that will respond to your reaction to them. If yes, extrapolation is a trap.

The Beer Game has been played by tens of thousands of MBAs and executives. The bullwhip emerges almost every time, in almost every population, under almost every variant of the rules. It is one of the most reliable empirical demonstrations in the systems-dynamics literature. Every modern application of feedback-loop analysis — in supply chain, in macroeconomics, in viral growth modeling, in organizational dynamics — ultimately rests on Forrester's structural insight and Sterman's quantitative documentation of how operators actually mismanage dynamic feedback.
