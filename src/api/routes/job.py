from typing import Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from api import deps
from api.crud import job
from api.schemas.job import Job

job_router = APIRouter(
    prefix="/api/v1/jobs",
    tags=["jobs"]
)

@job_router.get('/', status_code=200, response_model=List[Job])
def get_jobs(
    db: Session = Depends(deps.get_db),
) -> list:
    return job.get_jobs(db=db)