# Studio review, lesson sample audit and collaboration contract

Date: 2026-11-15  
Repository: `JohnGAB7/JG-s-Learning-English`  
Complementary implementation branch: `feat/studios-practice-engine-current`  
Related review: PR #2 — `feat/platform-polish-for-claude-review`

## 1. Product boundary

The six Studios defined in `tools/data/en/espaces.py` are the correct six skill environments:

1. Listening Studio
2. Pronunciation Lab
3. Reading Room
4. Writing Workshop
5. Vocabulary & Expressions
6. Memory & Review

They should not become a second curriculum. The canonical lesson files remain the source of truth for grammar, vocabulary, examples, pronunciation notes, dialogues, exercises and references. Studios should turn selected lesson material into deliberate practice, with a clear return path to the source lesson.

The intended learning loop is:

**Understand in a lesson → practise one skill in a Studio → retrieve from memory → use it in Speak or writing → return to the next lesson.**

## 2. What the existing source already provides

The rich lesson schema contains enough reusable material to start building useful practice:
- CEFR level, number, title and learning objectives;
- structured sections, explanations, examples and grammar patterns;
- pronunciation notes;
- common learner errors;
- contextual dialogues with speaker turns;
- 8–10 vocabulary items with example sentences and meanings;
- progressive exercises and answer keys;
- related lesson IDs and checked references.

Examples reviewed from the English source:
- **A1-001 — The verb “to be”**: 4 teaching sections, 4 pronunciation notes, 5 common errors, a 6-line dialogue, 8 vocabulary items and 21 exercise items.
- **A2-041 — The past simple: regular verbs**: 5 teaching sections, 5 pronunciation notes, 7 common errors, an 8-line Brussels dialogue, 10 vocabulary items and 30 exercise items. Its pronunciation notes explicitly teach the three -ed endings.
- **B1-091 — The present perfect**: 6 sections covering experiences, present results, continuing situations and the contrast with past simple; 8 dialogue turns; 9 vocabulary items; 24 exercise items.
- **B2-151 — The passive voice**: 6 sections covering form, communicative purpose, by-phrases, two objects, prepositional verbs, questions, negatives and the get-passive; 8 dialogue turns; 10 vocabulary items.
- **C1-221 — Idioms at work**: 5 sections covering workplace idioms, projects, decisions and register; 8 dialogue turns; 10 vocabulary items.

These are promising content foundations. This was a representative sample, not a linguistic audit of every lesson.

## 3. Specific lesson-review findings

### Positive
- The rich schema is much stronger than a short grammar summary: it combines explanation, examples, pronunciation, errors, dialogue, vocabulary, exercises and references.
- The lesson specification establishes a useful minimum bar: at least 8 examples, 8–10 vocabulary items, 20 exercise items, 5–6 progressive exercises and matching vocabulary/order and exercise item counts between French and English.
- A2-041 is particularly useful as a Studio source because the dialogue and its -ed pronunciation notes reinforce the same learning objective.

### Corrections and risks
1. **A1-001 exercise numbering is out of order:** exercise 5 appears before exercise 4. This is a small editorial defect, but it is visible to learners and should be corrected.
2. **Structural validation is not editorial validation.** A schema checker cannot prove that English sounds natural, that every answer is correct, that examples are varied, or that a task is truly CEFR-appropriate. Those need editorial review and answer-key sampling.
3. **The source JSON inventory is asymmetric:** the current `master` tree contains 146 French lesson JSON files and 144 English lesson JSON files. The two French-only filenames are `a2-084.json` and `b1-119.json`; there are no English-only counterparts. Confirm whether these are intentionally covered by the legacy-data fallback or represent missing translations.
4. **Do not confuse JSON-file inventory with published lesson count.** The build uses `validate_lessons.check()` to decide whether a rich JSON record is accepted; invalid/incomplete records may fall back to the older catalogue. The README's manual “40 lessons online / 250 coming soon” statement should ultimately be generated from the same validated build result.
5. The build-level `check()` has a lower exercise-item threshold than the dedicated lesson validator. Keep one authoritative quality contract so the thresholds cannot drift.

## 4. Current Studio implementation on the complementary branch

The complementary implementation is maintained on `feat/studios-practice-engine-current`, based on the current `master`. It develops the first Studio pass using the existing lesson records rather than creating a separate curriculum.

