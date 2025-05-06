from contextlib import contextmanager
from sqlite3 import Binary
from sqlalchemy import create_engine, Column, LargeBinary, Boolean, Integer, String, event, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path


# setting up database file creation 
project_folder = Path(__file__).parent 
db_path = project_folder / 'ffdb.db'
DATABASE_URL = f"sqlite:///{db_path}"

# Base for all tables
Base = declarative_base()

# creating tables
class Users(Base):
        __tablename__ = 'users'
        userID = Column(String, primary_key=True)
        username = Column(String, unique=True, nullable=False)
        first_name = Column(String, nullable=False)
        last_name = Column(String, nullable=False)
        email = Column(String, unique=True, nullable=False)
        password = Column(LargeBinary(64), nullable=False)
        filename = Column(String, nullable=True)
        filepath= Column(String, nullable=True)
        notes = relationship('Notes', back_populates='users') 
        projects = relationship('Projects', back_populates='users')
        

class Projects(Base):
    __tablename__ = 'projects'
    projectID = Column(String, primary_key=True)
    userID = Column(String, ForeignKey('users.userID'))
    project_name = Column(String, nullable=False)
    date_created = Column(String, nullable=False)
    project_color = Column(String, nullable=False)
    users = relationship('Users', back_populates='projects')
    tasks = relationship('Tasks', back_populates='projects')

class Tasks(Base):
    __tablename__ = 'tasks'
    taskID = Column(String, primary_key=True)
    task_name = Column(String, nullable=False)
    task_data = Column(String, nullable=False)
    completed = Column(Boolean, nullable=False)
    priority = Column(Integer, nullable=False)
    difficulty = Column(Integer, nullable=False)
    date_created = Column(String, nullable=False)
    date_completed = Column(String)
    task_color = Column(String, nullable=False)
    projectID = Column(String, ForeignKey('projects.projectID'))
    projects = relationship('Projects', back_populates='tasks')

class Notes(Base):
    __tablename__ = 'notes'
    noteID = Column(String, primary_key=True)
    userID = Column(String, ForeignKey('users.userID'))
    note_name = Column(String, nullable=False)
    note_text = Column(String)
    date_created = Column(String, nullable=False)
    users = relationship('Users', back_populates ='notes' )

class Database:

    def __init__(self, database_url=DATABASE_URL):
        self.engine = create_engine(database_url, connect_args={"check_same_thread": False})
        self.Session = sessionmaker(bind=self.engine)
        self.initialize_db()

    def initialize_db(self):
        
        # Enabling foreign keys for sqlite
        @event.listens_for(self.engine, "connect")
        def set_sqlite_pragma(dbapi_connection, connection_record):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()
            print('Foreign Keys Enabled!')
        
        # Create all tables
        Base.metadata.create_all(self.engine)
        print(f'Database will be created at: {db_path}')

    @contextmanager
    def get_session(self):
        session = self.Session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
        
    

