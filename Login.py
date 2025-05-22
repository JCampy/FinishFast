import bcrypt
import customtkinter as ctk
from PIL import Image
from Testing import Testing
from SignUp import SignUp
from Database import Users
from UserModel import UserModel
from tkinter import messagebox
import os

class Login:

    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')

    def __init__(self, signup, database):
        self.db = database
        self.signup = signup
    
    # Call the login window method in ProjectManager.py when the login button is clicked
    def login_success(self, app, login, password):
        user = UserModel.check_pass(self.db, login.get())
        current_user = user[2]
        if user[0]:
            if bcrypt.checkpw(password.get().encode('utf-8'), user[1]):
                print('Correct Password')
                app.create_main_window(current_user)
            else:
                messagebox.showerror("Error", "Incorrect Password")
        else:
            messagebox.showerror("Error", "Incorrect email")

    
    def login_display(self, window, app): 
        
        # image login  ** Figure out how to resize image when screen resizes **
        image_path = os.path.join(os.path.dirname(__file__), "images", "gradient.png")
        image = Image.open(image_path)
        ctk_image =ctk.CTkImage(light_image=image, size=(200,450))
        image_label = ctk.CTkLabel(window, image=ctk_image, text='')
        image_label.grid(row=0, column=0, sticky='nws', rowspan=5, columnspan=2)

        # email
        login_label = ctk.CTkLabel(window, text='Email:', text_color=self.TEXT_COLOR)
        login_label.grid(row=1, column=2, sticky='sw', columnspan=3, padx=30)

        # email entry
        login = ctk.CTkEntry(window, placeholder_text="Enter your email.",
                            text_color='black', border_color=(self.SECONDARY_WHITE, self.THIRD_GRAY),
                            bg_color='transparent', corner_radius=20,
                            fg_color='#cccbc8')
        login.grid(row=2, column=2, columnspan=3, sticky='new', padx=30, pady=1)

        # password
        password_label = ctk.CTkLabel(window, text='Password:', text_color=self.TEXT_COLOR)
        password_label.grid(row=2, column=2, sticky='w', columnspan=3, padx=30, pady=5)

        # password entry
        password = ctk.CTkEntry(window, placeholder_text="Enter your password.",
                                bg_color='transparent', border_color=(self.SECONDARY_WHITE, self.THIRD_GRAY), 
                                corner_radius=20, text_color='black', show= '*',
                                fg_color='#cccbc8')
        password.grid(row=2, column=2, sticky='sew', columnspan=3, padx=30, pady=5)

        # login button
        login_button = ctk.CTkButton(window, text='Log In', fg_color=self.MAIN_COLOR,
                                    bg_color='transparent', corner_radius=20,
                                    text_color=self.TEXT_COLOR, command=lambda: self.login_success(app, login, password))
        login_button.grid(row=3, column=2, columnspan=3, sticky='n')

        # forgot button
        signup_button = ctk.CTkButton(window, text='Sign up',
                                     fg_color=self.MAIN_COLOR, bg_color='transparent', 
                                     corner_radius=20, text_color=self.TEXT_COLOR,
                                     command=lambda: self.signup.signUpWindow(app))
        signup_button.grid(row=3, column=2, columnspan=3)
