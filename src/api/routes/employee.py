from typing import Any, List, Optional
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm.session import Session

from api import deps
from api.crud import employee
from api.schemas.employee import Employee, Manager, Joined, EmployeeCreate

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

@employee_router.get("/search/", status_code=200, response_model=List[Employee])
def search_employees(
    request: Request, db: Session = Depends(deps.get_db), query: Optional[str] = None
) -> Any:
    employees = employee.search_employee(query, db=db)
    return employees


@employee_router.get('/joined', status_code=200, response_model=List[Joined])
def view(
    db: Session = Depends(deps.get_db),
) -> Any:
    return employee.get_view(db=db)

@employee_router.post('/', status_code=201, response_model=Employee)
def create_employee_entry(
    entry_in: EmployeeCreate, db: Session = Depends(deps.get_db)
):
    new_employee = employee.create_new_employee_entry(entry_in, db)
    return new_employee