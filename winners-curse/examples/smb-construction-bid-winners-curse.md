# Method in Action: The Overbidding Contractor (SMB fixed-price bidding)

> *Example for the [winners-curse](../SKILL.md) skill.*

Competitive fixed-price bidding by construction contractors is one of the most studied real-world habitats of the winner's curse, and one every small-business owner in a bid-driven trade can recognize. A general contractor bids a lump sum to complete a project whose true cost — labor hours, materials, weather delays, hidden site conditions — is genuinely uncertain. The client typically awards to the *lowest* bidder. This is the winner's curse in mirror image: instead of the highest *value* estimate winning, the lowest *cost* estimate wins — which is the bidder who most *under*-estimated the cost. The composite illustration below is not a single named firm, but the pattern is documented across the construction-economics literature and reflected in the finding that experienced bidders can still fall prey to the curse when the role is unfamiliar (Harrison & List, 2008).

**Step 1 — Classify the value.** The shared uncertain quantity is *the true cost to complete this specific job*. Every bidding contractor is estimating the same underlying cost from the same drawings and site — dispersion comes from different takeoffs, subcontractor quotes, and risk assumptions, not from taste. That makes it common-value. Gate passed.

**Step 2 — Count bidders and size dispersion.** A public or well-advertised job might draw five to ten bidders, and cost estimates for an ill-scoped renovation can scatter widely (hidden conditions, ambiguous specs). Many bidders + wide dispersion = the low bid is likely to be a serious *under*-estimate of true cost. The gate: shade *up* (add cost cushion), and shade more the more bidders there are.

**Step 3 — Condition on winning.** The discipline for a contractor: *if I win this job, it's because my cost estimate came in below every competitor's — which means I probably missed something they caught, or I priced the risks too cheaply.* So the estimate to trust is the cost *conditional on being the lowest of N bidders* — which is *higher* than the raw takeoff. A contractor who bids their honest expected cost plus a thin markup will win exactly the jobs they under-costed and lose the ones they priced right — staying busy while bleeding margin.

**Step 4 — Value-conditioned ceiling (here, a bid *floor*) and pre-commit.** Invert the ceiling: set a hard *minimum* acceptable bid equal to conditioned cost + required margin, and refuse to go below it to "win the work." The more bidders and the more ambiguous the scope, the larger the uncertainty premium added to the cost before markup.

**Step 5 — Guard against escalation.** The SMB fever is "we need the backlog — keep the crews working," which rationalizes bidding at or below true cost. The circuit-breaker: a pre-set floor and the recognition that an idle week costs less than a six-month job run at a loss. Also watch the tell — *a suspiciously high win rate on competitive bids* means you are systematically the low (over-optimistic) estimator.

**Bid Discipline Card:**
```
Item: Fixed-price bid on a construction/renovation job
Value type: common — shared unknown: true cost to complete this job
Bidders (N): 5–10        Dispersion: wide (hidden conditions, ambiguous specs)
Unconditional cost estimate: raw takeoff
Condition-on-winning adjustment: +uncertainty premium (low bidder likely under-costed)
Conditioned cost: takeoff + premium
Required margin: target %
--------------------------------------------------
BID FLOOR (pre-committed): conditioned cost + margin — never bid below
Escalation trap: "we need the backlog — keep the crews busy"
Circuit-breaker: an idle week beats a job run at a loss; hold the floor
Tell: if we win most competitive bids, we are systematically underpricing
```

**What it explains.** The chronically-busy-but-broke contractor is the winner's curse in one sentence: winning the bids you underpriced, losing the ones you priced right, and mistaking a full schedule for a healthy business. The fix is not "estimate costs more precisely" (individual takeoffs may be unbiased); it is "recognize that *winning the low bid* selects your under-estimates, and add the premium before you name a price."

The mapped steps:
1. Classify: common-value — shared unknown is true job cost
2. Count/disperse: many bidders, wide scatter → add cushion, more for more bidders
3. Condition on winning: winning the low bid means you likely under-costed — raise the working cost
4. Floor: conditioned cost + margin, pre-committed, never undercut for backlog
5. Escalation guard: idle beats loss-making; high win rate is a warning, not a trophy

**Founder takeaway:** If you run a bid-driven service business (construction, contracting, agencies, fabrication) and you win *most* of the competitive fixed-price work you chase, you are almost certainly the person who most under-estimates cost — you've selected yourself into your own worst-priced jobs. Add an explicit uncertainty premium to bids on ill-scoped work, set a bid floor before you quote, and treat a too-high win rate as the alarm, not the applause.

*Sources: Concept origin: Capen, E. C., Clapp, R. V., & Campbell, W. M. (1971). "Competitive Bidding in High-Risk Situations." *Journal of Petroleum Technology*, 23(6), 641–653 (https://onepetro.org/JPT/article/23/06/641/163651/Competitive-Bidding-in-High-Risk-Situations). Experience-does-not-fully-inoculate finding: Harrison, G. W., & List, J. A. (2008). "Naturally Occurring Markets and Exogenous Laboratory Experiments: A Case Study of the Winner's Curse." *The Economic Journal*, 118(528), 822–843 (https://ideas.repec.org/a/ecj/econjl/v118y2008i528p822-843.html). Survey: Thaler, R. H. (1988). "Anomalies: The Winner's Curse." *Journal of Economic Perspectives*, 2(1), 191–202.*
