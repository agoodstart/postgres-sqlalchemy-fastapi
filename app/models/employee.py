from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from app.database import Base

from app.models.region import Region
from app.models.location import Location
from app.models.country import Country
from app.models.job import Job
from app.models.department import Department

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
    # manager = relationship('Manager', backref='employees')
    department_id = Column(Integer, ForeignKey('departments.department_id'))

class Manager(Employee):
    # pass
    employees = relationship(lambda: Employee, foreign_keys=lambda: Employee.manager_id)