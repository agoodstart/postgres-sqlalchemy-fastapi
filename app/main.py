from fastapi import FastAPI

from app.db.base_model import Base
from app.db.session import database

from app.api.router.employee import employee_router

Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Fullstack"
)

app.include_router(employee_router)

@app.get("/", status_code=200)
async def index():
    return {
        "msg": "Hi!"
    }