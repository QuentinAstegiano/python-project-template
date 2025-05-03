from fastapi.testclient import TestClient


class TestApp:
    def test_app_version(self, test_client: TestClient):
        response = test_client.get("/")
        assert response.status_code == 200
        assert response.json()["app-name"] == "python-project-template"
