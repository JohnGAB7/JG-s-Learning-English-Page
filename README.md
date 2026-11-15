# JG's Learning English

A guided English-learning library from A1 to C1, with self-paced lessons and a curated world-news desk.

## Product direction

This repository powers a static website. Learners can open lessons directly without relying on crowded email threads. Email remains a lightweight notification channel; the site is the canonical home for learning content.

## Main areas

- **Learning paths** — CEFR levels A1, A2, B1, B2 and C1.
- **Lessons** — one page per notion, with explanation, examples, vocabulary, audio links, practice, answer key and common mistakes.
- **Practice Studios** — six skill-specific environments for listening, pronunciation, reading, writing, vocabulary and review.
- **News** — important world stories plus a country selector for country-focused coverage.
- **About** — method, editorial standards and how to use the platform.

## Initial lesson migration

The first migration set is based on lessons previously distributed by email:
- A1: 1–8
- A2: 41–48
- B1: 91–96
- B2: 151–157

Do not invent or silently rewrite source lessons. Import the original teaching content, then edit with a clear review trail.

## Architecture

- Static HTML/CSS/JavaScript; no framework required for the first release.
- Lesson data stored separately from page templates.
- News stored as structured records with publication date, country tags and source URLs.
- Country selection is a client-side filter, not a geolocation feature.
- GitHub Pages serves the `docs/` directory of `master` ("Deploy from a branch"). The custom workflow in `.github/workflows/pages.yml` is manual-only.

## Content quality

- Bilingual: French is the default (explanations in French, examples in English) and /en/ is the full English version, with a FR / EN switch on every page. Content lives in tools/data/fr/ and tools/data/en/. Decision of JG, 2026-11-14.
- Every vocabulary item includes a Cambridge Dictionary UK/US pronunciation link where available.
- Every news item must cite a reliable original source and show its publication date and relevant geography.
- Clearly label editorial context separately from reported facts.
- No fake live news, no fabricated links, and no implication that the news feed updates automatically unless a verified data pipeline exists.

## Site map
| Area | Path | Content | Source |
|---|---|---|---|
| Home | `docs/index.html` | overview, workshops, levels | `tools/build.py` |
| Path | `docs/path/` | full A1–C1 programme by skill | `tools/data/fr/espaces.py`, `tools/data/en/espaces.py`, `programme_complet.py` |
| Speak | `docs/speak/` | real-life topics, videos to imitate, shadowing | `tools/speaking.py` + localized universes in `tools/data/{fr,en}/espaces.py` |
| Lessons | `docs/lessons/<level>-<number>/` | one page per lesson, e.g. `lessons/b1-096/` | `tools/data/notions_*.py` |
| Studios | `docs/studios/` | six skill-specific practice experiences | `tools/studios.py`, `tools/build.py`, and `tools/data/{fr,en}/espaces.py` |
| Review | `docs/review/` | flip cards for every lesson word | built from the lessons |
| News | `docs/news/` | world + country tabs, each item sourced | `tools/data/{fr,en}/actualites.json` |
| About | `docs/about/` | method, commitments | `tools/build.py` |

Every page is generated: never edit `docs/` by hand. Add a lesson or a news item in `tools/data/`, then run `python3 tools/build.py`.

## Practice Studios — implementation layer (2026-11-15)

- The six Studios are practice engines over the canonical lesson corpus, not a second curriculum.
- `tools/studios.py` stores stable activity IDs, studio/skill, CEFR level, source lesson, duration, learning outcome, interaction type, explicit completion rule, editorial/media status and quiz data.
- `tools/build.py` validates the activity contracts and renders the bilingual Studio experiences. It reuses lesson dialogues, pronunciation notes, vocabulary and exercises rather than copying lesson content into a parallel catalogue.
- `tools/validate_studios.py` checks all six pilot activities against the English and French lesson corpus, including source existence, CEFR consistency and whether quiz evidence appears in the source dialogue.
- The Studio hub tracks completion across all six activities in browser-local storage. Listening/Reading complete on a correct answer; Pronunciation requires all self-checks; Writing requires a saved 50–70-word draft plus its self-checks; Vocabulary requires a new sentence plus a learner self-check; Memory is learner-confirmed after a review session.
- Checklists and vocabulary practice sentences are also stored locally. The interface discloses that progress is device/browser-specific and reports when browser storage is unavailable; no account or server profile is implied.
- Current pilots: Listening (A2-041), Pronunciation (B1-091), Reading (B1-091), Writing (A2-041), Vocabulary (B1-091), and Memory & Review (the existing review-card engine).
- Browser speech synthesis is synthetic practice audio, not a human recording. Pronunciation is self-assessed; no automatic speech score is claimed. Writing drafts stay in the browser and are not automatically corrected or uploaded.
- Validate with `python3 tools/validate_speaking.py` and `python3 tools/validate_studios.py`; then build locally with `python3 tools/build.py` when local validation is authorised. Do not run GitHub Actions or deploy without the owner's explicit approval.

## Visual identity
- **All colours live in `tools/palette.css`** (`:root` variables): Forest Green `#173A36`, Ivory `#F7F5EF`, Soft Gold `#C9A96E`, Sage Green `#A8B8A2`, Deep Teal `#315C57`, Warm White `#FFFEFA`, Charcoal `#292D2B`, Muted Grey `#777D77`.
- Workshop colours: Listening Studio `#7896A8`, Pronunciation Lab `#B97858`, Reading Room `#8FA58A`, Writing Workshop `#B98268`, Vocabulary & Expressions `#C9A96E`, Memory & Review `#547F80` (`--ws-*`). Use them through `data-ws="<key>"`, never as raw hex.
- Forest green + ivory are the base; gold is for accents only; text and buttons must keep WCAG AA contrast.
- The theme files in `tools/theme/` come from Actu-Basics unchanged; the build rewrites their hard-coded colours to palette variables (`COLOUR_MAP` in `tools/build.py`).
- Logos: originals in `assets/brand/`; web sizes and favicon (dark logo) in `tools/brand/`. Light logo on light theme, dark logo on dark theme.

## Repository status

Online lesson counts are derived from the validated lesson data during the build. Do not maintain a separate manual count here; the generated Lessons and Path pages are the source for current availability.


## Speak and practice platform expansion (2026-11-14)

- The current default branch is bilingual: French is the default and `/en/` is the English edition. New Speak work must preserve both editions.
- Shared Speak taxonomy and validation live in `tools/speaking.py`; language-specific source universes remain in `tools/data/fr/espaces.py` and `tools/data/en/espaces.py`.
- The original 24 topic definitions are retained, with 18 additional non-duplicate topics, for 42 topics across six universes. Stable IDs are language-independent.
- **Start from zero** is a separate pre-A1 entry point. It does not replace A1.
- The first complete published pilots are A1 Daily routine and A2 Food and dining out. Other topic/level records stay planned until authored.
- All six Studios now have a first usable activity. Browser speech synthesis is not recorded human audio.
- Speaking filters combine text, CEFR level, skill and editorial status. Learners can save notes and mark published units complete locally in their browser.
- News learning cards render only when level, summary, vocabulary, comprehension questions and discussion prompt are all supplied. Current records remain source-linked headlines.
- Review is active recall with local difficulty weighting, not a scheduled 3/7/30-day reminder system. Do not promise weekly Anki/Quizlet delivery.
- Validate the catalogue with `python3 tools/validate_speaking.py`; build both editions with `python3 tools/build.py`. Do not run GitHub Actions or deploy.
