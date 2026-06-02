from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_current_user
from app.core.database import get_db
from app.models.job import Job
from app.models.user import User
from app.schemas.job_schema import JobCreate, JobResponse, PublicJobResponse

router = APIRouter(
    prefix="/jobs", 
    tags=["Jobs"]
)

@router.post("/", response_model=JobResponse)
def create_job(
    job_data: JobCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
    ):
    new_job = Job(
        title=job_data.title,
        description=job_data.description,
        requirements=job_data.requirements,
        location=job_data.location, 
        recruiter_id=current_user.id
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job

@router.get("/", response_model=List[PublicJobResponse])
def list_jobs(db: Session = Depends(get_db)):
    results = (
        db.query(Job, User)
        .join(User, Job.recruiter_id == User.id)
        .filter(Job.is_active == True).all()
    )

    public_jobs = []

    for job, recruiter in results:
        public_jobs.append(
            {
                "id": job.id,
                "title": job.title,
                "description": job.description,
                "requirements": job.requirements,
                "location": job.location,
                "is_active": job.is_active,
                "recruiter_company_name": recruiter.company_name,
            }
        )

    return public_jobs
