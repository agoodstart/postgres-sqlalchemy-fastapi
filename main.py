from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

app=FastAPI()

@app.get('/')
def index():
    return {"Message":"Test"}