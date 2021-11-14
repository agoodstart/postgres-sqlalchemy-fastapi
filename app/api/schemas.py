from datetime import date
from typing import List, Optional, Dict

from pydantic import BaseModel, Field

from app.database import Base

class BaseConfig(BaseModel):
    class Config:
        orm_mode = True

class Employee(BaseConfig):
    employee_id: int
    first_name: str
    last_name: str
    email: str
    phone_number: Optional[str] = None
    hire_date: date
    job_id: int
    salary: float
    manager_id: Optional[int] = None
    department_id: int

class Manager(Employee):
    employees: List[Employee]

class Job(BaseConfig):
    job_id: int
    job_title: str
    min_salary: float
    max_salary: float
    employees: List[Employee] = None

class Department(BaseConfig):
    department_id: int
    department_name: str
    location_id: int

class Location(BaseConfig):
    location_id: int
    street_address: str
    postal_code: Optional[str] = None
    city: str
    state_province: Optional[str] = None
    country_id: str
    departments: List[Department] = None

class Country(BaseConfig):
    country_id: str
    country_name: str
    region_id: int
    locations: List[Location] = None
 
class Region(BaseConfig):
    region_id: int
    region_name: str
    countries: List[Country] = None

class Joined(BaseConfig):
    first_name: str
    last_name: str
    salary: float
    job_title: str
    manager_full_name: Optional[str] = None
    department_name: str
    current_location: str