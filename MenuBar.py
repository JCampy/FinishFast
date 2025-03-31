import customtkinter as ctk
from CTkMenuBar import *

class MenuBar():

    def __init__(self, frame):
        self.app = frame
        self.menu = CTkTitleMenu(master=frame, x_offset=100)

    def add_menu_bar(self):
        settings_button = self.menu.add_cascade('Settings')
        account_button = self.menu.add_cascade('Account')
        about_button = self.menu.add_cascade('About')
    
    

        