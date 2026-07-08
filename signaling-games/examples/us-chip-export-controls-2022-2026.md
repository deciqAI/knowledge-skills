# Method in Action: US Advanced-Chip Export Controls as a Signaling Game (2022–2026)

> *Example for the [signaling-games](../SKILL.md) skill.*

Most people read the US–China chip standoff of 2022–2026 as a straightforward story of technology denial: America controls the most advanced semiconductors and chip-making tools, so it withholds them from China. That framing misses what makes the episode hard. Neither side can directly observe the other's private information — how fast China can actually indigenize advanced chips, and how far the US is actually willing to escalate. In that fog, the *moves themselves* — a specific performance threshold, a purpose-built chip for one market, an export ban on a raw material — function as **costly signals** under asymmetric information about capability and resolve. This is a textbook setting for the signaling-games skill, and running the diagnosis on it is more illuminating than the denial narrative.

A word of caution up front, because this case is politically loaded and still unfolding: the framework below is an analytical lens, not a claim to read anyone's mind. Signaling theory tells you *what a move would have to cost, and to whom, for it to carry information* — it does not tell you the actors' true intentions. Use it to structure the question, not to manufacture certainty.

Let me run the skill's Process on it, step by step.

## 1. Asymmetry — what is hidden, who knows, who can't verify

Two distinct asymmetries run in opposite directions:

- **US → China's capability.** The US cannot directly verify how quickly China can design and, crucially, *manufacture at yield and scale* advanced logic chips without American and allied tools. China knows its own roadmap, foundry yields, and equipment substitution progress; the US does not.
- **China → US's resolve.** China cannot directly verify how far the US will actually go — whether controls are a one-time shot or the opening of a sustained, tightening regime that allies will join. The US administration knows its own tolerance for escalation and economic blowback; China must infer it.

Note this is not "China doesn't like the controls." The precise hidden variables are **China's manufacturing capability at the leading edge** and **US resolve to sustain and widen controls over years**. Both are unobservable and both parties have incentives to misrepresent them.

## 2. Types — name the hidden attribute

- On the capability axis: China is either a **fast-indigenizer** (can close the gap in a few product generations despite the controls) or a **slow-indigenizer** (structurally bottlenecked, e.g. at EUV-class lithography and high-yield advanced nodes, for a long time).
- On the resolve axis: the US is either a **committed regime-builder** (will tighten thresholds annually and pull allies in) or a **one-shot deterrer** (a single splashy action, then drift).

The whole game is each side trying to *learn the other's type* while managing what its own moves reveal.

## 3. Adverse selection — what happens without a credible signal

Absent any costly, hard-to-fake move, cheap talk dominates and gets priced at the average. China can *say* "the controls won't work, we'll indigenize"; the US can *say* "we'll escalate indefinitely." Because talk is free, a rational receiver discounts both toward the pooled mean — assuming middling Chinese capability and middling US resolve. That pooled belief is exactly what each side wants to move: China wants the US (and its own market) to believe indigenization is real; the US wants China (and allies) to believe the regime is durable. Words alone can't move the belief, so both reach for actions whose cost differs by type.

## 4. Enumerate the candidate signals actually observed

The 2022–2026 record supplies an unusually clean set of costly moves:

- **US: a numeric performance-threshold ban.** In **October 2022**, the US Bureau of Industry and Security (BIS) published sweeping controls restricting exports to China of the most advanced AI/computing chips and the equipment to make them, defined by technical performance thresholds rather than by named products.
- **US: an updated, tightened rule.** In **October 2023**, BIS revised the rules to close workarounds — notably catching chips that had been re-spec'd to sit just under the original limits.
- **Nvidia: purpose-built, throttled parts for China (H800, then H20).** Rather than exit China, Nvidia engineered China-specific parts designed to fall under the prevailing thresholds — the A800/H800 after 2022, and later the **H20** built for the tightened 2023 regime.
- **The H20 reversal episode (2025).** In **April 2025** Nvidia disclosed the US had effectively barred H20 sales to China (via a new export-licensing requirement), forcing the company to take a large inventory-related charge — Nvidia's April 2025 disclosure put the estimated charge at roughly **$5.5 billion** associated with H20. Later in 2025 US policy shifted again toward allowing some H20 sales to China under conditions — the on-again/off-again handling being itself informative.
- **China: rare-earth / critical-mineral export leverage.** China tightened export controls on gallium and germanium (**announced July 2023**), later added graphite and other items, and through 2024–2025 escalated controls over rare-earth-related materials and magnets — leverage over inputs the West cannot quickly replace.
- **China: demonstrated domestic advance (SMIC 7nm-class).** Huawei's **Mate 60 Pro (released August/September 2023)** shipped with a SMIC-fabricated ~7nm-class processor (the Kirin 9000S), a public, hard-to-fake demonstration that China had reached a node many assumed the controls would block.
- **DeepSeek shock (January 2025).** A Chinese lab's competitive open model triggered a sharp global market reaction — including a historic single-day drop in Nvidia's market value — and functioned as a signal that frontier-level AI results might be achievable with less of the very hardware the controls restrict.

