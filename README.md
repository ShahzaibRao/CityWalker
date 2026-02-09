# CityWalker
A gamified walking application that tracks users' walking routes and allows them to "capture" regions of their city. Compete with others, earn badges, and climb the leaderboards!

## Product Vision
CityWalker turns daily walking into a citywide game. Users claim neighborhoods by walking them, compete in weekly leagues, and build community through shared goals and challenges.

## Core Experience
1. **Track & Capture**: The app records walking routes and converts distance traveled into “capture energy.” Users can claim tiles/regions on a city map by walking within those boundaries.
2. **Compete & Climb**: Users earn ranks, badges, and seasonal points. Local leaderboards highlight daily, weekly, and all-time walkers.
3. **Community & Motivation**: Teams, challenges, and social feeds encourage engagement and friendly competition.

## Key Features
### 1. Map & Capture System
- **Grid/Region Map**: City map divided into capturable tiles (e.g., 200–500m squares).
- **Capture Meter**: Walking inside a tile fills a capture meter; first to 100% claims it.
- **Decay & Defense**: Captures slowly decay unless revisited, keeping gameplay active.
- **Neutral vs. Owned Regions**: Visual overlays show neutral, friendly, and rival regions.

### 2. Walking Tracker
- **Live Route Tracking**: GPS-based tracking with pause/resume.
- **Distance & Pace Stats**: Metrics displayed in real time.
- **Heatmap History**: Users view their walked routes across the city.

### 3. Progression System
- **Ranks**: Bronze → Silver → Gold → Platinum → Diamond.
- **Badges**: Milestones (e.g., "10km Streak", "Neighborhood Conqueror").
- **Season Points**: Earned from walking and capturing regions.

### 4. Leaderboards
- **Citywide Rankings**: Top walkers and top teams.
- **Neighborhood Rankings**: Competition based on captured territory.
- **Friends Leaderboard**: Compare with personal network.

### 5. Social & Community
- **Teams**: Join groups to co-capture areas.
- **Challenges**: Daily/weekly walking goals.
- **Activity Feed**: Show recent captures, milestones, and team wins.

## User Flow
1. **Onboarding** → Choose city + permissions → Tutorial on capturing.
2. **Home Dashboard** → See daily goal + active challenge.
3. **Start Walk** → Track route + capture nearby regions.
4. **Post-Walk Summary** → Distance, captures, points earned.
5. **Community** → View leaderboards + team updates.

## UI/UX Concept
### Primary Screens
- **Home**: Daily goal, active challenge, quick-start walk.
- **Map**: Interactive capturable map with overlays.
- **Walk Mode**: Live stats (distance, pace, capture progress).
- **Leaderboards**: Filterable by time + category.
- **Profile**: Badges, rank, stats, capture history.

### Design Style
- **Color Palette**: Vibrant map colors (greens, blues, oranges).
- **Typography**: Clean sans-serif for clarity.
- **Gamification**: Subtle animations on capture + badge unlocks.

## Motivation & Retention
- **Streaks**: Maintain daily walking streaks.
- **Seasonal Events**: Limited-time city challenges.
- **Rewards**: Unlock cosmetics (avatars, map skins).

## Suggested Tech Stack
- **Mobile**: React Native / Flutter
- **Backend**: Node.js + PostgreSQL
- **Maps**: Mapbox / Google Maps API
- **Gamification Engine**: Custom rules system for captures

## Suggested 3-Tier Architecture
### 1. Frontend (Mobile App)
- **Platform**: Flutter (cross-platform) or React Native.
- **Core Screens**: Map with routes + captured areas, profile (badges, ranks, stats), leaderboards, achievements.
- **Auth**: Login/Register with JWT-based sessions.

### 2. Backend (API)
- **Platform**: FastAPI.
- **Responsibilities**:
  - User authentication with JWT.
  - Store walking routes (GeoJSON/GPS coordinates).
  - Calculate captured regions based on distance and spatial overlap.
  - Manage badges, points, and rank progression.
  - Leaderboard endpoints (citywide + neighborhood).
  - Optional AI suggestions for motivation and challenges.

### 3. Database
- **Platform**: PostgreSQL + PostGIS.
- **Why PostGIS**: Enables spatial queries for distance, area, and polygon operations.
- **Core Tables**:
  - `users` → email, password hash, rank, points.
  - `routes` → user_id, start_time, end_time, path (GeoJSON).
  - `captured_areas` → user_id, polygon, date_captured.
  - `badges` → badge_name, criteria.
  - `leaderboards` → computed from points/territory.

## Optional Gamification Features
- Daily/weekly walking challenges.
- City-wide events (e.g., everyone capturing a region together).
- Social feed to share captures or photos.
- Rewards for consecutive walking streaks.

## Step to Start Quickly
1. Start the backend with FastAPI.
2. Create `users`, `routes`, and `captured_areas` tables.
3. Implement JWT auth.
4. Add endpoint to save a route → calculate captured area.
5. Add leaderboard endpoints.
6. Test the API via Postman or curl.
7. Build a minimal frontend: login, map, captured areas.
8. Connect the app to the backend API.

## Backend Scaffold (Initial Build)
An initial FastAPI scaffold lives in `backend/` with sample endpoints to validate contracts for routes, leaderboards, and challenge suggestions. Use it as a starting point before wiring up PostGIS and real capture logic.

---

This concept provides a foundation for building a gamified walking app that promotes fitness, friendly competition, and community.
