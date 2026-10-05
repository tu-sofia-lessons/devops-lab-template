def test_list_notes_empty(client):
    response = client.get("/notes")
    assert response.status_code == 200
    assert response.json() == []


def test_create_note(client):
    response = client.post("/notes", json={"title": "First", "body": "Hello"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "title": "First", "body": "Hello"}


def test_create_note_without_body(client):
    response = client.post("/notes", json={"title": "Only a title"})
    assert response.status_code == 201
    assert response.json()["body"] == ""


def test_created_notes_are_listed(client):
    client.post("/notes", json={"title": "One"})
    client.post("/notes", json={"title": "Two"})
    titles = [note["title"] for note in client.get("/notes").json()]
    assert titles == ["One", "Two"]


def test_ids_increase(client):
    first = client.post("/notes", json={"title": "A"}).json()
    second = client.post("/notes", json={"title": "B"}).json()
    assert second["id"] == first["id"] + 1


def test_get_note(client):
    created = client.post("/notes", json={"title": "Find me"}).json()
    response = client.get(f"/notes/{created['id']}")
    assert response.status_code == 200
    assert response.json() == created


def test_get_missing_note_returns_404(client):
    response = client.get("/notes/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Note not found"}


def test_title_is_required(client):
    response = client.post("/notes", json={"body": "No title"})
    assert response.status_code == 422


def test_title_must_not_be_empty(client):
    response = client.post("/notes", json={"title": ""})
    assert response.status_code == 422


def test_title_max_100_chars(client):
    assert client.post("/notes", json={"title": "x" * 100}).status_code == 201
    assert client.post("/notes", json={"title": "x" * 101}).status_code == 422
