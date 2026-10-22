#!/usr/bin/env python3
"""Check supported local Markdown links and heading fragments; no network access."""

import argparse
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit


def prose(source):
    """Ignore fenced examples, indented code and inline code in link scanning."""
    lines = []
    fence = None
    for line in source.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence:
            if re.match(r"^ {0,3}" + re.escape(fence[0]) + "{" + str(fence[1]) + r",}\s*$", line):
                fence = None
            lines.append("")
        elif marker:
            fence = (marker[1][0], len(marker[1]))
            lines.append("")
        elif line.startswith(("    ", "\t")):
            lines.append("")
        else:
            lines.append(line)
    return "\n".join(lines)


def anchors(source):
    found = set()
    for heading in re.findall(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", prose(source), re.M):
        heading = re.sub(r"!?\[([^]]+)\]\([^)]*\)", r"\1", heading)
        heading = re.sub(r"<[^>]*>", "", heading).lower()
        slug = "".join(c for c in heading if c in "_- " or unicodedata.category(c)[0] in "LN")
        slug = slug.replace(" ", "-")
        unique = slug
        suffix = 0
        while unique in found:
            suffix += 1
            unique = f"{slug}-{suffix}"
        found.add(unique)
    return found


def local_links(source):
    text = prose(source)
    text = re.sub(r"(`+).*?\1", "", text)
    definitions = dict(re.findall(r"^ {0,3}\[([^]]+)\]:\s*<?([^\s>]+)>?", text, re.M))
    for match in re.finditer(r"!?\[[^]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\s*\)", text):
        yield text.count("\n", 0, match.start()) + 1, match[1].strip("<>")
    for match in re.finditer(r"!?\[([^]\n]+)\]\[([^]\n]*)\]", text):
        key = match[2] or match[1]
        if key not in definitions:
            yield text.count("\n", 0, match.start()) + 1, "!undefined-reference:" + key
        else:
            yield text.count("\n", 0, match.start()) + 1, definitions[key]


def check(root):
    root = Path(root).resolve()
    errors = []
    count = 0
    files = sorted(p for p in root.rglob("*.md") if not any(x in {".git", "node_modules", ".venv"} for x in p.relative_to(root).parts))
    cache = {}
    for path in files:
        source = path.read_text(encoding="utf-8")
        for line, target in local_links(source):
            where = f"{path.relative_to(root)}:{line}"
            if target.startswith("!undefined-reference:"):
                errors.append(f"{where}: {target}")
                continue
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            count += 1
            dest = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not dest.is_relative_to(root):
                errors.append(f"{where}: target escapes repository: {target}")
            elif not dest.exists():
                errors.append(f"{where}: missing target: {target}")
            elif url.fragment and dest.suffix.lower() == ".md":
                if dest not in cache:
                    cache[dest] = anchors(dest.read_text(encoding="utf-8"))
                if unquote(url.fragment) not in cache[dest]:
                    errors.append(f"{where}: missing heading: {target}")
    return files, count, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    files, count, errors = check(args.root)
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Checked {len(files)} Markdown files and {count} local links; {len(errors)} errors.")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
