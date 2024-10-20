from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Bug Severity Predictor API"}

def test_predict_severity():
    response = client.post("/predict", json={"description": "Buffer overflow in NFS mountd gives root access to remote attackers, mostly in Linux systems."})
    assert response.status_code == 200
    assert "severity" in response.json()
    assert response.json().get("severity") == "HIGH"