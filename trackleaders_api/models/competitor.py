from time import time
from pydantic import BaseModel
from .route import Route
from typing import List, Dict, Optional

class Competitor(BaseModel):
    competitor_name: str
    competitor_from: Optional[str] = None
    # update this to route model
    #competitor_route: Route
    # update this to route model
    competitor_age: Optional[int] = None
    competitor_equipment: Optional[dict] = None
    competitor_status: str
    competitor_speed_units: Optional[str] = None
    competitor_elevation_units: Optional[str] = None
    competitor_current_speed: Optional[float] = None
    competitor_moving_average_speed: Optional[float] = None
    competitor_last_report: Optional[str] = None
    competitor_time_since_start: Optional[str] = None
    competitor_route_mile: Optional[str] = None
    competitor_elevation_gain: Optional[int] = None
    competitor_current_elevation: Optional[int] = None
    competitor_route_distance_per_day: Optional[int] = None
    competitor_moving_time: Optional[str] = None
    competitor_stopped_time: Optional[str] = None
    competitor_next_waypoint: Optional[str] = None
    competitor_distance_to_next_waypoint: Optional[float] = None
