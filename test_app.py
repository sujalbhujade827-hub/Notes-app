import pytest
from app import app  # Imports your Flask app from app.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test that the index/home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200