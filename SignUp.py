import uuid
import customtkinter as ctk
from PIL import Image
from Testing import Testing
from Database import Database, Users
import bcrypt

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
        with self.db.get_session() as session:
            new_user = Users(
                userID=str(uuid.uuid4()),
                username=user_data['username'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                email=user_data['email'],
                password=user_data['password'],
            )
            session.add(new_user)
        
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

    # Handle the input of data from the user when the sign up button is clicked
    def handle_signup(self, app, window, first_name_entry, last_name_entry, email_entry, username_entry,
                     password_entry, confirm_password_entry):
        
        # Create the user_data dictionary when the button is clicked
        user_data = {
            'first_name': first_name_entry.get(),
            'last_name': last_name_entry.get(),
            'email': email_entry.get(),
            'username': username_entry.get(),
            'password': bcrypt.hashpw(password_entry.get().encode('utf-8'), bcrypt.gensalt()),
            'confirm_password': bcrypt.hashpw(confirm_password_entry.get().encode('utf-8'), bcrypt.gensalt())
        }

        # Debug: Print the user_data dictionary
        print(user_data)

        # Call the user_signup method
        self.user_signup(app, window, user_data)

        
        
        