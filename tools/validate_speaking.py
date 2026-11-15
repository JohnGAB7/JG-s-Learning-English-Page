#!/usr/bin/env python3
"""Validate bilingual Speak catalogue parity and publication completeness."""
import importlib.util
from pathlib import Path

from speaking import build_catalogue, validate_catalogue

ROOT = Path(__file__).resolve().parent


def load_themes(lang):
    path = ROOT / "data" / lang / "espaces.py"
    spec = importlib.util.spec_from_file_location(f"{lang}_speaking_espaces", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.THEMES


def main():
    fr = build_catalogue(load_themes("fr"), "fr")
    en = build_catalogue(load_themes("en"), "en")
    validate_catalogue(fr)
    validate_catalogue(en)
    fr_ids = [x["id"] for x in fr["topics"]]
    en_ids = [x["id"] for x in en["topics"]]
    assert fr_ids == en_ids, "FR/EN topic IDs or order differ"
    assert len(fr["categories"]) == len(en["categories"]) == 6
    assert len(fr_ids) == len(en_ids) == 42
    assert set(
        (topic["id"], level)
        for topic in fr["topics"]
        for level, unit in topic["levels"].items()
        if unit["status"] == "published"
    ) == {("daily-routine", "A1"), ("food-dining-out", "A2")}
    assert fr["entry_point"]["id"] == en["entry_point"]["id"] == "start-from-zero"
    print("OK: FR/EN parity · 6 universes · 42 topics · 2 complete pilot units")


if __name__ == "__main__":
    main()
