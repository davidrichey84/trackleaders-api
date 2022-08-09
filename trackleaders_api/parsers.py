from bs4 import BeautifulSoup
from .models.race import Race
import re
import requests
from typing import List
from .models.route import Route

# TO-DO: Parent parser class
#class Parser(object):

class RaceParser(object):
    def __init__(self, page):
        #self.race_url = race_url
        #self.race = race_name
        self.page = page

    def _parse(self, page):
        soup = BeautifulSoup(page.content, "html.parser")
        active_races = soup.find_all("div", class_="activetrackers")
        for item in active_races:
            race_links = item.find_all("a")
        if len(race_links) > 0:
            active_race_list = []
            for link in race_links:
                if link.has_attr('title'):
                    href = link["href"]
                    race_title = re.findall(r'<h3>(.*)</h3>', link["title"])[0]
                    #print(f"Race Title: {race_title}   Race Link: {href}")
                    active_race_list.append(Race(race_name=race_title, race_link=href, race_active=True))
                    #active_race_list.append({"name": race_title, "race_link": href})
        
        
        return active_race_list

class RaceRouteParser(object):
    def _parse(self, race_link):
        page = self.get_page(race_link)
        if page is not None:
            soup = BeautifulSoup(page.content, "html.parser")
            route_options = soup.find_all(id="lbcourselabel")
            if len(route_options) > 0:
                race_routes_raw = route_options[0].next_sibling()
            
        
    def get_page(self, race_link):
        try:
            page = requests.get(race_link)
            if page.status_code == 200:
                return page
        except:
            print('http error... need to do more with this')
            return None