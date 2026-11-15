#!/usr/bin/env python3
"""Builds the whole JG's Learning English site into docs/.

French is the default version (docs/, explanations in French); docs/en/ is the full English version
(same paths, explanations in English). Every page has a FR / EN switch to its twin page (JG, 2026-11-14).

Every page is generated: do not edit docs/ by hand.
Content: tools/data/fr/ and tools/data/en/ · Colours: tools/palette.css (single source of truth)
Theme: tools/theme/ (colours remapped and old brand comments removed at build time) + tools/extra.css
Logos: assets/brand/ (originals) → tools/brand/ (web sizes)
Usage: python3 tools/build.py
"""
import html
import importlib.util
import json
import re
import shutil
import sys
from pathlib import Path

import validate_lessons  # noqa: E402
from speaking import build_catalogue, validate_catalogue  # noqa: E402
from studios import ACTIVITIES, validate_activities  # noqa: E402

ROOT = Path(__file__).resolve().parent
DOCS = ROOT.parent / "docs"
SITE = "JG's Learning English"
LANG = "fr"
OUT = DOCS
e = html.escape


def t(en, fr):
    """UI string in the language being built."""
    return fr if LANG == "fr" else en


def load(lang):
    """Loads one language's content into the module globals."""
    global REFS, LANG, OUT, NOTIONS, NIVEAUX, PAYS, PROGRAMME, ATELIERS, DIMENSIONS, NIVEAUX_DETAIL, METHODE_PARLER, THEMES, PROGRESSION_PARLER, NIV, EN, WS, NAV, NEWS, SPEAKING
    LANG, OUT = lang, (DOCS if lang == "fr" else DOCS / "en")
    d = ROOT / "data" / lang
    mods = {}
    for name in ("notions_a1_a2", "notions_b1_c1", "programme", "programme_complet", "espaces"):
        spec = importlib.util.spec_from_file_location(f"{lang}_{name}", d / f"{name}.py")
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        mods[name] = m
    base = {n["n"]: n for n in mods["notions_a1_a2"].NOTIONS + mods["notions_b1_c1"].NOTIONS}
    for f in sorted((d / "lessons").glob("*.json")):  # complete lessons (2026-11-14) replace the short ones
        k = int(f.stem.split("-")[1])
        if validate_lessons.check("fr", k) or validate_lessons.check("en", k):
            continue  # not finished or not valid yet in both languages: keep the short version (if any)
        rich = json.loads(f.read_text(encoding="utf-8"))
        assert f.stem == f"{rich['niveau'].lower()}-{rich['n']:03d}", f
        base[rich["n"]] = rich
    NOTIONS = sorted(base.values(), key=lambda x: x["n"])
    NIVEAUX, PAYS = mods["programme"].NIVEAUX, mods["programme"].PAYS
    PROGRAMME = mods["programme_complet"].PROGRAMME
    es = mods["espaces"]
    ATELIERS, DIMENSIONS, NIVEAUX_DETAIL = es.ATELIERS, es.DIMENSIONS, es.NIVEAUX_DETAIL
    METHODE_PARLER, THEMES, PROGRESSION_PARLER = es.METHODE_PARLER, es.THEMES, es.PROGRESSION_PARLER
    SPEAKING = build_catalogue(THEMES, lang)
    validate_catalogue(SPEAKING)
    NIV = {lvl["code"]: lvl for lvl in NIVEAUX}
    EN = {lvl["code"]: lvl["nom"] for lvl in NIVEAUX}
    WS = {a[0]: a[1] for a in ATELIERS}
    REFS = json.loads((ROOT / "data" / "references.json").read_text(encoding="utf-8"))
    NEWS = json.loads((d / "actualites.json").read_text(encoding="utf-8"))
    NAV = [("path/", t("Path", "Parcours")), ("speak/", t("Speak", "Parler")), ("lessons/", t("Lessons", "Leçons")), ("studios/", "Studios"), ("my-learning/", t("My learning", "Mon espace")),
           ("review/", t("Review", "Réviser")), ("news/", t("News", "Actualités")), ("about/", t("About", "À propos"))]


MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
OLD_DIRS = ("en", "parcours", "parler", "lecons", "ateliers", "reviser", "actualites", "a-propos", "apropos")
# Inherited theme colours → palette variables (keeps tools/theme/ identical to its source).
COLOUR_MAP = [
    (r"background:\s*#fff\b", "background:var(--surface)"),
    (r"(?<![-\w])color:\s*#fff\b", "color:var(--on-dark)"),
    (r"(stroke|fill):\s*#fff\b", r"\1:var(--on-dark)"),
    (r"#176b70\b", "var(--teal)"), (r"#(d5e0e7|c7d4d9)\b", "var(--on-dark-muted)"),
    (r"#(f1eee7|f0eee7)\b", "var(--paper-2)"), (r"#(fffefa)\b", "var(--surface)"), (r"#(faf8f3|f7f6f1|fbf3e2)\b", "var(--surface-2)"),
    (r"#(102638|0f2130|112c3a)\b", "var(--forest)"), (r"#(0c1c26)\b", "var(--forest-deep)"), (r"#(1b3d50|173c4a|1d3a50)\b", "var(--forest-2)"),
    (r"#(eef3f2|edf3f0|edf2ef|cfe1e0)\b", "var(--teal-soft)"), (r"#(e8e4da|e9e5db|e8e3d8|e7e3d9|ded9ce)\b", "var(--line)"),
    (r"#(d6a24b)\b", "var(--gold)"), (r"#(f0c979|e7c383|efc27f)\b", "var(--gold-on-dark)"), (r"#(b57d27)\b", "var(--gold-2)"),
    (r"#(8a5a00)\b", "var(--gold-text)"), (r"#(f1d89e)\b", "var(--gold-line)"), (r"#(f7eedc)\b", "var(--gold-soft)"),
    (r"#(f5efe0)\b", "var(--on-dark)"), (r"#(657583)\b", "var(--muted)"),
    (r"rgba\(\s*16,\s*38,\s*56,", "rgba(var(--forest-rgb),"), (r"rgba\(\s*(200,\s*144,\s*70|233,\s*163,\s*35),", "rgba(var(--gold-rgb),"),
    (r"rgba\(\s*(21,\s*92,\s*99|37,\s*104,\s*111),", "rgba(var(--teal-rgb),"), (r"rgba\(\s*(245,\s*239,\s*224|255,\s*255,\s*255),", "rgba(var(--ivory-rgb),"),
    (r"#(fff2d7|f4ead5)\b", "var(--gold-soft)"), (r"#(ead9b8)\b", "var(--gold-line)"), (r"#(ffdd8a|f3c66f|f2c978|f4d18c|e6b75e)\b", "var(--gold-on-dark)"),
    (r"#(9a681c|8a6328|66490f)\b", "var(--gold-text)"), (r"#(f8f7f2|f6f4ed|f5f3ed|f2f0e9)\b", "var(--surface-2)"),
    (r"#(eaf3ea|dce9e2|cfe4cf)\b", "var(--teal-soft)"), (r"#(e9e6de|e9e4d9|dcd8ce)\b", "var(--line)"), (r"#(d7d0c1|cfc8bb)\b", "var(--line-2)"),
    (r"#(0c202c|0d2230)\b", "var(--forest-deep)"), (r"#(102c3d|153a48|16394a)\b", "var(--forest-2)"), (r"#(1f6a3a|286b69)\b", "var(--teal)"),
    (r"#(405766|647481)\b", "var(--muted)"), (r"#(5c4928)\b", "var(--gold-text)"),
    (r"#(d6e1e5|d4e0e4|c7d6d8|c5d6d8|c3d0d9|9eafb9)\b", "var(--on-dark-muted)"),
]


def clean(text):
    """Removes the previous brand's name from inherited comments."""
    text = re.sub(r"\(?ACTU-BASICS premium\)?|ACTU-BASICS|Actu-Basics", "JG's Learning English", text)
    return text.replace("palette JG's Learning English inchangée", "palette du site")


def remap(css):
    css = re.sub(r":root\{color-scheme:light;[^}]*\}", "", css)  # main.css's own palette: replaced by palette.css
    for pat, rep in COLOUR_MAP:
        css = re.sub(pat, rep, css)
    return css


# --------------------------------------------------------------------------- helpers
def check():
    seen = set()
    for n in NOTIONS:
        assert n["n"] not in seen, f"lesson {n['n']} appears twice"
        seen.add(n["n"])
        lo, hi = NIV[n["niveau"]]["plage"]
        assert lo <= n["n"] <= hi, f"lesson {n['n']} outside its level range"
        if "sections" in n:
            for k in ("intro", "objectifs", "formule", "prononciation", "erreurs", "dialogue", "exercices", "a_retenir", "liens", "refs"):
                assert n.get(k), f"lesson {n['n']}: missing {k}"
            assert all(r in REFS for r in n["refs"]), f"lesson {n['n']}: unknown reference"
            assert sum(len(x["items"]) for x in n["exercices"]) >= 15, f"lesson {n['n']}: at least 15 exercise items"
        else:
            assert len(n["exercice"]) == len(n["corrige"]), f"lesson {n['n']}: exercise / answer key"
        assert len(n["mots"]) >= 5, f"lesson {n['n']}: at least 5 words"
        assert n["titre"] == PROGRAMME[n["n"]], f"lesson {n['n']}: title differs from the programme"
    assert len(PROGRAMME) == 290


def lid(n):
    return f"{n['niveau'].lower()}-{n['n']:03d}"


def cambridge(word):
    w = re.sub(r"[^a-z' -]", "", word.lower()).strip().replace(" ", "-")
    return f"https://dictionary.cambridge.org/dictionary/english/{w}"


def date_en(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {(MOIS if LANG == 'fr' else MONTHS)[int(m) - 1]} {y}"


def write(rel, content):
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, bytes):
        p.write_bytes(content)
    else:
        p.write_text(content, encoding="utf-8")


def ws_chip(key):
    return f'<span class="ws-chip" data-ws="{key}">{e(WS[key])}</span>'


def theme_btn():
    lab = t("Switch light / dark theme", "Changer de thème clair / sombre")
    return (f'<button class="theme-toggle" type="button" data-theme-toggle aria-label="{lab}" title="{lab}">'
            '<svg class="ico-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>'
            '<svg class="ico-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg></button>')


