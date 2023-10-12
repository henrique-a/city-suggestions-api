import pytest
from fastapi.testclient import TestClient

from routers import router


@pytest.fixture(scope="module")
def client():
    """
    Description: Pytest fixture for the FastAPI Test Client
    """
    with TestClient(router) as client:
        yield client
