from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from app.api import deps
from app.crud import department
from app.schemas.department import Department

department_router = APIRouter(
    prefix="/departments"
)

@department_router.get('/', status_code=200, response_model=List[Department])
def fetch_all(
    db: Session = Depends(deps.get_db),
) -> list:
    return department.get_departments(db=db)