| Studio | First activity on the branch | Source / interaction |
|---|---|---|
| Listening | Listen before revealing the transcript; answer a comprehension question | A2-041 dialogue; browser speech synthesis; transcript reveal |
| Pronunciation | Slow and natural-speed model, repeat and self-check | B1-091 dialogue and pronunciation notes |
| Reading | Read a lesson dialogue and answer a comprehension question | B1-091 dialogue |
| Writing | Short past-event writing brief, word count, self-review rubric and local draft saving | A2-041; draft remains in the browser |
| Vocabulary | Reveal meaning and example after attempting recall | B1-091 lesson vocabulary |
| Memory & Review | Continue into the existing review-card system | Existing Review experience |

The implementation is deliberately honest about limitations:
- browser speech synthesis is synthetic, not recorded human/native-speaker audio;
- no automatic pronunciation scoring is claimed;
- writing is not automatically corrected or uploaded;
- the first activities are pilots, not a complete graded catalogue across A1–C1.

Core source files include `tools/build.py`, `tools/extra.js`, `tools/extra.css`, `tools/studios.py` and `tools/validate_studios.py`, plus the Speak catalogue and theme changes carried forward from the earlier branch. No generated `docs/` files were edited, and no workflow, build, deployment or browser test was run.

## 5. What “professional-grade” should mean next

The current pilots are a foundation, not the final destination. The next architecture should make the Studios reusable and data-driven.

### Shared activity contract
Every activity should have:
- stable `activity_id`;
- Studio / skill;
- CEFR level and any prerequisite;
- learning objective and success criteria;
- estimated duration;
- source lesson IDs;
- content and media status;
- interaction type;
- task instructions;
- answer key or transparent self-review rubric;
- completion / retry behaviour;
- accessibility metadata and language variant.

A shared renderer should handle common behaviours: instructions, progress, answer feedback, transcript reveal, local draft saving, completion state and source-lesson links. Studio-specific components should only implement the interaction unique to that skill.

### Listening Studio — progression
1. Gist: identify topic, speaker intention and situation.
2. Detail: names, dates, places, sequence and reasons.
3. Inference: attitude, implied meaning and stance at higher levels.
4. Transcript reveal and phrase-level replay.
5. Vocabulary / connected-speech noticing.
6. A short retell or spoken response.

Real audio should eventually be recorded or sourced with explicit rights and accent metadata. Until then, generated speech must remain clearly labelled as synthetic.

### Pronunciation Lab — progression
- phoneme contrasts and minimal pairs;
- word stress and sentence stress;
- weak forms, linking and reductions;
- rhythm, thought groups and intonation;
- listen → notice → imitate → shadow → produce independently;
- optional self-recording, with no automated score unless a reliable assessment model is genuinely implemented.

### Reading Room — progression
- skimming for gist;
- scanning for evidence;
- reference and cohesion;
- inference and writer stance;
- vocabulary in context;
- source evaluation and critical reading at B2–C1.

Use reviewed lesson content or separately sourced and verified texts. Never label a synthetic text “authentic”.

### Writing Workshop — progression
- sentence accuracy;
- paragraph cohesion;
- message / email / narrative tasks;
- register, audience and purpose;
- argument, synthesis and professional writing;
- transparent rubric (task fulfilment, organisation, range, accuracy, register);
- local draft storage and export. Automated feedback is a separate future capability.

### Vocabulary & Expressions — progression
- recognition → retrieval → sentence completion → productive use;
- collocations and lexical chunks;
- word families and morphology;
- phrasal verbs and idioms in context;
- register and connotation at B2–C1;
- link each item to its lesson and a real example.

### Memory & Review — progression
- mixed retrieval across lessons and skills;
- review priority based on learner difficulty;
- spaced intervals with visible, explainable rules;
- progress stored locally unless the user later chooses an account-backed system;
- export only when a tested export exists.

## 6. Acceptance criteria before calling the Studios production-ready

- Six Studios have a distinct, useful end-to-end activity.
- Each activity has a CEFR level, a learning outcome, clear instructions and a source lesson or verified source.
- Every quiz has a checked answer key; every open task has a usable rubric.
- No empty sections, fake audio, fabricated “native” recordings or misleading availability labels.
- Keyboard-only operation, visible focus, screen-reader labels, reduced-motion support and mobile layouts.
- Local storage failures are handled gracefully; no learner draft is sent anywhere without consent.
- French and English versions remain in parity wherever both are published.
- A validation script checks activity IDs, source lesson existence, answer completeness, level/status consistency and media availability.
- Build and browser checks are performed only when the repository owner authorises them and the Actions/deployment constraints are resolved.

## 7. Collaboration contract

