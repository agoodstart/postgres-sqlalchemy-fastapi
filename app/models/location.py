from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Location(Base):
    __tablename__ = "locations"

    location_id = Column(Integer, primary_key=True, index=False)
    street_address = Column(String)
    postal_code = Column(String, nullable=True)
    city = Column(String)
    state_province = Column(String, nullable=True)
    country_id = Column(Integer, ForeignKey('countries.country_id'))

    country = relationship("Country", back_populates="locations")
    departments = relationship("Department", back_populates="location")