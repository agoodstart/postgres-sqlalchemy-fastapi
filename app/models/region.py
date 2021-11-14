from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Region(Base):
    __tablename__ = "regions"

    region_id = Column(Integer, primary_key=True, index=False)
    region_name = Column(String, unique=True, nullable=False)
    countries = relationship("Country", back_populates="region")