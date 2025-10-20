"""
Utility script for keeping Markdown, JSON, and Google Slides assets aligned.

Run from the project root:

    python3 slides.py                     # Process `_original/` by default
    python3 slides.py path/to/file.md     # Process a single Markdown file
    python3 slides.py path/to/folder      # Process an alternative folder

The script ensures that each Markdown file has a JSON export living in the
same directory with the same base filename. Google Slides automation is then
triggered for every directory that received a fresh JSON export.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

import dev.courses_json as courses_json
import dev.courses_update as courses_update
import dev.courses_google_slides as courses_google_slides


def _discover_markdown(target: Path) -> Tuple[Path, List[Path]]:
    """Return the directory to process and a list of Markdown files within it."""
    target = target.expanduser()
    if target.is_file():
        if target.suffix.lower() != ".md":
            raise ValueError(f"Expected a Markdown file, received: {target}")
        return target.parent.resolve(), [target.resolve()]

    if target.is_dir():
        directory = target.resolve()
        markdown_files = sorted(p for p in directory.glob("*.md") if p.is_file())
        if not markdown_files:
            raise FileNotFoundError(f"No Markdown files found in {directory}")
        return directory, markdown_files

    raise FileNotFoundError(f"Target does not exist: {target}")


def _generate_json(md_files: Sequence[Path]) -> List[Path]:
    """Create JSON exports next to each Markdown file and return their paths."""
    written_json: List[Path] = []

    for md_path in md_files:
        payload = courses_json.parse_markdown_file(str(md_path))
        json_path = md_path.with_suffix(".json")
        json_text = json.dumps(payload, indent=2, ensure_ascii=False)

        if json_path.exists():
            existing = json_path.read_text(encoding="utf-8")
            if existing == json_text:
                print(f"JSON already up to date: {json_path}")
                continue

        json_path.write_text(json_text, encoding="utf-8")
        print(f"Wrote JSON: {json_path}")
        written_json.append(json_path)

    return written_json


def _trigger_google_slides(json_paths: Iterable[Path]) -> None:
    """Run the Google Slides automation once per directory."""
    directories = sorted({path.parent for path in json_paths})
    for directory in directories:
        try:
            courses_google_slides.main(str(directory))
        except Exception as exc:  # pragma: no cover - external API interaction
            print(f"Google Slides automation failed for {directory}: {exc}")


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Synchronise Markdown files with JSON exports and Google Slides decks."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default="_original",
        help="Path to a Markdown file or a folder containing Markdown files.",
    )
    parser.add_argument(
        "--skip-rename",
        action="store_true",
        help="Skip sanitising filenames before processing.",
    )
    parser.add_argument(
        "--skip-google",
        action="store_true",
        help="Skip the Google Slides automation step.",
    )
    args = parser.parse_args(argv)

    target_path = Path(args.target)
    base_dir, markdown_files = _discover_markdown(target_path)

    if not args.skip_rename and target_path.is_dir():
        courses_update.rename_files_in_folder(str(base_dir))
        # Re-discover Markdown files after potential renames.
        _, markdown_files = _discover_markdown(base_dir)

    if not markdown_files:
        print("No Markdown files to process.")
        return

    print(f"Processing {len(markdown_files)} Markdown file(s) in {base_dir}")
    json_paths = _generate_json(markdown_files)

    if json_paths and not args.skip_google:
        _trigger_google_slides(json_paths)
    elif not json_paths:
        print("No JSON updates were necessary.")


if __name__ == "__main__":
    main()
