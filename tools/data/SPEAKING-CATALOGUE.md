# Speak catalogue — source and editorial rules

The shared data model is in `tools/speaking.py`. It assigns language-independent
IDs to the original 24 topics and adds 18 complementary topics (42 total).
Localized titles, descriptions and existing topic definitions come from
`tools/data/fr/espaces.py` and `tools/data/en/espaces.py`.

## Editorial states

- `planned`: topic/level reserved; no learner unit is advertised.
- `draft`: content being written.
- `needs_review`: content written, awaiting review.
- `reviewed`: checked and ready to publish.
- `published`: complete learner-facing unit.

Every topic carries all five CEFR level states. Pre-A1 **Start from zero** is
an entry point, not a sixth CEFR level or a replacement for A1.

## Unit standard

Real-life situation, outcomes, model dialogue, natural expressions,
contextual vocabulary, useful grammar, pronunciation focus, guided questions,
role-play, personalisation, writing task and self-check. Media assets are
separate: browser speech synthesis is not described as recorded human audio.

The initial published pilots are A1 **Daily routine** and A2 **Food and dining
out**. All other topic/level combinations remain planned until fully authored.

## Validation

Run `python3 tools/validate_speaking.py` to check bilingual topic-ID parity,
six universes, topic count and published-unit completeness. The normal site
build also validates each language catalogue.
