# Method in Action: Fine-Tuning a Third-Party Model on Proprietary Data (Reverse Information Paradox, 2026)

> *Example for the [reverse-information-paradox](../SKILL.md) skill.*

Nadella's July-2026 thesis names fine-tuning and retrieval on proprietary data as a textbook site of the Reverse Information Paradox: to make a general model perform on *your* domain, you must feed it your domain — and "the more of that knowledge you have to feed it," the more of your know-how leaves your boundary. Walk it through the Process. (Composite illustration of the described pattern.)

**Setup.** A mid-size insurer wants a domain model that drafts underwriting memos in-house style. Two paths on the table: (1) fine-tune the vendor's foundation model on 200,000 historical underwriting decisions, and (2) RAG over the same corpus. The data science team is ready to upload the training set to the vendor's fine-tuning API.

**Step 1 — Map the exhaust.** Fine-tuning path: the *entire* labeled decision history goes to the vendor — the single richest record of how the organization works and makes decisions the firm owns. RAG path: retrieved documents plus queries flow at inference time. Corrections and the eval rubric flow in both. Gate passed: each stream and its revealed fact named — the 200k decisions *are* the underwriting playbook.

**Step 2 — Classify what it reveals.** The training corpus and the eval rubric are the two most competitively-sensitive assets the insurer has; they encode its risk appetite and pricing judgment. Neutral streams: essentially none. Gate: everything here is sensitive.

**Step 3 — Locate the learning loop's owner.** Key question for the fine-tune path: where do the *adapted weights* live, and can the vendor use the training data or the resulting weights beyond this tenant? The default fine-tuning terms give the vendor a hosted adapter and broad usage rights on submitted data. Loop owner: *vendor* — the insurer would be paying to improve an asset it does not control.

**Step 4 — Decide the trust boundary.** Decision: prefer RAG with the index and embeddings on the insurer's side; if fine-tuning is used, require that the adapted weights be delivered to and hosted in the insurer's tenant, with a contractual bar on the vendor reusing the training data. Data, evals, memory, adapted weights, learning loop — all assigned **inside**. The eval rubric never leaves.

**Step 5 — Orchestration for portability.** Build retrieval and evaluation in an orchestration layer; keep the base model swappable. Confirm the RAG corpus and eval set move to a different base model without re-surrendering anything. If a vendor will only host the adapter on its side with no export, that is logged as a decision, not accepted as a default.

**Step 6 — Whose moat compounds.** Uploading 200k decisions to a shared fine-tuning pipeline would have handed the insurer's core judgment to a vendor whose model may serve rival carriers. RAG-on-own-side plus tenant-hosted weights keeps the flywheel — better drafts from every correction — compounding for the insurer.

**Intelligence Exhaust Map (abbreviated):**
```
# Intelligence Exhaust Map: Underwriting-memo domain model
Exhaust streams: 200k labeled decisions [SENSITIVE], inference queries, corrections,
  eval rubric [SENSITIVE]
Learning-loop owner (fine-tune default): vendor → (chosen): RAG own-side + tenant-hosted weights
Trust-boundary: data=inside · evals=inside · memory=inside · adapted weights=inside · loop=inside
Orchestration/portability: base model swappable; RAG corpus + eval set portable
Whose moat compounds: was vendor (shared fine-tune) → now insurer
Decision: RAG on own side; fine-tune only with tenant-hosted, non-reusable weights — owner: Head of DS
```

**What it explains.** The fastest route to a "custom model" — hand the vendor your labeled history — is the one that most fully realizes the paradox: you pay in cash *and* in the surrender of your entire decision record. RAG on your side of the boundary, and fine-tuning only with tenant-hosted, non-reusable weights, gets the domain performance without giving away the loop.

**Founder takeaway:** "Fine-tune on our data for a custom model" only makes you stronger if the adapted weights and the training corpus stay inside your boundary. If the vendor keeps the weights and reuse rights, you've paid to improve *their* asset. Default to RAG on your own side; make tenant-hosting and no-reuse a hard requirement before any proprietary corpus leaves.

*Sources: Satya Nadella, "Reverse Information Paradox" strategy essay, published 2026-07-12 (verbatim: "The better you want the model to perform, the more of that knowledge you have to feed it."). Coverage: MIT Sloan Management Review Middle East (https://mitsloanme.com); ANI News, 2026-07-13 (https://www.aninews.in); PPC Land (https://ppc.land). Parent concept: Kenneth J. Arrow (1962), "Economic Welfare and the Allocation of Resources for Invention," Princeton University Press. July-2026, single-origin thesis presented as a contemporary strategic argument, not established empirical canon; the insurer above is a composite illustration.*
