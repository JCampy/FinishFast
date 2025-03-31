import customtkinter as ctk 

class Methods:

    def __init__(self):
        pass

    def main_fill_grid(self, window, color):
        for i in range(5):
                for j in range(5):
                    color = ctk.CTkLabel(window, fg_color=color, text='')
                    color.grid(row=i, column=j,  sticky='news')