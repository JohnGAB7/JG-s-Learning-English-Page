# Writing a complete lesson (JG's Learning English)

JG's request (2026-11-14): the website must replace email lessons, so every lesson must be **extremely complete, correct, reliable and verifiable**, and every level must have **all** its lessons.

## Files
- One lesson = two JSON files with the same number:
  - `tools/data/fr/lessons/<level>-<NNN>.json` — explanations in **French** (examples stay in English, with a French translation or note).
  - `tools/data/en/lessons/<level>-<NNN>.json` — everything in **English** (simple, short sentences at A1–A2; richer from B1).
- `<level>` is a1, a2, b1, b2 or c1; `<NNN>` is the number on 3 digits (a1-007, b2-163).
- Levels: A1 = 1–40, A2 = 41–90, B1 = 91–150, B2 = 151–220, C1 = 221–290.
- **Model to follow exactly:** `tools/data/fr/lessons/a1-001.json` and `tools/data/en/lessons/a1-001.json`.
- `titre` must be **exactly** the title in `tools/data/fr/programme_complet.py` (fr) or `tools/data/en/programme_complet.py` (en). Copy it character for character (curly apostrophes ’ included).
- The short older version of some lessons is in `tools/data/{fr,en}/notions_*.py`: you may reuse its good parts, but the new lesson must be much richer.

## Fields (all required)
- `n` (int), `niveau` ("A1"…"C1"), `titre`, `intro` (1–2 sentences: what and why it is useful).
- `objectifs`: 3–5 "you will be able to…" items.
- `sections`: 4–7 sections that teach the whole notion in depth. Each: `titre`, `texte` (list of paragraphs), optional `tableau` {`entetes`, `lignes`} (every row has as many cells as headers), optional `exemples` [[english sentence, note/translation]], optional `note`. Cover, where relevant: form (affirmative, negative, question, short answers), every use with its signal words, spelling rules, exceptions, register (formal / informal), British vs American differences, contrasts with close notions. At least 8 examples in total.
- `formule`: the core pattern in one line.
- `prononciation`: 3–6 concrete points (IPA in /…/ where useful, stress, weak forms, linking, intonation).
- `erreurs`: 5–8 [wrong, right, why] — the real mistakes French speakers make.
- `dialogue`: {`contexte`, `lignes`: 6–10 [speaker, english line, translation (fr) / short note (en)]} — a natural, realistic scene using the notion. Use varied names and places (Cameroon, Belgium, France, Canada, elsewhere).
- `mots`: 8–10 [word, example sentence, meaning] — useful words linked to the topic. Single words or short expressions that exist in the Cambridge Dictionary. **fr and en must list the same words in the same order** (meaning in French for fr, a simple English definition for en).
- `exercices`: 5–6 exercises from easy to hard (recognise → complete → transform → correct mistakes / translate → free production). Each: `titre` ("1. …"), `consigne`, `items` [[question, answer]]. **At least 20 items in total**, every answer complete and correct. For the free production exercise, give one model answer. **fr and en must have the same number of items in each exercise** (the en version may replace translation exercises by an equivalent English-only task).
- `a_retenir`: 3–6 key points.
- `liens`: 2–5 related lesson numbers (earlier lessons to revise, later ones to go further).
- `refs`: 1–3 keys from `tools/data/references.json` (checked British Council / Cambridge pages). Pick the most relevant topic page; otherwise the level index (bc-a1a2, bc-b1b2, bc-c1) plus a Cambridge section. **Never invent a URL.**

## Quality bar
- Correct, standard English (British spelling by default; mention American differences when they matter). Every example natural and grammatical. Double-check every answer key.
- Teach, don't list: explain *why*, show contrasts, give the traps. A learner should not need another book for this notion at this level.
- Level-appropriate: no structure above the level in examples unless explained.
- Revision lessons ("Révision … et bilan"): sections recap the level's key notions with tables and examples; exercises are a mixed test covering the level; `liens` point to the main lessons revised.
- Vocabulary/function lessons (numbers, family, directions…): sections organise the vocabulary by theme in tables with phrases and usage notes.
- Valid JSON (UTF-8, double quotes, no trailing commas). Use “ ” or « » for quotes inside text, never unescaped ".
- Original writing: do not copy text from other websites.

## Check
Run `python3 tools/validate_lessons.py <first> <last>` from the repo root until it prints "no errors" for your range. Do **not** run tools/build.py, do not edit any other file, do not commit.
