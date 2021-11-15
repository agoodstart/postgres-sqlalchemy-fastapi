from .base import BaseConfig

class Department(BaseConfig):
    department_id: int
    department_name: str
    location_id: int