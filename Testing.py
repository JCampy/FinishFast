import customtkinter as ctk
import random

class Testing:
    
    def __init__(self):
        self.grid_colors = {}

    def fill_grid(self, window):
        for i in range(6):
                for j in range(5):
                    colors = random.randrange(0, 2**24)
                    hex_color = hex(colors)
                    #print(hex_color)
                    std_color = '#' + hex_color[2:].zfill(6)
                    self.grid_colors[(i,j)] = std_color
                    #print(self.grid_colors.values())
                    color = ctk.CTkLabel(window, fg_color=std_color, text='')
                    color.grid(row=i, column=j,  sticky='news')