- Claude owns the canonical lesson corpus, lesson authoring and its source-of-truth rules.
- This complementary branch focuses on Studio practice experiences and lesson → practice → review connections.
- Do not duplicate lesson content into independent Studio prose where a lesson reference or reusable data record will do.
- Coordinate changes to `tools/build.py` and shared data contracts before parallel edits.
- Keep all generated pages in `docs/` out of manual edits.
- No merge, workflow launch or deployment is authorised by this report.


## 8. Consolidation update — 2026-11-15

### Branch reconciliation
- The earlier branch `feat/learning-platform-expansion-current` had diverged from the current `master` (44 commits ahead, 5 behind at the time of review).
- A clean complementary branch, `feat/studios-practice-engine-current`, was created from the current `master`. The earlier source changes were ported without copying generated `docs/` output.
- The new branch includes the latest canonical lesson data on `master`; it was verified as ahead of `master` with no commits behind immediately after reconstruction. The old branch remains untouched.
- The theme token file is byte-for-byte identical to the current PR #2 version. The theme JavaScript has the same behaviour, with only a compatibility-comment wording difference. PR #2 remains separate and unmerged.

### Studio activity contract implemented
- `tools/studios.py` now defines stable activity IDs, studio, CEFR level, source lesson/source collection, duration, bilingual learning outcome, interaction type, explicit completion rule, content status, media status and quiz evidence.
- `tools/build.py` validates the six activity contracts before rendering and derives lesson references, duration labels and comprehension questions from the contract rather than repeating lesson IDs and quiz options in the HTML.
- The listening and reading quiz answer keys are checked against evidence in their source dialogue, and the declared correct option must contain that evidence. Correct-answer explanations and retry hints are stored with the activity data and surfaced to learners.
- The five lesson-based Studios expose stable `data-activity-id` values; Memory & Review is linked to the validated lesson-vocabulary collection.
- The writing activity now makes its 50–70 word target explicit and reports below-range, in-range and above-range states without preventing the learner from saving a draft.
- The Studio hero copy now describes the lesson library as the shared foundation, rather than incorrectly implying that every activity maps to exactly one lesson.

### Learner progress layer — 2026-11-15
- Added a six-activity progress overview and a persistent completion state scoped to the current browser/device.
- Listening and Reading complete only after a correct comprehension answer. Pronunciation requires all three self-checks. Writing requires all four checks, a saved draft and the 50–70-word target. Vocabulary requires a learner-produced sentence of at least four words plus an explicit self-check that a lesson expression was used accurately in context. Memory uses an explicit learner confirmation after a review session.
- Pronunciation, Writing and Vocabulary self-checks, plus the Vocabulary sentence, persist locally. Writing drafts still require an explicit save action. No learner data is sent to a server.
- Browser storage availability is checked and failure is disclosed in the progress panel. This is local progress, not an account-backed learning record or synchronised profile.
- These interactions have been reviewed at source level only; no browser, accessibility, storage-failure or full-build test has yet been run.

### Validation and remaining work
- Added `tools/validate_studios.py` to check both language editions, source existence, CEFR consistency, required source material, stable IDs and quiz evidence.
- The build itself also validates Studio contracts before rendering.
- The validation script, full build, mobile/browser checks and accessibility checks have **not yet been executed** in this session. No GitHub Actions workflow or deployment was run.
- Next work: execute the new validator and full build locally, then run keyboard, screen-reader, mobile and storage-failure checks. After those checks, expand Listening and Reading into multi-stage progressions and grow the CEFR-tagged activity catalogue. Do not mark the Studios production-ready until the acceptance criteria in section 6 pass.



### Quality pass — 2026-11-15 (continued)

- Corrected a Python syntax defect in the Studio completion-button renderer: an extra closing parenthesis prevented the generator from parsing.
- Tightened Vocabulary completion: a sentence of at least four words is no longer sufficient on its own; the learner must also complete every self-check confirming that a lesson expression was used accurately in context. The checklist is persisted with the other Studio checklists and can grow beyond one criterion.
- Aligned Listening instructions with the detail-based quiz (rather than asking for gist) and Reading instructions with the explicit-information question. The task prompt, learning outcome and assessed evidence now point to the same skill.
- Made the JavaScript completion evaluator fail closed: an unknown or unsupported completion rule leaves its button disabled. Extracted evaluator tests pass for unknown rules, manual review, all-check pronunciation, writing save/word-count/checklist requirements and Vocabulary sentence/self-check requirements.
- Local checks: JavaScript parses successfully with the V8 syntax parser; the corrected Python helper parses in isolation. The full Python build and validators remain unexecuted because no safe local repository runtime is available in this work session. Browser, keyboard, screen-reader, mobile and storage-failure tests also remain pending.
