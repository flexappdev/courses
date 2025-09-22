"""FastAPI application exposing course data endpoints."""
from __future__ import annotations

import os
from typing import List

from fastapi import Depends, FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from .models import CourseDetail, CourseSummary
from .storage import CourseStore, discover_data_directory


def get_store() -> CourseStore:
    data_dir = os.environ.get("COURSES_DATA_DIR")
    directory = discover_data_directory(data_dir)
    return CourseStore(directory)


app = FastAPI(title="Courses API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
def list_courses(store: CourseStore = Depends(get_store), search: str | None = Query(default=None)) -> List[CourseSummary]:
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