def page(title, body, depth, rel, current="", desc=""):
    """rel: the page's path inside a language root ('' for home), used for the FR / EN switch."""
    up = "../" * depth
    aup = up + ("../" if LANG == "en" else "")  # shared assets live in docs/assets/
    fr_url, en_url = (f"{up}{rel}", f"{up}en/{rel}") if LANG == "fr" else (f"{up}../{rel}", f"{up}{rel}")
    cur_fr = ' aria-current="true"' if LANG == "fr" else f' href="{fr_url}"'
    cur_en = ' aria-current="true"' if LANG == "en" else f' href="{en_url}"'
    switch = (f'<div class="lang-switch" role="group" aria-label="{t("Language", "Langue")}">'
              f'<a lang="fr" hreflang="fr"{cur_fr} title="Explications en français">FR</a>'
              f'<a lang="en" hreflang="en"{cur_en} title="Everything in English">EN</a></div>')
    links = "".join(f'<a href="{up}{h}"{" aria-current=\"page\"" if h == current else ""}>{l}</a>' for h, l in NAV)
    foot = "".join(f'<a href="{up}{h}">{l}</a>' for h, l in NAV)
    search_index = [
        {"kind": t("Lesson", "Leçon"), "title": n["titre"], "description": n["intro"],
         "keywords": " ".join(w for w, _, _ in n["mots"]), "url": f"{up}lessons/{lid(n)}/"}
        for n in NOTIONS
    ] + [
        {"kind": t("Conversation", "Conversation"), "title": topic["title"], "description": topic["description"],
         "keywords": " ".join(topic["keywords"]), "url": f"{up}speak/#{topic['id']}"}
        for topic in SPEAKING["topics"]
    ]
    search_json = json.dumps(search_index, ensure_ascii=False).replace("</", "<\\/")
    site_search = (
        f'<details class="site-search"><summary aria-label="{t("Search the whole site", "Rechercher sur tout le site")}"><span aria-hidden="true">⌕</span></summary>'
        f'<div class="site-search-panel"><label for="site-search-input">{t("Search lessons and conversations", "Rechercher des leçons et des conversations")}</label>'
        f'<input id="site-search-input" type="search" data-site-search placeholder="{t("Type a topic or keyword…", "Saisis un sujet ou un mot-clé…")}">'
        f'<div class="site-search-results" data-site-search-results aria-live="polite"></div></div></details>'
        f'<script>window.SITE_SEARCH_INDEX={search_json};</script>'
    )
    base = "https://johngab7.github.io/JG-s-Learning-English-Page/"
    default_desc = t("Learn English from A1 to C1, entirely in English: complete lessons, exercises with answers, a speaking lab about real life, review cards and world news.",
                     "Apprendre l’anglais de A1 à C1 : leçons complètes expliquées en français, exercices corrigés, laboratoire pour parler de sa vie, cartes de révision et actualités.")
    return f"""<!doctype html>
<html lang="{LANG}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{e(desc or default_desc)}">
<meta name="theme-color" content="#173A36"><title>{e(title)}</title>
<link rel="alternate" hreflang="fr" href="{base}{rel}"><link rel="alternate" hreflang="en" href="{base}en/{rel}">
<link rel="icon" href="{aup}assets/img/favicon.ico" sizes="any"><link rel="icon" href="{aup}assets/img/favicon-32.png" type="image/png" sizes="32x32"><link rel="apple-touch-icon" href="{aup}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,300..700;1,8..60,300..700&family=Inter:wght@400;500;600;700;850&display=swap">
<link rel="stylesheet" href="{aup}assets/css/tokens.css"><link rel="stylesheet" href="{aup}assets/css/main.css"><link rel="stylesheet" href="{aup}assets/css/premium.css"><link rel="stylesheet" href="{aup}assets/css/palette.css"><link rel="stylesheet" href="{aup}assets/css/jg.css"><link rel="stylesheet" href="{aup}assets/css/print.css" media="print">
<script>(function(){{try{{var t=localStorage.getItem("jg-learning-theme")||localStorage.getItem("ab-theme");if(t==="dark"||t==="light"){{document.documentElement.setAttribute("data-theme",t);}}}}catch(e){{}}}})();</script>
</head>
<body><a class="skip-link" href="#content">{t("Skip to content", "Aller au contenu")}</a>
<header class="site-header"><div class="nav-wrap">
<a class="brand" href="{up}index.html" aria-label="{e(SITE)}, {t("home", "accueil")}"><img class="brand-logo brand-logo-light" src="{aup}assets/img/logo-light-96.png" width="46" height="46" alt=""><img class="brand-logo brand-logo-dark" src="{aup}assets/img/logo-dark-96.png" width="46" height="46" alt=""><span class="brand-name">JG’s <em>Learning English</em></span></a>
<nav id="site-navigation" class="nav-links" aria-label="{t("Main navigation", "Navigation principale")}">{links}</nav>
<div class="nav-actions">{site_search}{switch}{theme_btn()}<button class="menu-toggle" type="button" aria-controls="site-navigation" aria-expanded="false" aria-label="{t("Open menu", "Ouvrir le menu")}">☰</button></div>
</div></header>
<main id="content">{body}</main>
<footer class="footer"><div class="footer-inner">
<div><h3>{e(SITE)}</h3><p><strong>{t("Clear English. For everyone.", "Clear English. For everyone.")}</strong></p><p>{t("English from A1 to C1, one lesson at a time. Understand the rule, hear it, say it, then talk about your own life.", "L’anglais de A1 à C1, une leçon à la fois. Comprendre la règle, l’entendre, la dire, puis parler de sa propre vie.")}</p><p>{t("An independent learning project, companion to the “Grandir chaque jour” newsletter.", "Un projet d’apprentissage indépendant, compagnon de la newsletter « Grandir chaque jour ».")}</p><p><a class="text-link" lang="{t("fr", "en")}" href="{fr_url if LANG == "en" else en_url}">{t("Version française (explications en français) →", "English version (everything in English) →")}</a></p></div>
<div><h3>{t("Explore", "Explorer")}</h3><div class="footer-links">{foot}</div></div>
<div><h3>{t("Free tools", "Outils gratuits")}</h3><div class="footer-links"><a href="https://dictionary.cambridge.org/" target="_blank" rel="noopener">Cambridge Dictionary ↗</a><a href="https://www.efset.org/" target="_blank" rel="noopener">{t("Test your level (EF SET)", "Tester son niveau (EF SET)")} ↗</a><a href="https://apps.ankiweb.net/" target="_blank" rel="noopener">Anki ↗</a></div></div>
</div><div class="footer-bottom"><span>© {e(SITE)} · {t("Independent learning project", "Projet d’apprentissage indépendant")}</span><span>{t("Written with the help of Claude (AI) and reviewed by the author.", "Rédigé avec l’aide de Claude (IA) et relu par l’auteur.")}</span></div></footer>
<script src="{aup}assets/js/site.js" defer></script></body></html>
"""


def hero_page(crumbs, eyebrow, h1, lead, depth):
    up = "../" * depth
    cr = f'<a href="{up}index.html">{t("Home", "Accueil")}</a>' + "".join(f" / {c}" for c in crumbs)
    return f'<section class="page-hero"><div class="container"><div class="breadcrumb">{cr}</div><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p>{lead}</p></div></section>'


def video_slots(soon_text=None):
    soon_text = soon_text or t("Video coming soon", "Vidéo bientôt disponible")
    return (f'<section class="video-section" data-ws="listening" aria-label="{t("Videos", "Vidéos")}"><h2>{t("Videos", "Vidéos")}</h2><div class="video-grid">'
            f'<figure class="video-slot video-slot-yt"><figcaption class="video-caption">YouTube · {t("explanation", "explication")}</figcaption><div class="video-frame video-frame-16x9 video-frame-soon"><span class="video-soon">{soon_text}</span></div></figure>'
            f'<figure class="video-slot video-slot-tt"><figcaption class="video-caption">{t("Short format · to imitate", "Format court · à imiter")}</figcaption><div class="video-frame video-frame-9x16 video-frame-soon"><span class="video-soon">{soon_text}</span></div></figure>'
            f'</div><p class="muted"><small>{t("Videos will appear here as soon as they are published.", "Les vidéos apparaîtront ici dès leur publication.")}</small></p></section>')


def lesson_card(n, up):
    return (f'<article class="card lesson-card" data-lesson data-category="{n["niveau"].lower()}" data-keywords="{e(" ".join(w for w, _, _ in n["mots"]))}">'
            f'<div class="card-top"><span class="lesson-code">{n["niveau"]} · {n["n"]:03d}</span></div><h3>{e(n["titre"])}</h3><p>{e(n["intro"])}</p>'
            f'<div class="card-badges"><span class="badge badge-level">{n["niveau"]} · {EN[n["niveau"]]}</span><span class="badge badge-state badge-state-lesson">{t("Lesson available", "Leçon disponible")}</span><span class="badge lesson-upcoming">{t("Video coming soon", "Vidéo bientôt")}</span></div>'
            f'<div class="card-bottom"><a class="text-link" href="{up}lessons/{lid(n)}/">{t("Open the lesson", "Ouvrir la leçon")} →</a></div></article>')


def workshops(up):
    return "".join(
        f'<a class="card ws-card" data-ws="{k}" href="{up}studios/#{k}"><div class="card-top"><span class="icon-tile" aria-hidden="true">{e(icon)}</span><span class="tag">{i + 1:02d}</span></div>'
        f'<h3>{e(name)}</h3><p>{e(desc)}</p><span class="text-link">{t("Open the studio", "Ouvrir l’atelier")} →</span></a>'
        for i, (k, name, desc, href, where, icon, formats, live) in enumerate(ATELIERS))


def plural(k, en, fr):
    return f"{k} {t(en, fr)}{'s' if k > 1 else ''}"


# --------------------------------------------------------------------------- pages
def build_home():
    counts = {c: sum(1 for n in NOTIONS if n["niveau"] == c) for c in NIV}
    lv = "".join(
        f'<a class="card path-card" data-number="{l["code"]}" href="path/#{l["code"].lower()}"><div class="card-top"><span class="icon-tile">{l["code"]}</span><span class="tag">{EN[l["code"]]}</span></div>'
        f'<h3>{e(NIVEAUX_DETAIL[l["code"]]["titre"])}</h3><p>{e(l["themes"])}</p><span class="text-link">{t("See the level", "Voir le niveau")} · {plural(counts[l["code"]], "lesson", "leçon")} →</span></a>' for l in NIVEAUX)
    une = next(n for n in NOTIONS if n["n"] == 96)
    themes = "".join(
        f'<a class="card" href="speak/#universe-{i + 1:02d}"><div class="card-top"><span class="icon-tile">{i + 1:02d}</span><span class="tag">{t("Speak", "Parler")}</span></div><h3>{e(g)}</h3><p>{e(d)}</p><span class="text-link">{sum(1 for topic in SPEAKING["topics"] if topic["category_id"] == f"universe-{i+1:02d}")} {t("topics", "sujets")} →</span></a>'
        for i, (g, d, tp) in enumerate(THEMES[:3]))
    logo = t("../assets/img/logo-dark-512.png", "assets/img/logo-dark-512.png")
    speaking_count = len(SPEAKING["topics"])
    home_speak_intro = t(f"Waking up, hobbies, work, family… {speaking_count} topics to build fluency, with model dialogues and guided practice.", f"Le réveil, les loisirs, le travail, la famille… {speaking_count} sujets pour gagner en aisance, avec des dialogues modèles et des activités guidées.")
    home_speak_link = t(f"See all {speaking_count} topics", f"Voir les {speaking_count} sujets")
    body = f"""<section class="hero"><div class="hero-inner"><div>
<span class="eyebrow">{t("English · from A1 to C1", "Anglais · de A1 à C1")}</span>
<h1>{t("Hello and welcome to my world!", "Hello and welcome to my world!")}</h1>
<p class="lead">{t("Here, you can learn English at your own pace, build confidence, and use English in real life.",
                   "Ici, tu peux apprendre l’anglais à ton rythme, gagner en confiance et utiliser l’anglais dans la vie réelle.")}</p>
<div class="hero-actions"><a class="button button-primary" href="path/">{t("Discover the path", "Découvrir le parcours")} <span aria-hidden="true">→</span></a><a class="button button-light" href="lessons/">{t("Explore the lessons", "Explorer les leçons")}</a></div>
<div class="hero-proof"><span><strong>290</strong> {t("lessons in the programme", "leçons au programme")}</span><span><strong>{len(NOTIONS)}</strong> {t("lessons online", "leçons en ligne")}</span><span><strong>{len(SPEAKING["topics"])}</strong> {t("speaking topics", "sujets pour parler")}</span></div>
</div><aside class="hero-note"><img class="hero-logo" src="{logo}" width="280" height="280" alt="{t("JG’s Learning English logo", "Logo JG’s Learning English")}"><strong>{t("One promise: really speak.", "Une promesse : parler vraiment.")}</strong><p>{t("Understand the rule, hear it, repeat it, then use it to talk about yourself. Every lesson links grammar, vocabulary and pronunciation.", "Comprendre la règle, l’entendre, la répéter, puis s’en servir pour parler de soi. Chaque leçon relie grammaire, vocabulaire et prononciation.")}</p></aside></div></section>
<section class="section"><div class="container"><div class="section-head"><div><span class="eyebrow">{t("Six workshops", "Six ateliers")}</span><h2>{t("One environment, six ways to learn.", "Un seul univers, six façons d’apprendre.")}</h2></div><p>{t("Each workshop has its own colour. You will find the same colour on the cards, the lesson sections and the exercises that belong to it.", "Chaque atelier a sa couleur. Tu la retrouves sur les cartes, les rubriques des leçons et les exercices qui lui appartiennent.")}</p></div>
<div class="grid-ws">{workshops("")}</div></div></section>
<section class="section band"><div class="container"><div class="section-head"><div><span class="eyebrow">{t("Start here", "Commencer ici")}</span><h2>{t("Choose your level.", "Choisis ton niveau.")}</h2></div><p>{t("Not sure of your level? The free", "Pas sûr de ton niveau ? Le test gratuit")} <a class="text-link" href="https://www.efset.org/" target="_blank" rel="noopener">EF SET ↗</a> {t("test measures it in about fifty minutes.", "le mesure en une cinquantaine de minutes.")}</p></div>
<div class="grid-3 grid-levels">{lv}</div></div></section>
<section class="section feature-section"><div class="container"><div class="feature-panel"><div class="feature-copy"><span class="eyebrow">{t("Featured", "À la une")} · B1 · {une["n"]}</span><span class="feature-kicker">{t("Imagine, dream, advise", "Imaginer, rêver, conseiller")}</span><h2>{e(une["titre"])}</h2><p>{e(une["intro"])} {t("“If I were you…”, “What would you do if…”: you hear this structure everywhere, in job interviews and among friends.", "« If I were you… », « What would you do if… » : on entend cette structure partout, en entretien comme entre amis.")}</p><div class="feature-meta"><span>{t("Rule and examples", "Règle et exemples")}</span><span>{t("5 words to hear", "5 mots à écouter")}</span><span>{t("Exercise with answers", "Exercice corrigé")}</span></div><a class="button button-primary" href="lessons/{lid(une)}/">{t("Explore the lesson", "Découvrir la leçon")} <span aria-hidden="true">→</span></a></div>
<div class="feature-visual" aria-hidden="true"><div class="feature-visual-top"><span>SECOND CONDITIONAL</span><span>B1</span></div><div class="feature-sentence"><p><b>If</b> I <em>had</em> more time,</p><p>I <em>would</em> learn Spanish.</p><small>If + past simple → would + {t("base verb", "base verbale")}</small></div><div class="feature-visual-foot"><strong>If I were you…</strong><span>{t("giving advice", "donner un conseil")}</span></div></div></div></div></section>
<section class="section band"><div class="container"><div class="section-head"><div><span class="eyebrow">Speak English in Real Life</span><h2>{t("Talk about everyday life.", "Parler de la vie de tous les jours.")}</h2></div><p>{home_speak_intro}</p></div><div class="grid-3">{themes}</div><p style="margin-top:22px"><a class="button button-outline" href="speak/">{home_speak_link} →</a></p></div></section>
<section class="section-tight"><div class="container"><div class="quote-panel"><div><span class="eyebrow">{e(SITE)}</span><h2>{t("Clear English. For everyone.", "Clear English. For everyone.")}</h2><p>{t("You don't need to know everything to start. One lesson, a little regularity and the wish to speak are enough.", "Pas besoin de tout savoir pour commencer. Une leçon, un peu de régularité et l’envie de parler suffisent.")}</p></div><a class="button button-primary" href="about/">{t("About the project", "À propos du projet")} →</a></div></div></section>"""
    write("index.html", page(f"{SITE} — Clear English. For everyone.", body, 0, "", desc=t("Learn English at your own pace, build confidence, and use English in real life.", "Apprendre l’anglais à son rythme, gagner en confiance et utiliser l’anglais dans la vie réelle.")))


