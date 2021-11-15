from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from api.db.base_model import Base

from api.models.region import Region
from api.models.location import Location
from api.models.country import Country
from api.models.job import Job
from api.models.department import Department

class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True, index=False, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=True)
    hire_date = Column(Date)
    job_id = Column(Integer, ForeignKey('jobs.job_id'), nullable=True)
    salary = Column(Float, nullable=True)
    manager_id = Column(Integer, ForeignKey('employees.employee_id'), nullable=True)
    # manager = relationship('Manager', backref='employees')
    department_id = Column(Integer, ForeignKey('departments.department_id'), nullable=True)

class Manager(Employee):
    # pass
    employees = relationship(lambda: Employee, foreign_keys=lambda: Employee.manager_id)