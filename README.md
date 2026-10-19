# Content Engine — AI Marketing Assistant for Small Nonprofits

> **Portfolio case study.** This is a sanitized copy of a production app I
> built as a contractor for a small-business nonprofit through the Pursuit
> SMB Builder Program. All organization, people, content and brand details
> here are **fictional** ("Harbor Light Fund"); the original client owns the
> real project and its data.

Staff enter event or campaign details and get a branded content package for
review and approval: newsletter/eblast/flyer blocks, social posts with
hashtags, a content calendar, and image prompts.

## The problem

A two-person marketing team needed to post three times a week and send
several newsletters a month. The bottleneck wasn't publishing, it was
**drafting and deciding when content was good enough to send**. Hashtags were
an afterthought.

## What I built

- **Structured generation, one schema per content type.** Social posts,
  hashtag sets, newsletter blocks and image prompts each have their own
  Pydantic schema and prompt function, produced through Claude tool-use
  structured output so every piece stays independently editable.
- **Compare-and-pick.** Social post + hashtag generation returns three
  options concurrently; staff choose one, and only the pick is persisted.
- **Structural variants, not one template.** Prompts support multiple
  structural variants per content type (standard / listicle / quote-style,
  per-platform styles) because the client wanted format variety to keep up
  with shifting social algorithms.
- **Modular newsletter blocks.** Feature article, events list, grant/flyer,
  tips/CTA, member spotlight and boilerplate blocks, each generated and
  stored separately.
- **Single-approver review flow.** Passcode-based approver auth with an
  email reset flow, an approval step, and edit-before-approve for all
  content.
- **Content calendar.** Month grid + list view assembled from generated
  content by date.
- **Photo/text composer.** Canvas-based composer with a staff photo library
  (Cloudflare R2), Pexels stock search and QR code layers.
- **Manual-click publishing to X.** OAuth 2.0 + PKCE connect flow,
  Fernet-encrypted token storage, and a secret-protected endpoint for a
  scheduled-post cron job. Instagram/Facebook scaffolded behind Meta App
  Review.
- **FLIP / shared-layout animations** (Framer Motion `layoutId`) for the
  platform tile rail and the featured-founders profile cards.

## Tech stack

- **Frontend:** Next.js (TypeScript), Tailwind, Framer Motion: `frontend/`
- **Backend:** FastAPI (Python), SQLAlchemy, Alembic: `backend/`
- **Database:** PostgreSQL (SQLite for tests and local dev)
- **LLM:** Anthropic Claude API with tool-use structured output
- **Infra:** Vercel (frontend), Railway (backend + Postgres), Cloudflare R2
- **Design decision:** no background job queue. At the client's volume
  (3 posts/week, 2-4 newsletters/month) generation is synchronous
  request/response.

## Running locally

```bash
# backend
cd backend && pip install -r requirements.txt
cp .env.example .env        # add ANTHROPIC_API_KEY
alembic upgrade head
python seed_key_makers_public.py
uvicorn app.main:app --reload

# frontend
cd frontend && npm install && npm run dev
```

Backend: `http://localhost:8000` (docs at `/docs`). Frontend:
`http://localhost:3000`. See [backend/README.md](./backend/README.md) for
setup detail and [docs/SCHEMA.sql](./docs/SCHEMA.sql) for the target schema.

## Testing

The backend has an end-to-end suite (`backend/tests/`, 106 tests) that
exercises every API route against an isolated SQLite database. Anthropic and
X calls are mocked, so tests are free, fast and need no API keys.

```bash
cd backend && pytest -v
```

CI (`.github/workflows/backend-e2e.yml`) runs the suite plus `alembic check`
to catch model/migration drift.

## Sample data

Everything the app ships with (featured founders, example social posts,
campaign emails, logo) is invented placeholder content created for this
portfolio copy.
