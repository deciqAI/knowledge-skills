# Method in Action: Mutual Fund Survivorship and Reported Returns (1971–1996)

> *Example for the [survivorship-bias](../SKILL.md) skill.*

Through the early 1990s, the standard evidence for "mutual funds deliver strong long-run returns" came from commercial fund databases and industry performance tables. The claim looked data-driven: average the annual returns of the funds in the database over a decade or two, and the industry's track record appears solid. The problem is Step 1 of the Process in miniature — a confident conclusion drawn from a sample nobody had audited for its filter.

**The survival filter (Step 2).** Fund databases of the era typically listed funds *currently in existence*. When a fund performed badly, its sponsor liquidated it or merged it into a better-performing sibling — and it silently dropped out of the historical tables. The population was every fund that ever operated over the sample period; the visible sample was only the funds that lasted to the end. Attrition was not rare: in Burton Malkiel's data on equity funds from 1971 to 1991, a substantial fraction of all funds that ever existed had disappeared before the end of the period, and disappearance was strongly associated with poor prior performance.

**The non-survivor hypothesis (Step 3).** The vanished funds were not a random subset. They were disproportionately the losers — funds that trailed the market, bled assets, and were shut down or merged away. If they had looked like the survivors, sponsors would have had no reason to kill them. So the visible sample's average return must overstate the average return an investor choosing a fund *at the start* of the period would actually have earned.

**Re-estimating the claim (Step 4).** Two studies made the correction quantitative. Malkiel (1995) reconstructed the full population of equity funds, including the dead ones, and found that the average annual return of surviving funds materially exceeded the average across all funds — a gap on the order of a percentage point or more per year during the 1980s. Elton, Gruber & Blake (1996) took the cleanest design: they froze the set of funds existing in 1977 and followed *every one of them* forward through 1993, tracking merged funds into their successors so nothing could exit the sample. They found that survivorship bias inflates measured performance by an amount that grows with the length of the sample period — roughly a percentage point per year over long horizons — enough to turn apparent stock-picking skill into underperformance after costs.

**The correction (Step 5).** The fix was structural, not rhetorical: rebuild the sample so the filter cannot operate. Follow-forward designs and survivor-bias-free databases (such as the CRSP mutual fund database) became the methodological standard in academic finance. Performance claims computed on survivor-only samples are now treated as upward-biased by construction, and the burden of proof sits on anyone citing them.

The episode is the pure financial analogue of Wald's bombers, with one difference that makes it more insidious: nobody shot the losing funds down in public. They were quietly merged away by the same institutions whose track records benefited from their disappearance — the filter and the beneficiary of the filter were the same party.

The mapped steps:

1. State the claim: "mutual funds earn strong long-run returns," sourced from databases of currently existing funds.
2. Identify the survival filter: poorly performing funds were liquidated or merged and dropped from historical tables; the sample is conditioned on lasting to the end of the period.
3. Construct the non-survivor hypothesis: the dead funds were disproportionately the underperformers; had they resembled survivors, they would not have been closed.
4. Re-estimate strength: follow-forward reconstructions (Malkiel 1995; Elton, Gruber & Blake 1996) show survivor-only averages overstate returns by roughly a percentage point per year, growing with horizon length.
5. Correct or mark: adopt survivor-bias-free samples that track every fund from inception forward, merging targets included; treat survivor-only performance tables as conditional evidence only.

Primary sources: Elton, E. J., Gruber, M. J., & Blake, C. R. (1996). "Survivorship Bias and Mutual Fund Performance." *Review of Financial Studies*, 9(4), 1097–1120. Malkiel, B. G. (1995). "Returns from Investing in Equity Mutual Funds 1971 to 1991." *Journal of Finance*, 50(2), 549–572.
