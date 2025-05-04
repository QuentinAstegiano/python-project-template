import pytest
from fastapi.testclient import TestClient

from main.app import app
from main.service import HaikuService


class MockRemoteSource:
    def get_remote_haiku(self) -> str:
        return """
            lorem ipsum
            #####
            line 1
            line 2
            line 3
            #####
            lorem ipsum
        """


@pytest.fixture(scope="session")
def haiku_service():
    return HaikuService(MockRemoteSource())


@pytest.fixture(scope="session")
def test_client(haiku_service: HaikuService):
    app.haiku_service = haiku_service
    return TestClient(app)
