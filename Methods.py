import customtkinter as ctk 

class Methods:
    
    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')


    def __init__(self):
        pass

    # Fil grid with colors    
    def main_fill_grid(self, window, color):
        for i in range(5):
                for j in range(5):
                    color = ctk.CTkLabel(window, fg_color=color, text='')
                    color.grid(row=i, column=j,  sticky='news')

    # Configure grid layouts
    def grid_configure(self, window, rows, cols, minsize=None):
        # Configure rows
        for i in range(rows):
            window.rowconfigure(i, weight=1, uniform='a', minsize=minsize)
        # Configure columns
        for j in range(cols):
            window.columnconfigure(j, weight=1, uniform='a', minsize=minsize)

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


    # return color choice based on current light or dark setting
    def color_choice(self):
        current_color = ''
        current_mode = ctk.get_appearance_mode()
        if current_mode == 'Light':
            current_color = self.SECONDARY_WHITE
        else:
            current_color = self.THIRD_GRAY
        return current_color
    
    # text warning
    def check_text_length_warning(self, text, max_length, method):
        if len(text) > max_length:
            warning = ctk.CTkToplevel()
            warning.title='Warning'
            warning.geometry('200x100')
            warning.attributes('-topmost', True)
            self.grid_configure(warning, 2, 1)
            self.center_window(warning, 50, 25)

            label = ctk.CTkLabel(warning, text='To many characters. Try again.')
            label.grid(row=0, column=0, sticky='nsew')

            button_close = ctk.CTkButton(warning, text='Close', command=warning.destroy, 
                                         width=50, height=15)
            button_close.grid(row=1, column=0, padx=2)

        else:

            return method(text)

    # method for making sure you want something deleted before completing transaction    
    def are_you_sure(self, curr_frame=None, restore_frame=None, method=None, method_two=None, m_args=(), 
                     m_two_args=(), restore_frame_kwargs={}):

        warning = ctk.CTkToplevel()
        warning.title='Warning'
        warning.geometry('200x100')
        warning.attributes('-topmost', True)
        self.grid_configure(warning, 2, 1)
        self.center_window(warning, 50, 25)

        label = ctk.CTkLabel(warning, text='To many characters. Try again.')
        label.grid(row=0, column=0, sticky='nsew')

        def pressed_yes():

            if curr_frame:
                curr_frame.destroy()
            if restore_frame:
                restore_frame.grid(**restore_frame_kwargs)
            if method:
                method(*m_args)
            if method_two:
                method_two(*m_two_args)
            
            print(f'Yes accepted')
            warning.destroy()

        def pressed_no():
            
            print(f'No accepted')
            warning.destroy()

        

        button_yes = ctk.CTkButton(warning, text='Yes', command=pressed_yes, 
                                        width=50, height=15)
        button_yes.grid(row=1, column=0, padx=15, sticky='w')

        button_no = ctk.CTkButton(warning, text='No', command=pressed_no, 
                                        width=50, height=15)
        button_no.grid(row=1, column=0, padx=15, sticky='e')

        