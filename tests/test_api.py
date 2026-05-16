import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app


def test_health():
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["ok"] is True


def test_create_and_list():
    client = app.test_client()
    res = client.post("/todos", json={"title": "demo"})
    assert res.status_code == 201
    body = res.get_json()
    assert body["title"] == "demo"
    listed = client.get("/todos").get_json()
    assert any(t["id"] == body["id"] for t in listed)

