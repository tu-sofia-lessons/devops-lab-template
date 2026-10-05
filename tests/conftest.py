import pytest
from fastapi.testclient import TestClient

from app.main import app, get_repository
from app.repository import InMemoryNoteRepository


@pytest.fixture
def client():
    """A test client with a fresh, empty repository for every test."""
    repo = InMemoryNoteRepository()
    app.dependency_overrides[get_repository] = lambda: repo
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
