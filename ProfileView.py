import customtkinter as ctk
from tkinter import filedialog, messagebox
from NotesModel import NotesModel
from UserModel import UserModel
from ProjectsModel import ProjectsModel
from pathlib import Path
from Methods import Methods
from PIL import Image, ImageOps, ImageDraw
import shutil

class ProfileView:
    
    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')

    # Folder will be created in source code
    BASE_DIR = Path(__file__).parent
    DEST_FOLDER = BASE_DIR / "uploads"

    def __init__(self, database, window, curr_user):
        self.window = window
        self.db = database
        self.curr_user = curr_user
        self.user_name = curr_user
        self.num_projects = ProjectsModel.num_of_projects(database, curr_user)
        self.num_notes = NotesModel.get_num_of_notes(database, curr_user)
        self.last_login = 'W.I.P.'

        self.m = Methods()

    def create_profile_frame(self):
        # Profile frame outline color
        profile_frame_bg = ctk.CTkFrame(self.window, bg_color='transparent', fg_color=self.MAIN_COLOR)
        profile_frame_bg.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='news', pady=2, padx=2)

        # Profile frame
        profile_frame = ctk.CTkFrame(profile_frame_bg, bg_color='transparent', fg_color='transparent')
        profile_frame.grid(row=0, column=0, sticky='news', pady=5, padx=5)

        # Profile picture frame
        self.profile_pic_frame = ctk.CTkFrame(profile_frame, width=100, height=100, bg_color='transparent',
                                         fg_color=self.SECONDARY_WHITE, corner_radius=50)
        self.profile_pic_frame.grid(row=0, column=0, padx=10, pady=10, sticky='n')
        self.m.grid_configure(self.profile_pic_frame, 1, 1)

        self.update_profile_photo() # method for being able to dynamically update profile photo

        # Change profile photo button
        change_photo_button = ctk.CTkButton(profile_frame, text="Change Photo", fg_color=self.MAIN_COLOR,
                                            text_color="white", command=self.change_profile_photo)
        change_photo_button.grid(row=1, column=0, padx=10, pady=10, sticky='n')

        # User name
        #user_name_label = ctk.CTkLabel(profile_frame, text=self.user_name, font=("Arial", 18, "bold"),
        #                               text_color=self.TEXT_COLOR)
        #user_name_label.grid(row=2, column=0, padx=10, pady=5, sticky='n')

        # Stats frame
        stats_frame = ctk.CTkFrame(profile_frame, bg_color='transparent', fg_color='transparent')
        stats_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky='ne')

        # Number of projects
        self.projects_label = ctk.CTkLabel(stats_frame, text=f"Projects: {self.num_projects}", font=("Arial", 14),
                                       text_color=self.TEXT_COLOR)
        self.projects_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        # Number of notes
        self.notes_label = ctk.CTkLabel(stats_frame, text=f"Notes: {self.num_notes}", font=("Arial", 14),
                                    text_color=self.TEXT_COLOR)
        self.notes_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        # Last login
        last_login_label = ctk.CTkLabel(stats_frame, text=f"Last Login: {self.last_login}", font=("Arial", 12, "italic"),
                                        text_color=self.TEXT_COLOR)
        last_login_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')

    # helper method that is used in other classes to update the values for number of projects and notes dynamically
    def update_stats(self, num_projects=None, num_notes=None):
        if num_projects is not None:
            self.projects_label.configure(text=f"Projects: {ProjectsModel.num_of_projects(self.db, self.curr_user)}")
        if num_notes is not None:
            self.notes_label.configure(text=f"Notes: {NotesModel.get_num_of_notes(self.db, self.curr_user)}")

    def update_profile_photo(self):

        try:

            profile_photo_path = UserModel.get_profile_photo_path(self.db, self.curr_user)
            if profile_photo_path:  # Check if a profile photo path exists
                # Open the image
                image = Image.open(profile_photo_path).convert('RGBA').resize((100, 100))  # Resize to match the frame size

                # Create a circular mask
                mask = Image.new("L", (100, 100), 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, 100, 100), fill=255)

                # Apply the mask to the image
                circular_image = ImageOps.fit(image, (100, 100), centering=(0.5, 0.5))
                circular_image.putalpha(mask)

                # Paste onto solid background matching your frame (adjust color as needed)
                background_color =  self.m.hex_to_rgba(self.MAIN_COLOR)
                background = Image.new("RGBA", (100, 100), background_color)
                background.paste(circular_image, (0, 0), circular_image)

                # Convert to CTkImage
                print("IMAGE HERE")
                ctk_image = ctk.CTkImage(light_image=background, dark_image=background, size=(100, 100))
                profile_pic_label = ctk.CTkLabel(self.profile_pic_frame, image=ctk_image, text='')
                profile_pic_label.grid(row=0, column=0, sticky='news')
            else:
                # Placeholder if no profile photo exists
                print("Nothing")
                profile_pic_label = ctk.CTkLabel(self.profile_pic_frame, text="P", font=("Arial", 36, "bold"),
                                                text_color=self.THIRD_GRAY)
                profile_pic_label.grid(row=0, column=0, )
        except FileNotFoundError:

            # Placeholder for profile picture
            profile_pic_label = ctk.CTkLabel(self.profile_pic_frame, text="P", font=("Arial", 36, "bold"),
                                            text_color=self.THIRD_GRAY)
            profile_pic_label.grid(row=0, column=0)

    def change_profile_photo(self):
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("All files", "*.png;*.jpg;*.jpeg;*.bmp")]
        )
        
        if not file_path:
            return

        try:

            # check old file path
            old_file_path = UserModel.get_profile_photo_path(self.db, self.curr_user)

            if old_file_path: # if it exist

                old_file_path = Path(old_file_path) # converting to path object
                if old_file_path.exists():

                    old_file_path.unlink() # remove it
                    print(f'File deleted: {old_file_path}')

                    source_path = Path(file_path) # Convert file_path to a Path object
                    self.DEST_FOLDER.mkdir(parents=True, exist_ok=True) # Ensure the destination folder exists
                    dest_path = self.DEST_FOLDER / source_path.name # Construct the destination path
                    shutil.copy2(source_path, dest_path) # Copy the file to the destination
                    UserModel.update_profile_photo(self.db, self.curr_user, source_path.name, str(dest_path)) # adding the filename and filepath to database
                    self.update_profile_photo()
                    messagebox.showinfo("Success", f"File saved to {dest_path}")

            # if it doesn't proceed as usual.
            else:
            
                source_path = Path(file_path) # Convert file_path to a Path object
                self.DEST_FOLDER.mkdir(parents=True, exist_ok=True) # Ensure the destination folder exists
                dest_path = self.DEST_FOLDER / source_path.name # Construct the destination path
                shutil.copy2(source_path, dest_path) # Copy the file to the destination
                UserModel.update_profile_photo(self.db, self.curr_user, source_path.name, str(dest_path)) # adding the filename and filepath to database
                self.update_profile_photo()
                messagebox.showinfo("Success", f"File saved to {dest_path}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{str(e)}")