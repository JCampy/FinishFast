from tkinter import messagebox
import customtkinter as ctk
from sqlalchemy import func
from Database import Database, Users
import uuid


class UserModel:

    def __init__(self, db):
        
        self.db = db

    # create a new user and return its value
    @classmethod
    def create_user(cls, database, f_name, l_name, email, username, password):
        
        db = database

        if f_name is None or l_name is None or email is None or username is None or password is None:
            raise ValueError("Please fill out all forms")
        else:
            with db.get_session() as session:
                new_user = Users(
                        userID=str(uuid.uuid4()),
                        username=username,
                        first_name=f_name,
                        last_name=l_name,
                        email=email,
                        password=password,
                    )
                
                session.add(new_user)

                user_data = {
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'email': new_user.email,
                'username': new_user.username,
                'password': password
            }
            
            return user_data

    # check login password
    @staticmethod
    def check_pass(database, email):
        with database.get_session() as session:
            user = session.query(Users).filter_by(email=email).first()
            if user:
                return (user, user.password, user.userID)  # Return user details if found
            else:
                return (None, None, None)  # Return None values if no user is found

    # change profile photo        
    @staticmethod
    def update_profile_photo(database, curr_user, filename, filepath):
        with database.get_session() as session:
            user = session.query(Users).filter_by(userID=curr_user).first()
            user.filename = filename
            user.filepath = filepath
            session.commit()

    @staticmethod
    def get_profile_photo_path(database, curr_user):
        with database.get_session() as session:
            user = session.query(Users).filter_by(userID=curr_user).first()
            if user:
                return user.filepath

            return user.filepath
        
    @staticmethod
    def does_email_exist(database, email):
        with database.get_session() as session:
            user = session.query(Users).filter_by(email=email).first()
            if user:
                messagebox.showerror(f'Error', 'Email already exist')
                return True
            else:
                return False

    @staticmethod
    def does_username_exist(database, username):
        normalized_username = username.strip().lower()  # Normalize to lowercase for comparison
        with database.get_session() as session:
            user = session.query(Users).filter(func.lower(Users.username) == normalized_username).first()
            if user:
                messagebox.showerror('Error', 'Username already exists')
                return True
            else:
                return False