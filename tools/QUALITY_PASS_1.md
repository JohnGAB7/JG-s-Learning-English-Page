# Independent quality pass — 15 November 2026

Repository: `JohnGAB7/JG-s-Learning-English-Page`  
Working branch: `chatgpt/platform-quality-pass-1`  
Base: `master`

## Scope

This pass is deliberately complementary to the lesson-authoring and Studio-engine work. It adds a repeatable static integrity check for the generated bilingual website. It does not create a second lesson catalogue, rewrite lesson content, deploy the site, or modify `master`.

## Change

- Added `tools/validate_site.py`.
- The validator checks every generated HTML page for:
  - supported document language (`fr` or `en`);
  - non-empty title and meta description;
  - exactly one H1;
  - duplicate HTML IDs;
  - missing `alt` attributes on images;
  - broken local links, scripts, stylesheets, images and media references;
  - missing in-page fragments on local HTML links.
- It uses Python's standard library only; no browser, network access or third-party package is required.

## Local verification against the synchronized archive

Commands executed from the repository root:

| Command | Result |
|---|---|
| `python3 tools/validate_speaking.py` | PASS — 6 universes, 42 topics, bilingual parity, 2 complete pilot units |
| `python3 tools/validate_studios.py` | PASS — six activity contracts and source evidence |
| `python3 tools/validate_lessons.py 1 30` | PASS — 30/30 |
| `python3 tools/build.py` | PASS — French and English editions built, 144 lessons each |
| `python3 tools/validate_site.py` | PASS — 306 HTML pages and 12,984 local references; no broken paths or fragments, no metadata/H1/ID/image-alt issues |

### Important content-completeness finding

The full-curriculum check `python3 tools/validate_lessons.py` does **not** pass yet:

- 144 of 290 numbered lesson slots are structurally complete in both languages.
- 146 slots are missing at least one language's lesson JSON.
- Current valid counts by level: A1 40/40, A2 38/50, B1 30/60, B2 18/70, C1 18/70.
- Missing slots: A2 70–74 and 84–90; B1 119–130 and 133–150; B2 169–220; C1 239–290.

This is a content coverage gap, not a broken build: the generator successfully produces the 144 available lessons in both editions. Do not fill these gaps with invented lessons or label the 290-slot curriculum complete. Import source lessons or commission clearly labelled new drafts, then validate them.

## Not covered / not claimed

- No browser-based interaction tests, keyboard/screen-reader audit, visual regression, mobile device testing or real-user testing.
- No external-link availability check; the validator intentionally avoids network requests.
- Structural validation does not establish linguistic correctness, CEFR suitability or pedagogical quality.
- No GitHub Actions workflow was dispatched, rerun or relied upon. No deployment was attempted.
- No change was made to `master`.

## Suggested next work

1. Add browser-level smoke tests for the six Studios and the Speak practice flows.
2. Audit the generated pages for keyboard operation, focus visibility, reduced-motion behaviour and mobile navigation.
3. Build a transparent lesson-coverage dashboard from validated data, distinguishing published, draft, missing and needs-review states.
4. Prioritise faithful source migration for the missing lesson slots before expanding the curriculum with new material.


## Learner continuity enhancement — 15 November 2026

- The **My learning** page now offers a direct resume link to the most recently opened lesson.
- It stores only the lesson identifier, displayed title and same-site path in the learner's browser (jg-last-lesson-v1). No history of every page, external browsing data, account or server-side profile is created.
- The stored path is checked to remain on the same origin and to match a valid A1–C1 lesson route before it is rendered as a link.
- If no lesson has been opened yet, the dashboard directs the learner to the learning path.
- Browser execution, storage-denied behaviour and real-device navigation have not yet been tested; this is a source-level implementation awaiting local build and browser verification.
