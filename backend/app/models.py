"""Pydantic models describing the course data returned by the API."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, List, Optional

from pydantic import BaseModel, Field


class CourseMetadata(BaseModel):
    """High level metadata extracted from the course JSON files."""

    id: str
    slug: str
    title: str
    name: Optional[str] = None
    tagline: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    category: Optional[str] = None
    cta: Optional[str] = None
    year: Optional[str] = None
    updated: Optional[datetime] = None
    topics: List[str] = Field(default_factory=list)
    source: str


class CourseSession(BaseModel):
    """A single item (or slide) inside a course."""

    id: str
    title: Optional[str] = None
    name: Optional[str] = None
    slug: Optional[str] = None
    tagline: Optional[str] = None
    description: Optional[str] = None
    keyIdeas: List[str] = Field(default_factory=list)
    status: Optional[str] = None
    category: Optional[str] = None
    db: Optional[str] = None
    collection: Optional[str] = None
    data: Optional[str] = None
    callToAction: Optional[str] = None
    year: Optional[str] = None
    image: Optional[str] = None
    rank: Optional[int] = None


class CourseSummary(BaseModel):
    """Summary information surfaced in the course list view."""

    id: str
    slug: str
    title: str
    description: Optional[str] = None
    tagline: Optional[str] = None
    status: Optional[str] = None
    topics: List[str] = Field(default_factory=list)
    updated: Optional[datetime] = None
    source: str


class CourseDetail(CourseSummary):
    """Full course payload returned for detail views."""

    metadata: CourseMetadata
    sessions: List[CourseSession] = Field(default_factory=list)


def build_metadata(raw: dict[str, Any], source: Path, fallback_slug: str) -> CourseMetadata:
    """Transform raw ``listData`` dictionaries into :class:`CourseMetadata`."""

    topics = raw.get("topics") or []
    date_str = raw.get("date")
    updated = None
    if isinstance(date_str, str):
        try:
            updated = datetime.fromisoformat(date_str.strip())
        except ValueError:
            updated = None

    slug = raw.get("slug") or fallback_slug
    course_id = raw.get("id") or raw.get("slug") or raw.get("name") or fallback_slug

    metadata = CourseMetadata(
        id=str(course_id),
        slug=str(slug),
        title=raw.get("title") or raw.get("name") or fallback_slug,
        name=raw.get("name"),
        tagline=raw.get("tagline"),
        description=raw.get("description"),
        status=raw.get("status"),
        category=raw.get("cat"),
        cta=raw.get("cta"),
        year=raw.get("year"),
        updated=updated,
        topics=[str(topic) for topic in topics],
        source=str(source),
    )
    return metadata


def build_sessions(raw_sessions: Iterable[dict[str, Any]]) -> List[CourseSession]:
    """Convert raw session dictionaries to :class:`CourseSession` objects."""

    sessions: List[CourseSession] = []
    for raw in raw_sessions:
        if not isinstance(raw, dict):
            continue
        session_id = raw.get("id") or raw.get("slug")
        if not session_id:
            continue
        session = CourseSession(
            id=str(session_id),
            title=raw.get("title") or raw.get("name"),
            name=raw.get("name"),
            slug=raw.get("slug"),
            tagline=raw.get("tagline"),
            description=raw.get("description"),
            keyIdeas=[str(item) for item in raw.get("key-ideas", []) if isinstance(item, str)],
            status=raw.get("status"),
            category=raw.get("cat"),
            db=raw.get("db"),
            collection=raw.get("collection"),
            data=raw.get("data"),
            callToAction=raw.get("cta"),
            year=raw.get("year"),
            image=raw.get("image"),
            rank=raw.get("rank"),
        )
        sessions.append(session)
    return sessions


def build_summary(metadata: CourseMetadata) -> CourseSummary:
    """Create a :class:`CourseSummary` from :class:`CourseMetadata`."""

    return CourseSummary(
        id=metadata.id,
        slug=metadata.slug,
        title=metadata.title,
        description=metadata.description,
        tagline=metadata.tagline,
        status=metadata.status,
        topics=list(metadata.topics),
        updated=metadata.updated,
        source=metadata.source,
    )


def build_detail(metadata: CourseMetadata, sessions: Iterable[CourseSession]) -> CourseDetail:
    """Create a :class:`CourseDetail` from metadata and sessions."""

    return CourseDetail(
        **build_summary(metadata).model_dump(),
        metadata=metadata,
        sessions=list(sessions),
    )
