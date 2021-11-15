from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from app.api import deps
from app.crud import region
from app.schemas.region import Region

region_router = APIRouter(
    prefix="/regions"
)

@region_router.get('/', status_code=200, response_model=List[Region])
def fetch_all(
    db: Session = Depends(deps.get_db),
) -> list:
    return region.get_regions(db=db)