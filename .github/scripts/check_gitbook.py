"""Validate the GitBook site configuration and table of contents before GitBook sees them.

Checks:
1. gitbook-docs.yaml validates against GitBook's published JSON Schema.
2. The import rules GitBook enforces but the schema cannot express
   (unique keys, exactly one default per level, no `..`, directories exist,
   one language per directory).
3. Every relative link in each space's SUMMARY.md resolves to an existing file,
   and no file is listed twice.

Exit code is non-zero on any problem; each message starts with "review:".
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import unquote

import yaml
from jsonschema import Draft202012Validator

SCHEMA_URL = "https://api.gitbook.com/gitbook-docs.yaml"
SITE_CONFIG = "gitbook-docs.yaml"
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def load_schema(source: str) -> dict[str, Any]:
    if source.startswith(("http://", "https://")):
        with urllib.request.urlopen(source, timeout=30) as response:
            return yaml.safe_load(response.read())
    return yaml.safe_load(Path(source).read_text(encoding="utf-8"))


def walk(nodes: list[dict[str, Any]], parent: dict[str, Any] | None = None):
    for node in nodes:
        yield node, parent
        yield from walk(node.get("children") or [], node)


def check_schema(config: Any, schema: dict[str, Any]) -> list[str]:
    errors = []
    for error in sorted(Draft202012Validator(schema).iter_errors(config), key=lambda e: list(e.path)):
        where = ".".join(map(str, error.absolute_path)) or "<root>"
        details = "; ".join(sorted({sub.message for sub in error.context or []}))
        errors.append(
            f"review: {SITE_CONFIG} at {where}: {error.message[:200]}"
            + (f" (candidates: {details[:400]})" if details else "")
        )
    return errors


def check_import_rules(structure: list[dict[str, Any]], project: Path) -> list[str]:
    errors = []
    nodes = list(walk(structure))

    keys = Counter(node.get("key") for node, _ in nodes)
    for key, count in keys.items():
        if count > 1:
            errors.append(f"review: {SITE_CONFIG}: key {key!r} is used {count} times; every key must be unique")

    sections = [node for node, _ in nodes if node.get("type") == "section"]
    top_spaces = [node for node in structure if node.get("type") == "space"]
    if sections:
        defaults = [s.get("key") for s in sections if s.get("default")]
        if len(defaults) != 1:
            errors.append(
                f"review: {SITE_CONFIG}: exactly one section must be `default: true`, found {defaults or 'none'}"
            )
        if top_spaces:
            errors.append(
                f"review: {SITE_CONFIG}: spaces {[s.get('key') for s in top_spaces]} sit at the top level "
                "of a site that declares sections; move them into a section"
            )
        groups = [(s.get("key"), [c for c in s.get("children") or [] if c.get("type") == "space"]) for s in sections]
    else:
        groups = [("<site root>", top_spaces)]
    for owner, spaces in groups:
        defaults = [s.get("key") for s in spaces if s.get("default")]
        if spaces and len(defaults) != 1:
            errors.append(
                f"review: {SITE_CONFIG}: under {owner} exactly one space must be `default: true`, "
                f"found {defaults or 'none'}"
            )

    languages: dict[str, set[str | None]] = {}
    for node, _ in nodes:
        if node.get("type") != "space":
            continue
        directory = (node.get("content") or {}).get("directory")
        if directory is None:
            continue
        if ".." in Path(directory).parts:
            errors.append(f"review: {SITE_CONFIG}: space {node.get('key')!r} directory {directory!r} uses `..`")
            continue
        resolved = resolve_directory(directory, project)
        if not resolved.is_dir():
            errors.append(
                f"review: {SITE_CONFIG}: space {node.get('key')!r} directory {directory!r} "
                f"does not exist (looked at {resolved})"
            )
        languages.setdefault(str(resolved), set()).add((node.get("content") or {}).get("language"))
    for directory, langs in languages.items():
        if len(langs) > 1:
            errors.append(f"review: {SITE_CONFIG}: directory {directory} is mapped with several languages {langs}")
    return errors


def resolve_directory(directory: str, project: Path) -> Path:
    repo_root = project
    while not (repo_root / ".git").exists() and repo_root.parent != repo_root:
        repo_root = repo_root.parent
    if directory.startswith("/"):
        return (repo_root / directory.lstrip("/")).resolve()
    return (project / directory).resolve()


def summary_path(space_dir: Path) -> tuple[Path, Path]:
    """Return (content root, SUMMARY.md path), honouring an optional per-space .gitbook.yaml."""
    root, summary = space_dir, "SUMMARY.md"
    space_config = space_dir / ".gitbook.yaml"
    if space_config.is_file():
        data = yaml.safe_load(space_config.read_text(encoding="utf-8")) or {}
        root = (space_dir / data.get("root", "./")).resolve()
        summary = (data.get("structure") or {}).get("summary", summary)
    return root, root / summary


def check_summary(space_dir: Path, repo_root: Path) -> list[str]:
    root, summary = summary_path(space_dir)
    if not summary.is_file():
        return []
    shown = summary.relative_to(repo_root)
    errors = []
    targets: list[str] = []
    for number, line in enumerate(summary.read_text(encoding="utf-8").splitlines(), start=1):
        for raw in LINK.findall(line):
            if re.match(r"^[a-z][a-z0-9+.-]*:", raw, re.IGNORECASE) or raw.startswith("#"):
                continue
            target = unquote(raw.split("#", 1)[0])
            targets.append(target)
            if not (root / target).is_file():
                errors.append(f"review: {shown}:{number} links {target} which does not exist")
    for target, count in Counter(targets).items():
        if count > 1:
            errors.append(f"review: {shown} lists {target} {count} times; GitBook allows each file once")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--project", default=".", help="Git Sync project directory (holds gitbook-docs.yaml)")
    parser.add_argument("--schema", default=SCHEMA_URL, help="Schema URL or local file")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    config_file = project / SITE_CONFIG
    if not config_file.is_file():
        print(f"review: {config_file} is missing; GitBook site sync reads this file", file=sys.stderr)
        return 1

    config = yaml.safe_load(config_file.read_text(encoding="utf-8"))
    errors = check_schema(config, load_schema(args.schema))
    if not errors:
        structure = config["site"]["structure"]
        errors += check_import_rules(structure, project)
        repo_root = resolve_directory("/", project)
        seen: set[Path] = set()
        for node, _ in walk(structure):
            directory = (node.get("content") or {}).get("directory") if node.get("type") == "space" else None
            if directory is None or ".." in Path(directory).parts:
                continue
            space_dir = resolve_directory(directory, project)
            if space_dir.is_dir() and space_dir not in seen:
                seen.add(space_dir)
                errors += check_summary(space_dir, repo_root)

    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        print(f"{len(errors)} problem(s) found", file=sys.stderr)
        return 1
    print("GitBook configuration and SUMMARY.md links are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
