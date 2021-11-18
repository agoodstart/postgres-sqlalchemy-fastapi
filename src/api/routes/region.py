from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from api import deps
from api.crud import region
from api.schemas.region import Region

region_router = APIRouter(
    prefix="/api/v1/regions",
    tags=["regions"]
)

@region_router.get('/', status_code=200, response_model=List[Region])
def all_regions(
    db: Session = Depends(deps.get_db),
) -> list:
    return region.get_regions(db=db)