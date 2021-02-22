from pydantic import BaseModel


class Meal(BaseModel):
    id: int
    image: str
    carbs: float
    time: str

    class Config:
        orm_mode = True
