from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_create_order():
    response = client.post("/order/", json={
        "user_id": 1,
        "item_ids": [101, 102],
        "total_amount": 49.99
    })
    assert response.status_code == 200
    assert response.json()["status"] == "Pending"
