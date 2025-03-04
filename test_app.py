import pytest
import json
from app import app  # Import Flask app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_success(client):
    """Test /predict endpoint with valid input."""
    data = {        
        "Recency": 15,
        "Frequency": 5,
        "Monetary": 2000
    }

    response = client.post('/predict', data=json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    response_json = response.get_json()
    assert "prediction" in response_json

def test_predict_missing_data(client):
    """Test /predict with missing input data."""
    data = {}  # Empty payload

    response = client.post('/predict', data=json.dumps(data), content_type='application/json')

    assert response.status_code == 400
    response_json = response.get_json()
    assert "error" in response_json
