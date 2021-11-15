from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.db.base_model import Base

class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, index=False)
    department_name = Column(String)
    location_id = Column(Integer, ForeignKey('locations.location_id'))

    location = relationship("Location", back_populates="departments")