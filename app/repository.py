import psycopg

from app.models import Note, NoteCreate


class InMemoryNoteRepository:
    """Keeps notes in a Python dict. Data is lost when the app restarts.

    Used when DATABASE_URL is not set (local runs and tests).
    """

    def __init__(self) -> None:
        self._notes: dict[int, Note] = {}
        self._next_id = 1

    def list(self) -> list[Note]:
        return list(self._notes.values())

    def get(self, note_id: int) -> Note | None:
        return self._notes.get(note_id)

    def add(self, data: NoteCreate) -> Note:
        note = Note(id=self._next_id, title=data.title, body=data.body)
        self._notes[note.id] = note
        self._next_id += 1
        return note

    def ping(self) -> bool:
        return True


class PostgresNoteRepository:
    """Keeps notes in PostgreSQL (Lab 4 and later).

    Used when DATABASE_URL is set, e.g. postgresql://notes:secret@db:5432/notes.
    It connects on every call, so the app starts even if the database is not up yet;
    /ready tells whether the database can be reached.
    """

    def __init__(self, dsn: str) -> None:
        self._dsn = dsn
        self._table_ready = False

    def _connect(self) -> psycopg.Connection:
        conn = psycopg.connect(self._dsn, connect_timeout=3)
        if not self._table_ready:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS notes ("
                " id SERIAL PRIMARY KEY,"
                " title VARCHAR(100) NOT NULL,"
                " body TEXT NOT NULL DEFAULT '')"
            )
            conn.commit()
            self._table_ready = True
        return conn

    def list(self) -> list[Note]:
        with self._connect() as conn:
            rows = conn.execute("SELECT id, title, body FROM notes ORDER BY id").fetchall()
        return [Note(id=r[0], title=r[1], body=r[2]) for r in rows]

    def get(self, note_id: int) -> Note | None:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT id, title, body FROM notes WHERE id = %s", (note_id,)
            ).fetchone()
        return Note(id=row[0], title=row[1], body=row[2]) if row else None

    def add(self, data: NoteCreate) -> Note:
        with self._connect() as conn:
            row = conn.execute(
                "INSERT INTO notes (title, body) VALUES (%s, %s) RETURNING id",
                (data.title, data.body),
            ).fetchone()
        return Note(id=row[0], title=data.title, body=data.body)

    def ping(self) -> bool:
        try:
            with self._connect() as conn:
                conn.execute("SELECT 1")
            return True
        except psycopg.Error:
            return False
