from sqlalchemy import Column, Integer, String, Float, Date, MetaData;
from sqlalchemy.orm import relationship

from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    job_id = Column(Integer, primary_key=True, index=False)
    job_title = Column(String)
    min_salary = Column(Float)
    max_salary = Column(Float)
    employees = relationship("Employee")
