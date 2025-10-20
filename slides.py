"""Synchronise Markdown files with equally named JSON and Google Slides artefacts.

All derived assets are written next to the Markdown source using the same
stem so that course materials stay co-located and easy to track.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable, Tuple

import dev.courses_google_slides as courses_google_slides
import dev.courses_json as courses_json
import dev.courses_update as courses_update


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_MARKDOWN_ROOT = BASE_DIR / "_original"


def _rel(path: Path) -> str:
    """Return *path* relative to the repository root when possible."""

    try:
        return str(path.relative_to(BASE_DIR))
    except ValueError:
        return str(path)


def collect_markdown_files(target: Path) -> Iterable[Path]:
    """Yield Markdown files under *target* (or *target* itself if it is a file)."""

    if target.is_file():
        if target.suffix.lower() != ".md":
            raise ValueError(f"Expected a Markdown file, received '{target}'.")
        yield target
        return

    if not target.exists():
        raise FileNotFoundError(f"Markdown folder '{target}' does not exist.")

    for path in sorted(target.rglob("*.md")):
        if path.is_file():
            yield path


def write_json_for_markdown(markdown_path: Path) -> Tuple[Path, dict]:
    """Parse *markdown_path* and write a sibling ``.json`` file with the same stem."""

    data = courses_json.parse_markdown_file(str(markdown_path))
    json_path = markdown_path.with_suffix(".json")
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Saved JSON: {_rel(json_path)}")
    return json_path, data


def derive_course_subtitle(list_data: dict) -> str:
    """Replicates the legacy subtitle logic used by the Google Slides workflow."""

    subtitle = list_data.get("tagline", "")
    if subtitle.strip().upper() == "NA":
        content = list_data.get("content", "")
        subtitle = " ".join(content.split()[:10])
    return subtitle


def update_google_slides(json_path: Path, doc_json: dict, *, template_id: str,
                         slides_service, drive_service) -> None:
    """Create or replace a Google Slides presentation named after *json_path* stem."""

    presentation_name = json_path.stem
    list_data = doc_json.get("listData", {})
    course_title = list_data.get("title") or list_data.get("name") or presentation_name
    course_subtitle = derive_course_subtitle(list_data)

    existing_id = courses_google_slides.find_presentation_by_name(drive_service, presentation_name)
    if existing_id:
        print(f"Deleting existing presentation '{presentation_name}' (ID: {existing_id}).")
        drive_service.files().delete(fileId=existing_id).execute()

    new_id = courses_google_slides.duplicate_template(drive_service, template_id, presentation_name)
    if not new_id:
        print(f"Failed to duplicate template for '{presentation_name}'. Skipping Google Slides update.")
        return

    courses_google_slides.populate_slides(slides_service, new_id, doc_json, course_title, course_subtitle)
    print(f"Updated Google Slides presentation '{presentation_name}'.")


def authenticate_google_services():
    """Attempt to authenticate with Google Slides/Drive; return ``(slides, drive, template_id)``."""

    slides_service, drive_service = courses_google_slides.auth_slides()
    template_id = courses_google_slides.find_template(drive_service)
    if not template_id:
        raise RuntimeError("Template presentation defined by TEMPLATE_NAME was not found.")
    return slides_service, drive_service, template_id


def main(argv: Iterable[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Generate JSON exports next to Markdown files and optionally refresh "
            "their Google Slides decks."
        )
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=str(DEFAULT_MARKDOWN_ROOT),
        help="Markdown file or directory to process (defaults to '_original').",
    )
    parser.add_argument(
        "--skip-rename",
        action="store_true",
        help="Skip normalising Markdown filenames in the target directory.",
    )
    parser.add_argument(
        "--skip-google",
        action="store_true",
        help="Do not touch Google Slides presentations.",
    )

    args = parser.parse_args(list(argv) if argv is not None else None)
    target = Path(args.path).expanduser().resolve()

    if target.is_dir() and not args.skip_rename:
        courses_update.rename_files_in_folder(str(target))

    markdown_files = list(collect_markdown_files(target))
    if not markdown_files:
        print(f"No Markdown files found under '{target}'.")
        return

    slides_service = drive_service = template_id = None
    if not args.skip_google:
        try:
            slides_service, drive_service, template_id = authenticate_google_services()
        except Exception as exc:  # pragma: no cover - depends on external credentials
            print(f"Skipping Google Slides updates: {exc}")

    for md_path in markdown_files:
        json_path, doc_json = write_json_for_markdown(md_path)
        if slides_service and drive_service and template_id:
            try:
                update_google_slides(
                    json_path,
                    doc_json,
                    template_id=template_id,
                    slides_service=slides_service,
                    drive_service=drive_service,
                )
            except Exception as exc:  # pragma: no cover - network/API failure handling
                print(f"Failed to update Google Slides for '{json_path.name}': {exc}")


if __name__ == "__main__":
    main()

