from app.main import app
from tests.client import TestClient


PREFIX = "/"
client = TestClient(PREFIX, app)


class TestServerHealth:
    def test_get(self):
        response = client.get("/")
        assert response.ok
        assert response.json() == {'state': 'healthy'}
