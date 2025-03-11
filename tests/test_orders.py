import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app import app

client = TestClient(app)
BASE_URL = "http://localhost:3000/api"  # Base API URL


def test_create_order():
    """Test creating an order."""
    order_payload = {
        "order_id": 1,
        "user_id": 101,
        "item_ids": [201, 202],
        "total_amount": 99.99
    }

    with patch("routes.orders.create_order_service", return_value={"message": "Order received", "order_id": 1}):
        response = client.post(f"{BASE_URL}/order", json=order_payload)

    assert response.status_code == 200
    assert response.json() == {"message": "Order received", "order_id": 1}


def test_get_order_status():
    """Test fetching order status."""
    with patch("routes.orders.get_order_status_service", return_value={"order_id": 1, "status": "Pending"}):
        response = client.get(f"{BASE_URL}/order/1")

    assert response.status_code == 200
    assert response.json() == {"order_id": 1, "status": "Pending"}


def test_get_order_status_not_found():
    """Test fetching a non-existent order should return 404."""
    with patch("routes.orders.get_order_status_service", return_value=None):
        response = client.get(f"{BASE_URL}/order/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Order not found"


def test_get_metrics():
    """Test fetching order metrics."""
    mock_metrics = {
        "total_orders": 10,
        "orders_pending": 3,
        "orders_processing": 2,
        "orders_completed": 5,
        "average_processing_time": 2.5
    }

    with patch("routes.metrics.get_metrics_service", return_value=mock_metrics):
        response = client.get(f"{BASE_URL}/metrics")

    assert response.status_code == 200
    assert response.json() == mock_metrics
