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
    race_competitors: Optional[List[Competitor]] = []

    def get_competitors(self):
        if self.race_routes is not None:
            print("getting racers")
        else:
            print("getting race routes first")

    def _get_race_competitors(self, route=None):
        temp_race_name = self.race_link.split("/")[3]
        page = self.get_page(f"http://trackleaders.com/spot/{temp_race_name}/summary.php")
        if page:
            initial_soup = BeautifulSoup(page.content, "html.parser")
            racer_table = initial_soup.find('table')
            rows = racer_table.find_all('tr')
            competitor_names = []
            for row in rows:
                # Extract all cells (td or th) in the row
                cells = row.find_all('td')
                if len(cells) > 0:
                    competitor_names.append(cells[0].get_text(strip=True))
            
            for competitor in competitor_names:
                competitor_name_link = re.sub(r'[ !@#$%^&*]', '_', competitor)
                competitor_page = self.get_page(f"{self.race_link}i.php?name={competitor_name_link}")
                if competitor_page:
                    competitor_soup = BeautifulSoup(competitor_page.content, "html.parser")
                    table = competitor_soup.find('table', id='statustable')
                    table_rows = table.find_all('tr')
                    competitor_dict = {'competitor_name': competitor}
                    for row in table_rows:
                        cells = row.find_all('td')
                        cell_texts = [cell.get_text(strip=True) for cell in cells]
                        if len(cell_texts) > 0:
                            if cell_texts[0].lower() == 'race status':
                                competitor_dict['competitor_status'] =cell_texts[1].split(' ')[0]
                            elif cell_texts[0].lower() == 'status':
                                competitor_dict['competitor_status'] =cell_texts[1].split(' ')[0]
                            elif cell_texts[0].lower() == "last ppdate rec'd":
                                pass
                            elif cell_texts[0].lower() == 'current speed':
                                competitor_dict['competitor_current_speed'] = cell_texts[1].split(' ')[0]
                            elif cell_texts[0].lower() == 'route mile':
                                competitor_dict['competitor_route_mile'] = cell_texts[1].split(' ')[0]
                            elif cell_texts[0].lower() == 'elevation gain':
                                competitor_dict['competitor_elevation_gain'] = cell_texts[1].split(' ')[0]
                            elif cell_texts[0].lower() == 'current elevation':
                                competitor_dict['competitor_current_elevation'] = cell_texts[1].split(' ')[0]
                            elif cell_texts[0].lower() == 'moving time':
                                competitor_dict['competitor_moving_time'] = cell_texts[1].split(' ')[0]
                            elif cell_texts[0].lower() == 'stopped time':
                                competitor_dict['competitor_stopped_time'] = cell_texts[1].split(' ')[0]
                            elif cell_texts[0].lower() == 'moving average speed':
                                competitor_dict['competitor_moving_average_speed'] = cell_texts[1].split(' ')[0]
                            elif cell_texts[0].lower() == 'next waypoint':
                                competitor_dict['competitor_next_waypoint'] = cell_texts[1].split(' ')[0]
                            elif cell_texts[0].lower() == 'distance to next waypoint':
                                competitor_dict['competitor_distance_to_next_waypoint'] = cell_texts[1].split(' ')[0]
                    print(competitor_dict)
                    self.race_competitors.append(Competitor.model_validate(competitor_dict))

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

    #def get_competitors(self):
        #temp_race_name = self.race_link.split("/")[3]
        #page = self.get_page(f"http://trackleaders.com/spot/{temp_race_name}/summary.php")
        #if page:
        #    print("got the page... gets parse some racers!")
        #    soup = BeautifulSoup(page.content, "html.parser")
        #    racer_table = soup.find('table')

    def get_page(self, race_link):
        try:
            page = requests.get(race_link)
            if page.status_code == 200:
                return page
        except:
            print('http error... need to do more with this')
            return None
