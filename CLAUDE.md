# Claude — project handover

## Identity and objective
Project name: **JG's Learning English**.
Build a polished, accessible English-learning platform from A1 to C1. The website is the canonical library of lessons; email should be reduced to concise notifications and reminders, not full lesson delivery.

## Repository facts
- Repository: JohnGAB7/JG-s-Learning-English
- Default branch: master
- GitHub Pages source: GitHub Actions workflow in .github/workflows/pages.yml
- Static site root: docs/
- The repository is currently private. GitHub Pages availability depends on the owner's plan and repository settings; do not assume deployment is enabled.

## Design direction
- Premium editorial learning platform: dark deep-teal hero, warm off-white background, muted green/lime accents, elegant serif headlines and clean sans-serif body text.
- Calm, confident, modern, readable. Avoid gamified clutter and dense dashboards.
- Mobile-first, accessible navigation and visible keyboard focus.
- The first scaffold is intentionally framework-free HTML/CSS/JS.

## Main navigation
1. Home
2. Parcours A1–C1 — full CEFR curriculum
3. Speak English in Real Life — everyday speaking and real-life conversation lab with authored dialogues and guided practice
4. Lessons library, searchable/filterable
5. Practice Studios — listening, pronunciation, reading, writing, vocabulary and review
6. News: world coverage + country selector (Cameroon, Belgium, France, Canada initially)
7. About / method

## Two separate pedagogical spaces

### English Foundations & Mastery
A complete A1–C1 curriculum. Each level covers grammar/sentence building, vocabulary/collocations, pronunciation, listening, speaking, reading, writing and functional English. The CEFR page describes scope and objectives; it is not a claim that all lesson content is already authored.

### Speak English in Real Life
A separate cross-level conversation lab organised by real-life themes, not grammar chapters. Initial theme clusters: daily routines and personal life; interests and hobbies; work, studies and ambitions; family, relationships and social life; practical everyday situations; opinions, ideas and storytelling.
Each theme should support a model dialogue, optional audio/transcript, key expressions, pronunciation notes, listen-and-repeat, shadowing, personal substitutions, guided Q&A, spontaneous response and self-assessment. Same theme can recur from A1 to C1 with increasing complexity. Never show a video as available unless the actual media exists; use a clearly marked coming-soon state.

The full architecture and content model are in `docs/architecture-pedagogique.md`. Speaking lab page: `docs/speak/index.html` (generated from `tools/build.py`).

## Lesson design standard
Each notion gets an independent canonical URL and must contain:
- CEFR level, notion number and objective
- Explanation in French on the default site, and in English on the /en/ version (simple English at A1/A2, richer from B1; JG, 2026-11-14)
- Clear rule and form/usage notes
- Affirmative, negative and question forms where relevant
- Short examples with a brief English note
- Five contextualized vocabulary words, each with Cambridge Dictionary audio/pronunciation link when available
- Typical mistakes / pitfalls
- Active-recall exercises and progressive practice
- Collapsible answer key and explanation
- Related lessons and spaced-revision links

## Migration set from earlier email editions
- A1: 1–8
- A2: 41–48
- B1: 91–96
- B2: 151–157
Preserve original numbering. Import full original lesson content from source messages/files; do not invent content or claim reconstructed material is the original. The A1.01 page in the scaffold is a proposed introductory sample and should be cross-checked against the actual sent lesson before marking it as migrated. The A2.41 page is explicitly a placeholder.

## News standard
- Separate world news from country-tagged news.
- Country selection is explicit UI selection; do not geolocate.
- Every item must show publication date, source publisher, source link, countries/tags, concise summary and why it matters.
- No false live-feed claims. Do not publish a story unless sources are current and verified.
- Keep content records separated from templates, preferably JSON data files.

## Operational constraint — GitHub Actions
John reports that the monthly GitHub Actions minutes quota is exhausted and has received workflow error emails. Do not manually run, rerun, dispatch, or test any workflow. The Pages workflow currently has a push trigger on `docs/**`; commits to those paths can automatically trigger it. Before further pushes to the default branch that touch `docs/**`, first arrange to neutralize the automatic push trigger without running a workflow, or work on a branch until the owner can safely merge after quota renewal. Do not claim deployment or successful tests unless verified.

## Technical next steps
1. Run link and mobile checks across all pages.
2. Confirm GitHub Pages availability for this private repository and its Actions permissions.
3. Import and verify the exact lesson source texts.
4. Replace placeholder news cards with sourced, timestamped records.
5. Add search indexing and a lesson catalogue data model.
6. Test accessibility, keyboard navigation, broken links and responsive layout.

