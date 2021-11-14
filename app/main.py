from fastapi import Depends, FastAPI, APIRouter, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

from app import deps

from app.api.root import root
from app.api.employees import employees

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fullstack"
)

app.include_router(root)
app.include_router(employees)

api_router = APIRouter()
@app.get('/', status_code=200)
def read_all(db: Session = Depends(deps.get_db)):
    views = crud.get_view(db)
    return views