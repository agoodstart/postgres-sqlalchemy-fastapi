from datetime import date
from typing import List, Optional, Sequence

from .base import BaseConfig

class Employee(BaseConfig):
    employee_id: int
    first_name: str
    last_name: str
    email: str
    phone_number: Optional[str] = None
    hire_date: date
    job_id: Optional[int] = None
    salary: Optional[int] = None
    manager_id: Optional[int] = None
    department_id: Optional[int] = None


class Manager(Employee):
    employees: List[Employee]

class EmployeeCreate(BaseConfig):
    first_name: str
    last_name: str
    email: str
    phone_number: Optional[str] = None
    hire_date: date
    job_id: Optional[int] = None
    salary: Optional[int] = None
    manager_id: Optional[int] = None
    department_id: Optional[int] = None

class Joined(BaseConfig):
    first_name: str
    last_name: str
    ceiled_salary: float
    job_title: str
    manager_full_name: Optional[str] = None
    department_name: str
    current_location: str
    salary_count: int