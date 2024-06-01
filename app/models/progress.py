from pydantic import BaseModel
from datetime import date

class Progress(BaseModel):
    id: int
    user_id: int
    activity: str
    duration: int
    distance: float
    intensity: int
    calories_burned: float
    date: date

    class Config:
        orm_mode = True
