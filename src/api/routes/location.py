from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from api import deps
from api.crud import location
from api.schemas.location import Location

location_router = APIRouter(
    prefix="/api/v1/locations",
    tags=["locations"]
)

@location_router.get('/', status_code=200, response_model=List[Location])
def all_locations(
    db: Session = Depends(deps.get_db),
) -> list:
    return location.get_locations(db=db)