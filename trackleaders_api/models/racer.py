from asyncio import SendfileNotAvailableError
from time import time
from pydantic import BaseModel
from .route import Route
from typing import List

class Racer(BaseModel):
    racer_name: str
    racer_from: str
    # update this to route model
    #racer_route: Route
    # update this to route model
    racer_format: str
    racer_age: int
    racer_equipment: dict
    racer_status: str
    racer_speed_units: str
    racer_elevation_units: str
    racer_current_speed: float
    racer_moving_average_speed: float
    racer_last_report: time
    racer_time_since_start: str
    racer_route_mile: float
    racer_elevation_gain: int
    racer_current_elevation: int
    racer_route_distance_per_day: int
    racer_moving_time: time
    racer_stopped_time: time
    racer_next_waypoint: str
    racer_distance_to_next_waypoint: float
