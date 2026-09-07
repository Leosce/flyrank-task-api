from fastapi import FastAPI

from app.routes.users import router as users_router

app = FastAPI(
    title="FlyRank Users API",
    description="An in-memory REST API built with FastAPI.",
    version="1.0.0",
)

app.include_router(users_router)


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    """Return a lightweight health status for deployments and monitoring."""
    return {"status": "ok"}
