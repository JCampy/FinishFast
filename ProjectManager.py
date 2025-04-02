import customtkinter as ctk
import random
from Testing import Testing
from Login import Login
from Title import Title
from MenuBar import MenuBar
from MainView import MainView
from Database import Database
from SignUp import SignUp
from Methods import Methods

class ProjectManager:
    
    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')

    def __init__(self):

        self.methods = Methods()
        self.window_setup()
        self.initialize_gui()

        # run loop
        self.window.mainloop()
    
    def window_setup(self):

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("FinishFast/custom_themes/jcolor.json")

        # login window
        self.window = ctk.CTk()
        self.methods.center_window(self.window, 400, 450)
        self.window.title("FinishFast")
        self.window.geometry("400x450")
        self.window.resizable(False, False)

        # close window handler
        self.window.protocol("WM_DELETE_WINDOW", lambda: self.methods.close_app(self.window))
    
        self.methods.grid_configure(self.window, 5, 5)
    
        dark_light_var = ctk.StringVar(value='on')
        dark_light = ctk.CTkSwitch(self.window, width=10, switch_height=12, switch_width=18, progress_color='black',
                                button_color=('black', 'white'), bg_color='transparent',
                                fg_color=('black', 'white'), corner_radius=50, text='',
                                command=lambda: self.methods.light_or_dark_mode(dark_light_var.get()), variable=dark_light_var,
                                onvalue='on', offvalue='off')
        dark_light.grid(row=0, column=2, sticky='ne', columnspan=3)

    def initialize_gui(self):

        # database
        self.db = Database()

        # title
        self.title = Title()
        self.title.add_title(self.window)

        # Sign up
        self.signup = SignUp(self.db)

        # login
        self.login = Login(self.signup, self.db)
        self.login.login_display(self.window, self) 
        

    # Sign up window
    def sign_up_window(self):

        # hiding old window
        self.window.withdraw()

        # creating sign up window
        sign_up_window = ctk.CTkToplevel(self.window)
        self.methods.center_window(sign_up_window, 400, 450)
        sign_up_window.title("FinishFast")
        sign_up_window.geometry("400x450")
        sign_up_window.resizable(False, False)

        # close window handler
        sign_up_window.protocol("WM_DELETE_WINDOW", lambda: self.methods.close_app(sign_up_window))
    
        # grid
        self.methods.grid_configure(sign_up_window, 5, 6)
        
        self.signup.signUpDisplay(sign_up_window, self)

        #self.testing = Testing()
        #self.testing.fill_grid(sign_up_window)

    # Return Login Window
    def return_login(self, window):

        window.withdraw()
        self.window.deiconify()

    # new window
    def create_main_window(self, curr_user):

        #  hides old window 
        self.window.withdraw()

        # creating new window
        main_window = ctk.CTkToplevel(self.window)
        self.methods.center_window(main_window, 1200, 600)
        print('new window')
        main_window.title("FinishFast")
        main_window.geometry("1200x600")
        self.window._set_appearance_mode='dark'
        main_window.resizable(False, False)

        # close window handler
        main_window.protocol("WM_DELETE_WINDOW", lambda: self.methods.close_app(main_window))

        # new window grid
        self.methods.grid_configure(main_window, 9, 9)

        #self.testing = Testing()
        #self.testing.fill_grid(self.main_window)

        self.menu_bar = MenuBar(main_window)
        self.menu_bar.add_menu_bar()

        # main view
        self.main_view = MainView(main_window, self.db, curr_user)



if __name__ == "__main__":
    ProjectManager()