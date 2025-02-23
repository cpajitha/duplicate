import pytest
from fastapi.testclient import TestClient
from backend import app  # Import your FastAPI app

# Create a test client
client = TestClient(app)

def test_add():
    response = client.get("/add?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 15}

def test_subtract():
    response = client.get("/subtract?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_multiply():
    response = client.get("/multiply?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 50}

def test_divide():
    response = client.get("/divide?a=10&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_divide_by_zero():
    response = client.get("/divide?a=10&b=0")
    assert response.status_code == 200
    assert response.json() == {"error": "Division by zero is not allowed"}
