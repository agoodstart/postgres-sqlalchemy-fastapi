from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from app.api import deps
from app.crud import country
from app.schemas.country import Country

country_router = APIRouter(
    prefix="/countries"
)

@country_router.get('/', status_code=200, response_model=List[Country])
def fetch_all(
    db: Session = Depends(deps.get_db),
) -> list:
    return country.get_countries(db=db)