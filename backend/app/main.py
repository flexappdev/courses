"""FastAPI application exposing course data endpoints and Top100 editor."""
from __future__ import annotations

import os
import re
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Literal, Optional

from fastapi import Depends, FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from .models import CourseDetail, CourseSummary
from .storage import CourseStore, discover_data_directory


def get_store() -> CourseStore:
    data_dir = os.environ.get("COURSES_DATA_DIR")
    directory = discover_data_directory(data_dir)
    return CourseStore(directory)


BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"


app = FastAPI(title="Courses API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@app.get("/", summary="Service information")
def read_root() -> dict[str, str]:
    return {
        "message": "English Teacher course API",
        "documentation": "/docs",
    }


@app.get("/health", summary="Health check")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/courses", response_model=List[CourseSummary], summary="List courses")
def list_courses(
    store: CourseStore = Depends(get_store),
    search: str | None = Query(default=None),
) -> List[CourseSummary]:
    if search:
        return store.search(search)
    return store.list_courses()


@app.get(
    "/courses/{identifier}",
    response_model=CourseDetail,
    summary="Retrieve a course by slug or identifier",
)
def get_course(identifier: str, store: CourseStore = Depends(get_store)) -> CourseDetail:
    return store.get_course(identifier)


ClipStatus = Literal["todo", "queued", "rendering", "done", "error"]


class TopItem(BaseModel):
    rank: int = Field(ge=1, le=100)
    title: str
    tagline: str
    image_url: Optional[str] = None
    clip_status: ClipStatus = "todo"
    clip_url: Optional[str] = None
    source: Literal["library", "generated"] = "library"


class Top100(BaseModel):
    slug: str
    topic: str
    personality: str
    description: Optional[str] = ""
    items: List[TopItem] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


STORE: Dict[str, Top100] = {}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9\- ]+", "", value)
    slug = slug.strip().lower().replace(" ", "-")
    return re.sub(r"-+", "-", slug)


@app.get("/top100", response_class=HTMLResponse)
def top100_index(request: Request) -> HTMLResponse:
    sets = sorted(STORE.values(), key=lambda data: data.updated_at, reverse=True)
    return templates.TemplateResponse(
        "top100_index.html",
        {
            "request": request,
            "sets": sets,
            "active_page": "top100",
        },
    )


@app.get("/top100/new", response_class=HTMLResponse)
def top100_new(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "top100_edit.html",
        {
            "request": request,
            "payload": None,
            "active_page": "top100",
        },
    )


@app.get("/top100/{slug}", response_class=HTMLResponse)
def top100_edit(slug: str, request: Request) -> HTMLResponse:
    data = STORE.get(slug)
    if not data:
        raise HTTPException(status_code=404, detail="Top100 not found")
    return templates.TemplateResponse(
        "top100_edit.html",
        {
            "request": request,
            "payload": data.model_dump(),
            "active_page": "top100",
        },
    )


@app.get("/api/top100/{slug}")
def api_get_top100(slug: str) -> Top100:
    data = STORE.get(slug)
    if not data:
        raise HTTPException(status_code=404, detail="Top100 not found")
    return data


class CreateTopRequest(BaseModel):
    topic: str
    personality: str
    description: Optional[str] = ""
    items: Optional[List[TopItem]] = None


@app.post("/api/top100")
def api_create_top100(req: CreateTopRequest) -> dict[str, str | bool]:
    slug = slugify(f"{req.topic}-{req.personality}-{uuid.uuid4().hex[:6]}")
    if req.items is not None and len(req.items) != 100:
        raise HTTPException(status_code=400, detail="items must be exactly 100")
    items = req.items or [
        TopItem(
            rank=index + 1,
            title=f"Item {index + 1}",
            tagline=f"One-liner for {req.topic} #{index + 1}",
        )
        for index in range(100)
    ]
    data = Top100(
        slug=slug,
        topic=req.topic,
        personality=req.personality,
        description=req.description,
        items=items,
    )
    STORE[slug] = data
    return {"ok": True, "slug": slug}


class UpdateTopRequest(BaseModel):
    topic: Optional[str] = None
    personality: Optional[str] = None
    description: Optional[str] = None
    items: Optional[List[TopItem]] = None


@app.post("/api/top100/{slug}")
def api_update_top100(slug: str, req: UpdateTopRequest) -> dict[str, str | bool]:
    data = STORE.get(slug)
    if not data:
        raise HTTPException(status_code=404, detail="Top100 not found")
    if req.topic is not None:
        data.topic = req.topic
    if req.personality is not None:
        data.personality = req.personality
    if req.description is not None:
        data.description = req.description
    if req.items is not None:
        if len(req.items) != 100:
            raise HTTPException(status_code=400, detail="items must be exactly 100")
        data.items = req.items
    data.updated_at = datetime.utcnow()
    STORE[slug] = data
    return {"ok": True, "slug": slug}


class GenerateRequest(BaseModel):
    mode: Literal["library", "generate", "mixed"] = "mixed"
    seconds_per_clip: int = 10


@app.post("/api/top100/{slug}/generate")
def api_generate(slug: str, req: GenerateRequest) -> dict[str, int | str | bool]:
    data = STORE.get(slug)
    if not data:
        raise HTTPException(status_code=404, detail="Top100 not found")
    for index, item in enumerate(data.items):
        data.items[index] = item.model_copy(update={"clip_status": "queued"})
    data.updated_at = datetime.utcnow()
    STORE[slug] = data
    return {
        "ok": True,
        "queued": len(data.items),
        "seconds_per_clip": req.seconds_per_clip,
        "mode": req.mode,
    }
