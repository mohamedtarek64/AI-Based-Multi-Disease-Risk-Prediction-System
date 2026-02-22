import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "Mega AI Service Online" in response.json()["message"]

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_diabetes_prediction_structure():
    payload = {
        "age": 45,
        "gender": "male",
        "bmi": 28.5,
        "glucose": 150,
        "blood_pressure": 85,
        "insulin": 100,
        "family_history": True,
        "physical_activity": "medium",
        "smoking": "never"
    }
    response = client.post("/predict/diabetes", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "risk_score" in data
    assert "risk_level" in data
