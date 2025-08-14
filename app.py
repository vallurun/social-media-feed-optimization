from flask import Flask, jsonify, request
from functools import lru_cache
import time

app = Flask(__name__)

# Mock posts: each post has (post_id, freshness, user_affinity, engagement_score)
POSTS = [
    {"id": 1, "freshness": 0.9, "affinity": 0.8, "engagement": 0.6, "text": "Hello from Meta-like feed!"},
    {"id": 2, "freshness": 0.5, "affinity": 0.6, "engagement": 0.9, "text": "Photos from your friends"},
    {"id": 3, "freshness": 0.7, "affinity": 0.9, "engagement": 0.7, "text": "Trending story"},
]

def rank_score(p):
    # Simple tunable scoring function
    return 0.5 * p["freshness"] + 0.3 * p["affinity"] + 0.2 * p["engagement"]

@lru_cache(maxsize=128)
def cached_feed(user_id):
    # Simulate heavier computation
    time.sleep(0.1)
    sorted_posts = sorted(POSTS, key=rank_score, reverse=True)
    return tuple([p["id"] for p in sorted_posts])

@app.route("/feed")
def feed():
    user_id = request.args.get("user_id", "guest")
    post_ids = cached_feed(user_id)
    ranked = [next(p for p in POSTS if p["id"] == pid) for pid in post_ids]
    return jsonify({"user_id": user_id, "posts": ranked})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
