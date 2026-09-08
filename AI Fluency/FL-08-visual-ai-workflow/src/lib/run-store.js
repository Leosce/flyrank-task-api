const runs = new Map();

export function createRun(runId) {
  runs.set(runId, { id: runId, status: "queued", steps: [], createdAt: new Date().toISOString() });
}

export function getRun(runId) {
  return runs.get(runId);
}

export function markRunRunning(runId) {
  const run = runs.get(runId);
  if (run) run.status = "running";
}

export function appendRunStep(runId, step) {
  const run = runs.get(runId);
  if (run) run.steps.push({ ...step, completedAt: new Date().toISOString() });
}

export function finishRun(runId) {
  const run = runs.get(runId);
  if (run) run.status = "completed";
}

export function failRun(runId, message) {
  const run = runs.get(runId);
  if (run) {
    run.status = "failed";
    run.error = message;
  }
}
