#!/usr/bin/env python3
"""Imports the newsletter's news into the site data.

Source: /mnt/project-files/grandir-chaque-jour/actualites-site.json (written by the sending thread before each slot,
in French). Each new item (by url) is added to tools/data/fr/actualites.json, and to tools/data/en/actualites.json
with "todo_en": true until its English title / summary are written. Prints the items that still need English.
"""
import json
import sys
from pathlib import Path

SRC = Path("/mnt/project-files/grandir-chaque-jour/actualites-site.json")
D = Path(__file__).resolve().parent / "data"
KEYS = ("date", "pays", "titre", "resume", "pourquoi", "source", "url", "lang")
PAYS = {"monde", "afrique", "belgique", "cameroun", "canada", "france"}


def main():
    if not SRC.exists():
        print("no source file")
        return
    new = json.loads(SRC.read_text(encoding="utf-8"))
    for lang in ("fr", "en"):
        p = D / lang / "actualites.json"
        items = json.loads(p.read_text(encoding="utf-8"))
        seen = {it["url"] for it in items}
        added = 0
        for it in new:
            if it.get("pays") not in PAYS or not str(it.get("url", "")).startswith("https://") or not it.get("titre") or it["url"] in seen:
                continue
            rec = {k: it[k] for k in KEYS if it.get(k)}
            if lang == "en":
                rec["todo_en"] = True
            items.append(rec)
            seen.add(it["url"])
            added += 1
        p.write_text(json.dumps(items, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"{lang}: {added} added")
    todo = [it for it in json.loads((D / "en" / "actualites.json").read_text(encoding="utf-8")) if it.get("todo_en")]
    print(f"{len(todo)} item(s) still need English in tools/data/en/actualites.json")
    sys.exit(0)


if __name__ == "__main__":
    main()
