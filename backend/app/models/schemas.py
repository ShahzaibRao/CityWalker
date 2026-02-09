from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class GeoPoint(BaseModel):
    lat: float = Field(..., ge=-90, le=90)
    lng: float = Field(..., ge=-180, le=180)


class RouteCreate(BaseModel):
    user_id: str
    start_time: datetime
    end_time: datetime
    path: List[GeoPoint]


class RouteSummary(BaseModel):
    route_id: str
    distance_m: float
    captured_area_sq_m: float


class CaptureSummary(BaseModel):
    area_id: str
    user_id: str
    captured_at: datetime
    polygon_points: List[GeoPoint]


class LeaderboardEntry(BaseModel):
    user_id: str
    rank: int
    points: int
    captured_tiles: int


class LeaderboardResponse(BaseModel):
    scope: str
    entries: List[LeaderboardEntry]


class ChallengeSuggestion(BaseModel):
    title: str
    description: str
    expires_at: Optional[datetime] = None
