# Remaining Submission Workflow

The repository now contains the code and run instructions for the supplied backend and AI Fluency assignments. The items below require a live local runtime, personal account, camera, or portal access, so they cannot be truthfully generated from source code alone.

## 1. Capture A1 Swagger evidence

1. In `Assignment-01-fastapi-backend`, activate the virtual environment and run `uvicorn app.main:app --reload`.
2. Open `http://127.0.0.1:8000/docs`.
3. Use **Try it out** to create, read, update, and delete a task.
4. Take one screenshot showing the Swagger page and at least one successful response. Keep it locally or add it under `Assignment-01-fastapi-backend/docs/` with no secrets visible.

## 2. Run A7 in the Inngest dashboard

1. In `Assignment-07-inngest-background-jobs`, create and activate a virtual environment, then run `pip install -r requirements.txt`.
2. Terminal one: `uvicorn main:app --reload`.
3. Terminal two: `inngest dev -u http://localhost:8000/api/inngest`.
4. Send `POST /reports` with `{ "topic": "cats" }`, then poll the returned URL until it becomes `done`.
5. Send `{ "topic": "fail" }` and capture the dashboard showing three failed attempts. Wait two minutes and capture two heartbeat runs.
6. Paste the real responses and screenshots into the A7 README. Do not invent timestamps or dashboard output.

## 3. Render and inspect A8's PDF

1. In `Assignment-08-pdf-report-generator`, create and activate a virtual environment.
2. Run `pip install -r requirements.txt`, then `playwright install chromium`.
3. Run `python seed.py` and `uvicorn main:app --reload`.
4. `POST /reports`, download the returned file URL, and open the PDF.
5. Confirm the report has at least two pages, repeated table headers, and no split rows. Capture page one and add the real response and screenshot to the A8 README.
6. Send a second `POST /reports` on the same day and confirm it returns the same ID. Send `{ "force": true }` to confirm a new report is created.

## 4. Run A9 against the practice sandbox

1. In `Assignment-05-web-scrapper-fastapi/scraper`, create and activate a virtual environment and run `pip install -r requirements.txt`.
2. Run `python main.py` once. Confirm `catalogue_pages=3`, `discovered=60`, `unique_urls=60`, and `valid_records=60` in the terminal and `output/run-report.json`.
3. Run it again and confirm cache-hit messages and no duplicate records.
4. Run `python main.py --include-broken-url` and confirm one failed page is logged while 60 valid records remain.
5. Paste the three real run-report excerpts into the A9 README. Never scrape a different target without checking its rules and terms.

## 5. Verify Gemini-backed projects

1. Revoke the API key previously pasted in chat and create a replacement in Google AI Studio.
2. Put the replacement only in ignored local `.env` or `.env.local` files. Never commit it.
3. For RuleGuard, configure `Assignment-07-ruleguard-ai/backend/.env`, build its FAISS index, run its test suite, then run one real request and the evaluation command from its README.
4. For Decision Flow Studio, configure `AI Fluency/FL-08-visual-ai-workflow/.env.local`, run the Next.js app and Inngest dev server, then capture one YES and one NO execution path.
5. Record the actual test/evaluation summaries and screenshots in the relevant READMEs.

## 6. Complete the AI Fluency submission items

1. Record a 3–5 minute live demo of the chosen agent or workflow. Show a real end-to-end run, explain one design decision and one limitation, then upload it as an unlisted video.
2. Add the video URL, actual evaluation results, limitations, and a short AI-use transparency note to that project README.
3. Write the 500–800 word retrospective in your own voice. Include what changed, what you would build next, and three transferable lessons.
4. Complete the hours log, publish the personal FlyRank-domain site and build-in-public post, then submit for the required human review. These portal and publishing actions must be performed by you under your own account.

## Commit History

The repository has five authentic commits. The original briefs ask for one meaningful commit per stage, but those staged historical commits cannot be recreated honestly after the work. Keep future verification changes in focused commits with the real command output or screenshot they add.
