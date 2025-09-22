# Agents Guide

This repository adopts the [AGENTS.md specification](https://agents.md/) for agent instructions. The notes below apply to the entire project unless a more specific file overrides them.

## Documentation
- Keep `README.md` structured with a single H1 (`# English Teacher`) followed by the five H2 sections in this order: Product, UX, Tech, Flow, Marketing.
- When documenting command-line usage, present commands in fenced code blocks and describe the context for running them.
- Preserve references to the eight-session / eight-slide course format when updating examples or templates.

## Development Workflow
- When modifying Python modules or scripts, run `python -m compileall .` from the repo root before committing to ensure syntax validity.
- Store generated assets in the existing directories (`_original/`, `json/`, `slides/`, `updated/`) so the automation scripts continue to function.
- Record every automated check or script invocation in the PR/testing notes.

## Writing Style
- Prefer clear, instructional language suited for educators and course builders.
- Highlight integrations (e.g., Google Slides, Swiper) whenever related files change so downstream consumers stay informed.
