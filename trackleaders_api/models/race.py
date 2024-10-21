from pydantic import BaseModel
from .route import Route
from .competitor import Competitor
from typing import List, Optional
from datetime import date
from bs4 import BeautifulSoup
import requests

class Race(BaseModel):
    race_name: str
    race_description: Optional[str] = None
    race_link: str
    race_date: Optional[str] = None
    race_news: Optional[list] = None
    race_active: bool
    race_routes: Optional[List[Route]] = None
    race_competitors: Optional[List[Competitor]] = None

    def get_competitors(self):
        if self.race_routes is not None:
            print("getting racers")
        else:
            print("getting race routes first")

    def get_routes(self):
        page = self.get_page(self.race_link)
        if page is not None:
            print("got page... let's parse some routes")
            soup = BeautifulSoup(page.content, "html.parser")
            route_options = soup.find_all(id="lbcourselabel")
            if len(route_options) > 0:
                race_routes_raw = route_options[0].next_sibling()
                print(race_routes_raw)

    def get_page(self, race_link):
        try:
            page = requests.get(race_link)
            if page.status_code == 200:
                return page
        except:
            print('http error... need to do more with this')
            return None
