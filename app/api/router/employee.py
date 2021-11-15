from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from app.api import deps
from app.crud import employee
from app.schemas.employee import Employee, Manager, Joined

employee_router = APIRouter(
    prefix="/employees"
)

@employee_router.get('/', status_code=200, response_model=List[Employee])
def fetch_all(
    db: Session = Depends(deps.get_db),
) -> list:
    return employee.get_employees(db=db)

@employee_router.get('/managers', status_code=200, response_model=List[Manager])
def fetch_all(
    db: Session = Depends(deps.get_db),
) -> list:
    return employee.get_managers(db=db)

@employee_router.get('/president', status_code=200, response_model=Employee)
def fetch_all(
    db: Session = Depends(deps.get_db),
) -> Any:
    return employee.get_the_president(db=db)

@employee_router.get('/joined', status_code=200, response_model=List[Joined])
def fetch_all(
    db: Session = Depends(deps.get_db),
) -> Any:
    return employee.get_view(db=db)