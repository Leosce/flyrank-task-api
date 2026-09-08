import OpenAI from "openai";

import { inngest } from "@/inngest/client";
import { appendRunStep, failRun, finishRun, markRunRunning } from "@/lib/run-store";
import { findOutgoingEdge } from "@/lib/workflow";

async function decide(prompt) {
  const apiKey = process.env.OPENAI_API_KEY;
  if (!apiKey) throw new Error("OPENAI_API_KEY is not configured.");

  const client = new OpenAI({ apiKey });
  const completion = await client.chat.completions.create({
    model: process.env.OPENAI_MODEL || "gpt-4o-mini",
    temperature: 0,
    messages: [
      { role: "system", content: "Return exactly one token: YES or NO. Do not add punctuation or explanation." },
      { role: "user", content: prompt },
    ],
  });
  const answer = completion.choices[0]?.message?.content?.trim().toUpperCase();
  if (answer !== "YES" && answer !== "NO") throw new Error("The model did not return YES or NO.");
  return answer;
}

export const executeWorkflow = inngest.createFunction(
  { id: "execute-yes-no-workflow", retries: 2 },
  { event: "workflow/execute" },
  async ({ event, step }) => {
    const { runId, nodes, edges, startNodeId } = event.data;
    markRunRunning(runId);
    const nodesById = new Map(nodes.map((node) => [node.id, node]));
    let currentNodeId = startNodeId || nodes[0]?.id;
    const visited = new Set();

    try {
      while (currentNodeId && !visited.has(currentNodeId)) {
        const node = nodesById.get(currentNodeId);
        if (!node) throw new Error(`Node ${currentNodeId} does not exist.`);
        visited.add(currentNodeId);
        const outcome = await step.run(`decide-${currentNodeId}`, () => decide(node.data.prompt));
        const nextEdge = findOutgoingEdge(edges, currentNodeId, outcome);
        await step.run(`record-${currentNodeId}`, () => appendRunStep(runId, {
          nodeId: currentNodeId,
          title: node.data.title,
          prompt: node.data.prompt,
          outcome,
          edgeId: nextEdge?.id || null,
        }));
        currentNodeId = nextEdge?.target;
      }
      if (currentNodeId) throw new Error("The workflow contains a cycle.");
      finishRun(runId);
    } catch (error) {
      failRun(runId, error instanceof Error ? error.message : "Workflow execution failed.");
      throw error;
    }
  },
);
