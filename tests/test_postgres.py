"""Runs only when TEST_DATABASE_URL points to a PostgreSQL database (Lab 4)."""

import os

import pytest

from app.models import NoteCreate
from app.repository import PostgresNoteRepository

DSN = os.getenv("TEST_DATABASE_URL")
pytestmark = pytest.mark.skipif(not DSN, reason="TEST_DATABASE_URL is not set")


def test_notes_are_stored_in_postgres():
    repo = PostgresNoteRepository(DSN)
    assert repo.ping()
    note = repo.add(NoteCreate(title="from postgres", body="b"))
    assert repo.get(note.id) == note
    assert note in repo.list()
    assert repo.get(999999) is None


def test_category_is_stored():
    repo = PostgresNoteRepository(DSN)
    note = repo.add(NoteCreate(title="buy milk"), category="shopping")
    assert repo.get(note.id).category == "shopping"


def test_ping_is_false_when_database_is_unreachable():
    assert not PostgresNoteRepository("postgresql://x:y@127.0.0.1:1/none").ping()
