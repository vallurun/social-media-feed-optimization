import json
from app import app

def test_feed():
    client = app.test_client()
    resp = client.get('/feed?user_id=test')
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert "posts" in data and isinstance(data["posts"], list)
