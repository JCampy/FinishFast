from datetime import datetime
from Database import Database
import uuid

class NotesModel:
    def __init__(self, db: Database):
        self.db = db

    def create(self, title: str, content: str) -> None:
        note_id = str(uuid.uuid4())
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db.execute(
            "INSERT INTO notes (id, title, content, created_at) VALUES (?, ?, ?, ?)",
            (note_id, title, content, created_at)
        )

    def get_all(self) -> list:
        return self.db.query("SELECT * FROM notes")