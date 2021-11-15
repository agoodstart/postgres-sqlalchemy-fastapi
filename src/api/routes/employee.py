from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from api import deps
from api.crud import employee
from api.schemas.employee import Employee, Manager, Joined

employee_router = APIRouter(
    prefix="/employees"
)

@employee_router.get('/', status_code=200, response_model=List[Employee])
def all_employees(
    db: Session = Depends(deps.get_db),
) -> list:
    return employee.get_employees(db=db)

@employee_router.get('/managers', status_code=200, response_model=List[Manager])
def all_managers(
    db: Session = Depends(deps.get_db),
) -> list:
    return employee.get_managers(db=db)

@employee_router.get('/president', status_code=200, response_model=Employee)
def the_president(
    db: Session = Depends(deps.get_db),
) -> Any:
    return employee.get_the_president(db=db)

@employee_router.post('/joined', status_code=200, response_model=List[Joined])
def view(
    db: Session = Depends(deps.get_db),
) -> Any:
    return employee.get_view(db=db)