## 5. Test single-crossing — is each move meaningfully cheaper for one type?

This is the load-bearing step. A move is a real signal only if the *wrong type* would find it prohibitively costly to fake.

- **A numeric performance threshold** is a strong single-crossing device. It is expensive for a one-shot deterrer to sustain (it demands continuous rule-writing, enforcement, allied coordination, and absorbing industry lobbying) but comparatively affordable for a committed regime-builder who intends to ratchet it anyway. A threshold also creates a bright line that makes *future tightening* legible — it separates "we'll keep moving the line" from "we made a gesture." **Passes**, on the resolve axis.
- **Chinese rare-earth/mineral controls** pass single-crossing on the *resolve* axis for China: only a state willing to accept reputational cost and to push customers toward diversification will actually pull the lever, and China's dominant processing share made the threat non-trivial. But note the erosion risk (step 8): the more it is used, the faster the West invests to bridge it.
- **SMIC 7nm-in-a-shipping-phone** is the cleanest capability signal in the set. A *slow-indigenizer* cannot fake a working advanced-node SoC inside millions of retail units — yield, packaging, and supply at volume are unbearably expensive to counterfeit. Shipping it publicly is precisely the "unbearable for the wrong type" test. **Passes**, on the capability axis — though it stops short of proving *leading-edge* (sub-5nm) parity or EUV independence, which is where skeptics correctly locate the remaining bottleneck.
- **Nvidia's China-specific throttled chips** are the interesting near-miss. Re-spec'ing a part to sit just under a threshold is a *cheap* move relative to the underlying capability — which is exactly why the US treated the H800 as a workaround and tightened the rule in 2023. A signal that the low-cost path can imitate tends to get closed. This is single-crossing *failing*, and the system responding by moving the line.

## 6. Determine the equilibrium

The observed pattern is a **repeated, partially-separating (screening) equilibrium**, not a clean one-shot separation:

- Each US tightening round is a screen: it reveals US resolve *and* forces China to reveal capability by observing what China can still ship under the new line.
- China's public demonstrations (SMIC node, DeepSeek-class results) push its believed type toward *fast-indigenizer*, which is precisely what would make the US regime look less effective.
- Because the game repeats and the line keeps moving, no stable full-separation is reached — it looks like the [`repeated-games-reputation`](../repeated-games-reputation/SKILL.md) dynamic layered on a signaling game, with each round updating both sides' beliefs.

## 7. Check receiver response — does the receiver reward the signal?

Signals only hold if the receiver acts on them.

- Did the US *reward* (i.e. respond to) China's capability signals? Yes — the 2023 tightening and subsequent rounds are consistent with the US updating toward "China can work around single-generation gaps," which sustains China's incentive to keep demonstrating.
- Did China *reward* US resolve signals? The rare-earth escalation and the indigenization push are consistent with China updating toward "this is a durable regime, not a gesture," which is exactly the belief that justifies costly self-reliance investment.
- The **H20 on-again/off-again** handling is where receiver response gets muddied. Policy that bans, then partially permits, then re-conditions a single China-specific chip sends a *noisy* resolve signal — it can be read as either strategic calibration or wavering commitment. Noisy signals weaken separation; the receiver can't cleanly infer type, which is one reason both sides' beliefs stayed unsettled into 2026.

## 8. Watch for signal inflation / erosion

Every signal in this case has a half-life:

- **Rare-earth leverage erodes fastest.** Each use accelerates Western investment in alternative processing and recycling; the threat is strongest before it is used repeatedly. Classic signal decay — the more you pull it, the cheaper it becomes for the receiver to bridge.
- **Performance thresholds inflate** the way credentials do: China re-specs under the line, the US moves the line, repeat. The signal must be re-invested (new rules) to stay informative — a direct analogue of credential creep in Spence's model.
- **A single node demonstration ages.** SMIC 7nm-class in 2023 shifts beliefs, but to keep signaling *fast-indigenizer* China must keep demonstrating at successive nodes; a one-time show pools back toward the prior if not repeated.

## 9. As receiver, decode carefully — what cost was actually borne?

The decoding traps here are severe and worth naming, because this is where confident misreadings happen:

