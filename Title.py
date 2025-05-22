import customtkinter as ctk
from PIL import Image
import os

class Title:
    
    def __init__(self):
        pass

    def add_title(self, window):

        # title logo
        # Get the absolute path to the image
        image_path = os.path.join(os.path.dirname(__file__), "images", "finishfast_250px_noBG.png")
        image = Image.open(image_path)
        ctk_image =ctk.CTkImage(light_image=image, size=(250,50))
        image_label = ctk.CTkLabel(window, image=ctk_image, text='')
        image_label.grid(row=1, column=2, columnspan=3, sticky='n')
        