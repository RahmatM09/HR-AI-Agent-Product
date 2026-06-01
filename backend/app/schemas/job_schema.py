from typing import Optional
from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str
    description: str
    requirements: str
    location: Optional[str] = None


class JobResponse(BaseModel):
    id: int
    recruiter_id: Optional[int] = None
    title: str
    description: str
    requirements: str
    location: Optional[str] = None
    is_active: bool

    class Cinfig:
        from_attributes = True
