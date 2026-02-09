from datetime import datetime, timedelta
from uuid import uuid4

from fastapi import APIRouter, status

from app.models.schemas import (
    ChallengeSuggestion,
    LeaderboardEntry,
    LeaderboardResponse,
    RouteCreate,
    RouteSummary,
)

router = APIRouter()


@router.get("/health", status_code=status.HTTP_200_OK)
def health_check() -> dict:
    return {"status": "ok", "timestamp": datetime.utcnow().isoformat()}


@router.post("/routes", response_model=RouteSummary, status_code=status.HTTP_201_CREATED)
def submit_route(payload: RouteCreate) -> RouteSummary:
    route_id = str(uuid4())
    distance_m = max(len(payload.path) - 1, 0) * 120.0
    captured_area_sq_m = distance_m * 5.5
    return RouteSummary(
        route_id=route_id,
        distance_m=distance_m,
        captured_area_sq_m=captured_area_sq_m,
    )


@router.get("/leaderboards", response_model=LeaderboardResponse)
def get_leaderboard(scope: str = "city") -> LeaderboardResponse:
    entries = [
        LeaderboardEntry(user_id="user-123", rank=1, points=1280, captured_tiles=18),
        LeaderboardEntry(user_id="user-456", rank=2, points=1100, captured_tiles=14),
        LeaderboardEntry(user_id="user-789", rank=3, points=950, captured_tiles=10),
    ]
    return LeaderboardResponse(scope=scope, entries=entries)


@router.get("/challenges/suggestions", response_model=ChallengeSuggestion)
def get_challenge_suggestion() -> ChallengeSuggestion:
    return ChallengeSuggestion(
        title="Sunset Streak",
        description="Walk 2 km after 6 PM this week to earn a bonus badge.",
        expires_at=datetime.utcnow() + timedelta(days=7),
    )
