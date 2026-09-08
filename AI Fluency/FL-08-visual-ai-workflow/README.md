# Decision Flow Studio

A visual AI workflow editor for branching YES/NO decisions. The frontend uses React Flow to create and connect nodes; Inngest executes every node as a durable step; OpenAI supplies the decision and must return exactly `YES` or `NO`.

## Features

- React Flow canvas with editable decision nodes and dedicated YES/NO source handles
- Local workflow state, browser save/load, and JSON import/export
- Inngest-backed execution with one durable step per node
- Strict OpenAI decision parsing, retries, visible errors, and loop protection
- Execution log, active-node styling, and animated active edges

## Setup

```bash
npm install
cp .env.example .env.local
npm run dev
```

In a second terminal, start the Inngest development server:

```bash
npm run inngest
```

Open `http://localhost:3000`, add your `OPENAI_API_KEY` to `.env.local`, and run a flow. The Inngest dev UI will connect to `http://localhost:3000/api/inngest`.

## Workflow behavior

Each node submits its prompt to the model with a constrained instruction to answer `YES` or `NO`. The matching YES or NO edge determines the next node. A path ends when the selected outcome has no outgoing edge. Cycles are rejected during execution.

## Project structure

```text
src/app/                     Next.js UI and API routes
src/components/              React Flow node and Shadcn-style UI components
src/inngest/                 Client and durable workflow function
src/lib/                     Shared graph helpers and development run state
```

The run-state store is deliberately in-memory for local development. Replace it with a durable database before deploying to a serverless production environment.
