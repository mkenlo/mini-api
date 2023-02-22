import json


def test_route_entry(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Hello"


def test_route_compute(client):
    response = client.post("/compute", json={"number": 9})
    data = json.loads(response.text)
    assert response.status_code == 200
    assert data["square_root"] == 3.0
