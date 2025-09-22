# syntax=docker/dockerfile:1.4

#############################
# Frontend (React + Vite)
#############################
FROM node:20-bullseye-slim AS frontend
WORKDIR /app
COPY frontend/package*.json ./frontend/
RUN --mount=type=cache,target=/root/.npm cd frontend && npm install
COPY frontend ./frontend
WORKDIR /app/frontend
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "2048"]

#############################
# Backoffice (Vite + shadcn)
#############################
FROM node:20-bullseye-slim AS backoffice
WORKDIR /app
COPY backoffice/package*.json ./backoffice/
RUN --mount=type=cache,target=/root/.npm cd backoffice && npm install
COPY backoffice ./backoffice
WORKDIR /app/backoffice
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "2050"]

#############################
# Backend (FastAPI)
#############################
FROM python:3.11-slim AS backend
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r backend/requirements.txt
COPY backend /app/backend
COPY json /app/json
ENV COURSES_DATA_DIR=/app/json
ENV PYTHONPATH=/app
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
