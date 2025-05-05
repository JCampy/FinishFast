import customtkinter as ctk
from tkinter import filedialog
from NotesModel import NotesModel
from ProjectsModel import ProjectsModel

class ProfileView:
    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')

    def __init__(self, database, window, curr_user):
        self.window = window
        self.db = database
        self.curr_user = curr_user
        self.user_name = curr_user
        self.num_projects = ProjectsModel.num_of_projects(database, curr_user)
        self.num_notes = NotesModel.get_num_of_notes(database, curr_user)
        self.last_login = 'Hello'

    def create_profile_frame(self):
        # Profile frame outline color
        profile_frame_bg = ctk.CTkFrame(self.window, bg_color='transparent', fg_color=self.MAIN_COLOR)
        profile_frame_bg.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='news', pady=2, padx=2)

        # Profile frame
        profile_frame = ctk.CTkFrame(profile_frame_bg, bg_color='transparent', fg_color='transparent')
        profile_frame.grid(row=0, column=0, sticky='news', pady=5, padx=5)

        # Profile picture frame
        profile_pic_frame = ctk.CTkFrame(profile_frame, width=100, height=100, bg_color='transparent',
                                         fg_color=self.SECONDARY_WHITE, corner_radius=50)
        profile_pic_frame.grid(row=0, column=0, padx=10, pady=10, sticky='n')

        # Placeholder for profile picture
        profile_pic_label = ctk.CTkLabel(profile_pic_frame, text="P", font=("Arial", 36, "bold"),
                                         text_color=self.THIRD_GRAY)
        profile_pic_label.place(relx=0.5, rely=0.5, anchor="center")

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

    def update_stats(self, num_projects=None, num_notes=None):
        if num_projects is not None:
            self.projects_label.configure(text=f"Projects: {ProjectsModel.num_of_projects(self.db, self.curr_user)}")
        if num_notes is not None:
            self.notes_label.configure(text=f"Notes: {NotesModel.get_num_of_notes(self.db, self.curr_user)}")
            
    def change_profile_photo(self):
        file_path = filedialog.askopenfilename(
            title="Select Profile Photo",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")]
        )
        if file_path:
            print(f"Selected file: {file_path}")
            # Add logic to update the profile picture