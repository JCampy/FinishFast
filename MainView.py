import customtkinter as ctk
from ProjectsModel import ProjectsModel
from NotesView import NotesView
from ProfileView import ProfileView
from ProjectsView import ProjectsView
from SingleProjectView import SingleProjectView

class MainView:

    def __init__(self, window, database, curr_user):

        self.curr_user = curr_user
        self.db = database

        self.curr_window = window

        self.profile_view = ProfileView(database, window, curr_user)
        self.notes_view = NotesView(window, database, curr_user, self.profile_view)
        # Transfer method for calling single project view
        self.projects_view = ProjectsView(window, database, curr_user, self.load_single_project_view, self.profile_view) 
        
        self.notes_view.create_notes_frame()
        self.notes_view.get_current_notes()

        self.profile_view.create_profile_frame()
        
        self.projects_view.create_projects_frame()
        self.projects_view.check_project_grid(self.projects_view.projects_frame) # test this later
        self.projects_view.get_current_projects(curr_user)

    # Handling transition to SingleProjectView
    def load_single_project_view(self, project_id, prev_frame, projects_view, proj_button):
        
        print(f'Loading singleProjectView For project ID: {project_id}')
        prev_frame.grid_forget()
        
        spv = SingleProjectView(self.curr_window, self.db, self.curr_user, project_id, prev_frame, projects_view, proj_button)
        spv.single_project_data()

        
    



