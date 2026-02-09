# CityWalker Backend (FastAPI)

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Available Endpoints
- `GET /health` — service health check.
- `POST /routes` — submit a walking route (mock capture stats for now).
- `GET /leaderboards?scope=city` — mock leaderboard data.
- `GET /challenges/suggestions` — sample motivational challenge.

## Notes
This is an initial scaffold to validate API shapes and data contracts. Integrate PostGIS and real capture logic in the next iteration.
