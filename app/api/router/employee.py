from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from app.api import deps
from app.crud import employee
from app.schemas.employee import Employee

employee_router = APIRouter()

@employee_router.get('/', status_code=200, response_model=List[Employee])
def fetch_all(
    db: Session = Depends(deps.get_db),
) -> list:
    all = employee.get_employees(db=db)
    return all