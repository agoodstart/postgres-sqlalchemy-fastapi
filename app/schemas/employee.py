from datetime import date
from typing import List, Optional

from app.schemas.base import BaseConfig

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

class Joined(BaseConfig):
    first_name: str
    last_name: str
    salary: float
    job_title: str
    manager_full_name: Optional[str] = None
    department_name: str
    current_location: str