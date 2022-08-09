from pydantic import BaseModel
from .route import Route
from .racer import Racer
from typing import List, Optional
#from ..parsers import R

class RaceType(BaseModel):
    race_name: str
    race_description: Optional[str]
    race_link: str
    race_date: Optional[str]
    race_news: Optional[list]
    race_active: bool
    race_routes: Optional[List[Route]] = None
    race_racers: Optional[List[Racer]] = None

class Race(RaceType):
    def get_racers(self):
        if self.race_routes is not None:
            print("getting racers")
        else:
            print("getting race routes first")

    #def get_routes(self):
