from typing import List
from fastapi import Header, APIRouter

root = APIRouter(
    prefix="/"
)

@root.get("/", status_code=200)
async def index():
    return {
        "msg": "Hi!"
    }