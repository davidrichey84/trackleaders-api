from pydantic import BaseModel
from .route import Route
from .competitor import Competitor
from typing import List, Optional
from datetime import date
from bs4 import BeautifulSoup
import requests
import re

class Race(BaseModel):
    race_name: str
    race_description: Optional[str] = None
    race_link: str
    race_date: Optional[str] = None
    race_news: Optional[list] = None
    race_active: bool
    race_routes: Optional[List[Route]] = []
    race_competitors: Optional[List[Competitor]] = None

    def get_competitors(self):
        if self.race_routes is not None:
            print("getting racers")
        else:
            print("getting race routes first")

    def get_routes(self):
        page = self.get_page(f"{self.race_link}f.php")
        if page:
            print("got page... let's parse some routes")
            soup = BeautifulSoup(page.content, "html.parser")
            #route_dropdown = soup.find('select', {'name': 'leaderboardroutedropdown'})
            #if len(route_dropdown) > 0:
            #    options = route_dropdown.find_all('option')
            #    race_routes = [option.text for option in options]
            #    self.race_routes = race_routes
            routes_div = soup.find('div', id='maintabs-6')
            routes = re.findall(r'█████\s+(.+?)\s+-\s+([\d.]+)\s+mi', routes_div.get_text())
            for route in routes:
                self.race_routes.append(Route(route_name=route[0], route_distance=route[1]))

    def get_competitors(self):
        temp_race_name = self.race_link.split("/")[3]
        page = self.get_page(f"http://trackleaders.com/spot/{temp_race_name}/summary.php")
        if page:
            print("got the page... gets parse some racers!")
            soup = BeautifulSoup(page.content, "html.parser")
            racer_table = soup.find('table')


    def get_page(self, race_link):
        try:
            page = requests.get(race_link)
            if page.status_code == 200:
                return page
        except:
            print('http error... need to do more with this')
            return None
