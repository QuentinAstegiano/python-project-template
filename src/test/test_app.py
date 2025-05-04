from fastapi.testclient import TestClient


class TestApp:
    def test_app_version(self, test_client: TestClient):
        response = test_client.get("/")
        assert response.status_code == 200
        assert response.json()["app-name"] == "python-project-template"

    def test_get_new_haiku(self, test_client: TestClient):
        response = test_client.get("/haiku")
        assert response.status_code == 200

        poem = response.json()["poem"]
        assert len(poem) == 3
        for line in poem:
            assert len(poem) > 0
