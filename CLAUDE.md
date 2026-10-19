# Content Engine (portfolio copy)

AI-powered marketing/content assistant for a fictional nonprofit, Harbor Light
Fund. This is a sanitized portfolio copy of a real client project; all
organization, people and content details are invented. See README.md.

## Tech stack

- Frontend: Next.js (TypeScript), `frontend/`
- Backend: FastAPI (Python), `backend/`
- Database: PostgreSQL (SQLite for tests)
- LLM: Anthropic Claude API, structured JSON output via tool-use, one schema
  per content type (see `backend/app/schemas/content.py`)
- No background job queue — generation is synchronous request/response.

## Commands

```bash
# backend
cd backend && pip install -r requirements.txt
uvicorn app.main:app --reload
pytest -v

# frontend
cd frontend && npm install && npm run dev
```

## Conventions

- Each content type (social post, hashtag set, newsletter) has its own
  Pydantic schema and prompt function — never merge them into one freeform
  text generation call.
- Content structure is a flexible baseline, not a locked format; prompts
  support multiple structural variants per content type.
- Brand voice reference lives in `backend/app/services/brand_voice.py`.
- `content_items.platform` stays nullable/unused so future posting automation
  doesn't require a schema migration.
- Manual-click publishing (a human clicks "Post") is built for X; no
  fire-and-forget scheduling infrastructure beyond the cron-called
  `POST /api/social/x/run-scheduled-posts` endpoint.
