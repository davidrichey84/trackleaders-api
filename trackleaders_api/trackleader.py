import requests

from .parsers import RaceParser
from .models.race import Race
#from .models.racer import Racer
from .models.route import Route

RACE_SITE = "http://trackleaders.com"

def get_races():
    page = requests.get(RACE_SITE)
    if page.status_code == 200:
        return page


def parse(page):
    return RaceParser(page)
    