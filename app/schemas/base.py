from pydantic import BaseModel

class BaseConfig(BaseModel):
    class Config:
        orm_mode = True