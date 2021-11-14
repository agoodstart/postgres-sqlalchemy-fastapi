from typing import List
from fastapi import Header, APIRouter

from app.api.schemas import Employee, Manager, Joined

employees = APIRouter(
    prefix="/employees"
)

# @employees.get('/')
# async def 
