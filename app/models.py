from sqlalchemy import Boolean, Column, ForeignKey, Integer, String;
from sqlalchemy.orm import relationship

from .database import Base

class Region(Base):
    __tablename__ = "regions"

    region_id = Column(Integer, primary_key=True, index=False)
    region_name = Column(String, unique=True, nullable=False)
    countries = relationship("Country", back_populates="region")

class Country(Base):
    __tablename__ = "countries"

    country_id = Column(String, primary_key=True, index=False)
    country_name = Column(String)
    region_id = Column(Integer, ForeignKey('regions.region_id'))
    
    region = relationship("Region", back_populates="countries")
    locations = relationship("Location", back_populates="country")

class Location(Base):
    __tablename__ = "locations"

    location_id = Column(Integer, primary_key=True, index=False)
    street_address = Column(String)
    postal_code = Column(String)
    city = Column(String)
    state_province = Column(String)

    country_id = Column(Integer, ForeignKey('countries.country_id'))
    country = relationship("Country", back_populates="locations")