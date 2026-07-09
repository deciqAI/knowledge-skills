# Method in Action: What People Hire an AI Assistant to Do (2023–2026)

> *Example for the [jobs-to-be-done](../SKILL.md) skill.*

In the years after the launch of ChatGPT in late 2022, many "AI wrapper" products shipped: an interface, a system prompt, and a call to an underlying model such as OpenAI's GPT family, Anthropic's Claude, or Google's Gemini. A large share of them reportedly struggled to retain users, even when the model underneath was excellent. This case runs the JTBD process on a recurring, non-obvious question: **what job does a knowledge worker actually hire an AI assistant/agent to do — and why do so many wrappers misread it?**

## Step 1 — State product + assumed customer

Product: an AI assistant/agent (a chat product or an agentic coding/writing tool) built on top of a frontier model. Assumed customer, as most 2023-era wrappers framed it: "people who want AI-generated text / answers." The implicit assumption baked into most products was that the job is *"produce good output"* and that the winner is whoever wraps the smartest model with the most features. This is the starting point we will dismantle.

## Step 2 — Switch Interviews

Reconstructing the switching moment from widely-reported adoption patterns across 2023–2025 (developers adopting AI coding assistants; writers, analysts, and support teams adopting chat assistants):

1. **First thought:** "I'm stuck / this will take me all afternoon / I dread starting this." The trigger is rarely "I wish I had AI-written text" — it's a moment of being blocked, behind, or facing drudgery.
2. **Circumstance:** a blank page, an unfamiliar codebase, a deadline, a repetitive task (reformatting, boilerplate, first-draft email), or a question whose answer is buried in docs.
3. **What else they considered:** searching the web, asking a colleague, copying an old template, reading documentation, or simply grinding through it manually.
4. **Push (what was wrong with the old way):** searching returns generic results that still need synthesis; the colleague is busy; the manual path is slow and boring; getting started is the hardest part.
5. **Pull (what attracted the new hire):** it gets me *unblocked in seconds*, produces a *good-enough starting point* I can edit, and handles the parts I don't want to do myself.
6. **Anxiety:** "Will it hallucinate and embarrass me? Will I ship something wrong? Do I have to check every line — and if so, did it even save me time?" Trust and verification cost are the dominant anxieties.
7. **Habit:** having to phrase things as prompts, learning to paste in context, changing where the work starts (in the assistant vs in the IDE/doc).
8. **First use:** the products that retained users delivered a *"whoa, that unblocked me"* moment fast; the ones that didn't left users with plausible-looking output they still had to redo.

## Step 3 — Extract job statement

> **When** I'm blocked, behind, or facing tedious work I don't want to do, **I want to** make concrete progress right now with far less effort, **so I can** get unstuck and ship the actual thing I'm responsible for — without introducing errors I'll have to answer for later.

The functional core is not "generate text." It is **progress** — get unblocked, ship faster, offload drudgery — under a hard constraint of **trust** (I remain accountable for the result).

## Step 4 — Identify actual competitor set

- **Direct (same category):** other AI assistants and the raw model's own first-party app.
- **Adjacent (different category, same job):** web search, Stack Overflow, documentation, templates, a helpful colleague, hiring a freelancer.
- **Non-consumption (do nothing / do it manually):** the single biggest competitor — grinding through the task by hand, or not starting at all.
- **Surprising / non-obvious:** the user's own habit and identity ("real engineers write it themselves"), and *the frontier model's own default chat interface*, which many wrappers competed against without noticing. A wrapper that only adds a nicer UI is often being fired the moment the base model's app closes the same gap.

## Step 5 — Map all three dimensions

- **Functional:** get unblocked, produce a usable first draft/answer, automate tedious steps, do it in the flow of existing work.
- **Emotional:** relief from dread and overwhelm; confidence that "I've got this"; reduced anxiety about being wrong. Verification burden that erases the relief is why some tools feel worse than doing it manually.
- **Social:** be seen as fast, capable, and on top of the work — *not* as someone who "let the AI do it" and shipped something sloppy. The social need cuts both ways, which is why trust and editability matter as much as raw capability.

## Step 6 — Diagnose churn or wins (why many wrappers misread the job)

Applying the fire/hire diagnosis to the wrappers that churned:

