import customtkinter as ctk
from ProjectsModel import ProjectsModel
from NotesView import NotesView
from ProfileView import ProfileView
from ProjectsView import ProjectsView

class MainView:

    def __init__(self, window, database, curr_user):

        self.curr_user = curr_user
        self.db = database

        self.curr_window = window

       
        self.notes_view = NotesView(window)
        self.profile_view = ProfileView(window)
        self.projects_view = ProjectsView(window, database, curr_user)
        
        self.notes_view.create_notes_frame()
        self.profile_view.create_profile_frame()
        self.projects_view.create_projects_frame()
        self.projects_view.check_grid(self.projects_view.projects_frame)
        self.projects_view.get_current_projects(curr_user)

        
    



