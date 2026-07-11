# Method in Action: Offshore Oil-Lease Auctions (1971)

> *Example for the [winners-curse](../SKILL.md) skill.*

The winner's curse was not discovered in a psychology lab — it was diagnosed in the field, in the Gulf of Mexico offshore oil-lease auctions of the 1960s. Three engineers at Atlantic Richfield (ARCO) — E. C. Capen, R. V. Clapp, and W. M. Campbell — noticed that firms winning federal lease tracts through competitive sealed bidding were, as a group, earning disappointing returns on those very tracts. In 1971 they published the explanation in the *Journal of Petroleum Technology*, coining the term and laying out the mechanism that this skill operationalizes.

**Step 1 — Classify the value.** An offshore lease is a textbook *common-value* asset. The tract holds some fixed, unknown quantity of recoverable oil and gas — the shared uncertain quantity is *barrels of recoverable reserves*. Every bidder is trying to estimate the *same* true number from its own seismic surveys and geological models. Their estimates differ only because their information and interpretations differ, not because the oil is "worth more" to one firm's taste. The gate is passed: the shared uncertain quantity is stated in one sentence.

**Step 2 — Count bidders and size dispersion.** These auctions drew many bidders per tract, and reserve estimation from seismic data is *extremely* noisy — different companies' pre-drill estimates for the same tract could differ by large multiples. Wide dispersion plus many bidders is the worst case: the highest of many very noisy estimates sits far above the truth. The gate flags the danger — more bidders and wider scatter both demand *more* shading, not less.

**Step 3 — Condition on winning.** This is the paper's central insight. Capen, Clapp & Campbell observed that whichever firm submits the highest bid is, almost by definition, the firm whose geologists were the most optimistic about that tract. As they put it:

> "If it is true, as common sense tells us, that a lease winner tends to be the bidder who most overestimates reserves potential, it follows that the 'successful' bidders may not have been so successful after all."

So a firm should not bid off its raw reserve estimate. It should ask: *given that our bid would only win if it topped every rival's, our estimate is probably the high outlier — so the tract likely holds less oil than we think.* Re-estimate value conditional on winning, and it drops. The gate: the working value is revised down.

**Step 4 — Value-conditioned ceiling and pre-commit.** The paper's practical prescription is that bidders must *deliberately bid below* their engineering estimate of value — the more competitors and the more uncertain the geology, the deeper the discount. This is exactly a value-conditioned ceiling: compute the conditioned reserve value, subtract required return, and cap the bid there *before* submitting. ARCO's own later practice (per industry accounts) was to install disciplined bidding rules precisely to avoid winning "everything it bid on" and starving the budget.

**Step 5 — Guard against escalation.** In sealed-bid lease sales the fever is subtler than a live auction, but real: pressure to "book acreage," to not be shut out of a hot play, and to justify the exploration team's aggressive estimate. The circuit-breaker is the pre-committed, value-conditioned cap that a desire to win acreage cannot override.

**Bid Discipline Card (reconstructed):**
```
Item: Offshore Gulf of Mexico oil-and-gas lease tract
Value type: common — shared uncertain quantity: recoverable reserves (barrels)
Bidders (N): many          Estimate dispersion: wide (seismic estimation is very noisy)
Unconditional value estimate: <firm's engineering NPV of the tract>
Condition-on-winning discount: large (high N × wide dispersion)
Conditioned value: engineering NPV minus a substantial adverse-selection haircut
Required return: exploration hurdle rate
--------------------------------------------------
BID CEILING (pre-committed): conditioned value − required return
Escalation trap: pressure to book acreage / not be shut out of a hot play
Circuit-breaker: submit no bid above the value-conditioned cap
```

**What it explains.** The apparent paradox — firms winning tracts yet earning poor returns as a group — dissolves. They were not unlucky; they were *systematically* winning the tracts they most over-estimated and losing the ones they priced soberly. Absent correction, that adverse selection quietly transfers the value of the oil to the seller (the government) and to the more disciplined bidders. The fix is not "estimate reserves better" (the estimates were roughly unbiased individually); it is "recognize that *winning* selects your high-tail estimates, and shade accordingly."

The mapped steps:
1. Classify: common-value — shared unknown is recoverable reserves
2. Count/disperse: many bidders, wide estimate scatter → shade heavily
3. Condition on winning: the winner is the most optimistic estimator; discount the estimate
4. Ceiling: bid deliberately below the engineering estimate, pre-committed
5. Escalation guard: don't let "book the acreage" override the cap

*Sources: Capen, E. C., Clapp, R. V., & Campbell, W. M. (1971). "Competitive Bidding in High-Risk Situations." *Journal of Petroleum Technology*, 23(6), 641–653 (https://onepetro.org/JPT/article/23/06/641/163651/Competitive-Bidding-in-High-Risk-Situations). Industry context on ARCO bidding discipline: American Association of Petroleum Geologists, "Bid Winners Can Face 'Curse'" (https://www.aapg.org/news-and-media/explorer/bid-winners-can-face-curse/). Survey: Thaler, R. H. (1988), "Anomalies: The Winner's Curse," *Journal of Economic Perspectives*, 2(1), 191–202.*
