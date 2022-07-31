from datetime import date
from pydantic import BaseModel
class Race(BaseModel):
    race_name: str
    race_date: date
    racers: list
    race_date: date
