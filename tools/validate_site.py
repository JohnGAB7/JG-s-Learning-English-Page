#!/usr/bin/env python3
"""Validate generated site metadata and local links without a browser or network.

Run after ``python3 tools/build.py`` from the repository root.
"""
from __future__ import annotations

import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / "docs"
ALLOWED_LANGUAGES = {"fr", "en"}
IGNORED_SCHEMES = {"data", "javascript", "mailto", "tel", "sms"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.references: list[tuple[str, str]] = []
        self.language = ""
        self.title = ""
        self.description = ""
        self.h1_count = 0
        self.images_without_alt: list[str] = []
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.language = values.get("lang") or ""
        if tag == "title":
            self._in_title = True
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta" and values.get("name", "").lower() == "description":
            self.description = values.get("content") or ""
        if "id" in values and values["id"]:
            self.ids.append(values["id"] or "")
        if tag == "img" and "alt" not in values:
            self.images_without_alt.append(values.get("src") or "(image without src)")
        for attribute in ("href", "src", "poster"):
            value = values.get(attribute)
            if value:
                self.references.append((attribute, value))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data


def parse(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    return parser


def resolve_target(source: Path, raw_url: str) -> tuple[Path, str]:
    parts = urlsplit(raw_url)
    decoded_path = unquote(parts.path)
    if not decoded_path:
        target = source
    else:
        target = (source.parent / decoded_path).resolve()
        if target.is_dir():
            target /= "index.html"
    return target, unquote(parts.fragment)


def main() -> int:
    if not ROOT.is_dir():
        print(f"ERROR: generated site directory not found: {ROOT}")
        return 2

    pages = sorted(ROOT.rglob("*.html"))
    if not pages:
        print("ERROR: no generated HTML pages found")
        return 2

    parsed = {page: parse(page) for page in pages}
    errors: list[str] = []
    checked_references = 0

    for page, document in parsed.items():
        relative = page.relative_to(ROOT).as_posix()
        if document.language not in ALLOWED_LANGUAGES:
            errors.append(f"{relative}: missing or unsupported html lang={document.language!r}")
        if not document.title.strip():
            errors.append(f"{relative}: missing title")
        if not document.description.strip():
            errors.append(f"{relative}: missing meta description")
        if document.h1_count != 1:
            errors.append(f"{relative}: expected exactly one h1, found {document.h1_count}")
        duplicates = [key for key, count in Counter(document.ids).items() if count > 1]
        if duplicates:
            errors.append(f"{relative}: duplicate id(s): {', '.join(sorted(duplicates))}")
        for image_src in document.images_without_alt:
            errors.append(f"{relative}: img missing alt attribute: {image_src}")

        for attribute, raw_url in document.references:
            parts = urlsplit(raw_url)
            if parts.scheme.lower() in IGNORED_SCHEMES or parts.netloc:
                continue
            target, fragment = resolve_target(page, raw_url)
            checked_references += 1
            if not target.exists():
                errors.append(f"{relative}: broken {attribute}={raw_url!r}")
                continue
            if fragment and target.suffix.lower() == ".html" and target in parsed:
                if fragment not in parsed[target].ids:
                    errors.append(f"{relative}: missing fragment #{fragment} in {target.relative_to(ROOT)}")

    if errors:
        print("SITE VALIDATION FAILED")
        print("\n".join(f"- {error}" for error in errors))
        print(f"\n{len(errors)} issue(s) across {len(pages)} HTML pages; {checked_references} local references checked.")
        return 1

    print(f"OK: {len(pages)} HTML pages · {checked_references} local references · language/title/description/H1 · unique IDs · image alt attributes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
