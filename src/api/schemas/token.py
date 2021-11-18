from typing import Optional

from pydantic import BaseModel

class TokenData(BaseModel):
    admin_email: Optional[str] = None

class Status(BaseModel):
    message: str