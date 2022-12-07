from pydantic import BaseModel


class Username(BaseModel):
    name: str
    
    class Config:
        orm_mode = True