from pydantic import BaseModel

class Route(BaseModel):
    route_name: str
    route_distance: float
