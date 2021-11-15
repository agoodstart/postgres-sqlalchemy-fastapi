from fastapi import FastAPI

from app.db.base_model import Base
from app.db.session import database

from app.api.router.employee import employee_router
from app.api.router.region import region_router
from app.api.router.job import job_router
from app.api.router.country import country_router
from app.api.router.department import department_router
from app.api.router.location import location_router

Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Fullstack"
)

app.include_router(region_router)
app.include_router(country_router)
app.include_router(location_router)
app.include_router(department_router)
app.include_router(job_router)
app.include_router(employee_router)


@app.get("/", status_code=200)
async def index():
    return {
        "msg": "Hi!"
    }