def build_path():
    dims = "".join(f'<div class="pillar"{f" data-ws={chr(34)}{w}{chr(34)}" if w else ""}><span class="pillar-number">{i + 1:02d}</span><h2>{e(a)}</h2><p>{e(b)}</p>{ws_chip(w) if w else ""}</div>' for i, (a, b, w) in enumerate(DIMENSIONS))
    levels = []
    for l in NIVEAUX:
        c = l["code"]
        d = NIVEAUX_DETAIL[c]
        lo, hi = l["plage"]
        mine = [n for n in NOTIONS if n["niveau"] == c]
        blocs = "".join(f'<article class="card"{f" data-ws={chr(34)}{w}{chr(34)}" if w else ""}><h3>{e(x0)}</h3><p>{e(x)}</p>{ws_chip(w) if w else ""}</article>' for x0, w, x in d["blocs"])
        chips = "".join(f'<a href="../lessons/{lid(n)}/">{n["n"]} · {e(n["titre"])}</a>' for n in mine)
        levels.append(f'<section class="section level-block" id="{c.lower()}"><div class="container"><div class="section-head"><div><span class="eyebrow">{c} · {t("CEFR", "CECRL")} · {EN[c]} · {t("lessons", "leçons")} {lo} {t("to", "à")} {hi}</span><h2>{e(d["titre"])}</h2></div><p>{e(d["objectif"])}</p></div>'
                      f'<div class="grid-3">{blocs}</div><div class="level-lessons"><p><strong>{t("Lessons online", "Leçons en ligne")} ({len(mine)} {t("of", "sur")} {hi - lo + 1})</strong></p><div class="module-lessons">{chips}</div>'
                      f'<a class="button button-outline" href="../lessons/#{c.lower()}">{t(f"All {c} lessons", f"Toutes les leçons {c}")} →</a></div></div></section>')
    body = (hero_page([t("Path", "Parcours")], t("The complete path", "Le parcours complet"), t("Build your English, step by step.", "Construis ton anglais, étape par étape."),
                      t("A programme that develops every skill: understanding, reading, writing, pronouncing, interacting and expressing yourself precisely. Each level has its own goals and lessons, numbered from 1 to 290.",
                        "Un programme qui développe toutes les compétences : comprendre, lire, écrire, prononcer, interagir et s’exprimer avec précision. Chaque niveau a ses objectifs et ses leçons, numérotées de 1 à 290."), 1)
            + f'<section class="section"><div class="container"><div class="section-head"><div><span class="eyebrow">{t("One language · eight skills", "Une langue · huit compétences")}</span><h2>{t("Grammar is one pillar, not the whole programme.", "La grammaire est un pilier, pas tout le programme.")}</h2></div><p>{t("Each level links knowledge to real use. The coloured skills belong to one of the six workshops.", "Chaque niveau relie le savoir à l’usage réel. Les compétences en couleur appartiennent à l’un des six ateliers.")}</p></div><div class="pillars pillars-4">{dims}</div></div></section>'
            + f'<section class="section band"><div class="container"><div class="section-head"><div><span class="eyebrow">{t("Six workshops", "Six ateliers")}</span><h2>{t("Where each skill is practised.", "Là où chaque compétence s’entraîne.")}</h2></div><p>{t("The workshops run through every level, from A1 to C1.", "Les ateliers traversent tous les niveaux, de A1 à C1.")}</p></div><div class="grid-ws">{workshops("../")}</div></div></section>'
            + "".join(levels))
    write("path/index.html", page(f"{t('Path from A1 to C1', 'Parcours de A1 à C1')} — {SITE}", body, 1, "path/", "path/"))


def _speaking_unit(topic, level, unit):
    dialogue = "".join(f'<p><strong>{e(a)}:</strong> {e(b)} <button class="phrase-audio" type="button" data-speak-text="{e(b)}" aria-label="{t("Listen to this line", "Écouter cette réplique")}">▶</button></p>' for a, b in unit["dialogue"])
    expressions = "".join(f"<li>{e(x)}</li>" for x in unit["expressions"])
    words = "".join(f'<tr><th scope="row">{e(a)}</th><td>{e(b)}</td><td>{e(c)}</td></tr>' for a, b, c in unit["vocabulary"])
    questions = "".join(f"<li>{e(x)}</li>" for x in unit["questions"])
    outcomes = "".join(f"<li>{e(x)}</li>" for x in unit["outcomes"])
    checks = "".join(f"<li>{e(x)}</li>" for x in unit["self_check"])
    speech = e(" ".join(line for _, line in unit["dialogue"]))
    key = topic["id"] + "-" + level.lower()
    related = [n for n in NOTIONS if n["n"] in topic.get("related_lesson_ids", [])]
    related_html = "".join(f'<li><a href="../lessons/{lid(n)}/">{n["n"]} · {e(n["titre"])}</a></li>' for n in related)
    related_block = f'<h4>{t("Related grammar lessons", "Leçons de grammaire liées")}</h4><ul>{related_html}</ul>' if related else ""
    return (
        f'<details class="speaking-unit" id="{key}"><summary>{level} · {t("Complete practice unit", "Unité de pratique complète")} <span class="badge badge-state">{t("Available", "Disponible")}</span></summary>'
        f'<div class="speaking-unit-body"><p class="eyebrow">{t("Real-life situation", "Situation réelle")}</p><p>{e(unit["scenario"])}</p>'
        f'<h4>{t("Your goals", "Tes objectifs")}</h4><ul>{outcomes}</ul>'
        f'<h4>{t("Model dialogue", "Dialogue modèle")}</h4><div class="dialogue-box" lang="en">{dialogue}</div>'
        f'<button class="button button-outline" type="button" data-speak-text="{speech}">{t("Listen to the dialogue", "Écouter le dialogue")}</button><p class="muted">{t("Listen to each line, repeat it, then shadow the full dialogue.", "Écoute chaque réplique, répète-la, puis fais du shadowing sur le dialogue complet.")}</p>'
        f'<h4>{t("Natural expressions", "Expressions naturelles")}</h4><ul>{expressions}</ul>'
        f'<h4>{t("Vocabulary in context", "Vocabulaire en contexte")}</h4><div class="table-wrap"><table class="words"><thead><tr><th>{t("Expression", "Expression")}</th><th>{t("Example", "Exemple")}</th><th>{t("Meaning", "Sens")}</th></tr></thead><tbody>{words}</tbody></table></div>'
        f'<h4>{t("Useful grammar", "Grammaire utile")}</h4><p>{e(unit["grammar"])}</p>{related_block}'
        f'<h4>{t("Pronunciation focus", "Point de prononciation")}</h4><p>{e(unit["pronunciation"])}</p>'
        f'<h4>{t("Guided speaking", "Expression orale guidée")}</h4><ol>{questions}</ol>'
        f'<h4>{t("Role-play", "Jeu de rôle")}</h4><p>{e(unit["roleplay"])}</p>'
        f'<h4>{t("Free speaking", "Expression orale libre")}</h4><p>{e(unit["free_speaking"])}</p>'
        f'<h4>{t("Make it personal", "Personnalise ta réponse")}</h4><label class="activity-label" for="response-{key}">{t("Write notes for your answer", "Note les idées de ta réponse")}</label>'
        f'<textarea id="response-{key}" class="activity-response" rows="4" placeholder="{t("Use your own details…", "Utilise tes propres informations…")}"></textarea>'
        f'<p><small>{t("Your notes stay in this browser only when you choose Save.", "Tes notes restent dans ce navigateur uniquement si tu choisis de les enregistrer.")}</small></p>'
        f'<button class="button button-outline" type="button" data-save-response="{key}">{t("Save my notes", "Enregistrer mes notes")}</button><p class="save-feedback" data-save-feedback="{key}" aria-live="polite"></p>'
        f'<h4>{t("Short writing task", "Courte activité d’écriture")}</h4><p>{e(unit["writing"])}</p>'
        f'<h4>{t("Self-check", "Autoévaluation")}</h4><ul>{checks}</ul>'
        f'<button class="button button-primary" type="button" data-complete-unit="{key}" data-complete-label="{t("Mark this unit complete", "Marquer cette unité comme terminée")}" data-completed-label="{t("✓ Completed", "✓ Terminée")}">{t("Mark this unit complete", "Marquer cette unité comme terminée")}</button>'
        f'<p class="save-feedback" data-complete-feedback="{key}" aria-live="polite"></p></div></details>'
    )


