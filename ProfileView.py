import customtkinter as ctk

class ProfileView:
    
        MAIN_COLOR = '#39BCCE'
        SECONDARY_WHITE = '#f8f2f2'
        THIRD_GRAY = 'gray14'
        TEXT_COLOR = ('black', 'white')
    
        def __init__(self, window):
            self.window = window
    
        def create_profile_frame(self):
    
            # profile frame outline color
            profile_frame_bg = ctk.CTkFrame(self.window, bg_color='transparent',
                                        fg_color=self.MAIN_COLOR)
            profile_frame_bg.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='news', pady=2, padx=2)

            # profile frame
            profile_frame = ctk.CTkFrame(self.window, bg_color='transparent',
                                        fg_color='transparent')
            profile_frame.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='news', pady=5, padx=5)