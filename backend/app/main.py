from fastapi import FastAPI

from app.routes import job_routes, apply_routes

app = FastAPI(
    title="HR AI Agent Backend",
    description="API-first HR AI Agent backend for job posting, resume evaluation, and applicant communication.",
    version="1.0.0"  
    ) 

@app.get("/")
def root():
    return{
        "message": "HR AI Agent Backend is running.",
        "docs_url": "/docs",
    }

app.include_router(job_routes.router) 
app.include_router(apply_routes.router) 