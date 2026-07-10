# Method in Action: AI Incidents — Incompetence and Emergent Error as a Prior Over Malice (2024–2026)

> *Example for the [hanlons-razor](../SKILL.md) skill.*

Between 2024 and 2026, as large language models and AI agents moved into mass adoption, a recurring interpretive question arose: when a model produces a harmful, biased, or embarrassing output — or when a competitor makes a surprising, seemingly aggressive move — is the right default *deliberate malice* or *incompetence / honest error / emergent bug*? Hanlon's razor supplies the calibrated starting prior. This walkthrough runs the incident class through the skill's own Process, using two concrete, well-documented public examples.

---

## Case A: A model produces a harmful output

**Anchor:** In February 2024, Google paused the image-generation feature of its Gemini model after it produced historically inaccurate images — including racially diverse depictions of subjects where that was historically wrong. A wave of online commentary framed this as a deliberate ideological agenda encoded on purpose.

### Step 1 — Describe the action and harm (factual, not interpretive)

```
- What was done: A production image model generated historically inaccurate outputs; the vendor
  publicly paused the feature and apologized.
- Harm to me (the observer/user): Loss of trust in the tool; the outputs were wrong and, for
  some prompts, offensive.
- Gut attribution: "They did this on purpose to push an agenda."
```

### Step 2 — Construct the non-malice explanation

```
- Bad information / didn't realize: Post-training fine-tuning and system-prompt-level guardrails
  meant to reduce a KNOWN failure mode (over-representation of one group in image outputs) were
  applied too bluntly and generalized to cases where they produced absurd results.
- Optimizing for: A real, previously-criticized bias problem — over-correction, not a coherent plot.
- Under pressure from: Ship pace; guardrails tuned and tested unevenly across prompt types;
  emergent interaction between the model and the correction layer that was not fully anticipated.
- Coverage: This explains ~90% of the observed behavior — including the vendor's own fast public
  pause-and-apologize, which is what an embarrassed org does, not what a covert-agenda org does.
```

### Step 3 — Name what malice would additionally require

```
- Info they'd need: Foreknowledge that these exact absurd outputs would occur and be shipped anyway.
- Motivation at your expense: A deliberate intent to deceive users, accepting near-certain
  reputational damage and a public reversal — against the vendor's own commercial interest.
- Harm predictable from their position? A deliberate plot predicts a cover-up, not a same-week
  public apology and rollback. The observed response is the OPPOSITE of what malice predicts.
```

### Step 4 — Choose starting posture · Step 5 — Set override signal · Step 6 — Hold prior

```
- Prior: emergent over-correction / honest engineering error (not malice)
- Starting posture: treat as a capability + evaluation failure, not a conspiracy
- First move: read the vendor's own post-incident statement; look for whether the fix is
  process/eval-level (consistent with error) or absent (would raise the malice prior)
- Override trigger: internal documents or credible reporting showing the outputs were a
  KNOWN, intended result shipped deliberately — then update toward malice.
```

---

## Case B: A competitor makes a surprising move

**Anchor:** In early 2025, the Chinese lab DeepSeek released a high-performing open-weight model (DeepSeek-R1) that reportedly matched or approached frontier reasoning models at dramatically lower stated training cost. The release briefly rattled US markets and prompted some commentary framing it as a coordinated strategic strike, sabotage, or fabricated numbers designed to mislead rivals.

### Step 1 — Describe the action and harm (factual)

```
- What was done: A competitor shipped a strong open-weight model and published a low cost figure.
- Harm to me (an incumbent/investor): Competitive threat; a sharp, surprising market reaction.
- Gut attribution: "This is a deliberate psy-op / the numbers are a lie meant to hurt us."
```

### Step 2 — Construct the non-malice explanation

```
- Bad information they had: None required — a genuinely capable lab shipped a genuine result.
- What you didn't realize: Efficient training and open-weight release are ordinary competitive
  strategies; a rival can simply be good at engineering.
- Optimizing for: Their OWN adoption, mindshare, and talent draw — not primarily your harm.
- Coverage: ~85%. "A competent competitor made a strong, self-interested move" explains the
  release fully; it does NOT require any plot against you.
```

### Step 3 — Name what malice would additionally require

```
- Info they'd need: A coordinated intent to manipulate specifically YOUR outcomes.
- Motivation at your expense: Assumes your harm is the goal rather than a side effect of their gain.
- Harm predictable from their position? A rival advancing its own position predicts exactly this
  move WITHOUT any conspiracy — the market reaction is a consequence, not necessarily an aim.
```

### Step 4–6 — Posture, override, hold

```
- Prior: ordinary competent competition (self-interest), not a targeted attack
- Starting posture: benchmark the claim on its merits; compete, don't accuse
- First move: independently verify the published figures rather than assuming fabrication;
  "surprising" is not "dishonest"
- Override trigger: reproducible evidence the headline numbers were knowingly falsified, or
  documented coordination aimed at your specific harm — then update.
```

---

## Why the razor is the right prior here — but only a prior

Modern AI systems make the mistake-prior *more* defensible than in ordinary human affairs, because they add failure modes that look intentional but are not:

- **Emergent behavior.** Outputs arise from statistical training over vast data; harmful or biased results routinely appear that no engineer designed, chose, or foresaw. "It happened" does not imply "someone wanted it to."
- **The correction-layer interaction.** Guardrails, system prompts, and fine-tuning can interact with the base model to produce absurd results — an *accident of composition*, not a hidden message.
- **Competitive surprise ≠ sabotage.** A rival's self-interested move can hurt you as a side effect while your harm is not the goal — the fundamental attribution error (Ross 1977) pushes observers to read intent into what is structural incentive.

And the same guardrails from the SKILL apply. The razor is a **prior, not a proof**:

- It does **not** excuse harm. A biased output is still harmful and still demands an evaluation/process fix — attribution is not accountability.
- **Override on evidence.** If credible reporting or internal documents show a harmful output was a *known, intended* result shipped deliberately, or that a competitor knowingly falsified results to damage a specific rival, update toward malice.
- **Watch the power/stakes asymmetry.** Where the cost of wrongly assuming non-malice is catastrophic (safety-critical deployment, deceptive-by-design products), shift toward a defensive posture *before* intent is proven.

**Operational takeaway:** For 2024–2026 AI incidents, default to *emergent bug / honest error / ordinary self-interested competition* as the starting explanation, run the mistake-coverage estimate, name what malice would additionally require, and pre-commit an override signal. This produces a diagnostic conversation (root-cause, evals, verification) rather than a conspiracy narrative — while leaving the door open to update the moment real evidence of intent arrives.

*Sources: Google, "Gemini image generation got it wrong. We'll do better." (The Keyword / official Google blog, February 23, 2024); reporting on the Gemini image-generation pause, e.g., The Verge and BBC News (February 2024). DeepSeek, "DeepSeek-R1" release and technical report (January 2025); contemporaneous market-reaction reporting, e.g., Reuters and the Financial Times (late January 2025). Ross, L. (1977). "The intuitive psychologist and his shortcomings," Advances in Experimental Social Psychology, 10, 173–220. Exact cost/benchmark figures are as publicly reported by the vendors and had not been independently verified at the time of the events.*
