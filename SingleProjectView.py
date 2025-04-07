import customtkinter as ctk
from ProjectsModel import ProjectsModel, Projects

class SingleProjectView:

    def __init__(self, window, database, curr_user, project_id):
        
        self.window = window
        self.db = database
        self.curr_user = curr_user
        self.pid = project_id

    def single_project_frame(self, window, database, curr_user):
        pass
        