def build_speak():
    validate_catalogue(SPEAKING)
    entry = SPEAKING["entry_point"]
    zero = (
        '<section class="section band" id="start-from-zero"><div class="container">'
        f'<div class="section-head"><div><span class="eyebrow">Pre-A1 · {t("A gentle first step", "Un premier pas en douceur")}</span><h2>{e(entry["title"])}</h2></div><p>{e(entry["description"])} {t("This is an entry point, not a replacement for A1.", "C’est une porte d’entrée, pas un remplacement du niveau A1.")}</p></div>'
        f'<div class="grid-3"><article class="card"><h3>Hello!</h3><p lang="en">Hello. Hi. Good morning.</p><button class="button button-outline" type="button" data-speak-text="Hello. Hi. Good morning.">{t("Listen and repeat", "Écouter et répéter")}</button></article>'
        f'<article class="card"><h3>{t("Say your name", "Dire son nom")}</h3><p lang="en">My name is… What is your name?</p><button class="button button-outline" type="button" data-speak-text="My name is… What is your name?">{t("Listen and repeat", "Écouter et répéter")}</button></article>'
        f'<article class="card"><h3>{t("Be polite", "Être poli")}</h3><p lang="en">Please. Thank you. Yes. No. Sorry.</p><button class="button button-outline" type="button" data-speak-text="Please. Thank you. Yes. No. Sorry.">{t("Listen and repeat", "Écouter et répéter")}</button></article></div>'
        f'<p class="muted">{t("Audio uses your browser’s speech voice when available. No recorded human audio is supplied here.", "L’audio utilise la voix de synthèse de ton navigateur lorsqu’elle existe. Aucun enregistrement humain n’est fourni ici.")}</p></div></section>'
    )
    level_options = "".join('<option value="' + lv + '">' + lv + '</option>' for lv in SPEAKING["levels"])
    filters = (
        '<section class="section" id="catalogue"><div class="container">'
        f'<div class="section-head"><div><span class="eyebrow">{t("Conversation catalogue", "Catalogue de conversations")}</span><h2>{t("Choose a situation. Build your voice.", "Choisis une situation. Développe ta voix.")}</h2></div><p>{len(SPEAKING["topics"])} {t("topics across six universes. A unit is available only when its content is complete.", "sujets répartis dans six univers. Une unité est disponible uniquement lorsque son contenu est complet.")}</p></div>'
        f'<div class="catalog-tools"><input class="search-input" type="search" data-speaking-search placeholder="{t("Search a topic or expression…", "Rechercher un sujet ou une expression…")}" aria-label="{t("Search speaking topics", "Rechercher des sujets de conversation")}">'
        f'<select class="filter-select" data-speaking-level aria-label="{t("Filter by level", "Filtrer par niveau")}"><option value="all">{t("All levels", "Tous les niveaux")}</option>{level_options}</select>'
        f'<select class="filter-select" data-speaking-skill aria-label="{t("Filter by skill", "Filtrer par compétence")}"><option value="all">{t("All skills", "Toutes les compétences")}</option><option value="speaking">{t("Speaking", "Expression orale")}</option><option value="listening">{t("Listening", "Écoute")}</option><option value="pronunciation">{t("Pronunciation", "Prononciation")}</option><option value="vocabulary">{t("Vocabulary", "Vocabulaire")}</option><option value="writing">{t("Writing", "Écriture")}</option></select>'
        f'<select class="filter-select" data-speaking-status aria-label="{t("Filter by availability", "Filtrer par disponibilité")}"><option value="all">{t("All statuses", "Tous les statuts")}</option><option value="published">{t("Available units", "Unités disponibles")}</option><option value="planned">{t("Coming later", "À venir")}</option></select></div>'
        f'<p class="empty-state" data-speaking-empty hidden>{t("No topic matches these filters.", "Aucun sujet ne correspond à ces filtres.")}</p></div></section>'
    )
    groups = []
    for category in SPEAKING["categories"]:
        cards = []
        for topic in [x for x in SPEAKING["topics"] if x["category_id"] == category["id"]]:
            published = [lv for lv in SPEAKING["levels"] if topic["levels"][lv]["status"] == "published"]
            search_text = " ".join([topic["title"], topic["description"], *topic["keywords"]]).lower()
            level_html = "".join(
                _speaking_unit(topic, lv, topic["levels"][lv]) if topic["levels"][lv]["status"] == "published"
                else f'<p class="level-status"><strong>{lv}</strong> · {t("Learning unit planned", "Unité pédagogique prévue")}</p>'
                for lv in SPEAKING["levels"]
            )
            skills = "speaking,listening,pronunciation,vocabulary" + (",writing" if published else "")
            cards.append(
                f'<article class="card speaking-topic" id="{topic["id"]}" data-topic-card data-topic-search="{e(search_text)}" data-topic-levels="{",".join(published) if published else "none"}" data-topic-skills="{skills}" data-topic-status="{"published" if published else "planned"}">'
                f'<div class="card-top"><span class="tag">{e(topic["tag"])}</span><span class="badge lesson-upcoming">{" · ".join(published) if published else t("In development", "En préparation")}</span></div>'
                f'<h3>{e(topic["title"])}</h3><p>{e(topic["description"])}</p><p class="kw" lang="en">{e(" · ".join(topic["keywords"]))}</p>'
                f'<div class="topic-levels"><span class="eyebrow">{t("CEFR progression", "Progression CECRL")}</span>{level_html}</div></article>'
            )
        groups.append(
            f'<section class="section" id="{category["id"]}"><div class="container"><div class="section-head"><div><span class="eyebrow">{t("Conversation universe", "Univers de conversation")}</span><h2>{e(category["title"])}</h2></div><p>{e(category["description"])}</p></div><div class="grid-2">{"".join(cards)}</div></div></section>'
        )
    progression = [
        ("A1", t("Essential words and model sentences; short guided answers.", "Mots essentiels et phrases modèles ; réponses courtes et guidées.")),
        ("A2", t("Everyday exchanges, questions and connected simple ideas.", "Échanges quotidiens, questions et idées simples reliées.")),
        ("B1", t("Descriptions, stories, explanations and opinions.", "Descriptions, récits, explications et opinions.")),
        ("B2", t("Spontaneous interaction, argument and nuance.", "Interaction spontanée, argumentation et nuances.")),
        ("C1", t("Precision, subtlety, fluency and register.", "Précision, subtilité, aisance et registre.")),
    ]
    prog = "".join(f'<article class="card"><div class="card-top"><span class="icon-tile">{lv}</span></div><p>{desc}</p></article>' for lv, desc in progression)
    body = (
        hero_page([t("Speak", "Parler")], "Speak English in Real Life",
                  t("Don’t just learn English. <em>Live it.</em>", "N’apprends pas seulement l’anglais. <em>Vis-le.</em>"),
                  t("A practical conversation lab built around real situations. Start from zero, choose a topic, practise with model language and gradually make the conversation your own.",
                    "Un laboratoire de conversation autour de situations réelles. Commence de zéro, choisis un sujet, appuie-toi sur des modèles puis construis progressivement tes propres réponses."), 1)
        + zero + filters + "".join(groups)
        + f'<section class="section band"><div class="container"><div class="section-head"><div><span class="eyebrow">{t("Progression", "Progression")}</span><h2>{t("Same situation, richer language.", "Même situation, langue plus riche.")}</h2></div><p>{t("Revisit familiar topics as your ability grows.", "Reviens sur les mêmes sujets à mesure que tu progresses.")}</p></div><div class="grid-4">{prog}</div></div></section>'
    )
    write("speak/index.html", page(f"{t('Speak', 'Parler')} — Speak English in Real Life — {SITE}", body, 1, "speak/", "speak/"))


def build_library():
    secs = []
    for l in NIVEAUX:
        c = l["code"]
        lo, hi = l["plage"]
        mine = [n for n in NOTIONS if n["niveau"] == c]
        have = {n["n"] for n in mine}
        todo = [k for k in range(lo, hi + 1) if k not in have]
        cards = "".join(lesson_card(n, "../") for n in mine)
        soon = "".join(f'<li><span class="lesson-code">{c} · {k:03d}</span> {e(PROGRAMME[k])}</li>' for k in todo)
        secs.append(f'<section class="module-section" id="{c.lower()}" data-module-section="{c}" data-category="{c.lower()}"><div class="module-head"><div class="module-head-text"><span class="eyebrow">{t("Level", "Niveau")} {c} · {t("lessons", "leçons")} {lo} {t("to", "à")} {hi}</span><h2>{c} · {EN[c]}</h2><p>{e(l["themes"])}</p></div><span class="module-count" data-visible-count>{len(mine)} {t("lessons", "leçons")}</span></div>'
                    f'<div class="grid-3 module-grid">{cards}</div><details class="soon-list"><summary>{t(f"{c} programme: the {len(todo)} other lessons coming soon", f"Programme {c} : les {len(todo)} autres leçons à venir")}</summary><ol class="soon-ol">{soon}</ol></details></section>')
    opts = "".join(f'<option value="{l["code"].lower()}">{l["code"]} · {EN[l["code"]]}</option>' for l in NIVEAUX)
    body = (hero_page([t("Lessons", "Leçons")], t("Library", "Bibliothèque"), t("Find a lesson, pick up where you like.", "Trouve une leçon, reprends où tu veux."),
                      t(f"The programme has 290 lessons, from A1 to C1. {len(NOTIONS)} are online; the others arrive week by week, with the same numbers as in the “Grandir chaque jour” newsletter.",
                        f"Le programme compte 290 leçons, de A1 à C1. {len(NOTIONS)} sont en ligne ; les autres arrivent semaine après semaine, avec les mêmes numéros que dans la newsletter « Grandir chaque jour »."), 1)
            + f'<section class="section"><div class="container"><div class="catalog-tools"><input class="search-input" type="search" placeholder="{t("Search a lesson or a word (passive, used to, afford…)", "Chercher une leçon ou un mot (passif, used to, afford…)")}" data-search aria-label="{t("Search a lesson", "Chercher une leçon")}"><select class="filter-select" data-filter aria-label="{t("Filter by level", "Filtrer par niveau")}"><option value="all">{t("All levels", "Tous les niveaux")}</option>{opts}</select></div>'
            + f'<p class="empty-state" data-empty hidden>{t("No online lesson matches. Have a look at the programme coming soon for each level.", "Aucune leçon en ligne ne correspond. Regarde le programme à venir de chaque niveau.")}</p>'
            + "".join(secs) + "</div></section>")
    write("lessons/index.html", page(f"{t('Lesson library', 'Bibliothèque des leçons')} — {SITE}", body, 1, "lessons/", "lessons/"))


def lesson_nav(i):
    prev = NOTIONS[i - 1] if i > 0 else None
    nxt = NOTIONS[i + 1] if i + 1 < len(NOTIONS) else None
    nav = f'<nav class="module-nav" aria-label="{t("Nearby lessons", "Leçons voisines")}">'
    nav += f'<a class="module-nav-link module-nav-prev" href="../{lid(prev)}/"><span class="module-nav-label">← {t("Previous lesson", "Leçon précédente")}</span><span class="module-nav-title">{prev["n"]}. {e(prev["titre"])}</span></a>' if prev else "<span></span>"
    nav += f'<a class="module-nav-link module-nav-next" href="../{lid(nxt)}/"><span class="module-nav-label">{t("Next lesson", "Leçon suivante")} →</span><span class="module-nav-title">{nxt["n"]}. {e(nxt["titre"])}</span></a>' if nxt else "<span></span>"
    return nav + "</nav>"


def level_of(k):
    return next(l["code"] for l in NIVEAUX if l["plage"][0] <= k <= l["plage"][1])


def build_lesson_rich(i, n):
    c = n["niveau"]
    online = {x["n"] for x in NOTIONS}
    def table(tb):
        head = "".join(f"<th>{e(h)}</th>" for h in tb["entetes"])
        rows = "".join("<tr>" + "".join(f"<td>{e(x)}</td>" for x in r) + "</tr>" for r in tb["lignes"])
        return f'<div class="table-wrap"><table class="grammar-table"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
    secs = ""
    for s_ in n["sections"]:
        secs += f'<h2>{e(s_["titre"])}</h2>' + "".join(f"<p>{e(p)}</p>" for p in s_.get("texte", []))
        if s_.get("tableau"):
            secs += table(s_["tableau"])
        if s_.get("exemples"):
            secs += '<ul class="examples">' + "".join(f'<li><strong lang="en">{e(a)}</strong><br><span class="example-note">{e(b)}</span></li>' for a, b in s_["exemples"]) + "</ul>"
        if s_.get("note"):
            secs += f'<div class="notice">{e(s_["note"])}</div>'
    obj = "".join(f"<li>{e(o)}</li>" for o in n["objectifs"])
    pron = "".join(f"<li>{e(p)}</li>" for p in n["prononciation"])
    err = "".join(f'<tr><td class="wrong" lang="en">✗ {e(a)}</td><td class="right" lang="en">✓ {e(b)}</td><td>{e(w)}</td></tr>' for a, b, w in n["erreurs"])
    dl = n["dialogue"]
    dia = "".join(f'<div class="dialogue-line"><span class="dialogue-who">{e(who)}</span><p><strong lang="en">{e(line)}</strong><br><span class="example-note">{e(tr)}</span></p></div>' for who, line, tr in dl["lignes"])
    mots = "".join(f'<tr><td><a class="text-link" lang="en" href="{cambridge(w)}" target="_blank" rel="noopener" title="{t("Listen on Cambridge Dictionary", "Écouter sur le Cambridge Dictionary")}">{e(w)} 🔊</a></td><td lang="en">{e(s)}</td><td>{e(d)}</td></tr>' for w, s, d in n["mots"])
    exos = ""
    for x in n["exercices"]:
        qs = "".join(f"<li>{e(q)}</li>" for q, _ in x["items"])
        ans = "".join(f"<li>{e(a)}</li>" for _, a in x["items"])
        exos += (f'<div class="exercise" data-ws="writing"><h3>{e(x["titre"])}</h3><p>{e(x["consigne"])}</p><ol>{qs}</ol>'
                 f'<details class="answer" data-ws="writing"><summary>{t("Show the answers", "Voir le corrigé")}</summary><ol>{ans}</ol></details></div>')
    keep = "".join(f"<li>{e(k)}</li>" for k in n["a_retenir"])
    rel = "".join((f'<li><a class="text-link" href="../{level_of(k).lower()}-{k:03d}/">{level_of(k)} · {k} — {e(PROGRAMME[k])}</a></li>' if k in online
                   else f'<li>{level_of(k)} · {k} — {e(PROGRAMME[k])} <span class="muted">({t("coming soon", "bientôt")})</span></li>') for k in n["liens"])
    refs = "".join(f'<li><a class="text-link" href="{REFS[r][1]}" target="_blank" rel="noopener">{e(REFS[r][0])} ↗</a></li>' for r in n["refs"])
    other = t('<p class="lang-note">Prefer explanations in French? <a class="text-link" lang="fr" href="../../../lessons/{id}/">Version française de cette leçon →</a></p>',
              '<p class="lang-note">Envie d’immersion ? <a class="text-link" lang="en" href="../../en/lessons/{id}/">This lesson in English →</a></p>').replace("{id}", lid(n))
    body = (f'<section class="page-hero"><div class="container"><div class="breadcrumb"><a href="../../index.html">{t("Home", "Accueil")}</a> / <a href="../index.html">{t("Lessons", "Leçons")}</a> / {c} · {n["n"]:03d}</div>'
            f'<span class="eyebrow">{c} · {EN[c]} · {t("lesson", "leçon")} {n["n"]}</span><h1>{e(n["titre"])}</h1><p>{e(n["intro"])}</p></div></section>'
            f'<section class="section"><div class="container lesson-layout"><article class="lesson-content">'
            f'<div class="lesson-meta"><span>⏱ <strong>30–45 min</strong></span><span>✎ {t("Written by", "Rédigé par")} <strong>JG</strong></span><span>◎ {t("Level", "Niveau")} <strong>{c}</strong></span></div>{other}'
            f'<div class="objectives"><strong>{t("By the end of this lesson, you will be able to:", "À la fin de cette leçon, tu sauras :")}</strong><ul>{obj}</ul></div>'
            f'{video_slots()}{secs}'
            f'<h2>{t("The formula", "La formule")}</h2><div class="formula" lang="en">{e(n["formule"])}</div>'
            f'<h2>{t("Pronunciation", "Prononciation")}</h2><p class="ws-label" data-ws="pronunciation">{e(WS["pronunciation"])}</p><ul>{pron}</ul>'
            f'<h2>{t("Common mistakes", "Les erreurs fréquentes")}</h2><div class="table-wrap"><table class="mistakes"><thead><tr><th>{t("Don’t say", "À éviter")}</th><th>{t("Say", "À dire")}</th><th>{t("Why", "Pourquoi")}</th></tr></thead><tbody>{err}</tbody></table></div>'
            f'<h2>{t("In a conversation", "En situation")}</h2><p class="ws-label" data-ws="listening">{e(WS["listening"])}</p><p class="muted">{e(dl["contexte"])}</p><div class="dialogue" data-ws="listening">{dia}</div>'
            f'<h2>{t("Words to remember", "Les mots à retenir")}</h2><p class="ws-label" data-ws="vocabulary">{e(WS["vocabulary"])}</p><p class="muted">{t("Click a word to hear its British and American pronunciation.", "Clique sur un mot pour entendre sa prononciation britannique et américaine.")}</p>'
            f'<div class="table-wrap"><table class="words" data-ws="vocabulary"><thead><tr><th>{t("Word", "Mot")}</th><th>{t("In context", "En contexte")}</th><th>{t("Meaning", "Sens")}</th></tr></thead><tbody>{mots}</tbody></table></div>'
            f'<h2>{t("Exercises", "Exercices")}</h2><p class="ws-label" data-ws="writing">{e(WS["writing"])}</p><p>{t("From easy to harder. Answer without looking at the lesson, then check each exercise.", "Du plus simple au plus difficile. Réponds sans regarder la leçon, puis vérifie chaque exercice.")}</p>{exos}'
            f'<aside class="lesson-takeaway" aria-label="{t("Key points", "À retenir")}"><strong>{t("Key points", "À retenir")}</strong><ul>{keep}</ul></aside>'
            f'<h2>{t("Go further", "Pour aller plus loin")}</h2><p><strong>{t("Related lessons", "Leçons liées")}</strong></p><ul>{rel}</ul><p><strong>{t("Check it in the references", "Vérifier dans les références")}</strong></p><ul>{refs}</ul>'
            f'{lesson_nav(i)}</article>'
            f'<aside class="lesson-aside"><span class="tag">{t("Complete lesson", "Leçon complète")}</span><h3>{t("At a glance", "En bref")}</h3><p><strong>{t("Lesson", "Leçon")}</strong><br>{c} · {n["n"]:03d}</p>'
            f'<nav data-lesson-toc aria-label="{t("In this lesson", "Dans cette leçon")}" class="lesson-toc"><p><strong>{t("In this lesson", "Dans cette leçon")}</strong></p></nav>'
            f'<p><strong>{t("Method", "Méthode")}</strong><br>{t("Read, listen, do the exercises without looking, check. Come back in 3 days, then in 7.", "Lis, écoute, fais les exercices sans regarder, vérifie. Reviens dans 3 jours, puis dans 7.")}</p>'
            f'<button class="button button-dark" type="button" data-print>{t("Print the lesson", "Imprimer la leçon")}</button><a class="button button-outline" href="../../review/">{t("Review the words", "Réviser les mots")}</a><a class="button button-outline" href="../index.html#{c.lower()}">{t(f"All {c} lessons", f"Toutes les leçons {c}")}</a></aside></div></section>')
    write(f"lessons/{lid(n)}/index.html", page(f"{c} · {n['n']} — {n['titre']} — {SITE}", body, 2, f"lessons/{lid(n)}/", "lessons/", n["intro"]))


