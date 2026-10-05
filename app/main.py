import os
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Response

from app.models import Note, NoteCreate
from app.repository import InMemoryNoteRepository, PostgresNoteRepository

DEFAULT_VERSION = "0.1.0"

app = FastAPI(title="Notes API")

# With DATABASE_URL the notes live in PostgreSQL (Lab 4); without it, in memory.
NoteRepository = InMemoryNoteRepository | PostgresNoteRepository


def make_repository() -> NoteRepository:
    dsn = os.getenv("DATABASE_URL")
    return PostgresNoteRepository(dsn) if dsn else InMemoryNoteRepository()


_repository = make_repository()


def get_repository() -> NoteRepository:
    return _repository


Repository = Annotated[NoteRepository, Depends(get_repository)]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/ready")
def ready(repo: Repository, response: Response) -> dict[str, str]:
    """Is the app ready to serve? Checks that the storage can be reached."""
    if repo.ping():
        return {"status": "ready"}
    response.status_code = 503
    return {"status": "storage unavailable"}


@app.get("/version")
def version() -> dict[str, str]:
    return {"version": os.getenv("APP_VERSION", DEFAULT_VERSION)}


@app.get("/notes")
def list_notes(repo: Repository) -> list[Note]:
    return repo.list()


@app.post("/notes", status_code=201)
def create_note(data: NoteCreate, repo: Repository) -> Note:
    return repo.add(data)


@app.get("/notes/{note_id}")
def get_note(note_id: int, repo: Repository) -> Note:
    note = repo.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note
