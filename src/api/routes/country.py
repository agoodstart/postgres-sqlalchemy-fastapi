from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from api import deps
from api.crud import country
from api.schemas.country import Country

country_router = APIRouter(
    prefix="/countries"
)

@country_router.get('/', status_code=200, response_model=List[Country])
def fetch_all(
    db: Session = Depends(deps.get_db),
) -> list:
    return country.get_countries(db=db)