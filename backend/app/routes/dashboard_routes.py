from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.job import Job
from app.models.user import User
from app.schemas.job_schema import JobResponse
from app.models.application import Application
from app.schemas.application_schema import JobApplicationsResponse

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashbaord"],
)

@router.get("/my-jobs", response_model=List[JobResponse])
def get_my_jobs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    jobs = db.query(Job).filter(Job.recruiter_id == current_user.id).all()

    return jobs

@router.get(
    "/jobs/{job_id}/applications",
    response_model=JobApplicationsResponse
)
def get_applications_for_job(
    job_id: int,
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    job = (
        db.query(Job).
        filter(Job.id == job_id, Job.recruiter_id == current_user.id).
        first()
    )

    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Job Not Found.",
        )
    
    applications = db.query(Application).filter(Application.job_id == job.id).all()

    shortlisted = [
        application
        for application in applications
        if application.ai_status == "shortlisted"
    ]

    rejected = [
        application
        for application in applications
        if application.ai_status == "rejected"
    ]

    return {
        "job_id": job.id,
        "job_title": job.title,
        "total_applications": len(applications),
        "shortlisted_count": len(shortlisted),
        "rejected_count": len(rejected),
        "shortlisted": shortlisted,
        "rejected": rejected,
    }