from sqlalchemy import Boolean, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    recruiter_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    requirements = Column(Text, nullable=False)
    location = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)

    application = relationship("Application", back_populates="job")
    recruiter = relationship("User", back_populates="jobs")

