from pydantic import BaseModel

class Race(BaseModel):
    race_name: str
    race_description: str
    race_link: str
    race_date: str
    race_news: list