def build_lesson(i, n):
    if "sections" in n:
        return build_lesson_rich(i, n)
    regle = "".join(f"<li>{e(r)}</li>" for r in n["regle"])
    ex = "".join(f'<li><strong lang="en">{e(a)}</strong><br><span class="example-note">{e(b)}</span></li>' for a, b in n["exemples"])
    mots = "".join(f'<tr><td><a class="text-link" lang="en" href="{cambridge(w)}" target="_blank" rel="noopener" title="{t("Listen on Cambridge Dictionary", "Écouter sur le Cambridge Dictionary")}">{e(w)} 🔊</a></td><td lang="en">{e(s)}</td><td>{e(d)}</td></tr>' for w, s, d in n["mots"])
    exo = "".join(f"<li>{e(q)}</li>" for q in n["exercice"])
    cor = "".join(f"<li>{e(c)}</li>" for c in n["corrige"])
    prev = NOTIONS[i - 1] if i > 0 else None
    nxt = NOTIONS[i + 1] if i + 1 < len(NOTIONS) else None
    nav = f'<nav class="module-nav" aria-label="{t("Nearby lessons", "Leçons voisines")}">'
    nav += f'<a class="module-nav-link module-nav-prev" href="../{lid(prev)}/"><span class="module-nav-label">← {t("Previous lesson", "Leçon précédente")}</span><span class="module-nav-title">{prev["n"]}. {e(prev["titre"])}</span></a>' if prev else "<span></span>"
    nav += f'<a class="module-nav-link module-nav-next" href="../{lid(nxt)}/"><span class="module-nav-label">{t("Next lesson", "Leçon suivante")} →</span><span class="module-nav-title">{nxt["n"]}. {e(nxt["titre"])}</span></a>' if nxt else "<span></span>"
    nav += "</nav>"
    c = n["niveau"]
    other = t('<p class="lang-note">Prefer explanations in French? <a class="text-link" lang="fr" href="../../../lessons/{id}/">Version française de cette leçon →</a></p>',
              '<p class="lang-note">Envie d’immersion ? <a class="text-link" lang="en" href="../../en/lessons/{id}/">This lesson in English →</a></p>').replace("{id}", lid(n))
    body = (f'<section class="page-hero"><div class="container"><div class="breadcrumb"><a href="../../index.html">{t("Home", "Accueil")}</a> / <a href="../index.html">{t("Lessons", "Leçons")}</a> / {c} · {n["n"]:03d}</div>'
            f'<span class="eyebrow">{c} · {EN[c]} · {t("lesson", "leçon")} {n["n"]}</span><h1>{e(n["titre"])}</h1><p>{e(n["intro"])}</p></div></section>'
            f'<section class="section"><div class="container lesson-layout"><article class="lesson-content">'
            f'<div class="lesson-meta"><span>⏱ <strong>10 min</strong> {t("of practice", "de pratique")}</span><span>✎ {t("Written by", "Rédigé par")} <strong>JG</strong></span><span>◎ {t("Level", "Niveau")} <strong>{c}</strong></span></div>{other}'
            f'{video_slots()}'
            f'<h2>{t("The rule", "La règle")}</h2><ul>{regle}</ul><div class="formula" lang="en">{e(n["formule"])}</div>'
            f'<h2>{t("Examples", "Exemples")}</h2><ul class="examples">{ex}</ul>'
            f'<h2>{t("Five words to remember", "Cinq mots à retenir")}</h2><p class="ws-label" data-ws="vocabulary">{e(WS["vocabulary"])}</p><p class="muted">{t("Click a word to hear its British and American pronunciation.", "Clique sur un mot pour entendre sa prononciation britannique et américaine.")}</p>'
            f'<div class="table-wrap"><table class="words" data-ws="vocabulary"><thead><tr><th>{t("Word", "Mot")}</th><th>{t("In context", "En contexte")}</th><th>{t("Meaning", "Sens")}</th></tr></thead><tbody>{mots}</tbody></table></div>'
            f'<h2>{t("Exercise", "Exercice")}</h2><p class="ws-label" data-ws="writing">{e(WS["writing"])}</p><p>{t("Answer without looking at the rule, then check.", "Réponds sans regarder la règle, puis vérifie.")}</p><ol>{exo}</ol><details class="answer" data-ws="writing"><summary>{t("Show the answers", "Voir le corrigé")}</summary><ol>{cor}</ol></details>'
            f'<h2>{t("Watch out", "Attention")}</h2><div class="notice">{e(n["piege"])}</div>'
            f'<aside class="lesson-takeaway" aria-label="{t("Key point", "À retenir")}"><strong>{t("Key point", "À retenir")}</strong><p lang="en">{e(n["formule"])}</p></aside>{nav}</article>'
            f'<aside class="lesson-aside"><span class="tag">{t("Lesson available", "Leçon disponible")}</span><h3>{t("At a glance", "En bref")}</h3><p><strong>{t("Lesson", "Leçon")}</strong><br>{c} · {n["n"]:03d}</p>'
            f'<nav data-lesson-toc aria-label="{t("In this lesson", "Dans cette leçon")}" class="lesson-toc"><p><strong>{t("In this lesson", "Dans cette leçon")}</strong></p></nav>'
            f'<p><strong>{t("Method", "Méthode")}</strong><br>{t("Read, listen, do the exercise without looking, check. Come back in 3 days, then in 7.", "Lis, écoute, fais l’exercice sans regarder, vérifie. Reviens dans 3 jours, puis dans 7.")}</p>'
            f'<button class="button button-dark" type="button" data-print>{t("Print the summary", "Imprimer la fiche")}</button><a class="button button-outline" href="../../review/">{t("Review the words", "Réviser les mots")}</a><a class="button button-outline" href="../index.html#{c.lower()}">{t(f"All {c} lessons", f"Toutes les leçons {c}")}</a></aside></div></section>')
    write(f"lessons/{lid(n)}/index.html", page(f"{c} · {n['n']} — {n['titre']} — {SITE}", body, 2, f"lessons/{lid(n)}/", "lessons/", n["intro"]))


