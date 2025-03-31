import customtkinter as ctk
import random
from Testing import Testing
from Login import Login
from Title import Title
from MenuBar import MenuBar
from MainView import MainView
from Database import Database
from SignUp import SignUp

class ProjectManager:
    
    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')

    def __init__(self):

        self.window_setup()
        self.initialize_gui()

        # run loop
        self.window.mainloop()
    
    def window_setup(self):

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("FinishFast/custom_themes/jcolor.json")

        # login window
        self.window = ctk.CTk()
        self.center_window(self.window, 400, 450)
        self.window.title("FinishFast")
        self.window.geometry("400x450")
        self.window.resizable(False, False)

        # close window handler
        self.window.protocol("WM_DELETE_WINDOW", lambda: self.close_app(self.window))
        #self.window.configure(fg_color='white')
    
        self.grid_configure(self.window, 5, 5)
    
        dark_light_var = ctk.StringVar(value='on')
        dark_light = ctk.CTkSwitch(self.window, width=10, switch_height=12, switch_width=18, progress_color='black',
                                button_color=('black', 'white'), bg_color='transparent',
                                fg_color=('black', 'white'), corner_radius=50, text='',
                                command=lambda: self.change_light(dark_light_var.get()), variable=dark_light_var,
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
        self.login.login_display(self.window, self) #self.testing.grid_colors
        

    # Sign up window
    def sign_up_window(self):

        # hiding old window
        self.window.withdraw()

        # creating sign up window
        sign_up_window = ctk.CTkToplevel(self.window)
        self.center_window(sign_up_window, 400, 450)
        sign_up_window.title("FinishFast")
        sign_up_window.geometry("400x450")
        sign_up_window.resizable(False, False)

        # close window handler
        sign_up_window.protocol("WM_DELETE_WINDOW", lambda: self.close_app(sign_up_window))
    
        # grid
        self.grid_configure(sign_up_window, 5, 6)
        
        self.signup.signUpDisplay(sign_up_window, self)

        #self.testing = Testing()
        #self.testing.fill_grid(sign_up_window)
        # example for showing old window is window.deconify()

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
        self.center_window(main_window, 1200, 600)
        print('new window')
        main_window.title("FinishFast")
        main_window.geometry("1200x600")
        self.window._set_appearance_mode='dark'
        main_window.resizable(False, False)

        # close window handler
        main_window.protocol("WM_DELETE_WINDOW", lambda: self.close_app(main_window))

        # new window grid
        self.grid_configure(main_window, 9, 9)

        #self.testing = Testing()
        #self.testing.fill_grid(self.main_window)

        # title menu bar - windows only
        self.menu_bar = MenuBar(main_window)
        self.menu_bar.add_menu_bar()

        # main view
        self.main_view = MainView(main_window, self.db, curr_user)
        #self.main_view.dashboard_top(self.main_window)
        #self.main_view.inner_frame(self.main_window)

    # light and dark mode method
    def change_light(self, val):

        if val == 'on':
            ctk.set_appearance_mode("light")
            print('light')
        else:
                ctk.set_appearance_mode("dark")
                print('dark')  

    # method to close windows properly
    def close_app(self, curr_window):

        # Get a list of all open windows
        open_windows = self.window.winfo_children()

        for win in open_windows:
            if isinstance(win, ctk.CTkToplevel) and win.winfo_exists():
                win.destroy()

        # Close the main window if it's still open
        if self.window and self.window.winfo_exists():
            self.window.destroy()

        print("All windows closed. Exiting...")
        self.window.quit()

    
    def center_window(self, window, width, height):

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"+{x}+{y}")

    def grid_configure(self, window, rows, cols):
        window.columnconfigure(list(range(cols)), weight=1, uniform='a')
        window.rowconfigure(list(range(rows)), weight=1, uniform='a')

if __name__ == "__main__":
    ProjectManager()