def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_version_default(client, monkeypatch):
    monkeypatch.delenv("APP_VERSION", raising=False)
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "0.1.0"}


def test_version_from_env(client, monkeypatch):
    monkeypatch.setenv("APP_VERSION", "1.2.3")
    response = client.get("/version")
    assert response.json() == {"version": "1.2.3"}
