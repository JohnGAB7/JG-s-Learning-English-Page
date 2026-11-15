#!/usr/bin/env python3
"""Checks complete lessons in tools/data/{fr,en}/lessons/. Usage: python3 tools/validate_lessons.py [first last]"""
import importlib.util
import json
import sys
from pathlib import Path

D = Path(__file__).resolve().parent / "data"


def mod(lang, name):
    spec = importlib.util.spec_from_file_location(f"{lang}{name}", D / lang / f"{name}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


REFS = json.loads((D / "references.json").read_text(encoding="utf-8"))
PROG = {l: mod(l, "programme_complet").PROGRAMME for l in ("fr", "en")}
LEVELS = [(l["code"], *l["plage"]) for l in mod("en", "programme").NIVEAUX]


def level(k):
    return next(c for c, lo, hi in LEVELS if lo <= k <= hi)


def check(lang, k):
    errs = []
    f = D / lang / "lessons" / f"{level(k).lower()}-{k:03d}.json"
    if not f.exists():
        return [f"{f.name} ({lang}) missing"]
    try:
        n = json.loads(f.read_text(encoding="utf-8"))
    except Exception as ex:  # noqa: BLE001
        return [f"{lang}/{f.name}: invalid JSON: {ex}"]
    w = lambda m: errs.append(f"{lang}/{f.name}: {m}")  # noqa: E731
    if n.get("n") != k: w("wrong n")
    if n.get("niveau") != level(k): w("wrong niveau")
    if n.get("titre") != PROG[lang][k]: w(f"titre must be exactly {PROG[lang][k]!r}")
    for key, mn in (("objectifs", 3), ("sections", 3), ("prononciation", 3), ("erreurs", 5), ("mots", 8), ("exercices", 4), ("a_retenir", 3), ("liens", 2), ("refs", 1)):
        if len(n.get(key) or []) < mn: w(f"{key}: at least {mn}")
    if not n.get("intro") or not n.get("formule"): w("intro and formule required")
    for s in n.get("sections", []):
        if not s.get("titre") or not (s.get("texte") or s.get("tableau") or s.get("exemples")): w("each section needs titre + content")
        tb = s.get("tableau")
        if tb and any(len(r) != len(tb["entetes"]) for r in tb["lignes"]): w(f"table rows/headers mismatch in {s['titre']!r}")
        for ex in s.get("exemples", []):
            if len(ex) != 2: w("exemples are [english, note]")
    if sum(len(s.get("exemples", [])) for s in n.get("sections", [])) < 8: w("at least 8 examples across sections")
    for x in n.get("erreurs", []):
        if len(x) != 3: w("erreurs are [wrong, right, why]")
    for x in n.get("mots", []):
        if len(x) != 3: w("mots are [word, sentence, meaning]")
    dl = n.get("dialogue") or {}
    if not dl.get("contexte") or len(dl.get("lignes", [])) < 6 or any(len(x) != 3 for x in dl.get("lignes", [])): w("dialogue: contexte + at least 6 lines [who, line, note]")
    items = 0
    for x in n.get("exercices", []):
        if not x.get("titre") or not x.get("consigne") or any(len(i) != 2 or not i[1] for i in x.get("items", [])): w("exercise needs titre, consigne, items [question, answer]")
        items += len(x.get("items", []))
    if items < 20: w(f"at least 20 exercise items (has {items})")
    for r in n.get("refs", []):
        if r not in REFS: w(f"unknown ref {r!r} (use keys of references.json)")
    for k2 in n.get("liens", []):
        if not (isinstance(k2, int) and 1 <= k2 <= 290 and k2 != k): w(f"bad lien {k2}")
    return errs


def main():
    a, b = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) == 3 else (1, 290)
    errs, ok = [], 0
    for k in range(a, b + 1):
        e = check("fr", k) + check("en", k)
        if not e:
            fr = json.loads((D / "fr" / "lessons" / f"{level(k).lower()}-{k:03d}.json").read_text(encoding="utf-8"))
            en = json.loads((D / "en" / "lessons" / f"{level(k).lower()}-{k:03d}.json").read_text(encoding="utf-8"))
            if [len(x["items"]) for x in fr["exercices"]] != [len(x["items"]) for x in en["exercices"]]:
                e.append(f"{k}: fr and en exercises must have the same number of items")
            if [m[0] for m in fr["mots"]] != [m[0] for m in en["mots"]]:
                e.append(f"{k}: fr and en must use the same words in the same order")
        errs += e
        ok += not e
    print("\n".join(errs) or "no errors")
    print(f"{ok}/{b - a + 1} lessons valid")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
