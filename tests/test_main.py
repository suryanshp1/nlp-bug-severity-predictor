from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Bug Severity Predictor API"}

def test_predict_severity():
    response = client.post("/predict", json={"description": "Application crashes when uploading large files"})
    assert response.status_code == 200
    assert "severity" in response.json()