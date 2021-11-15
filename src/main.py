from fastapi import FastAPI

from api.db.base_model import Base
from api.db.session import database

from api.routes.employee import employee_router
from api.routes.region import region_router
from api.routes.job import job_router
from api.routes.country import country_router
from api.routes.department import department_router
from api.routes.location import location_router

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