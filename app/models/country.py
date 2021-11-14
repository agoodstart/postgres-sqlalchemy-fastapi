from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Country(Base):
    __tablename__ = "countries"

    country_id = Column(String, primary_key=True, index=False)
    country_name = Column(String)
    region_id = Column(Integer, ForeignKey('regions.region_id'))
    
    region = relationship("Region", back_populates="countries")
    locations = relationship("Location", back_populates="country")