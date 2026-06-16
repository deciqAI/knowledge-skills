# Method in Action: Klemperer's Foundational Theory and IBM Mainframe Lock-in

> *Example for the [switching-costs](../SKILL.md) skill.*

**Paul Klemperer**, then at Oxford, published *"Markets with Consumer Switching Costs"* in the *Quarterly Journal of Economics* in May 1987 (Vol. 102, No. 2, pp. 375-394). The paper was the first rigorous economic treatment of switching costs as a structural market property.

Klemperer's central result, stated in the abstract:

> "When consumers face costs of switching between functionally similar brands, the markets for such brands appear competitive ex ante but each firm faces a downward-sloping demand curve ex post; firms with established market shares earn supernormal profits."

— Klemperer, P. (1987). "Markets with Consumer Switching Costs." *Quarterly Journal of Economics*, 102(2), p. 376.

The paper formalized what business observation had long understood:

> "Switching costs convert what would otherwise be a competitive market into one with characteristics of monopolistic competition or even oligopoly. Firms that have acquired customers can extract supernormal profits from those customers until the customer's accumulated dissatisfaction exceeds the switching cost."

— Klemperer (1987), p. 380.

In a 1995 follow-up, *"Competition When Consumers Have Switching Costs"* (*Review of Economic Studies*, 62(4), pp. 515-539), Klemperer showed that the rational response of firms in switching-cost markets is to **compete heavily for new customers** (because each acquired customer is then locked in) and **price discriminate** against locked-in customers (charging incumbent customers more than new customers, because the incumbents can't easily leave). This pattern is observable in real markets: banks offering high promotional rates to new account openings; cell-phone carriers offering deep new-customer discounts; SaaS companies often pricing new customers lower than renewals.

The empirical case most thoroughly documented in the academic literature is **IBM's mainframe lock-in from the 1960s through 1980s**. By the late 1960s, IBM dominated business computing not primarily through better hardware (Burroughs, Honeywell, NCR, RCA, Sperry, and CDC all sold competitive mainframes) but through **switching-cost moats** that competitors could not match:

1. **IBM 360 software ecosystem.** Software written for IBM mainframes used IBM-specific instructions, file formats, and operating system calls. Migrating an application to non-IBM hardware required rewriting it.

2. **JCL (Job Control Language).** IBM's JCL had become the standard for mainframe operations. Operations staff had thousands of hours of accumulated skill in JCL. Switching meant retraining the entire operations team.

3. **IBM customer engineers and integrators.** IBM employed thousands of customer engineers who were embedded with major customers, providing on-site support, custom development, and operational expertise. Switching meant losing that institutional relationship.

4. **Plug-compatible peripheral fear.** IBM made its protocols subtly proprietary, so that even when competitors made plug-compatible peripherals (Memorex's tape drives, Telex's terminals), customers feared that IBM would change something next year and the compatibility would break.

The result: through the 1970s, IBM commanded ~60-70% of US mainframe revenue and ~80% of operating profit in the segment, despite competing with multiple firms that built comparable or better hardware. The 1969-1982 US antitrust case against IBM (*US v. IBM*, never resolved before government dropped it in 1982) explicitly documented these switching-cost mechanisms.

What ultimately broke IBM's switching-cost moat was not a competitor matching it. It was a **technological discontinuity** — minicomputers, then PCs, then client-server architectures — that allowed customers to *bypass* the entire mainframe ecosystem rather than switch within it. Switching from IBM mainframe to a comparable non-IBM mainframe was nearly impossible; switching from "doing the work on a mainframe" to "doing it on a network of PCs" did not require interacting with the mainframe switching costs at all.

This pattern recurs in modern switching-cost markets: **the moat is not broken by direct switching but by structural bypass.** Microsoft Office's switching-cost moat in the 2000s was not broken by a better word processor; it was bypassed by Google's "your document lives in the cloud, accessible from anywhere" reframing that made certain Office switching costs irrelevant. Bloomberg Terminal's moat has not been broken by a better terminal; competitors are trying to bypass it through different workflows (Symphony's chat-first approach, Sentieo's research-document-first approach).

Several points from this combined case worth internalizing:

**First, switching costs are routinely the most important determinant of competitive outcome in mature markets.** Klemperer's formal model and IBM's 25-year dominance both establish this. New entrants who assume "better product wins" without doing the switching-cost math are pricing in optimism that the historical record does not support.

**Second, the seven types of switching costs are not equivalent.** Financial costs are usually the smallest. Learning, integration, and risk premium are usually the largest. Founders who design "data migration tools" but don't address learning curves and integration redos solve the smallest piece of the problem.

**Third, value-focused integration depth produces durable moats; extraction-focused lock-in produces churn cascades.** The first compounds with customer success; the second decays with the first available alternative.

**Fourth, technological discontinuity can bypass switching costs in ways that direct competition cannot match.** When you are losing in a switching-cost market, the strategic question is not "how do I match the incumbent?" but "what bypass am I building that makes the incumbent's switching costs irrelevant?"

**Fifth, in switching-cost markets, the asymmetric pricing strategy (low new-customer prices, high incumbent prices) is rational and predictable.** Customers should anticipate this — and structure procurement contracts to lock in pricing before becoming locked in by the product.
