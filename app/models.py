from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    """Data the client sends when creating a note."""

    title: str = Field(min_length=1, max_length=100)
    body: str = ""


class Note(BaseModel):
    """A stored note, as returned by the API."""

    id: int
    title: str
    body: str
