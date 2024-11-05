from time import time
from pydantic import BaseModel
from .route import Route
from typing import List, Dict, Optional

class Competitor(BaseModel):
    competitor_name: str
    competitor_from: Optional[str]
    # update this to route model
    #competitor_route: Route
    # update this to route model
    competitor_format: str
    competitor_age: int
    competitor_equipment: dict
    competitor_status: str
    competitor_speed_units: str
    competitor_elevation_units: str
    competitor_current_speed: float
    competitor_moving_average_speed: float
    competitor_last_report: str
    competitor_time_since_start: str
    competitor_route_mile: float
    competitor_elevation_gain: int
    competitor_current_elevation: int
    competitor_route_distance_per_day: int
    competitor_moving_time: str
    competitor_stopped_time: str
    competitor_next_waypoint: str
    competitor_distance_to_next_waypoint: float
