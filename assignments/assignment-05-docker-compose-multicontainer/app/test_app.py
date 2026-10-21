"""
Automated Unit Tests for Assignment 05 Multi-Container Flask Application
Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune
"""

import pytest
from app import app, init_db

@pytest.fixture
def client():
    app.config["TESTING"] = True
    init_db()
    with app.test_client() as client:
        yield client

def test_index_route(client):
    """Test dashboard renders with student details and visit counter."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Rutuja Deepak Jagtap" in response.data
    assert b"123B1B146" in response.data
    assert b"Persistent Visitor Counter" in response.data

def test_health_endpoint(client):
    """Test health endpoint returns status healthy."""
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "healthy"

def test_db_endpoint(client):
    """Test db health check endpoint returns connection status."""
    response = client.get("/db")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "connected"
    assert "total_visits_logged" in json_data
