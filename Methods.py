import customtkinter as ctk 

class Methods:

    def __init__(self):
        pass

    # Fil grid with colors    
    def main_fill_grid(self, window, color):
        for i in range(5):
                for j in range(5):
                    color = ctk.CTkLabel(window, fg_color=color, text='')
                    color.grid(row=i, column=j,  sticky='news')

    # Configure grid layouts
    def grid_configure(self, window, rows, cols):
        window.columnconfigure(list(range(cols)), weight=1, uniform='a')
        window.rowconfigure(list(range(rows)), weight=1, uniform='a')

    # Center window
    def center_window(self, window, width, height):

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"+{x}+{y}")

    # Close Window / Application
    def close_app(self, curr_window):

        # Get a list of all open windows
        open_windows = curr_window.winfo_children()

        for win in open_windows:
            if isinstance(win, ctk.CTkToplevel) and win.winfo_exists():
                win.destroy()

        # Close the main window if it's still open
        if curr_window and curr_window.winfo_exists():
            curr_window.destroy()

        print("All windows closed. Exiting...")
        curr_window.quit()

    # light and dark mode method
    def light_or_dark_mode(self, val):

        if val == 'on':
            ctk.set_appearance_mode("light")
            print('light')
        else:
            ctk.set_appearance_mode("dark")
            print('dark')  