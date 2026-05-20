from fastapi import FastAPI

from app.routes import job_routes

app = FastAPI(title="HR AI Agent Backend")

app.include_router(job_routes.router)