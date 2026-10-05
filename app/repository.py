from app.models import Note, NoteCreate


class InMemoryNoteRepository:
    """Keeps notes in a Python dict.

    Data is lost when the app restarts. In Lab 4 this class gets replaced by one
    that talks to a database; the rest of the app only uses the methods below,
    so nothing else has to change.
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
