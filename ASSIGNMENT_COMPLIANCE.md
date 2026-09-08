# Assignment Compliance Map

This portfolio contains both internship deliverables and earlier course projects. The names and functionality below identify which folders meet each supplied backend brief, and which items still need a dedicated implementation.

| Brief | Current repository status | Location / notes |
| --- | --- | --- |
| A1: In-memory Task API | Meets core requirements | `Assignment-01-fastapi-backend` now provides the required `/tasks` CRUD contract, health endpoint, and FastAPI docs. |
| A2: SQLite Task API | Meets core requirements | `Assignment-02-sqlite-task-api` preserves A1's task routes using seed-once SQLite persistence and parameterized queries. |
| A3: Postgres + Docker Task API | Meets core requirements | `Assignment-03-with FastAPi-PostgreSQL-Docker/a2-postgres` provides the task routes, parameterized persistence, Docker Compose, env example, and seeded database. |
| A4: Supabase Auth | Meets core requirements | `Assignment-04-jwt-auth-fastapi` delegates signup/login/logout and bearer-token validation to Supabase Auth. The configured project returned a successful Auth settings response. |
| A7: Inngest background job | Needs alignment | `Assignment-06-job-processing-service-v1.0.0` uses Celery/Redis rather than Inngest and is a more advanced but different project. |
| A8: PDF report generator | Missing | No dedicated report generator folder exists yet. |
| A9: Polite scraper | Needs alignment | `Assignment-05-web-scrapper-fastapi` is only a FastAPI scraping scaffold; it does not yet document the complete 60-book pipeline and evidence required by the brief. |
| A17: LLM behind an API | Largely covered, verify with live credentials | `Assignment-07-ruleguard-ai` includes a narrow validated LLM endpoint, retry/timeout handling, a kill switch, and eval cases. It uses Gemini rather than OpenAI, which the brief permits. |
| AI visual workflow | Meets the supplied workflow brief | `AI Fluency/FL-08-visual-ai-workflow` contains React Flow, Inngest, strict OpenAI YES/NO branching, execution logs, active path visuals, and local JSON save/load/import/export. |

## Notes

- The local `mars/` folder is preserved as source material and intentionally excluded from the GitHub repository. It should not be described as a submitted deliverable until it is moved into a dedicated A2 folder with its own README and verification evidence.
- Do not claim the A1, A2, A4, A7, A8, or A9 briefs are complete until their listed gaps are resolved and their documented checkpoints are run.
