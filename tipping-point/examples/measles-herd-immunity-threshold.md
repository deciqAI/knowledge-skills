# Method in Action: The Measles Herd-Immunity Threshold and U.S. Elimination (1963 → 2000)

> *Example for the [tipping-point](../SKILL.md) skill.*

Epidemic transmission is a textbook tipping system. Whether measles spreads explosively or dies out is governed by a sharp threshold in population immunity, and vaccination programs are, in tipping-point terms, a deliberate campaign to push the system across that threshold in the *downward* direction — collapsing self-reinforcing transmission.

**Step 1 — System.** The phenomenon is measles transmission through a susceptible population. The self-reinforcement mechanism is contagion: each infected person infects, on average, some number of others, who each infect others. The direction of the tip is set by whether that chain amplifies (outbreak) or damps (elimination). Measles is among the most contagious human diseases, so its reproduction dynamics are unforgiving.

**Step 2 — Threshold.** Standard epidemiology defines the basic reproduction number R₀ as the average number of secondary infections one case produces in a fully susceptible population. Transmission amplifies when the *effective* reproduction number exceeds 1 and collapses when it falls below 1. The critical immune fraction that pushes the system below 1 is the herd-immunity threshold, p꜀ = 1 − 1/R₀ (Anderson & May, 1991; Fine, 1993). For measles, R₀ is conventionally cited in the range of roughly 12–18, which places the threshold at approximately 92–95% immunity. Below that band, chains amplify; above it, they die out.

**Step 3 — Current state.** After the first measles vaccine was licensed in the United States in 1963, sustained childhood immunization pushed population immunity upward over decades. The distance-from-threshold that matters is not the *average* national coverage but coverage within each locally-mixing community, because a susceptible pocket can sit below p꜀ even when the national figure clears it.

**Step 4 — Leverage, monitoring, defense.** Near the threshold, marginal vaccination has outsized effect: adding coverage that carries a community from just below p꜀ to just above it flips its effective reproduction number under 1 and extinguishes local chains — a step-change, not a linear gain. Sustained high coverage drove endemic transmission to zero, and the CDC declared measles eliminated in the United States in 2000. The downward-tipping defense is symmetric and continuous: if coverage in a community erodes back below the threshold, imported cases re-ignite self-reinforcing outbreaks. Elimination is therefore not a terminal, safe state — it is a threshold that must be actively held above p꜀. Documented resurgences in under-vaccinated pockets are the early-warning signal of a system tipping back up toward outbreak.

The lesson mirrors Schelling's: the macro outcome (endemic disease vs. elimination) is not the linear sum of individual vaccination choices. It is a threshold phenomenon in which a few percentage points of coverage, applied at the right margin, separate two qualitatively different worlds.

The mapped steps:
1. System: measles transmission | tipping point = herd-immunity threshold (effective reproduction number crossing 1) | self-reinforcement = contagion chains | direction: up (outbreak) or down (elimination)
2. Threshold: p꜀ = 1 − 1/R₀; for R₀ ≈ 12–18, threshold ≈ 92–95% immunity
3. Current state: coverage built up after the 1963 vaccine; distance-from-threshold measured per locally-mixing community, not by national average
4. Leverage + defense: marginal coverage near p꜀ flips local transmission below 1; U.S. elimination declared 2000; defense = hold coverage above p꜀, watch under-vaccinated pockets as downward-tip early warning

Primary source: Anderson, R. M., & May, R. M. (1991). *Infectious Diseases of Humans: Dynamics and Control.* Oxford University Press. ISBN 978-0198545996. See also Fine, P. E. M. (1993). "Herd Immunity: History, Theory, Practice." *Epidemiologic Reviews*, 15(2), 265-302. https://doi.org/10.1093/oxfordjournals.epirev.a036121