def build_studios():
    """Build six practice experiences from the canonical lesson corpus."""
    contract_errors = validate_activities(ACTIVITIES, NOTIONS)
    if contract_errors:
        raise ValueError("Invalid Studio activity contract: " + "; ".join(contract_errors))
    activity_by_studio = {activity["studio_id"]: activity for activity in ACTIVITIES}

    def source_lesson(number):
        return next((item for item in NOTIONS if item.get("n") == number), None)

    def dialogue_for(item):
        dialogue = (item or {}).get("dialogue") or {}
        return dialogue.get("lignes") or []

    def lesson_link(item):
        if not item:
            return "../lessons/"
        return f"../lessons/{lid(item)}/"

    def quiz_html(activity):
        quiz = activity["quiz"]
        key = activity["activity_id"]
        options = "".join(
            f'<label><input type="radio" name="{e(key)}" value="{e(option["id"])}"> '
            f'{e(t(option["en"], option["fr"]))}</label>'
            for option in quiz["options"]
        )
        return (
            f'<div class="studio-quiz" data-studio-quiz><fieldset>'
            f'<legend>{e(t(quiz["prompt_en"], quiz["prompt_fr"]))}</legend>{options}</fieldset>'
            f'<button class="button button-outline" type="button" data-check-quiz="{e(key)}" '
            f'data-answer="{e(quiz["correct_option_id"])}" data-correct-feedback="{e(t(quiz["feedback_en"], quiz["feedback_fr"]))}" '
            f'data-retry-feedback="{e(t(quiz["retry_en"], quiz["retry_fr"]))}">{t("Check my answer", "Vérifier ma réponse")}</button>'
            f'<p class="studio-feedback" data-quiz-feedback="{e(key)}" aria-live="polite"></p></div>'
        )

    def activity_progress(activity):
        key = e(activity["activity_id"])
        return (
            f'<p class="studio-progress" data-activity-status="{key}" role="status">'
            f'{t("Not completed yet", "Pas encore terminée")}</p>'
        )

    def completion_button(activity, label_en, label_fr):
        key = e(activity["activity_id"])
        return (
            f'<button class="button button-outline" type="button" data-complete-activity="{key}" '
            f'disabled>{t(label_en, label_fr)}</button>'
        )

    listening_activity = activity_by_studio["listening"]
    listening_lesson = source_lesson(listening_activity["source_lesson_id"])
    listening_lines = dialogue_for(listening_lesson)
    listening_html = "".join(
        f'<p><strong>{e(str(line[0]))}:</strong> {e(str(line[1]))}</p>'
        for line in listening_lines if len(line) >= 2
    )
    listening_text = " ".join(str(line[1]) for line in listening_lines if len(line) >= 2)
    listening_level = (listening_lesson or {}).get("niveau", "A2")
    listening_number = (listening_lesson or {}).get("n", 41)

    pronunciation_activity = activity_by_studio["pronunciation"]
    pronunciation_lesson = source_lesson(pronunciation_activity["source_lesson_id"])
    pronunciation_points = (pronunciation_lesson or {}).get("prononciation") or []
    pronunciation_tips = "".join(f"<li>{e(str(point))}</li>" for point in pronunciation_points[:4])
    pronunciation_line = next(
        (str(line[1]) for line in dialogue_for(pronunciation_lesson) if len(line) >= 2),
    )
    pronunciation_level = (pronunciation_lesson or {}).get("niveau", "B1")
    pronunciation_number = (pronunciation_lesson or {}).get("n", 91)

    reading_activity = activity_by_studio["reading"]
    reading_lesson = source_lesson(reading_activity["source_lesson_id"])
    reading_lines = dialogue_for(reading_lesson)
    reading_html = "".join(
        f'<p><strong>{e(str(line[0]))}:</strong> {e(str(line[1]))}</p>'
        for line in reading_lines if len(line) >= 2
    )
    reading_level = (reading_lesson or {}).get("niveau", "C1")
    reading_number = (reading_lesson or {}).get("n", 221)
    reading_title = (reading_lesson or {}).get("titre", "Reading in context")

    writing_activity = activity_by_studio["writing"]
    writing_lesson = source_lesson(writing_activity["source_lesson_id"])
    writing_level = (writing_lesson or {}).get("niveau", "A2")
    writing_number = (writing_lesson or {}).get("n", 41)

    vocabulary_activity = activity_by_studio["vocabulary"]
    vocabulary_lesson = source_lesson(vocabulary_activity["source_lesson_id"])
    vocabulary_words = (vocabulary_lesson or {}).get("mots") or []
    vocab_cards = "".join(
        f'<details class="studio-vocab-item"><summary>{e(str(word[0]))}</summary><p lang="en">{e(str(word[1]))}</p><p>{e(str(word[2]))}</p></details>'
        for word in vocabulary_words[:8] if len(word) >= 3
    )
    vocab_level = (vocabulary_lesson or {}).get("niveau", "B1")
    vocab_number = (vocabulary_lesson or {}).get("n", 91)
    vocab_count = min(len(vocabulary_words), 8)
    memory_activity = activity_by_studio["memory"]

    cards = (
        f'<article class="card ws-card studio-card" id="listening" data-ws="listening" data-activity-id="{listening_activity["activity_id"]}" data-completion-rule="{listening_activity["completion_rule"]}">'
        f'<div class="studio-card-head"><span class="tag">01 / LISTENING</span><span class="badge badge-level">{listening_level}</span></div>'
        f'<h3>Listening Studio</h3><p>{t("Train focused listening and confidence with a real lesson dialogue.", "Entraîne ton écoute ciblée et ta confiance avec un dialogue issu d’une leçon.")}</p>'
        f'<p class="studio-outcome"><strong>{t("You will practise:", "Objectif :")}</strong> {e(t(listening_activity["outcome_en"], listening_activity["outcome_fr"]))}</p>'
        f'<div class="studio-activity-meta"><span>{t("Source lesson", "Leçon source")} {listening_number:03d}</span><span>·</span><span>{t(listening_activity["duration_en"], listening_activity["duration_fr"])}</span></div>'
        f'{activity_progress(listening_activity)}'
        f'<div class="studio-task"><p class="eyebrow">{t("First listen · no transcript", "Première écoute · sans transcription")}</p>'
        f'<p>{t("Listen once without reading. Then answer the detail question below.", "Écoute une première fois sans lire. Réponds ensuite à la question de détail ci-dessous.")}</p>'
        f'<button class="button button-primary" type="button" data-speak-text="{e(listening_text)}" data-speak-rate="0.88">{t("Play the dialogue", "Écouter le dialogue")} <span aria-hidden="true">▶</span></button>'
        f'{quiz_html(listening_activity)}'
        f'<details class="studio-reveal"><summary>{t("Reveal the transcript", "Afficher la transcription")}</summary><div class="dialogue-box" lang="en">{listening_html}</div></details>'
        f'<a class="text-link" href="{lesson_link(listening_lesson)}">{t("Study the grammar behind this dialogue", "Étudier la notion grammaticale liée à ce dialogue")} →</a></div>'
        f'<p class="studio-disclosure">{t("Audio is generated by your browser’s English voice. It is synthetic practice audio, not a human recording.", "L’audio est généré par la voix anglaise de ton navigateur. Il s’agit d’une voix synthétique, pas d’un enregistrement humain.")}</p></article>'

        f'<article class="card ws-card studio-card" id="pronunciation" data-ws="pronunciation" data-activity-id="{pronunciation_activity["activity_id"]}" data-completion-rule="{pronunciation_activity["completion_rule"]}">'
        f'<div class="studio-card-head"><span class="tag">02 / PRONUNCIATION</span><span class="badge badge-level">{pronunciation_level}</span></div>'
        f'<h3>Pronunciation Lab</h3><p>{t("Move from hearing a model to producing a clearer, more controlled sentence.", "Passe de l’écoute d’un modèle à une production plus claire et mieux maîtrisée.")}</p>'
        f'<p class="studio-outcome"><strong>{t("You will practise:", "Objectif :")}</strong> {e(t(pronunciation_activity["outcome_en"], pronunciation_activity["outcome_fr"]))}</p>'
        f'<div class="studio-activity-meta"><span>{t("Source lesson", "Leçon source")} {pronunciation_number:03d}</span><span>·</span><span>{t(pronunciation_activity["duration_en"], pronunciation_activity["duration_fr"])}</span></div>'
        f'{activity_progress(pronunciation_activity)}'
        f'<div class="studio-task"><p class="eyebrow">{t("Listen · mark · repeat", "Écoute · repère · répète")}</p>'
        f'<p class="pronunciation-line" lang="en">{e(pronunciation_line)}</p>'
        f'<div class="studio-button-row"><button class="button button-primary" type="button" data-speak-text="{e(pronunciation_line)}" data-speak-rate="0.82">{t("Slow model", "Modèle lent")}</button><button class="button button-outline" type="button" data-speak-text="{e(pronunciation_line)}" data-speak-rate="1">{t("Natural speed", "Vitesse naturelle")}</button></div>'
        f'<p>{t("Repeat three times: first for accuracy, then for rhythm, then without looking.", "Répète trois fois : d’abord pour la précision, ensuite pour le rythme, enfin sans regarder.")}</p>'
        f'<details><summary>{t("Pronunciation focus from the lesson", "Points de prononciation de la leçon")}</summary><ul class="studio-focus-list">{pronunciation_tips}</ul></details>'
        f'<fieldset class="studio-self-check" data-activity-checklist="{pronunciation_activity["activity_id"]}"><legend>{t("My self-check", "Mon auto-évaluation")}</legend>'
        f'<label><input type="checkbox"> {t("I stressed the key content words.", "J’ai accentué les mots porteurs de sens.")}</label>'
        f'<label><input type="checkbox"> {t("I kept the sentence groups smooth.", "J’ai gardé un rythme fluide entre les groupes de mots.")}</label>'
        f'<label><input type="checkbox"> {t("I repeated without reading the model.", "J’ai répété sans lire le modèle.")}</label></fieldset>'
        f'<a class="text-link" href="{lesson_link(pronunciation_lesson)}">{t("Open the source lesson", "Ouvrir la leçon source")} →</a></div>'
        f'{completion_button(pronunciation_activity, "Mark pronunciation practice complete", "Terminer la pratique de prononciation")}'
        f'<p class="studio-completion-hint">{t("Complete all three checks to record this practice.", "Coche les trois critères pour valider cette pratique.")}</p>'
        f'<p class="studio-disclosure">{t("This is guided self-assessment. The browser does not score your voice or accent.", "Il s’agit d’une auto-évaluation guidée. Le navigateur ne note pas ta voix ni ton accent.")}</p></article>'

        f'<article class="card ws-card studio-card" id="reading" data-ws="reading" data-activity-id="{reading_activity["activity_id"]}" data-completion-rule="{reading_activity["completion_rule"]}">'
        f'<div class="studio-card-head"><span class="tag">03 / READING</span><span class="badge badge-level">{reading_level}</span></div>'
        f'<h3>Reading Room</h3><p>{t("Read a lesson dialogue carefully and locate a specific detail in context.", "Lis attentivement un dialogue de leçon et retrouve une information précise dans son contexte.")}</p>'
        f'<p class="studio-outcome"><strong>{t("You will practise:", "Objectif :")}</strong> {e(t(reading_activity["outcome_en"], reading_activity["outcome_fr"]))}</p>'
        f'<div class="studio-activity-meta"><span>{t("Source lesson", "Leçon source")} {reading_number:03d}</span><span>·</span><span>{t(reading_activity["duration_en"], reading_activity["duration_fr"])}</span></div>'
        f'{activity_progress(reading_activity)}'
        f'<div class="studio-task"><p class="eyebrow">{t("Read for meaning", "Lire pour comprendre")}</p><h4>{e(reading_title)}</h4><div class="reading-passage" lang="en">{reading_html}</div>'
        f'{quiz_html(reading_activity)}'
        f'<a class="text-link" href="{lesson_link(reading_lesson)}">{t("Explore the language in its lesson", "Approfondir la langue dans la leçon")} →</a></div></article>'

        f'<article class="card ws-card studio-card" id="writing" data-ws="writing" data-activity-id="{writing_activity["activity_id"]}" data-completion-rule="{writing_activity["completion_rule"]}">'
        f'<div class="studio-card-head"><span class="tag">04 / WRITING</span><span class="badge badge-level">{writing_level}</span></div>'
        f'<h3>Writing Workshop</h3><p>{t("Write for a real purpose, then review your draft with a clear rubric.", "Écris avec un objectif réel, puis relis ton texte à l’aide d’une grille claire.")}</p>'
        f'<p class="studio-outcome"><strong>{t("You will practise:", "Objectif :")}</strong> {e(t(writing_activity["outcome_en"], writing_activity["outcome_fr"]))}</p>'
        f'<div class="studio-activity-meta"><span>{t("Source lesson", "Leçon source")} {writing_number:03d}</span><span>·</span><span>{t(writing_activity["duration_en"], writing_activity["duration_fr"])}</span></div>'
        f'{activity_progress(writing_activity)}'
        f'<div class="studio-task"><p class="eyebrow">{t("Writing brief", "Consigne d’écriture")}</p><h4>{t("A short account of a recent experience", "Raconter une expérience récente")}</h4>'
        f'<p>{t("Write 50–70 words about something you did recently. Include when it happened, what you did, who was involved and how you felt. Use the past simple accurately.", "Écris 50 à 70 mots sur une expérience récente. Précise quand elle a eu lieu, ce que tu as fait, avec qui et ce que tu as ressenti. Utilise correctement le past simple.")}</p>'
        f'<label class="activity-label" for="studio-writing">{t("Your draft", "Ton brouillon")}</label><textarea id="studio-writing" class="activity-response" rows="7" maxlength="1600" placeholder="{t("Last weekend, I…", "Last weekend, I…")}" data-draft-field="studio-writing"></textarea>'
        f'<p class="studio-word-count" data-word-count="studio-writing" data-min-words="50" data-max-words="70" role="status" aria-live="polite">0 / 70 {t("words", "mots")} · {t("target: 50–70", "objectif : 50–70")}</p>'
        f'<fieldset class="studio-self-check" data-activity-checklist="{writing_activity["activity_id"]}"><legend>{t("Before you finish", "Avant de terminer")}</legend>'
        f'<label><input type="checkbox"> {t("My text has a clear beginning, middle and end.", "Mon texte a un début, un développement et une fin clairs.")}</label>'
        f'<label><input type="checkbox"> {t("I used past forms consistently.", "J’ai utilisé les formes du passé de manière cohérente.")}</label>'
        f'<label><input type="checkbox"> {t("I checked irregular verbs and time expressions.", "J’ai vérifié les verbes irréguliers et les expressions de temps.")}</label>'
        f'<label><input type="checkbox"> {t("I used linking words to guide the reader.", "J’ai utilisé des connecteurs pour guider le lecteur.")}</label></fieldset>'
        f'<button class="button button-outline" type="button" data-writing-save="studio-writing">{t("Save draft on this device", "Enregistrer le brouillon sur cet appareil")}</button><p class="studio-feedback" data-writing-feedback="studio-writing" aria-live="polite"></p>'
        f'{completion_button(writing_activity, "Mark writing task complete", "Terminer l’activité d’écriture")}'
        f'<p class="studio-completion-hint">{t("Save a 50–70 word draft and complete every self-check to finish.", "Enregistre un brouillon de 50 à 70 mots et coche chaque critère pour terminer.")}</p>'
        f'<a class="text-link" href="{lesson_link(writing_lesson)}">{t("Review the grammar for this task", "Réviser la grammaire utile pour cette tâche")} →</a></div>'
        f'<p class="studio-disclosure">{t("Your draft stays in this browser. It is not sent for automatic correction.", "Ton brouillon reste dans ce navigateur. Il n’est pas envoyé pour une correction automatique.")}</p></article>'

        f'<article class="card ws-card studio-card" id="vocabulary" data-ws="vocabulary" data-activity-id="{vocabulary_activity["activity_id"]}" data-completion-rule="{vocabulary_activity["completion_rule"]}">'
        f'<div class="studio-card-head"><span class="tag">05 / VOCABULARY</span><span class="badge badge-level">{vocab_level}</span></div>'
        f'<h3>Vocabulary &amp; Expressions</h3><p>{t("Build useful vocabulary from the lesson corpus, not from a disconnected word list.", "Développe ton vocabulaire à partir des leçons, pas d’une liste de mots déconnectée.")}</p>'
        f'<p class="studio-outcome"><strong>{t("You will practise:", "Objectif :")}</strong> {e(t(vocabulary_activity["outcome_en"], vocabulary_activity["outcome_fr"]))}</p>'
        f'<div class="studio-activity-meta"><span>{t("Source lesson", "Leçon source")} {vocab_number:03d}</span><span>·</span><span>{t(vocabulary_activity["duration_en"], vocabulary_activity["duration_fr"])} · {vocab_count} {t("items", "éléments")}</span></div>'
        f'{activity_progress(vocabulary_activity)}'
        f'<div class="studio-task"><p class="eyebrow">{t("Active recall", "Rappel actif")}</p><p>{t("Try to explain each expression before opening it. Read the example aloud and make a new sentence of your own.", "Essaie d’expliquer chaque expression avant de l’ouvrir. Lis l’exemple à voix haute et crée ta propre phrase.")}</p>{vocab_cards}'
        f'<label class="activity-label" for="studio-vocab-sentence">{t("Write one new sentence with a lesson expression", "Écris une nouvelle phrase avec une expression de la leçon")}</label><input id="studio-vocab-sentence" class="activity-response" type="text" maxlength="240" data-vocab-sentence placeholder="{t("I have gained experience...", "I have gained experience...")}">'
        f'<fieldset class="studio-self-check" data-activity-checklist="{vocabulary_activity["activity_id"]}"><legend>{t("Check your sentence", "Vérifie ta phrase")}</legend><label><input type="checkbox"> {t("I used a lesson expression accurately and checked the meaning in context.", "J’ai utilisé correctement une expression de la leçon et vérifié son sens en contexte.")}</label></fieldset>'
        f'{completion_button(vocabulary_activity, "Mark vocabulary practice complete", "Terminer la pratique du vocabulaire")}'
        f'<p class="studio-completion-hint">{t("Write a sentence of at least four words to demonstrate the expression in context.", "Écris une phrase d’au moins quatre mots pour utiliser l’expression en contexte.")}</p>'
        f'<a class="text-link" href="{lesson_link(vocabulary_lesson)}">{t("Study the full lesson", "Étudier la leçon complète")} →</a></div></article>'

        f'<article class="card ws-card studio-card" id="memory" data-ws="memory" data-activity-id="{memory_activity["activity_id"]}" data-completion-rule="{memory_activity["completion_rule"]}">'
        f'<div class="studio-card-head"><span class="tag">06 / MEMORY &amp; REVIEW</span><span class="badge badge-state">{t("Available", "Disponible")}</span></div>'
        f'<h3>Memory &amp; Review</h3><p>{t("Turn lesson vocabulary into repeated retrieval. Your local review history helps bring difficult words back.", "Transforme le vocabulaire des leçons en rappels réguliers. Ton historique local aide à faire revenir les mots difficiles.")}</p>'
        f'<p class="studio-outcome"><strong>{t("You will practise:", "Objectif :")}</strong> {e(t(memory_activity["outcome_en"], memory_activity["outcome_fr"]))}</p>'
        f'<div class="studio-activity-meta"><span>{t(memory_activity["duration_en"], memory_activity["duration_fr"])}</span></div>'
        f'{activity_progress(memory_activity)}'
        f'<div class="studio-task"><p class="eyebrow">{t("Your review system", "Ton système de révision")}</p>'
        f'<ul class="studio-focus-list"><li>{t("Retrieve before revealing the answer.", "Retrouve la réponse avant de la révéler.")}</li><li>{t("Mark difficult words honestly.", "Signale honnêtement les mots difficiles.")}</li><li>{t("Mix levels and revisit related lessons.", "Mélange les niveaux et reviens aux leçons liées.")}</li></ul>'
        f'<a class="button button-primary" href="../review/">{t("Open the review cards", "Ouvrir les cartes de révision")} →</a>'
        f'{completion_button(memory_activity, "I completed a review session", "J’ai terminé une séance de révision")}'
        f'</div></article>'
    )

    body = (hero_page([t("Studios", "Studios")], t("Six ways to make English yours", "Six façons de faire tien l’anglais"),
                      t("Practise deliberately. <em>Make every skill usable.</em>", "Entraîne-toi avec méthode. <em>Rends chaque compétence vivante.</em>"),
                      t("Six focused practice spaces grounded in the lesson library. Start with one short task, check your understanding, then return to the source lesson or review cards to deepen what you have learnt.", "Six espaces d’entraînement ciblés, ancrés dans la bibliothèque de leçons. Commence par une activité courte, vérifie ta compréhension, puis retourne à la leçon source ou aux cartes de révision pour approfondir."), 1)
            + f'<section class="section"><div class="container"><div class="section-head"><div><span class="eyebrow">{t("The practice studios", "Les studios d’entraînement")}</span><h2>{t("One skill at a time. A stronger English.", "Une compétence à la fois. Un anglais plus solide.")}</h2></div><p>{t("Activities are linked to the canonical lesson library. They are first practice modules, not a complete graded catalogue for every level.", "Les activités sont reliées à la bibliothèque canonique de leçons. Ce sont des premiers modules d’entraînement, pas encore un catalogue complet pour tous les niveaux.")}</p></div><div class="studio-progress-overview" data-studio-overview><div><strong data-studio-progress-count>0 / 6</strong><span>{t("activities completed", "activités terminées")}</span></div><progress max="6" value="0" data-studio-progress-bar aria-label="{t("Studio activities completed", "Activités Studio terminées")}"></progress><small data-studio-storage-status role="status">{t("Progress is saved only in this browser.", "La progression est enregistrée uniquement dans ce navigateur.")}</small></div><div class="grid-ws">{cards}</div>'
            + f'<div class="quote-panel" style="margin-top:48px"><div><span class="eyebrow">{t("A learning loop", "Une boucle d’apprentissage")}</span><h2>{t("Learn it. Practise it. Retrieve it. Use it.", "Apprendre. S’entraîner. Retrouver. Utiliser.")}</h2><p>{t("A studio activity should never be an isolated click: it should send you back to a lesson, prepare you for a real conversation or strengthen your next review.", "Une activité de studio ne doit jamais être un clic isolé : elle doit te ramener vers une leçon, te préparer à une vraie conversation ou renforcer ta prochaine révision.")}</p></div><a class="button button-primary" href="../path/">{t("Explore the A1–C1 path", "Explorer le parcours A1–C1")} →</a></div></div></section>')
    write("studios/index.html", page(f"{t('Practice Studios', 'Studios d’entraînement')} — {SITE}", body, 1, "studios/", "studios/"))

