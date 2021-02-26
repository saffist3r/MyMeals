from pydantic import BaseModel
from datetime import datetime


class Meal(BaseModel):
    id: int
    image: str
    carbs: float
    time: datetime

    class Config:
        orm_mode = True
