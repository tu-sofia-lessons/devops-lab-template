from app.main import app, get_classifier


class _FakeModel:
    path = "models/fake.joblib"

    def predict(self, text: str) -> str:
        return "shopping" if "buy" in text.lower() else "work"


def test_no_model_means_no_category(client):
    assert client.get("/model").json() == {"model": None}
    assert client.post("/notes", json={"title": "Buy milk"}).json()["category"] is None


def test_model_sets_category(client):
    app.dependency_overrides[get_classifier] = lambda: _FakeModel()
    assert client.get("/model").json() == {"model": "models/fake.joblib"}
    note = client.post("/notes", json={"title": "Buy milk"}).json()
    assert note["category"] == "shopping"
    assert client.get(f"/notes/{note['id']}").json()["category"] == "shopping"
