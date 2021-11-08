from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, VARCHAR;
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

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")