from typing import List

from .base import BaseConfig
from .employee import Employee

class Job(BaseConfig):
    job_id: int
    job_title: str
    min_salary: float
    max_salary: float
    employees: List[Employee] = None