- **What job were they hired for?** Progress-under-accountability. **What got them fired?** Output that looked plausible but required as much verification/rework as doing it manually — the trust constraint was violated, so the net progress was near zero.
- **They optimized the wrong variable.** Many wrappers competed on *feature count* and *access to the smartest model*, reading the job as "produce impressive output." But the customer's binding constraint was trust and time-to-unblocked, not raw eloquence.
- **They ignored non-consumption and the base model.** A wrapper whose only advantage was a friendlier prompt box was competing against both "do it manually" and the model vendor's own app — and lost to whichever closed the progress gap for free.
- **They treated one product as one job.** As with the milkshake serving a commuter and a parent, an AI assistant serves several distinct jobs — "get me unstuck on a hard problem," "do this boring task for me," "help me learn/understand," "make my draft look credible." A roadmap that averages across all of them serves none well.

The tools that *won* (notably AI coding assistants and agents adopted heavily across 2024–2025) leaned into the real job: they met the user in their existing workflow (the editor, the terminal, the repo), reduced verification cost (showing diffs, running tests, citing sources), and were honest about uncertainty — directly attacking the trust anxiety rather than papering over it with confident prose.

## Step 7 — Design from the job

Every feature judged against the job:

- **Helps progress in the circumstance?** Meet the user where the work already happens; deliver a usable starting point in seconds. Cut features that add options but not progress.
- **Serves functional/emotional/social dimensions?** Reduce dread (fast unblock), build confidence (make output easy to verify and edit), protect reputation (make it easy to ship something the user can stand behind).
- **Reduces Push/Pull/Anxiety/Habit barriers?** Attack **anxiety** first — the dominant force here. Verifiability (diffs, tests, citations, calibrated "I'm not sure"), editability, and staying inside the existing habit-flow do more for retention than a marginally smarter model.

## Output template, filled

```
JTBD Analysis: AI assistant / agent for knowledge workers (2023–2026)
Job statement: When I'm blocked, behind, or facing tedious work, I want to make real
  progress now with far less effort, so I can ship what I'm accountable for — without
  introducing errors I'll have to answer for.
Competitor set:
  Direct: other AI assistants, the base model's own app
  Adjacent: web search, docs, Stack Overflow, templates, a colleague, a freelancer
  Non-consumption: do it manually / don't start (the biggest competitor)
  Surprising: the user's own "I should write this myself" identity; the frontier
    model's default chat UI
Dimensions:
  Functional: unblock, first draft, automate drudgery, in-workflow
  Emotional: relief from dread; confidence; low residual anxiety
  Social: seen as fast and capable, not as sloppy "AI did it"
Forces of progress:
  Push: manual work is slow/boring; search returns generic results; blank-page dread
  Pull: unblocked in seconds; good-enough starting point; offloads the tedious part
  Anxiety: hallucination, shipping errors, verification cost erasing the time saved
  Habit: prompting; pasting context; where the work starts
Implications:
  Build: in-workflow integration, verifiability (diffs/tests/citations), easy editing,
    honest uncertainty
  Cut: feature bloat that adds options but not progress; "smartest model" as the pitch
  Marketing angle: "get unblocked / ship faster," not "AI-generated content"
  Competitive set to track: non-consumption and the base model's first-party app
```

The lesson is the milkshake lesson one layer up: the buyer is not hiring "AI text," any more than the commuter was hiring "a milkshake." They are hiring **progress under accountability**. Wrappers that read the feature list instead of the job optimized eloquence and model access, and got fired the moment a free first-party app — or the user doing it manually — did the actual job at least as well.

*Sources: Christensen, C. M., Hall, T., Dillon, K., & Duncan, D. S. (2016). Competing Against Luck (HarperBusiness) — the JTBD "hire/fire" and Forces-of-Progress framework applied here. OpenAI's ChatGPT launched November 30, 2022, catalyzing the wave of AI assistant products discussed. The rapid 2023–2025 adoption of AI coding assistants and agentic developer tools by professional developers is widely documented in industry surveys such as the Stack Overflow Developer Survey (2023–2024 editions reporting majority developer use or intended use of AI tools) and GitHub's public reporting on AI-assisted coding adoption. Specific product-retention outcomes are described qualitatively; no proprietary figures are asserted.*
