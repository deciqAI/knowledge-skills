# Method in Action: Eisenhower's D-Day Weather Decision (June 1944)

> *Example for the [decision-tree](../SKILL.md) skill.*

On June 4–5, 1944, General Dwight D. Eisenhower faced the highest-stakes go/no-go decision of the war: launch Operation Overlord into marginal weather, or postpone. The decision was never written up as a formal tree — the method postdates it — but the deliberation at Southwick House maps onto the decision-tree process almost node for node, which is why decision analysts have cited it ever since.

**The root decision node (square):** Go on June 6, or postpone. The branch set was tightly constrained: the invasion needed moonlight for the airborne drops and a low dawn tide to expose beach obstacles, so only a few days per month qualified. If June 6 was scrubbed, the next tidal window was around June 19 — roughly two weeks away.

**The chance nodes (circles):** Each option led straight into an uncertainty Eisenhower did not control.

- *Go, June 6* → chance node: does the brief break in the storm forecast by Group Captain James Stagg, SHAEF's chief meteorologist, actually hold? If yes: landings proceed under rough but workable conditions. If no: landing craft swamped, air support grounded, the assault force wrecked on the beaches.
- *Postpone to June 19* → chance node: unknown weather two weeks out (beyond any 1944 forecast horizon), compounded by near-certain costs — nearly 200,000 troops were already sealed aboard ships and briefed, and every day of delay increased the odds that German intelligence would fix the time and place of the invasion.

**Probabilities:** Stagg's team forecast a short interval of improved weather for June 6 amid a stormy period — a genuine probabilistic judgment made against disagreeing British and American forecasting teams. Illustrative reconstruction (not historical record): call the window-holds branch p ≈ 0.7, and the June 19 branch a coin flip at best with the secrecy-compromise cost accruing regardless. No participant wrote such numbers down; the structure of the argument, however, was exactly this.

**Payoffs:** The asymmetry drove the answer. *Go and the window holds*: the liberation of Western Europe begins. *Go and it fails*: a bloody repulse — but a repulse that a second attempt could survive. *Postpone*: certain, compounding losses (secrecy, morale, tide, the Soviet-front timetable) plus an unresolved weather gamble two weeks later. Postponement was not the "safe" branch; it was a different bet with worse certain costs.

**Value of information — the June 4 postponement:** Eisenhower's first move was a textbook EVPI play. On June 4 he scrubbed the original June 5 date and bought exactly one more forecast cycle — trading one day of the window for one more update from Stagg. When Stagg's June 5 briefing confirmed the break, the value of further waiting had collapsed: no additional forecast could resolve the remaining uncertainty before the tide window closed. The cost of more information now exceeded its value.

**Rollback:** Folding back from the leaves: the *go* branch's expected outcome — even weighted for a serious chance of failure — beat the *postpone* branch's certain security erosion plus unresolved weather risk. In the early hours of June 5, Eisenhower gave the order to go. Before the landings he drafted a note taking sole responsibility in case of failure — evidence that he had priced the losing branch explicitly rather than wishing it away.

**The sensitivity check history ran for free:** June 19 — the fallback window — brought the worst Channel storm in decades, wrecking the American Mulberry harbor off Omaha Beach. Had Eisenhower postponed, the invasion would have sailed into it. The decision was right at the assigned probabilities, and the unchosen branch turned out even worse than estimated.

The mapped steps:
1. Root: go June 6 vs. postpone to ~June 19 — options fixed by tide and moon (Process Step 1)
2. Chance nodes: forecast window holds/fails; June 19 weather unknown + secrecy erosion — MECE branches on each option (Step 2)
3. Probabilities: Stagg's explicit short-window forecast against dissenting teams; reconstruction here is illustrative, the probabilistic reasoning is documented (Step 3)
4. Payoffs: asymmetric — recoverable failure on *go* vs. certain compounding costs on *postpone* (Step 4)
5. Rollback: *go* dominates once the June 5 forecast update lands; order given early June 5 (Step 5)
6. Value of information: the 24-hour postponement bought one more forecast cycle, then EVPI of further delay fell below its cost — decide now (Step 6)

Primary source: Eisenhower, D. D. (1948). *Crusade in Europe.* Doubleday — Eisenhower's own account of the postponement and the go decision. Corroborating: Stagg, J. M. (1971). *Forecast for Overlord.* Ian Allan — the SHAEF chief meteorologist's account of the forecasts behind the decision.
