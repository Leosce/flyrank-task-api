# Assignment Compliance Map

This portfolio contains both internship deliverables and earlier course projects. The names and functionality below identify which folders meet each supplied backend brief, and which items still need a dedicated implementation.

| Brief | Current repository status | Location / notes |
| --- | --- | --- |
| A1: In-memory Task API | Meets core requirements | `Assignment-01-fastapi-backend` now provides the required `/tasks` CRUD contract, health endpoint, and FastAPI docs. |
| A2: SQLite Task API | Meets core requirements | `Assignment-02-sqlite-task-api` preserves A1's task routes using seed-once SQLite persistence and parameterized queries. |
| A3: Postgres + Docker Task API | Meets core requirements | `Assignment-03-with FastAPi-PostgreSQL-Docker/a2-postgres` provides the task routes, parameterized persistence, Docker Compose, env example, and seeded database. |
| A4: Supabase Auth | Meets core requirements | `Assignment-04-jwt-auth-fastapi` delegates signup/login/logout and bearer-token validation to Supabase Auth. The configured project returned a successful Auth settings response. |
| A7: Inngest background job | Implemented; live dashboard verification pending | `Assignment-07-inngest-background-jobs` returns `202`, persists status, runs the eight-second task in durable retriable steps, and exposes an every-minute heartbeat cron. |
| A8: PDF report generator | Implemented; Playwright rendering verification pending | `Assignment-08-pdf-report-generator` seeds 200 SQLite orders, aggregates them, renders a stored PDF by link, and prevents duplicate same-day reports. |
| A9: Polite scraper | Implemented; live sandbox run pending | `Assignment-05-web-scrapper-fastapi/scraper` follows exactly three catalogue pages, caches and paces requests, validates records, isolates failures, and writes JSON outputs plus a run report. |
| A17: LLM behind an API | Largely covered, verify with live credentials | `Assignment-07-ruleguard-ai` includes a narrow validated LLM endpoint, retry/timeout handling, a kill switch, and eval cases. It uses Gemini rather than OpenAI, which the brief permits. |
| AI visual workflow | Implemented; Inngest/Gemini verification pending | `AI Fluency/FL-08-visual-ai-workflow` contains React Flow, Inngest, strict Gemini-or-OpenAI YES/NO branching, execution logs, active path visuals, and local JSON save/load/import/export. |

## Notes

- The local `mars/` folder is preserved as source material and intentionally excluded from the GitHub repository. It should not be described as a submitted deliverable until it is moved into a dedicated A2 folder with its own README and verification evidence.
- A1, A2, A3, and A4 have local verification coverage. A7, A8, A9, A17, and the visual workflow require the listed external service or browser runtime to complete their live checkpoints.
