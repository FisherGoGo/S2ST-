"""Validate local Markdown/Wikilink targets; does not fetch external URLs."""
import argparse
from pathlib import Path
import re
from urllib.parse import unquote


def check(kb):
    vault = kb.parent
    errors = []
    checked = 0
    pages = list(kb.rglob("*.md"))
    if (vault / "首页.md").exists():
        pages.append(vault / "首页.md")
    for path in pages:
        body = path.read_text(encoding="utf-8-sig")
        body = re.sub(r"(?ms)^```.*?^```[^\n]*", "", body)
        for destination in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", body):
            destination = destination.strip().strip("<>")
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", destination):
                continue
            target = unquote(destination.split("#", 1)[0])
            if not target:
                continue
            checked += 1
            if not (path.parent / target).exists():
                errors.append(f"{path.relative_to(vault)} -> {destination}")
        for destination in re.findall(r"\[\[([^\]\n]+)\]\]", body):
            target = destination.split("|", 1)[0].split("#", 1)[0]
            # In this project, fixed wiki navigation is vault-root relative.
            if not target or not target.startswith("S2ST-Research/"):
                continue
            checked += 1
            candidate = vault / target
            if not candidate.exists() and not candidate.with_suffix(".md").exists():
                errors.append(f"{path.relative_to(vault)} -> [[{destination}]]")
    return pages, checked, errors


def main():
    parser = argparse.ArgumentParser(description="Check local note links, without external requests.")
    parser.add_argument("--kb", required=True, type=Path)
    args = parser.parse_args()
    if not args.kb.is_dir():
        parser.error("Knowledge-base directory does not exist.")
    pages, count, errors = check(args.kb.resolve())
    print(f"Pages: {len(pages)}; local links checked: {count}; broken: {len(errors)}")
    for error in errors:
        print(error)
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
