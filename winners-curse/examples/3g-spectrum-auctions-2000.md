# Method in Action: The 2000 European 3G Spectrum Auctions

> *Example for the [winners-curse](../SKILL.md) skill.*

In 2000–2001, European governments auctioned licenses for third-generation (3G) mobile spectrum. The UK auction (March–April 2000) raised roughly £22.5 billion for five licenses; the German auction that followed raised even more, on the order of €50 billion. Telecom economists have debated how much of this was the winner's curse versus deliberate strategic overpayment — but the episode is a canonical, well-documented setting in which operators committed enormous sums for an asset whose true value nobody knew, and several later struggled under the resulting debt. It is a clean tech-sector illustration of the discipline.

**Step 1 — Classify the value.** A 3G license is largely *common-value*: the shared uncertain quantity is *the future cash flows from mobile data services on that spectrum* — how fast 3G adoption would come, how much consumers would pay for mobile data, what the technology would cost to build out. In 2000, nobody knew. Every operator was estimating the same unknown future market. (There is a private-value sliver — an incumbent's existing base or spectrum position — but the dominant driver was a shared, wildly uncertain forecast.) Gate passed: the shared unknown is future 3G revenue.

**Step 2 — Count bidders and size dispersion.** Multiple large operators competed, and the dispersion in value estimates was enormous — this was a brand-new technology with no adoption history, so revenue forecasts ranged across a very wide band. Many bidders plus extreme dispersion is the maximum-danger configuration: the *winning* forecast was likely to be far above the eventual truth. The gate says shade hard.

**Step 3 — Condition on winning.** The winner's-curse discipline says each operator should have asked: *if our bid wins, it is because our forecast of 3G's future was the most bullish in the room — so the real market is probably smaller than we think.* The value used to justify the bid should have been the value *conditional on being the most optimistic bidder*, which is materially lower than the raw forecast. In the event, 3G adoption arrived years later and more slowly than the most bullish 2000-era forecasts implied, and several winners carried heavy license-related debt.

**Step 4 — Value-conditioned ceiling and pre-commit.** The corrective: build the bid off the *conditioned* revenue forecast (bullish case haircut for adverse selection), subtract the required return, and cap the bid there *before* the auction — and hold the cap when rivals kept raising. The UK auction's ascending design in particular made it easy for prices to climb well past sober pre-auction valuations.

**Step 5 — Guard against escalation.** The fever here was strategic and existential: "3G is the future of mobile — we *cannot* be locked out." That framing has no ceiling; "can't be locked out" justifies any price. The circuit-breaker is a pre-committed value-conditioned cap plus an honest answer to "is being shut out actually fatal, or is that auction fever talking?" Some operators dropped out as prices climbed; that was the discipline working, not weakness.

**Bid Discipline Card (reconstructed):**
```
Item: National 3G mobile spectrum license
Value type: common (mostly) — shared unknown: future 3G data cash flows
Bidders (N): several major operators   Dispersion: extreme (new tech, no adoption history)
Unconditional value estimate: bullish 3G revenue NPV
Condition-on-winning discount: large (high N × extreme dispersion)
Conditioned value: revenue NPV minus heavy adverse-selection haircut
--------------------------------------------------
BID CEILING (pre-committed): conditioned value − required return
Escalation trap: "3G is the future — we can't be locked out"
Circuit-breaker: hold the cap; drop out rather than chase past it
```

**Founder takeaway:** When a "we can't miss the next platform" narrative is driving a competitive bid — a hot category, a scarce asset, a must-win auction — that is exactly when the winner's curse bites hardest, because the value is a shared *forecast* of an unproven future and the winner is whoever forecast most bullishly. Write your walk price off your *own* conditioned model before the process starts, and treat "we can't be locked out" as a feeling to price against, not a blank check.

*Sources: Binmore, K., & Klemperer, P. (2002). "The Biggest Auction Ever: The Sale of the British 3G Telecom Licences." *The Economic Journal*, 112(478), C74–C96 (https://onlinelibrary.wiley.com/doi/abs/10.1111/1468-0297.00020). Klemperer, P. (2002). "How (Not) to Run Auctions: The European 3G Telecom Auctions." *European Economic Review*, 46(4–5), 829–845. UK auction proceeds (~£22.5bn): Wikipedia, "Spectrum auction" (https://en.wikipedia.org/wiki/Spectrum_auction). Foundational concept: Capen, Clapp & Campbell (1971), *Journal of Petroleum Technology*, 23(6), 641–653.*
