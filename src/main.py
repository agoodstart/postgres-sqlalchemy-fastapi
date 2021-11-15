from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRouter

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
    title="Fullstack",
)

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(region_router)
app.include_router(country_router)
app.include_router(location_router)
app.include_router(department_router)
app.include_router(job_router)
app.include_router(employee_router)

@app.get("/", status_code=200)
async def index(request: Request):
    url_list = [
        {'path': route.path, 'name': route.name.replace('_', ' ').capitalize()}
        for route in request.app.routes
            if 'all' in route.name or 'president' in route.name
    ]
    return url_list