def build_my_learning():
    """Build a transparent, browser-local overview of the progress the site already stores."""
    studio_ids = [activity["activity_id"] for activity in ACTIVITIES]
    speaking_keys = [
        topic["id"] + "-" + level.lower()
        for topic in SPEAKING["topics"]
        for level in SPEAKING["levels"]
        if topic["levels"][level]["status"] == "published"
    ]
    studio_json = e(json.dumps(studio_ids, ensure_ascii=False))
    speaking_json = e(json.dumps(speaking_keys, ensure_ascii=False))
    body = (
        hero_page([t("My learning", "Mon espace")], t("Your personal overview", "Ton espace de progression"),
                  t("See your progress. <em>Choose your next step.</em>", "Vois tes progrès. <em>Choisis la suite.</em>"),
                  t("A simple overview of the practice you have completed and the work you have saved in this browser. No account is required.",
                    "Un aperçu simple des activités terminées et du travail enregistré dans ce navigateur. Aucun compte n’est nécessaire."), 1)
        + f'<section class="section"><div class="container"><div class="section-head"><div><span class="eyebrow">{t("Your activity", "Ton activité")}</span><h2>{t("Progress you can actually see.", "Une progression visible et concrète.")}</h2></div><p>{t("These figures come from the activities that currently save progress. They are local to this browser and are not synchronised across devices.", "Ces chiffres proviennent des activités qui enregistrent actuellement une progression. Ils restent dans ce navigateur et ne sont pas synchronisés entre appareils.")}</p></div>'
        + f'<div class="grid-3 learning-stats" data-learning-dashboard data-studio-ids="{studio_json}" data-speaking-keys="{speaking_json}">'
        + f'<article class="card learning-stat"><span class="eyebrow">{t("Practice Studios", "Studios d’entraînement")}</span><strong data-learning-value="studios">—</strong><progress max="{len(studio_ids)}" value="0" data-learning-progress="studios" aria-label="{t("Completed Studio activities", "Activités Studio terminées")}"></progress><p>{t("Activities completed", "Activités terminées")}</p></article>'
        + f'<article class="card learning-stat"><span class="eyebrow">Speak English in Real Life</span><strong data-learning-value="speaking">—</strong><progress max="{max(1, len(speaking_keys))}" value="0" data-learning-progress="speaking" aria-label="{t("Completed conversation units", "Unités de conversation terminées")}"></progress><p>{t("Published conversation units completed", "Unités de conversation disponibles terminées")}</p></article>'
        + f'<article class="card learning-stat"><span class="eyebrow">{t("Memory & Review", "Mémoire et révision")}</span><strong data-learning-value="review">—</strong><p>{t("Words with a saved review score", "Mots avec un score de révision enregistré")}</p><small data-learning-value="review-priority">—</small></article>'
        + f'<article class="card learning-stat"><span class="eyebrow">{t("Writing", "Écriture")}</span><strong data-learning-value="drafts">—</strong><p>{t("Saved writing drafts", "Brouillons d’écriture enregistrés")}</p></article>'
        + f'<article class="card learning-stat"><span class="eyebrow">{t("Conversation notes", "Notes de conversation")}</span><strong data-learning-value="notes">—</strong><p>{t("Topics with notes saved on this device", "Sujets avec des notes enregistrées sur cet appareil")}</p></article>'
        + f'</div><p class="muted" data-learning-storage-status role="status" aria-live="polite">{t("Reading your local progress…", "Lecture de ta progression locale…")}</p>'
        + f'<div class="quote-panel" style="margin-top:40px"><div><span class="eyebrow">{t("A useful next step", "Une prochaine étape utile")}</span><h2>{t("Keep the learning loop moving.", "Fais vivre la boucle d’apprentissage.")}</h2><p>{t("Study a lesson, practise one skill, then return to review. You can resume from any of the spaces below.", "Étudie une leçon, entraîne une compétence, puis reviens réviser. Tu peux reprendre depuis l’un des espaces ci-dessous.")}</p></div><div class="hero-actions"><a class="button button-primary" href="../path/">{t("Explore the path", "Explorer le parcours")}</a><a class="button button-outline" href="../studios/">{t("Open the Studios", "Ouvrir les Studios")}</a><a class="button button-outline" href="../speak/">{t("Practise speaking", "Pratiquer l’oral")}</a></div></div>'
        + f'<p class="small muted" style="margin-top:28px">{t("Transparency note: lesson-page completion is not tracked yet. This overview reports only Studio activities, published Speak units, saved review scores, writing drafts and conversation notes.", "Transparence : la lecture des leçons n’est pas encore suivie comme une activité terminée. Cette page ne présente que les activités Studio, les unités Speak publiées, les scores de révision, les brouillons d’écriture et les notes de conversation.")}</p>'
        + '</div></section>'
    )
    write("my-learning/index.html", page(f"{t('My learning', 'Mon espace')} — {SITE}", body, 1, "my-learning/", "my-learning/"))


