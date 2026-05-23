from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    applicant_name = Column(String,  nullable=False)
    applicant_email = Column(String, nullable=False)
    resume_file_path = Column(String, nullable=False)

    ai_score = Column(Integer, nullable=True)
    ai_status = Column(String, nullable=True)
    ai_reason = Column(Text, nullable=True)
    ai_strengths = Column(Text, nullable=True)
    ai_weaknesses = Column(Text, nullable=True)
    ai_recommendation = Column(Text, nullable=True)

    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)