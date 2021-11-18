from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from api import deps
from api.crud import department
from api.schemas.department import Department

department_router = APIRouter(
    prefix="/api/v1/departments",
    tags=["departments"]
)

@department_router.get('/', status_code=200, response_model=List[Department])
def all_departments(
    db: Session = Depends(deps.get_db),
) -> list:
    return department.get_departments(db=db)