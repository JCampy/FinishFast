from datetime import datetime
from Database import Database, Notes
import uuid

class NotesModel:
    def __init__(self, db: Database):

        self.db = db

    @classmethod
    def create_note(cls, database, owner, title, text):
        
        db = database
        if owner is None and text is None:
            raise ValueError("Please enter a valid text")
        else:
            with db.get_session() as session:
                new_note = Notes(
                    noteID = str(uuid.uuid4()),
                    userID = owner,
                    note_name = title,
                    note_text = text,
                    date_created = datetime.now()
                )
                session.add(new_note)
                print(f'New Note added{title}')

                note_data = {
                    "noteID" : new_note.noteID,
                    "userID" : new_note.userID,
                    "note_name" : new_note.note_name,
                    "note_text" : new_note.note_text,
                    "date_created" : new_note.date_created
                }
                return note_data

     # get all notes for current user 
    @staticmethod       
    def get_notes(database, user_id):

        with database.get_session() as session:
            notes = session.query(Notes).filter_by(userID=user_id).all()
        return notes
    
    # return the number of current notes 
    @staticmethod
    def get_num_of_notes(database, user_id):

        with database.get_session() as session:
            num_notes = session.query(Notes).filter_by(userID=user_id).all()
        return len(num_notes)
    
    # delete note
    @staticmethod
    def delete_note(database, user_id, note_id):

        with database.get_session() as session:
            note = session.query(Notes).filter_by(userID=user_id, noteID=note_id).first()
            session.delete(note)

    # change note name and text
    @staticmethod
    def update_task(database, user_id, note_id, title, text):
        
        with database.get_session() as session:
            note = session.query(Notes).filter_by(userID=user_id, noteID=note_id).first()
            note.note_name = title
            note.note_text = text