from datetime import datetime
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
    def grid_configure(self, window, rows, cols, minsize=None, weight=1, uniform='a'):

        # Configure rows
        for i in range(rows):
            window.rowconfigure(i, weight=weight, uniform=uniform, minsize=minsize)
        # Configure columns
        for j in range(cols):
            window.columnconfigure(j, weight=weight, uniform=uniform, minsize=minsize)

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
    
    # text length warning
    def check_text_length_warning(self, text, max_length, min_length, method=None, m_param=True):

        if len(text) > max_length:
            warning = ctk.CTkToplevel()
            warning.title='Warning'
            warning.geometry('200x100')
            warning.attributes('-topmost', True)
            self.grid_configure(warning, 2, 1)
            self.center_window(warning, 50, 25)

            label = ctk.CTkLabel(warning, text='To many characters!')
            label.grid(row=0, column=0, sticky='nsew')

            button_close = ctk.CTkButton(warning, text='Close', command=warning.destroy, 
                                         width=50, height=15)
            button_close.grid(row=1, column=0, padx=2)
        elif len(text) <= min_length:
            warning = ctk.CTkToplevel()
            warning.title='Warning'
            warning.geometry('200x100')
            warning.attributes('-topmost', True)
            self.grid_configure(warning, 2, 1)
            self.center_window(warning, 50, 25)

            label = ctk.CTkLabel(warning, text='Please enter a project \n name!')
            label.grid(row=0, column=0, sticky='nsew')

            button_close = ctk.CTkButton(warning, text='Close', command=warning.destroy, 
                                         width=50, height=15)
            button_close.grid(row=1, column=0, padx=2)
        elif method and m_param:
            return method(text)
        elif method and not m_param:
            print('returning just method')
            return method()
        else:
            return text

    # return corrected date format
    def reformat_date(self, date_input):

        # Check if the input is a string and parse it into a datetime object
        if isinstance(date_input, str):
            date_input = datetime.strptime(date_input, '%Y-%m-%d %H:%M:%S.%f')  # Adjust format as needed

        # Format the datetime object into the desired format (e.g., DD-MM-YYYY)
        date = date_input.strftime('%d-%m-%Y')
        return date
    
    # method for making sure you want something deleted before completing transaction    
    def are_you_sure(self, curr_frame=None, restore_frame=None, method=None, method_two=None, method_three=None, 
                     m_args=(), m_two_args=(), restore_frame_kwargs={}):

        warning = ctk.CTkToplevel()
        warning.title='Warning'
        warning.geometry('200x100')
        warning.attributes('-topmost', True)
        self.grid_configure(warning, 2, 1)
        self.center_window(warning, 50, 25)

        label = ctk.CTkLabel(warning, text='Are you sure you want to delete \n the entire project?')
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
            if method_three:
                method_three()
            
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

    # Get's color to ensure text will constrast the chosen color for the project/task
    def get_contrasting_text_color(self, bg_color):

        # Convert hex color to RGB
        bg_color = bg_color.lstrip('#')
        r, g, b = int(bg_color[0:2], 16), int(bg_color[2:4], 16), int(bg_color[4:6], 16)
        # Calculate brightness
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        # Return black for bright backgrounds, white for dark backgrounds
        return "black" if brightness > 128 else "white"

        