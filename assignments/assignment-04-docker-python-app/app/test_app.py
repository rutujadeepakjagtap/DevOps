"""
Automated Unit Tests for Assignment 04 Python Microservice
Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune
"""

import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test landing page renders successfully and contains student details."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Rutuja Deepak Jagtap" in response.data
    assert b"123B1B146" in response.data
    assert b"PCCOE Pune" in response.data

def test_health_endpoint(client):
    """Test healthcheck endpoint returns JSON status healthy."""
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "healthy"
    assert "container_id" in json_data

def test_api_info_endpoint(client):
    """Test JSON API returns correct assignment and student metadata."""
    response = client.get("/api/info")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["prn"] == "123B1B146"
    assert "assignment" in json_data
