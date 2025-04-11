import customtkinter as ctk


class NotesView:

    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')

    def __init__(self, window):
        self.window = window

    def create_notes_frame(self):

        # notes label
        notes_label = ctk.CTkLabel(self.window, text='Notes',
                                    text_color=self.TEXT_COLOR, font=('',20,'bold'))
        notes_label.grid(row=3, column=0, columnspan=3, sticky='news', pady=(15, 0))

        # notes frame outline color
        notes_frame_bg = ctk.CTkFrame(self.window, bg_color='transparent',
                                    fg_color=self.MAIN_COLOR)
        notes_frame_bg.grid(row=4, column=0, rowspan=5, columnspan=3, sticky='news', pady=2, padx=2)

        # notes frame
        notes_frame = ctk.CTkFrame(self.window, bg_color='transparent',
                                    fg_color='transparent')
        notes_frame.grid(row=4, column=0, rowspan=5, columnspan=3, sticky='news', pady=5, padx=5)