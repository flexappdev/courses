"""Utilities for loading course JSON files."""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import List, Optional

from fastapi import HTTPException, status

from .models import (
    CourseDetail,
    CourseMetadata,
    CourseSession,
    CourseSummary,
    build_detail,
    build_metadata,
    build_sessions,
    build_summary,
)


class CourseStore:
    """Load and cache course definitions stored as JSON files."""

    def __init__(self, data_dir: Path) -> None:
        self.data_dir = data_dir
        if not self.data_dir.exists():
            raise FileNotFoundError(f"Course data directory does not exist: {self.data_dir}")

    @property
    def json_files(self) -> List[Path]:
        """Return all JSON files sorted alphabetically."""

        return sorted(self.data_dir.glob("*.json"))

    def _read_json(self, path: Path) -> dict:
        try:
            with path.open("r", encoding="utf-8") as handle:
                return json.load(handle)
        except FileNotFoundError as exc:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Course file not found: {path.name}",
            ) from exc
        except json.JSONDecodeError as exc:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Invalid JSON in {path.name}: {exc.msg}",
            ) from exc

    @lru_cache(maxsize=256)
    def _metadata_for(self, path: Path) -> CourseMetadata:
        raw = self._read_json(path)
        list_data = raw.get("listData") or {}
        if not list_data:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Missing listData in {path.name}",
            )
        return build_metadata(list_data, source=path, fallback_slug=path.stem)

    @lru_cache(maxsize=256)
    def _sessions_for(self, path: Path) -> List[CourseSession]:
        raw = self._read_json(path)
        list_items = raw.get("listItems") or []
        return build_sessions(list_items)

    def list_courses(self) -> List[CourseSummary]:
        summaries: List[CourseSummary] = []
        for file_path in self.json_files:
            try:
                metadata = self._metadata_for(file_path)
            except HTTPException:
                continue
            summaries.append(build_summary(metadata))
        return summaries

    def get_course(self, identifier: str) -> CourseDetail:
        path = self._resolve_identifier(identifier)
        metadata = self._metadata_for(path)
        sessions = self._sessions_for(path)
        return build_detail(metadata, sessions)

    def _resolve_identifier(self, identifier: str) -> Path:
        candidate = self.data_dir / f"{identifier}.json"
        if candidate.exists():
            return candidate

        for file_path in self.json_files:
            metadata = self._metadata_for(file_path)
            if identifier in {metadata.id, metadata.slug}:
                return file_path

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course '{identifier}' not found",
        )

    def search(self, query: str) -> List[CourseSummary]:
        query_lower = query.lower()
        results: List[CourseSummary] = []
        for summary in self.list_courses():
            haystack = " ".join(
                [
                    summary.title or "",
                    summary.description or "",
                    " ".join(summary.topics),
                ]
            ).lower()
            if query_lower in haystack:
                results.append(summary)
        return results


def discover_data_directory(candidate: Optional[str] = None) -> Path:
    """Find the directory containing the course JSON files."""

    if candidate:
        directory = Path(candidate).expanduser().resolve()
    else:
        directory = Path(__file__).resolve().parents[2] / "json"
    if not directory.exists():
        raise FileNotFoundError(
            f"Unable to locate course data directory at {directory}. "
            "Set the COURSES_DATA_DIR environment variable to override."
        )
    return directory
