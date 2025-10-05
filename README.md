# English Teacher

## Product
English Teacher is a content production toolkit for building business-focused English courses. Educators can outline an eight-session syllabus and automatically produce consistent lesson assets for every session. The repo includes reference topics such as **Customer and distribution** and **Marketing and advertising**, each designed with eight sessions and eight slides per session so learners gain repeated practice across vocabulary, analysis, and presentation skills. The toolkit now ships with dedicated frontend, backend, and backoffice apps so teams can browse, QA, and govern these multi-session catalogues from the browser as well as the command line.

## UX
Course builders work through a predictable set of deliverables. Markdown drafts live in `_original/`, JSON handoffs populate `json/`, and slide decks render in `slides/`. Helper scripts (`main.py`, `slides.py`, and `doc.py`) keep the workflow command-line friendly—run them from the project root to preview console output or regenerate artifacts once new content is ready. Prompts inside the repository guide how to brief the DOCAI assistant when fresh course sessions or slide scripts are needed. The new React interfaces mirror this flow: the `frontend/` catalogue highlights eight-session outlines for stakeholders, while the `backoffice/` dashboard gives editors shadcn-styled controls for searching, validating, and linking course assets.

## Tech
The project is written in Python and leans on small utilities in `dev/`:
- `courses_json.py` converts structured Markdown into JSON objects using `python-slugify` for stable identifiers.
- `courses_update.py` and `courses_slides.py` prepare course data for downstream consumers, including Swiper and Google Slides integrations.
- `courses_google_slides.py` connects to the Google Slides API to build presentations programmatically.
Supporting scripts share configuration for input/output folders so assets land in predictable directories alongside the source files.

The repo is now organised as a three-service stack:
- `backend/` hosts a FastAPI application that surfaces the course JSON catalogue, search helpers, and detailed slide data on port **2049**.
- `frontend/` contains a React + Vite client (port **2048**) that visualises every eight-session syllabus.
- `backoffice/` is a Vite project styled with the shadcn design system and Tailwind CSS; it provides admin-grade controls on port **2050**.
Shared Docker tooling (`Dockerfile`, `docker-compose.yml`, and `bash.sh`) automates local builds so the FastAPI API, Vite dev servers, and course assets stay in sync.

## Flow
1. Outline a course session in Markdown, following the eight-section template (Introduction, four numbered topics, Conclusion, Next steps, and Extra slide).
2. Use the DOCAI assistant to expand the outline into a fully populated CSV/JSON structure with titles, subtitles, intros, key ideas, and examples for every slide.
3. Convert Markdown or CSV drafts into JSON with `python3 main.py` or call `python3 doc.py` to refresh documentation-oriented outputs.
4. Generate presentation decks through `python3 slides.py`, or trigger the Google Slides workflow when a connected account is available.

   **Using a Google Slides template?** Before running the script, export your template folder (and/or deck) settings:
   ```bash
   export TEMPLATE_FOLDER_ID="16kEgj5o0Lsudoe1_uz0I9UPw9l2bzERv"
   export TEMPLATE_NAME="2025-TEMPLATE"
   # (or, to bypass name lookup, set TEMPLATE_ID to your template deck's file ID)
   ```
5. Review the produced materials, update objectives or transitions as needed, and iterate until each session meets the target learning outcomes.

Run the containerised stack from the project root whenever you want to explore the catalogue in the browser (React frontend, FastAPI backend, and shadcn backoffice will all rebuild):

```bash
./bash.sh
```

Once the services are up you can visit http://localhost:2048 for the learner-facing catalogue, http://localhost:2049 for the API, and http://localhost:2050 for the backoffice controls.

## Marketing
Position English Teacher as an accelerator for bilingual business programs. Highlight how automated slide scripts, consistent lesson templates, and branded prompts reduce prep time while keeping instruction aligned with professional use cases (e.g., Nike or Apple storytelling). Emphasize smooth slide transitions, clearly stated objectives, and concrete case studies so stakeholders see both pedagogical rigor and marketing polish. The new multi-app stack makes it easier to demo catalogue breadth to prospects, hand reviewers the API, and showcase shadcn-polished admin workflows alongside the eight-session learning journeys.
