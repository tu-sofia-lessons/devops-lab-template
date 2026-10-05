from app.main import app, get_repository


def test_ready_with_memory_storage(client):
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}


class _Unreachable:
    def ping(self) -> bool:
        return False


def test_ready_is_503_when_storage_unreachable(client):
    app.dependency_overrides[get_repository] = lambda: _Unreachable()
    response = client.get("/ready")
    assert response.status_code == 503
    assert response.json() == {"status": "storage unavailable"}
