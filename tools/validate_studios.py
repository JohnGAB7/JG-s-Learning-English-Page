#!/usr/bin/env python3
"""Validate the six Studio pilot activities against the canonical lesson corpus."""

import build
from studios import ACTIVITIES, validate_activities


def main():
    all_errors = []
    for language in ("en", "fr"):
        build.load(language)
        errors = validate_activities(ACTIVITIES, build.NOTIONS)
        all_errors.extend(f"{language}: {error}" for error in errors)

    if all_errors:
        print("\n".join(all_errors))
        raise SystemExit(1)

    print("OK: six Studio activities · stable IDs · bilingual outcomes/durations · completion rules · source lessons · CEFR levels · quiz evidence · FR/EN lesson corpora")


if __name__ == "__main__":
    main()