## Generated content (Claude, 2026-11-14)
- **Bilingual site (JG, 2026-11-14, 16:05): French is the default** (docs/, explanations in French, examples in English) and **docs/en/** is the full English version for learners who want immersion. Every page has a FR / EN switch to its twin page. Lesson URLs used in emails (docs/lessons/<a1-001>/) are the French pages.
- Every page is generated by `python3 tools/build.py` from `tools/data/fr/` and `tools/data/en/` (same files in each: notions_a1_a2.py, notions_b1_c1.py, programme.py, programme_complet.py, espaces.py, actualites.json). A new lesson must be written in both folders with the same number. Never hand-edit `docs/`. The build strips the old Actu-Basics brand name from the inherited theme files and fails if it remains.
- URLs (same under en/): path/, speak/, lessons/<a1-001>/, studios/, review/, news/, about/. The old French paths (parcours, parler, lecons, ateliers, reviser, actualites, apropos) are gone.
- The 30 lessons (A1 1-8, A2 41-48, B1 91-96, B2 151-157, C1 221) were written for the site from the email programme, keeping the original numbering; they are not verbatim copies of the sent emails.
- Colours: `tools/palette.css` is the single source of truth (JG's palette + six workshop colours). See README "Visual identity". Logos in `assets/brand/` (originals) and `tools/brand/` (web sizes, favicon from the dark logo).
- The Studios page integrates the "Practice Studios" hub JG added on master (commit 3e6c074), translated to English.

## Deployment
- GitHub Pages is set to "Deploy from a branch" (master, **root folder**), so the site lives at https://johngab7.github.io/JG-s-Learning-English/docs/ and the root `index.html` redirects there. If JG switches the Pages folder to /docs, the URL drops "/docs/" and the root redirect becomes unused. The built-in "pages build and deployment" run publishes the site. The custom `pages.yml` workflow failed on every push (it needs Source = GitHub Actions), so its push trigger was removed; it is manual-only. Do not run it.


## Current implementation status — 2026-11-14

- Bilingual default is French, with the English edition under `docs/en/`. Preserve FR/EN parity in all additions.
- Speak catalogue: 42 topics across six universes, based on the original 24 plus 18 non-duplicate additions. Shared model and stable IDs: `tools/speaking.py`.
- The Pre-A1 entry point **Start from zero** is separate from CEFR A1.
- Complete published pilots: Daily routine A1 and Food and dining out A2. Keep every other topic/level planned until the full learning unit is authored.
- Published unit standard: situation, outcomes, model dialogue, expressions, contextual vocabulary, grammar, pronunciation, guided questions, role-play, personalisation, writing and self-check.
- Six Studios each have a first functional activity. Browser speech synthesis is generated by the browser and must not be described as a recorded speaker.
- Local browser storage saves explicitly requested practice notes and unit-completion state. No user account or server-side profile exists.
- News cards are only full learning sheets when levelled summary, vocabulary, comprehension and discussion fields are complete. Current records remain source-linked headlines.
- Review uses active recall and local difficulty weighting; no scheduled 3/7/30-day review engine or weekly Anki/Quizlet distribution is implemented.
- Validate with `python3 tools/validate_speaking.py`; build locally with `python3 tools/build.py`. Never edit generated `docs/` files by hand. Do not run GitHub Actions or deploy.


## Practice Studios — implementation contract (2026-11-15)

- The six Studios are practice engines over the canonical lesson corpus. Do not create a parallel curriculum or duplicate lesson content unnecessarily.
- `tools/studios.py` is the canonical contract for pilot activities: stable `activity_id`, studio, CEFR level, source lesson, duration, learning outcome, interaction type, explicit `completion_rule`, editorial/media status and quiz evidence.
- `tools/build.py` validates those contracts before rendering. The same source lesson can power several distinct skill experiences, but each task must have a clear learning outcome and a traceable source.
- `tools/validate_studios.py` checks all six activities against both language editions, including source existence, level consistency, required source material and quiz evidence. Run it alongside `tools/validate_speaking.py` before a local build when authorised.
- Current pilots: Listening uses A2-041; Pronunciation and Reading use B1-091; Writing uses A2-041; Vocabulary uses B1-091; Memory & Review reuses the existing review-card engine.
- Browser speech synthesis must remain labelled synthetic. Do not claim human recordings, automatic pronunciation scoring, AI writing correction or server-side draft storage unless those capabilities are actually implemented.
- Writing drafts are local to the learner's browser. Word-count guidance is 50–70 words; the learner may still save a draft outside that range.
- The six Studio completion states are stored locally: Listening/Reading by correct quiz response; Pronunciation by all self-checks; Writing by saved 50–70-word draft plus checklist; Vocabulary by a learner-written example sentence plus an explicit self-check; Memory by explicit review-session confirmation. Pronunciation, Writing and Vocabulary checklist state, plus the Vocabulary sentence, are local too. This is not account-backed or cross-device progress. The JavaScript completion evaluator fails closed on unknown rules.
- Generated pages remain under `docs/` and must never be edited by hand. No workflow, CI run, deployment, merge or change to `master` without John's explicit approval.

## Current complementary implementation branch

- `feat/studios-practice-engine-current` is based on the current `master` and contains the Studio implementation plus its validation contract.
- It was reconstructed from the earlier `feat/learning-platform-expansion-current` branch so it includes the latest lesson corpus on `master` without copying generated `docs/` changes.
- The earlier branch remains intact for comparison. PR #2 remains separate and unmerged; compatible theme changes are already present in this branch.
- No local build, automated validation, browser test, GitHub Actions workflow or deployment is claimed by this handover.

