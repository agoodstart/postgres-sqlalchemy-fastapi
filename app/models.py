from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Date;
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

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
    postal_code = Column(String, nullable=True)
    city = Column(String)
    state_province = Column(String, nullable=True)
    country_id = Column(Integer, ForeignKey('countries.country_id'))

    country = relationship("Country", back_populates="locations")
    departments = relationship("Department", back_populates="location")

class Department(Base):
    __tablename__ = "departments"

    department_id = Column(Integer, primary_key=True, index=False)
    department_name = Column(String)
    location_id = Column(Integer, ForeignKey('locations.location_id'))

    location = relationship("Location", back_populates="departments")

class Job(Base):
    __tablename__ = "jobs"

    job_id = Column(Integer, primary_key=True, index=False)
    job_title = Column(String)
    min_salary = Column(Float)
    max_salary = Column(Float)
    employees = relationship("Employee")

class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, index=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String)
    hire_date = Column(Date)
    job_id = Column(Integer, ForeignKey('jobs.job_id'))
    salary = Column(Float, nullable=False)
    manager_id = Column(Integer, ForeignKey('employees.employee_id'), nullable=True)
    department_id = Column(Integer, ForeignKey('departments.department_id'))