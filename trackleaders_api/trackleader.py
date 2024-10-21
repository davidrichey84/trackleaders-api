import requests

from .parsers import RaceParser
from .models.race import Race
from .models.route import Route

from bs4 import BeautifulSoup
import re

RACE_SITE = "http://trackleaders.com"

def get_races():
    page = requests.get(RACE_SITE)
    if page.status_code == 200:
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
                    active_race_list.append(Race(race_name=race_title, race_link=f"http:{href}", race_active=True))
                    #active_race_list.append({"name": race_title, "race_link": href})
            return active_race_list
        else:
            return None
