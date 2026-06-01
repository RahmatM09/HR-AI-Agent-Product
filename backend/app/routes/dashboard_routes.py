from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.job import Job
from app.models.user import User
from app.schemas.job_schema import JobResponse

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