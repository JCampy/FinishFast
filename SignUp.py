import re
from tkinter import messagebox
import uuid
import customtkinter as ctk
from PIL import Image
from Testing import Testing
from Database import Database, Users
import bcrypt
from UserModel import UserModel

class SignUp:

    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')

    def __init__(self, database):
        self.db = database
        
    # Call the sign up window method in ProjectManager.py when the sign up button is clicked
    def signUpWindow(self, app):
        print('Sign up button!')
        app.sign_up_window()
    
    def user_signup(self, app, window, user_data):
        new_user = UserModel.create_user(self.db, user_data['first_name'], user_data['last_name'],
                                         user_data['email'], user_data['username'],
                                         user_data['password'])
        app.return_login(window)

        

    def signUpDisplay(self, window, app): 
        
        # Title
        signup_label = ctk.CTkLabel(window, text='Create Your Account', text_color=self.TEXT_COLOR, 
                                    bg_color='transparent', font=('Roboto', 20))
        signup_label.grid(row=0, column=0, sticky='ew', columnspan=5, padx=10, pady=10)

        #First Name
        first_name_entry = ctk.CTkEntry(window, placeholder_text="First Name",
                            text_color='black', border_color=(self.SECONDARY_WHITE, self.THIRD_GRAY),
                            bg_color='transparent', corner_radius=20,
                            fg_color='#cccbc8', height=40)
        first_name_entry.grid(row=1, column=0, columnspan=2, sticky='ew', padx=(25, 0))

        #Last Name
        last_name_entry = ctk.CTkEntry(window, placeholder_text="Last Name",
                            text_color='black', border_color=(self.SECONDARY_WHITE, self.THIRD_GRAY),
                            bg_color='transparent', corner_radius=20,
                            fg_color='#cccbc8', height=40)
        last_name_entry.grid(row=1, column=3, columnspan=2, sticky='ew', padx=(0, 25))

        #Email
        email_entry = ctk.CTkEntry(window, placeholder_text="Email",
                            text_color='black', border_color=(self.SECONDARY_WHITE, self.THIRD_GRAY),
                            bg_color='transparent', corner_radius=20,
                            fg_color='#cccbc8', height=40)
        email_entry.grid(row=2, column=0, columnspan=5, sticky='new', padx=25)
        
        #Username
        username_entry = ctk.CTkEntry(window, placeholder_text="Username",
                            text_color='black', border_color=(self.SECONDARY_WHITE, self.THIRD_GRAY),
                            bg_color='transparent', corner_radius=20,
                            fg_color='#cccbc8', height=40)
        username_entry.grid(row=3, column=0, columnspan=5, sticky='new', padx=25)

        #Password
        password_entry = ctk.CTkEntry(window, placeholder_text="Password",
                            text_color='black', border_color=(self.SECONDARY_WHITE, self.THIRD_GRAY),
                            bg_color='transparent', corner_radius=20,
                            fg_color='#cccbc8', show='*', height=40)
        password_entry.grid(row=4, column=0, columnspan=2, sticky='new', padx=(25, 0))

        #Confirm Password
        confirm_password_entry = ctk.CTkEntry(window, placeholder_text="Confirm Password",
                            text_color='black', border_color=(self.SECONDARY_WHITE, self.THIRD_GRAY),
                            bg_color='transparent', corner_radius=20,
                            fg_color='#cccbc8', show='*', height=40)
        confirm_password_entry.grid(row=4, column=4, columnspan=2, sticky='new', padx=(0, 25))

        #Sign Up Button
        signup_button = ctk.CTkButton(window, text='Sign Up', bg_color='transparent', fg_color=self.MAIN_COLOR, corner_radius=20,
                                    command=lambda: self.handle_signup(app, window, first_name_entry, last_name_entry, email_entry, username_entry,
                                    password_entry, confirm_password_entry), height=40)
        signup_button.grid(row=5, column=0, columnspan=5, sticky='ew', padx=25, pady=(0, 15))

    def passwords_match(self, password_entry, confirm_password_entry):
        # Get the values from the password fields
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        # Check if the passwords match
        if password == confirm_password:
            return True
        else:
            messagebox.showerror("Error", "Passwords do not match. Please try again.")
            return False
        
    def is_valid_email(self, email_entry):
        # Get the email value from the entry field
        email = email_entry.get()

        # Regular expression for validating an email address
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Check if the email matches the regex
        if re.match(email_regex, email):
            return True
        else:
            messagebox.showerror("Error", "Invalid email address. Please enter a valid email.")
            return False
        
    # Handle the input of data from the user when the sign up button is clicked
    def handle_signup(self, app, window, first_name_entry, last_name_entry, email_entry, username_entry,
                     password_entry, confirm_password_entry):
        
        # Check if passwords match
        if not self.passwords_match(password_entry, confirm_password_entry):
            return  # Stop the signup process if passwords don't match
        
        if not self.is_valid_email(email_entry):
            return # If email is invalid stop the signup process
        
        if UserModel.does_email_exist(self.db, email_entry.get()):
            return # Checking if email already exist
        
        if UserModel.does_username_exist(self.db, username_entry.get()):
            return # checking if user name already exist

        # Create the user_data dictionary when the button is clicked
        user_data = {
            'first_name': first_name_entry.get().strip(),
            'last_name': last_name_entry.get().strip(),
            'email': email_entry.get().strip().lower(),
            'username': username_entry.get(),
            'password': bcrypt.hashpw(password_entry.get().encode('utf-8'), bcrypt.gensalt())
        }

        # Debug: Print the user_data dictionary
        print(user_data)

        # Call the user_signup method
        self.user_signup(app, window, user_data)

        
        
        