from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class ApplicationResponse(BaseModel):
    id: int
    applicant_name: str
    applicant_email: str
    resume_file_path: str
    created_at: datetime
    evaluated_at: Optional[datetime] = None

    ai_score: Optional[int] = None
    ai_status: Optional[str] = None
    ai_reason: Optional[str] = None
    ai_strengths: Optional[str] = None
    ai_weaknesses: Optional[str] = None
    ai_recommendation: Optional[str] = None
    ai_provider: Optional[str] = None
    ai_model: Optional[str] = None

    job_id: int

    class Config:
        from_attributes = True

class JobApplicationsResponse(BaseModel):
    job_id: int
    job_title: str
    total_applications: int
    shortlisted_count: int
    rejected_count: int
    shortlisted: List[ApplicationResponse]
    rejected: List[ApplicationResponse]