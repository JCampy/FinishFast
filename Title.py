import customtkinter as ctk
from PIL import Image

class Title:
    
    def __init__(self):
        pass

    def add_title(self, window):

        # title logo
        image = Image.open('ProjectManager/images/finishfast_250px_noBG.png') # change to Project_Manager/images/gradient.png on desktop
        ctk_image =ctk.CTkImage(light_image=image, size=(250,50))
        image_label = ctk.CTkLabel(window, image=ctk_image, text='')
        image_label.grid(row=1, column=2, columnspan=3, sticky='n')
        