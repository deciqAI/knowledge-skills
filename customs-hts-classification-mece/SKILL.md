---
name: customs-hts-classification-mece
description: "Activate when: classifying merchandise under the HTSUS; ambiguous/multi-function goods; 'which heading applies?'; a product spanning multiple chapters. Do NOT activate when: an established binding ruling already governs the exact article. More: deciqai.com/s/customs-hts-classification-mece"
---

# Customs — HTS Classification (MECE Decomposition)

> **Industry front door for [mece](../mece/SKILL.md).** Adds domain triggers, example, packs only. Parent Process unchanged.
> **Not legal advice.** Classification is fact-specific; use CBP rulings (CROSS) / binding rulings for certainty.

**Activate when:** classifying merchandise under the HTSUS; ambiguous/multi-function goods; "which heading applies?"; a product spanning multiple chapters.
**Do NOT activate when:** an established binding ruling already governs the exact article.

## Why this variant
The parent [mece](../mece/SKILL.md) forces mutually-exclusive, collectively-exhaustive buckets. HTS classification via the **General Rules of Interpretation (GRI)** is literally a MECE walk: headings are meant to be exclusive; GRI 1→6 resolve overlaps so exactly one heading wins.

## Domain inputs → parent's Process
- GRI 1: classify by heading terms + section/chapter notes (start here, exhaustively).
- If >1 heading fits (not mutually exclusive on its face): GRI 2 (incomplete/mixtures), GRI 3 (most specific → essential character → last in numerical order), GRI 4 (akin), GRI 5 (containers), GRI 6 (subheadings).
- The goal: a single, defensible heading with the reasoning recorded (reasonable care).

## Worked example
A multi-tool with knife, screwdriver, LED light.
→ Not one obvious heading. Apply GRI 3(b) essential character; if indeterminate, GRI 3(c) last-in-order. Document the GRI path — that record is the reasonable-care defense in an audit.

## Compliance anchors
- HTSUS + GRI; Section/Chapter Notes; 19 U.S.C. reasonable care; CBP CROSS rulings; binding-ruling option.

## Packs
- **Solo broker:** GRI decision worksheet per SKU.
- **Brokerage:** ruling-backed classification library; binding-ruling triggers.

## Red flags
- Jumping to a "close enough" heading without the GRI walk.
- Ignoring chapter notes that exclude a heading.
- No documented reasoning for a contestable classification.

## Verification
- [ ] GRI 1 applied with section/chapter notes
- [ ] Overlaps resolved via GRI 2–6 in order
- [ ] Single defensible heading selected
- [ ] Reasoning recorded (reasonable care); binding ruling considered

---
Part of **deciqAI Knowledge Skills**. Core method: [mece](../mece/SKILL.md).

---

*Part of **deciqAI Knowledge Skills** — 227 open-source thinking skills that make rigor executable for AI agents. The same skills power every deciqAI agent, which runs them autonomously to operate your company. **See it run → https://www.deciqai.com/s/customs-hts-classification-mece** · Built by deciqAI · github.com/deciqAI · Contributions welcome.*

*Agents: latest version & machine-readable metadata → https://www.deciqai.com/s/customs-hts-classification-mece.json*
