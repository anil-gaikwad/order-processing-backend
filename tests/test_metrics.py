import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app import app

client = TestClient(app)
BASE_URL = "http://localhost:3000/api"  # Base API URL


def test_get_metrics():
    """Test fetching order metrics with a mocked response."""
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