def build_review():
    cards = [{"en": w, "ex": s, "def": d, "n": n["n"], "lvl": n["niveau"], "url": f"../lessons/{lid(n)}/"} for n in NOTIONS for w, s, d in n["mots"]]
    data = json.dumps(cards, ensure_ascii=False).replace("</", "<\\/")
    opts = "".join(f'<option value="{l["code"]}">{l["code"]}</option>' for l in NIVEAUX)
    body = (hero_page([t("Review", "Réviser")], "Memory &amp; Review", t("Review a little, remember a lot.", "Réviser un peu, retenir beaucoup."),
                      t(f"The {len(cards)} words from the lessons, as cards to flip: look at the word, say its meaning out loud, then flip the card. The words you miss come back more often.",
                        f"Les {len(cards)} mots des leçons, en cartes à retourner : regarde le mot, dis son sens à voix haute, puis retourne la carte. Les mots ratés reviennent plus souvent."), 1)
            + f'<section class="section"><div class="container"><div class="catalog-tools"><select class="filter-select" data-review-level aria-label="{t("Level", "Niveau")}"><option value="all">{t("All levels", "Tous les niveaux")}</option>{opts}</select><select class="filter-select" data-review-dir aria-label="{t("Direction", "Sens")}"><option value="en">{t("Word → meaning", "Anglais → français")}</option><option value="def">{t("Meaning → word", "Français → anglais")}</option></select></div>'
            + f'<div class="flashcard" data-ws="memory" data-flashcard tabindex="0" role="button" aria-label="{t("Flip the card", "Retourner la carte")}"><span class="fc-meta" data-fc-meta></span><p class="fc-front" data-fc-front></p><div class="fc-back" data-fc-back hidden></div></div>'
            + f'<div class="fc-actions"><button class="button button-outline" type="button" data-fc-flip>{t("Flip", "Retourner")}</button><button class="button button-outline" type="button" data-fc-again>{t("Again", "À revoir")}</button><button class="button button-primary" type="button" data-fc-know>{t("I know it", "Je sais")}</button></div><p class="muted" data-fc-score></p></div></section>'
            + f'<section class="section band"><div class="container"><div class="section-head"><div><span class="eyebrow">{t("Go further", "Aller plus loin")}</span><h2>{t("Free and reliable tools.", "Des outils gratuits et fiables.")}</h2></div><p>{t("To go beyond the lessons without spending money.", "Pour aller au-delà des leçons sans dépenser d’argent.")}</p></div><div class="grid-3">'
            + f'<article class="card"><div class="card-top"><span class="icon-tile">◎</span><span class="tag">{t("Level", "Niveau")}</span></div><h3>{t("Test your level", "Tester son niveau")}</h3><p>{t("The free EF SET test places you from A1 to C2 in about fifty minutes.", "Le test gratuit EF SET te situe de A1 à C2 en une cinquantaine de minutes.")}</p><a class="text-link" href="https://www.efset.org/" target="_blank" rel="noopener">efset.org ↗</a></article>'
            + f'<article class="card" data-ws="pronunciation"><div class="card-top"><span class="icon-tile">🔊</span><span class="tag">{t("Pronunciation", "Prononciation")}</span></div><h3>{t("Hear a word", "Écouter un mot")}</h3><p>{t("The Cambridge Dictionary gives the British and American audio for every word.", "Le Cambridge Dictionary donne l’audio britannique et américain de chaque mot.")}</p><a class="text-link" href="https://dictionary.cambridge.org/" target="_blank" rel="noopener">dictionary.cambridge.org ↗</a></article>'
            + f'<article class="card" data-ws="memory"><div class="card-top"><span class="icon-tile">↻</span><span class="tag">{t("Memory", "Mémoire")}</span></div><h3>{t("Anki cards", "Cartes Anki")}</h3><p>{t("Use the review cards on this site. No weekly Anki or Quizlet email is currently distributed.", "Utilise les cartes de révision du site. Aucun e-mail hebdomadaire Anki ou Quizlet n’est actuellement distribué.")}</p><a class="text-link" href="https://apps.ankiweb.net/" target="_blank" rel="noopener">apps.ankiweb.net ↗</a></article></div></div></section>'
            + f'<script>window.REVIEW_CARDS={data};</script>')
    write("review/index.html", page(f"{t('Review', 'Réviser')} — {SITE}", body, 1, "review/", "review/"))


def news_card(it):
    lang_note = " (in French)" if LANG == "en" and (it.get("lang") == "fr" or it.get("todo_en")) else ""
    learning_keys = ("resume", "pourquoi", "niveau", "vocabulaire", "questions", "question_discussion")
    has_learning = all(it.get(k) for k in learning_keys)
    learning = ""
    if has_learning:
        vocab = "".join(f'<li><strong>{e(word)}</strong> — {e(meaning)}</li>' for word, meaning in it["vocabulaire"])
        questions = "".join(f"<li>{e(q)}</li>" for q in it["questions"])
        learning = (f'<details class="news-learning"><summary>{t("Open the learning notes", "Ouvrir la fiche pédagogique")} · {e(it["niveau"])}</summary>'
                    f'<h4>{t("Levelled summary", "Résumé adapté au niveau")}</h4><p>{e(it["resume"])}</p>'
                    f'<h4>{t("Key vocabulary", "Vocabulaire essentiel")}</h4><ul>{vocab}</ul>'
                    f'<h4>{t("Comprehension", "Compréhension")}</h4><ol>{questions}</ol>'
                    f'<h4>{t("Discussion", "Discussion")}</h4><p>{e(it["question_discussion"])}</p></details>')
    else:
        learning = f'<p class="muted"><small>{t("Learning notes in preparation · headline and source link only", "Fiche pédagogique en préparation · titre et lien source uniquement")}</small></p>'
    return (f'<article class="card news-card" data-ws="reading" data-pays="{it["pays"]}"><div class="card-top"><span class="tag">{e(PAYS[it["pays"]])}</span><span class="muted"><small>{date_en(it["date"])}</small></span></div>'
            f'<h3{" lang=fr" if LANG == "en" and it.get("todo_en") else ""}>{e(it["titre"])}</h3>'
            + (f'<p><strong>{t("Reported facts", "Faits rapportés")}:</strong> {e(it["resume"])}</p>' if it.get("resume") and not has_learning else "")
            + (f'<p class="muted"><strong>{t("Learning context", "Contexte pédagogique")} :</strong> {e(it["pourquoi"])}</p>' if it.get("pourquoi") else "")
            + learning
            + f'<a class="text-link" href="{e(it["url"])}" target="_blank" rel="noopener">{t("Read the source", "Lire la source")} : {e(it["source"])}{lang_note} ↗</a></article>')


def build_news():
    items = sorted(NEWS, key=lambda x: x["date"], reverse=True)
    for it in items:
        assert it["pays"] in PAYS and it["url"].startswith("https://"), it
        learning_keys = ("resume", "pourquoi", "niveau", "vocabulaire", "questions", "question_discussion")
        if any(it.get(key) for key in learning_keys):
            assert all(it.get(key) for key in learning_keys), f"Incomplete news learning card: {it.get('titre', 'untitled')}"
    tabs = f'<button class="tab" type="button" role="tab" data-tab="all" aria-selected="true">{t("All", "Tout")}</button>' + "".join(f'<button class="tab" type="button" role="tab" data-tab="{k}" aria-selected="false">{e(v)}</button>' for k, v in PAYS.items())
    days = sorted({it["date"] for it in items}, reverse=True)
    def section(sel, depth):
        return (f'<section class="section"><div class="container"><div class="tabs" role="tablist" aria-label="{t("Choose a region", "Choisir une région")}">{tabs}</div><p class="empty-state" data-news-empty hidden>{t("No news for this country yet: it will come with the next editions.", "Pas encore d’actualité pour ce pays : elles arriveront avec les prochaines éditions.")}</p><div class="grid-2">{"".join(news_card(it) for it in sel)}</div>'
                + f'<p class="muted" style="margin-top:22px"><small>{t("Headlines are short summaries; details, figures and context are in the source article. You choose the region yourself: there is no geolocation.", "Les titres sont de courts résumés ; détails, chiffres et contexte sont dans l’article source. Tu choisis toi-même la région : aucune géolocalisation.")}</small></p>'
                + f'<p><strong>{t("By day", "Par jour")} :</strong> ' + " · ".join(f'<a class="text-link" href="{"../" * (depth - 1)}{d}/">{date_en(d)}</a>' for d in days) + "</p></div></section>")
    body = (hero_page([t("News", "Actualités")], t("The world, in context", "Le monde, en contexte"), t("The world, and your country.", "Le monde, et ton pays."),
                      t("Important stories from the newsletter, each dated and linked to its source. Choose a tab: “World” for international news, or your country. Your choice is remembered on this device.",
                        "Les grandes actualités de la newsletter, chacune datée et reliée à sa source. Choisis un onglet : « Monde » pour l’international, ou ton pays. Ton choix est retenu sur cet appareil."), 1)
            + section(items, 1))
    write("news/index.html", page(f"{t('World and country news', 'Actualités du monde et par pays')} — {SITE}", body, 1, "news/", "news/"))
    for d in days:
        sel = [it for it in items if it["date"] == d]
        body = (f'<section class="page-hero"><div class="container"><div class="breadcrumb"><a href="../../index.html">{t("Home", "Accueil")}</a> / <a href="../index.html">{t("News", "Actualités")}</a> / {date_en(d)}</div>'
                f'<span class="eyebrow">{t("News of the day", "Les actualités du jour")}</span><h1>{date_en(d)}</h1><p>{t("The stories of this edition, each linked to its source.", "Les actualités de cette édition, chacune reliée à sa source.")}</p></div></section>'
                + section(sel, 2))
        write(f"news/{d}/index.html", page(f"{t('News', 'Actualités')} · {date_en(d)} — {SITE}", body, 2, f"news/{d}/", "news/"))


def build_about():
    body = (hero_page([t("About", "À propos")], t("The project", "Le projet"), t("A library, not an inbox.", "Une bibliothèque, pas une boîte mail."),
                      t("The English lessons of the “Grandir chaque jour” newsletter were getting lost in emails. Here, every lesson has its own page, always available; the email keeps the exercises, the answers and the reminders.",
                        "Les leçons d’anglais de la newsletter « Grandir chaque jour » se perdaient dans les e-mails. Ici, chaque leçon a sa page, toujours disponible ; l’e-mail garde les exercices, les corrigés et les rappels."), 1)
            + '<section class="section"><div class="container"><div class="pillars">'
            + f'<div class="pillar"><span class="pillar-number">01</span><h2>{t("A guided path", "Un parcours guidé")}</h2><p>{t("The content follows the Common European Framework of Reference (CEFR), from A1 to C1, and keeps the numbers of the lessons already sent.", "Le contenu suit le Cadre européen commun de référence (CECRL), de A1 à C1, et garde les numéros des leçons déjà envoyées.")}</p></div>'
            + f'<div class="pillar"><span class="pillar-number">02</span><h2>{t("Your language, your choice", "Ta langue, ton choix")}</h2><p>{t("This English version explains everything in English. The French version (FR button) explains the same lessons in French.", "Les explications sont en français, les exemples en anglais. Le bouton EN donne la version entièrement en anglais, pour l’immersion totale.")}</p></div>'
            + f'<div class="pillar"><span class="pillar-number">03</span><h2>{t("Remember for the long term", "Retenir sur la durée")}</h2><p>{t("The review cards use active recall and a local difficulty score; scheduled reminders are not currently implemented.", "Les cartes utilisent le rappel actif et un score local de difficulté ; les rappels programmés ne sont pas encore implémentés.")}</p></div>'
            + f'</div><div class="narrow lesson-content" style="margin-top:56px"><h2>{t("Our commitments", "Nos engagements")}</h2><ul>'
            + f'<li><strong>{t("Accuracy.", "Exactitude.")}</strong> {t("Every word links to the Cambridge Dictionary; every news item links to its original article.", "Chaque mot renvoie au Cambridge Dictionary ; chaque actualité renvoie à son article d’origine.")}</li>'
            + f'<li><strong>{t("Transparency.", "Transparence.")}</strong> {t("The content is written with the help of Claude (AI) and reviewed. Found a mistake? Reply to the newsletter and it will be corrected.", "Le contenu est rédigé avec l’aide de Claude (IA) et relu. Une erreur ? Réponds à la newsletter et elle sera corrigée.")}</li>'
            + f'<li><strong>{t("Privacy.", "Confidentialité.")}</strong> {t("No cookies, no subscriber data. Only your theme, your news tab and your review progress are saved, in your own browser.", "Aucun cookie, aucune donnée d’abonné. Seuls ton thème, ton onglet d’actualités et ta progression de révision sont enregistrés, dans ton propre navigateur.")}</li>'
            + f'<li><strong>{t("Free.", "Gratuit.")}</strong> {t("The lessons are free, and so are the recommended tools.", "Les leçons sont gratuites, tout comme les outils recommandés.")}</li></ul></div></div></section>')
    write("about/index.html", page(f"{t('About', 'À propos')} — {SITE}", body, 1, "about/", "about/"))


def build_assets():
    th = ROOT / "theme"
    write("assets/css/tokens.css", clean((th / "tokens.css").read_text(encoding="utf-8")))
    for f in ("main.css", "premium.css", "print.css"):
        write(f"assets/css/{f}", clean(remap((th / f).read_text(encoding="utf-8"))))
    write("assets/css/palette.css", (ROOT / "palette.css").read_text(encoding="utf-8"))
    write("assets/css/jg.css", (ROOT / "extra.css").read_text(encoding="utf-8"))
    write("assets/js/site.js", clean((th / "site.js").read_text(encoding="utf-8")) + "\n" + (ROOT / "extra.js").read_text(encoding="utf-8"))
    for img in sorted((ROOT / "brand").iterdir()):
        write(f"assets/img/{img.name}", img.read_bytes())
    write(".nojekyll", "")


def build_language(lang):
    load(lang)
    check()
    build_home()
    build_path()
    build_speak()
    build_library()
    build_studios()
    build_my_learning()
    for i, n in enumerate(NOTIONS):
        build_lesson(i, n)
    build_review()
    build_news()
    build_about()
    print(f"OK: {lang} version built, {len(NOTIONS)} lessons")


def main():
    for d in ("path", "speak", "lessons", "studios", "my-learning", "review", "news", "about") + OLD_DIRS + ("assets",):
        shutil.rmtree(DOCS / d, ignore_errors=True)
    (DOCS / "index.html").unlink(missing_ok=True)
    load("fr")
    build_assets()
    build_language("fr")
    build_language("en")
    leftovers = [str(p) for p in DOCS.rglob("*") if p.suffix in (".css", ".js", ".html") and re.search(r"actu.?basics", p.read_text(encoding="utf-8"), re.I)]
    assert not leftovers, f"old brand name still in: {leftovers}"


if __name__ == "__main__":
    main()
