"""Validate and package this skill repository; never run an application's tests."""

from __future__ import annotations

import argparse
import json
import re
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def frontmatter(text: str) -> dict:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md must start with YAML frontmatter")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise TypeError("Frontmatter must be a mapping")
    return data


def validate(root: Path) -> list[Path]:
    data = frontmatter((root / "SKILL.md").read_text(encoding="utf-8"))
    if data.get("name") != "test-designer" or data.get("license") != "MIT":
        raise ValueError("Expected name test-designer and license MIT")
    description = data.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        raise ValueError("Description must contain 1..1024 characters")
    if "<" in description or ">" in description:
        raise ValueError("Description must not contain angle brackets")
    if (root / "docs").exists():
        raise ValueError("Repository guidance belongs in README/references, not docs")
    if "MIT License" not in (root / "LICENSE").read_text(encoding="utf-8"):
        raise ValueError("Missing MIT license text")

    markdown = [*root.glob("*.md"), *(root / "references").glob("*.md"),
                *(root / "evals").rglob("*.md"), *(root / ".github").rglob("*.md")]
    for path in markdown:
        text = path.read_text(encoding="utf-8")
        if path != root / "README.ru.md" and re.search(r"[\u0400-\u04ff]", text):
            raise ValueError(f"Unexpected Cyrillic text in {path.relative_to(root)}")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if "://" in target or target.startswith("mailto:"):
                continue
            relative, _, anchor = target.partition("#")
            destination = path.parent / relative if relative else path
            if not destination.exists():
                raise ValueError(f"Broken link in {path.relative_to(root)}: {target}")
            if anchor and destination.suffix == ".md":
                headings = re.findall(r"^#+\s+(.+)$", destination.read_text(encoding="utf-8"), re.MULTILINE)
                slugs = {re.sub(r"[^\w -]", "", h.lower()).replace(" ", "-") for h in headings}
                if anchor not in slugs:
                    raise ValueError(f"Broken anchor in {path.relative_to(root)}: {target}")

    tasks = json.loads((root / "evals/evals.json").read_text(encoding="utf-8"))
    if tasks.get("skill_name") != data["name"] or not tasks.get("evals"):
        raise ValueError("Missing skill evaluation scenarios")
    ids = set()
    for task in tasks["evals"]:
        if not {"id", "name", "prompt", "expected_output", "files", "expectations"} <= task.keys():
            raise ValueError("Incomplete evaluation scenario")
        if task["id"] in ids:
            raise ValueError("Duplicate evaluation ID")
        ids.add(task["id"])
        for fixture in task["files"]:
            if not (root / "evals" / fixture).is_file():
                raise ValueError(f"Missing evaluation fixture: {fixture}")
    triggers = json.loads((root / "evals/triggers.json").read_text(encoding="utf-8"))
    if not triggers or any(not isinstance(t.get("query"), str)
                           or not isinstance(t.get("should_trigger"), bool) for t in triggers):
        raise ValueError("Invalid trigger scenarios")
    return [root / "SKILL.md", root / "LICENSE", *sorted((root / "references").glob("*.md"))]


def package(root: Path, payload: list[Path]) -> Path:
    stage = root / "dist/test-designer"
    expected = {p.relative_to(root).as_posix() for p in payload}
    actual = {p.relative_to(stage).as_posix() for p in stage.rglob("*") if p.is_file()}
    if actual - expected:
        raise ValueError(f"Stale payload files: {sorted(actual - expected)}")
    for source in payload:
        destination = stage / source.relative_to(root)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(source.read_bytes())
    archive = root / "dist/test-designer.skill"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as output:
        for source in payload:
            output.write(source, "test-designer/" + source.relative_to(root).as_posix())
    with zipfile.ZipFile(archive) as output:
        if output.testzip() or set(output.namelist()) != {"test-designer/" + p for p in expected}:
            raise ValueError("Invalid archive entries or CRC")
        for source in payload:
            if output.read("test-designer/" + source.relative_to(root).as_posix()) != source.read_bytes():
                raise ValueError("Archive differs from source")
    return archive


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", action="store_true", help="Build the minimal .skill archive")
    args = parser.parse_args()
    try:
        files = validate(ROOT)
        if args.package:
            print(f"Packaged {len(files)} files: {package(ROOT, files)}")
        print("Repository validation passed; behavioral effectiveness is not established.")
    except (ValueError, TypeError, OSError, yaml.YAMLError) as error:
        parser.exit(1, f"Validation failed: {error}\n")
