from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.core.database import Base


def utc_now():
    return datetime.now(timezone.utc)

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    applicant_name = Column(String,  nullable=False)
    applicant_email = Column(String, nullable=False)
    resume_file_path = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)
    evaluated_at = Column(DateTime(timezone=True), nullable=True)

    ai_score = Column(Integer, nullable=True)
    ai_status = Column(String, nullable=True)
    ai_reason = Column(Text, nullable=True)
    ai_strengths = Column(Text, nullable=True)
    ai_weaknesses = Column(Text, nullable=True)
    ai_recommendation = Column(Text, nullable=True)
    ai_provider = Column(String, nullable=True)
    ai_model = Column(String, nullable=True)

    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    job = relationship("Job", back_populates="application")