- **A China-specific chip that sits under the line is a cheap imitation, not proof the line failed** — it can be closed by re-writing the threshold, which is what happened. Don't read "they shipped a compliant chip" as "the controls don't bind."
- **A single advanced-node phone SoC is a genuine capability signal but a bounded one** — it demonstrates a node reached, not leading-edge (EUV-class) parity or volume at the frontier. Reading it as "China has caught up entirely" over-decodes; reading it as "nothing happened" under-decodes. The disciplined read is the narrow one: *the specific bottleneck everyone assumed was blocked was not blocked at that node.*
- **A dramatic market reaction (DeepSeek, Jan 2025) is a signal about the receiver's beliefs, not a verified fact about capability** — markets moved on an *inference* that frontier results might need less restricted hardware. The signal to decode is "the market updated," which is distinct from "the underlying claim is fully verified."
- **On/off policy is a noisy signal** — before treating the H20 sequence as evidence of US resolve (either high or low), ask what cost the US actually bore in each move. A reversal that costs little reveals little.

## 10. Stop-rule — is the cost differential substantial and sustained?

The framework's discipline: only bet on separation where the differential is large *and* durable.

- **Sustained, credible:** the manufacturing bottleneck at the true leading edge (EUV-class lithography, high-yield sub-5nm) — this remains expensive for a slow-indigenizer to fake and cannot be shown in a phone teardown. Beliefs here should move only on repeated, volume, frontier-node evidence.
- **Marginal, collapsing:** re-spec'd threshold-compliant chips, one-off demonstrations without follow-through, and low-cost policy reversals. Per the stop-rule, treat these as weak signals — do not update hard on them.

## Signaling Diagnosis (filled)

```
# Signaling Diagnosis: US–China advanced-chip export controls, 2022–2026
## Asymmetry: China's true manufacturing capability at the leading edge (China knows, US can't verify); US resolve to sustain/widen controls (US knows, China can't verify)
## Types: fast- vs slow-indigenizer (China) | committed regime-builder vs one-shot deterrer (US)
## Adverse selection: absent costly moves, cheap talk pools both beliefs toward the middle
## Candidate signals:
##   Numeric performance threshold — passes single-crossing on resolve (costly to sustain for a one-shot deterrer)
##   Rare-earth/mineral controls — passes for China's resolve, but erodes with repeated use
##   SMIC 7nm-class in a shipping phone — passes on capability (unbearable for a slow-indigenizer to fake at volume)
##   Nvidia China-specific throttled chip (H800/H20) — FAILS single-crossing (cheap to imitate → line moved)
## Recommended read: weight the durable, hard-to-fake signals (frontier-node manufacturing, sustained threshold-tightening); discount cheap ones
## Equilibrium: repeated, partially-separating (screening) — no clean one-shot separation
## Receiver response: each side updated (tightening rounds; indigenization + rare-earth escalation); H20 on/off made the resolve signal noisy
## Inflation risk: rare-earth leverage decays fastest; thresholds inflate like credentials; single demos age
## Decoding: threshold-compliant chip = cheap imitation not proof; one phone SoC = bounded capability, not parity; market shock = belief-update not verified fact
```

## What this case teaches about running the diagnosis

1. **Costly signals show up in geopolitics, not just markets.** The single-crossing test — *would the wrong type find this unbearable?* — cuts through the noise of a politically charged standoff exactly as it does in hiring or branding.
2. **A move that the cheap type can imitate gets closed.** The H800/H20 re-spec is a near-perfect illustration of a signal *failing* single-crossing and the system responding by moving the line. When you see a signal that's cheap to fake, expect the receiver to redefine it.
3. **Separate the signal from the fact.** The DeepSeek market reaction and a phone-teardown node are signals about *beliefs* and about a *specific bounded capability* — decoding them as verified, total conclusions is the classic receiver trap the skill warns against.
4. **Noisy signals are worse than no signal.** On/off/conditional policy toward one chip degraded the information content of US resolve — a live reminder that consistency is part of what makes a signal credible.
5. **This is analysis, not attribution.** The framework tells you what a move would have to cost to be informative. It deliberately stops short of claiming to know intentions — and on a live, contested geopolitical case, that restraint is the responsible use of the tool.

*Sources: US Bureau of Industry and Security (BIS), advanced-computing/semiconductor export control rules (interim final rule, October 7, 2022; updated rules, October 17, 2023), U.S. Department of Commerce — https://www.bis.gov ; Nvidia Corp., Form 8-K and quarterly disclosures — an April 2025 disclosure estimated a charge of approximately $5.5 billion associated with H20 export restrictions, followed by subsequent 2025 policy developments — https://investor.nvidia.com ; China Ministry of Commerce (MOFCOM), export-control announcements on gallium and germanium (July 2023) and subsequent critical-mineral/rare-earth measures (2023–2025) — http://english.mofcom.gov.cn ; Huawei Mate 60 Pro launch (August/September 2023) and third-party teardowns identifying an SMIC ~7nm-class Kirin 9000S; DeepSeek model release and the associated late-January 2025 market reaction, including a historic single-day decline in Nvidia's market capitalization, as widely reported (e.g., Reuters, Bloomberg, Financial Times). Figures are stated as reported/approximate; exact thresholds and conditions evolved across successive rule rounds.*
