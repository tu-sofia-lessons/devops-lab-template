import os
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException

from app.models import Note, NoteCreate
from app.repository import InMemoryNoteRepository

DEFAULT_VERSION = "0.1.0"

app = FastAPI(title="Notes API")

# In-memory storage for now. A database comes in Lab 4.
_repository = InMemoryNoteRepository()


def get_repository() -> InMemoryNoteRepository:
    return _repository


Repository = Annotated[InMemoryNoteRepository, Depends(get_repository)]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


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
