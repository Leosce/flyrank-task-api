from fastapi import FastAPI

from app.routes.tasks import router as tasks_router

app = FastAPI(
    title="FlyRank Task API",
    description="An in-memory REST API for Assignment A1.",
    version="1.0.0",
)

app.include_router(tasks_router)


@app.get("/", tags=["info"])
def api_info() -> dict[str, str | list[str]]:
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    """Return a lightweight health status for deployments and monitoring."""
    return {"status": "ok"}
