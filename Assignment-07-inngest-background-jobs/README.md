# Assignment A7: Inngest Background Report API

An API that accepts a slow report request immediately and delegates an eight-second durable wait plus report generation to Inngest. Reports progress from `pending` to `running` to `done`.

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
$env:INNGEST_DEV = "1"
uvicorn main:app --reload
```

Start the local Inngest dev server in a second terminal:

```bash
inngest dev -u http://localhost:8000/api/inngest
```

## API

| Method | Endpoint | Result |
| --- | --- | --- |
| GET | `/health` | Health status |
| POST | `/reports` | Returns `202` and a pending report ID immediately |
| GET | `/reports/{id}` | Returns pending, running, done, or failed status |

`generate-report` uses durable `mark-running`, `do-the-slow-work`, `build-report`, and `mark-done` steps, with two retries. Sending `{ "topic": "fail" }` deliberately fails the build step so the dashboard shows all three attempts. `report-heartbeat` is an every-minute cron function that logs pending, done, and failed report totals.

Poll a returned `status_url`: a successful report is initially `pending`, then becomes `done` after roughly eight seconds. Invalid payloads are rejected before an event is sent. `0 8 * * *` runs daily at 08:00; `0 22 * * 0` runs every Sunday at 22:00.
