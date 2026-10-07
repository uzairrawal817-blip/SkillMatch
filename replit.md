# SkillMatch

A campus event and volunteer-matching foundation that will connect student skills with organizer needs.

## Run & Operate

- `pnpm --filter @workspace/api-server run dev` — run the API server (port 5000)
- `PORT=8000 python app.py` — run the SkillMatch Flask app
- `pnpm run typecheck` — full typecheck across all packages
- `pnpm run build` — typecheck + build all packages
- `pnpm --filter @workspace/api-spec run codegen` — regenerate API hooks and Zod schemas from the OpenAPI spec
- `pnpm --filter @workspace/db run push` — shared database package for other API artifacts only; do not use it for SkillMatch
- The SkillMatch foundation uses local JSON files; no database is configured for it.

## Stack

- SkillMatch: Python Flask, Jinja2 templates, HTMX, and JSON files
- pnpm workspaces, Node.js 24, TypeScript 5.9 (shared workspace services)
- API: Express 5
- Shared API database library: PostgreSQL + Drizzle ORM (not used by SkillMatch)
- Validation: Zod (`zod/v4`), `drizzle-zod`
- API codegen: Orval (from OpenAPI spec)
- Build: esbuild (CJS bundle)

## Where things live

- `app.py` — Flask app, home page, 404 handler, and four teammate Blueprint registration points
- `data_store.py` — shared JSON load/save helpers; data files go in `data/`
- `pyproject.toml` and `uv.lock` — Flask dependency declaration and Python lockfile
- `templates/` — shared Jinja layout, macros, starter home page, and 404 page
- `static/style.css` — SkillMatch styles and responsive breakpoints
- `static/js/app.js` — browser-only modal dismissal behavior
- `static/vendor/htmx.min.js` — locally vendored HTMX library
- `models.md` — source of truth for the JSON record shapes

## Architecture decisions

- Feature areas are kept separate through four commented Blueprint registration points in `app.py`.
- JSON files are project-local and accessed through `data_store.py`; no database is used for SkillMatch.
- HTMX owns dynamic server-rendered updates; custom JavaScript is limited to modal dismissal.

## Product

SkillMatch is intended to match student volunteers to campus events based on their skills. This commit establishes shared scaffolding only; feature routes and behavior are intentionally not implemented.

## User preferences

- Use Flask, Jinja2, and HTMX; do not use React, Vue, or another frontend framework for SkillMatch.
- Use JSON files through `data_store.py`; do not add a database.
- Allowed JavaScript is only the vendored HTMX library and `static/js/app.js`, with `app.js` kept under 100 lines total. Check whether HTMX can handle a behavior before adding JavaScript; every function in `app.js` needs a one-line reason Python/HTMX cannot handle it.
- Keep the four feature areas independently owned; each teammate makes their own GitHub commits.
- Leave changes unstaged. Do not run `git add`, `git commit`, or `git push`.

## Gotchas

- Do not store raw passwords; future password-based account features must store hashes.
- Keep browser-side behavior in HTMX unless a documented browser-only exception is necessary.

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
