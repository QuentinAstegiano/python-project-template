import pytest
from fastapi.testclient import TestClient

from main.app import app
from main.service import ComputeService


@pytest.fixture(scope="session")
def compute_service():
    return ComputeService()


@pytest.fixture(scope="session")
def test_client(compute_service: ComputeService):
    app.compute_service = compute_service
    return TestClient(app)
