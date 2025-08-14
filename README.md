# Social Media Feed Optimization (Flask)

A minimal **personalized content ranking API** inspired by a social media **News Feed**.  
Built with **Python + Flask**, featuring **caching**, **tunable ranking weights**, and a clean **/feed** endpoint you can call from a client or script.

This project demonstrates **algorithm design**, **API development**, **performance optimization** (memoization/cache), and **unit testing** for production-ready services.

---

## 🚀 Features
- **Ranking function** that combines freshness, user affinity, and engagement.
- **Caching** via `functools.lru_cache` to cut repeated ranking costs.
- **Tunable weights** so you can quickly experiment with scoring strategies.
- **Lightweight API** with health check for easy orchestration.
- **Unit tests** using Flask’s test client.

---

## 🧠 Ranking Overview

Each post has:
- `freshness` — how recent it is (0 to 1)
- `affinity` — how relevant it is to the user (0 to 1)
- `engagement` — how engaging the post is broadly (0 to 1)

**Score function:**
```python
score = 0.5 * freshness + 0.3 * affinity + 0.2 * engagement
You can tweak the weights in app.py to fit different objectives (e.g., more freshness vs. more affinity).

🧱 Architecture
bash
social-media-feed-optimization/
├── app.py               # Flask app with /feed and /health
├── requirements.txt     # Python deps
├── tests/
│   └── test_app.py      # Basic unit test for /feed
└── README.md            # This file
/feed: Ranks and returns posts for a user_id.

cached_feed(user_id): Memoized function to avoid recomputing for the same user quickly.

/health: Simple liveness check.

⚙️ Setup & Run
1) Create and activate a virtual environment
bash
python3 -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
2) Install dependencies
bash
pip install -r requirements.txt
3) Start the server
bash
python app.py
Server: http://localhost:5000

Feed endpoint: http://localhost:5000/feed?user_id=123

Health check: http://localhost:5000/health

🔌 API
GET /feed?user_id=<id>
Returns ranked posts for a user.

Request

bash
GET /feed?user_id=123
Response (example)

json
{
  "user_id": "123",
  "posts": [
    {"id": 1, "freshness": 0.9, "affinity": 0.8, "engagement": 0.6, "text": "Hello from Meta-like feed!"},
    {"id": 3, "freshness": 0.7, "affinity": 0.9, "engagement": 0.7, "text": "Trending story"},
    {"id": 2, "freshness": 0.5, "affinity": 0.6, "engagement": 0.9, "text": "Photos from your friends"}
  ]
}
cURL

bash
curl "http://localhost:5000/feed?user_id=test"
GET /health
Simple liveness probe.

Response

json
{"status": "ok"}
🧪 Testing
Run tests with:

bash
python -m pytest -q
# or:
pytest -q
(Uses Flask’s test client to verify /feed returns the expected structure.)

🏎️ Performance Notes
Caching: @lru_cache(maxsize=128) memoizes the post ranking per user_id.

Great for repeated requests (same user, short time window).

Complexity: Current approach sorts in-memory mock posts (O(n log n)).

Scaling ideas:

Replace in-memory posts with a DB (e.g., Postgres) and apply indexed queries.

Add Redis for request/user-level caching across processes.

Batch scoring or precompute partial scores offline.

🔧 Configuration & Tuning
Open app.py and adjust:

def rank_score(p):
    return 0.5 * p["freshness"] + 0.3 * p["affinity"] + 0.2 * p["engagement"]
Increase the freshness weight for more “breaking news” feel.

Increase the affinity weight for more personalization.

You can also expand the POSTS list with real fields (e.g., created_at, author_id) and compute freshness/affinity/engagement dynamically.

☁️ Deployment Tips
Gunicorn + gevent (or uvicorn via ASGI bridge) for concurrency.

Reverse proxy with Nginx.

Environment variables for config:

PORT (default 5000)

Connection strings for databases or Redis if you add them.

Containerization: Add a Dockerfile for easy deploys:

dockerfile

FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

📌 Roadmap
 Replace mock data with a real database (PostgreSQL)

 Add user profiles and compute real affinity

 A/B test different weight configurations

 Introduce Redis caching layer

 Add pagination and time-based windows

 Add auth & rate limiting

📄 License
MIT

yaml

---

