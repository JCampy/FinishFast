import customtkinter as ctk
from ProjectsModel import ProjectsModel, Projects
from Methods import Methods
from SingleProjectView import SingleProjectView
from Testing import Testing
from CTkColorPicker import *

class ProjectsView:

    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')

    def __init__(self, window, database, curr_user, on_proj_selected):
        self.window = window
        self.db = database
        self.curr_user = curr_user
        self.on_project_selected = on_proj_selected
        self.current_color = "black"

        self.test = Testing()
        self.methods = Methods()

        self.cols = 4
        self.rows = 4

        self.pm = ProjectsModel(database)
        self.num_of_projects = self.pm.num_of_projects(database, curr_user)
        print(f'Number of Projects: {self.num_of_projects}')

    # Projects
    def get_current_projects(self, curr_user):
        project_count = 0

        # Get current projects from database
        projects = ProjectsModel.get_projects(self.db, curr_user)
        with self.db.get_session() as session:
            for project in projects:
                session.add(project)
                print(f'Project: {project.project_name}')
                row_pos = project_count // self.cols
                col_pos = project_count % self.cols
                project_count += 1
                print(f'Row: {row_pos} and Column: {col_pos}')

                button = ctk.CTkButton(self.projects_frame, text=project.project_name,
                                    width=100, height=100, fg_color=project.project_color,
                                    hover_color=project.project_color)
                button._text_label.configure(wraplength=75, justify="center", padx=2, pady=2)
                button.configure(command = lambda p_id=project.projectID, pb=button: self.single_project_frame(p_id, pb))
                button.grid(row=row_pos, column=col_pos)

                self.check_project_grid(self.projects_frame)

    def create_projects_frame(self):

        # project Label
        curr_project = ctk.CTkLabel(self.window, text='Projects',
                                     text_color=self.TEXT_COLOR, font=('',20,'bold'))
        curr_project.grid(row=0, column=3, columnspan=6, sticky='nw',pady=(3,0), padx=(5,0))

        self.color_picker_button = ctk.CTkButton(self.window, text='    ', fg_color=self.current_color, width=12, height=8, command= self.ask_color)
        self.color_picker_button.grid(row=0, column=3, sticky='ne', pady=(5,5), padx=(0,2))

        # project name entry
        proj_name = ctk.CTkEntry(self.window, fg_color='#cccbc8', corner_radius=8, height=8)
        proj_name.grid(row=0, column=4, columnspan=4, sticky='new', pady=(5,5), padx=(3,3))

        # add project button
        add_project = ctk.CTkButton(self.window, text='Add Project', fg_color=self.MAIN_COLOR,
                                     width=12, height=8, command=lambda: 
                                     self.methods.check_text_length_warning(proj_name.get(), 60, 0, self.add_project))
        add_project.grid(row=0, column=8, columnspan=1, sticky='new', padx=(0,5), pady=(5,0))

        # projects frame outline color
        projects_bg_frame = ctk.CTkFrame(self.window, bg_color='transparent',
                                          fg_color=self.MAIN_COLOR)
        projects_bg_frame.grid(row=0, column=3, rowspan=9, columnspan=6, 
                               sticky='news', pady=(32,2), padx=2)

        # project frame
        self.projects_frame = ctk.CTkScrollableFrame(self.window, bg_color='transparent',
                                            fg_color='transparent')
        self.projects_frame.grid(row=0, column=3, rowspan=9, columnspan=6, sticky='news', pady=(35,5), padx=5)
        # new grid for projects frame
        self.update_project_grid(self.projects_frame)
    
    # Single Project Frame
    def single_project_frame(self, project_id, proj_button):
        self.on_project_selected(project_id, self.projects_frame, self, proj_button)


    # Add Project to database and GUI
    def add_project(self, proj_name):
        
        new_project_obj = ProjectsModel.create_project(self.db, proj_name, self.curr_user, self.current_color)
        row_pos = self.num_of_projects // self.cols
        col_pos = self.num_of_projects % self.cols

        button = ctk.CTkButton(self.projects_frame, text=new_project_obj["project_name"],
                            width=100, height=100, fg_color=self.current_color, hover_color=self.current_color)
        button._text_label.configure(wraplength=75, justify="center", padx=2, pady=2)
        button.configure(command = lambda pb = button : self.single_project_frame(new_project_obj["projectID"], pb))
        button.grid(row=row_pos, column=col_pos)

        if self.num_of_projects == (self.rows*self.cols):
            self.rows += 1
            self.update_project_grid(self.projects_frame)
        self.num_of_projects += 1

    def update_project_grid(self, window):
        
        # Update rows when adding during app usage
        for row in range(self.rows):
            window.rowconfigure(row, weight=1, uniform='a', minsize=125)
        # Update columns
        for col in range(self.cols):
            window.columnconfigure(col, weight=1, uniform='a', minsize=125)

    # Check grid at start of app when loading projects
    def check_project_grid(self, window):
        if self.num_of_projects == (self.rows*self.cols):
            self.rows += 1
            self.updateGrid(window)
        elif self.num_of_projects > (self.rows*self.cols):
            while self.num_of_projects > (self.rows*self.cols):
                self.rows += 1
                self.updateGrid(window)

    # shifts projects down when one is removed
    def shift_projects(self, proj_button):
        proj_button.destroy()
        projects_count = 0
        for widget in self.projects_frame.winfo_children():
            row_pos = projects_count // self.cols
            col_pos = projects_count % self.cols
            widget.grid(row=row_pos, column=col_pos)
            projects_count += 1
        
        # Adjust the number of rows dynamically
        new_rows = (projects_count + self.cols - 1) // self.cols  # Calculate required rows
        if new_rows < self.rows:  # Only shrink the grid if necessary
            self.rows = new_rows
            self.update_project_grid(self.projects_frame)

    # select color for project buttons
    def ask_color(self):

        pick_color= AskColor() # Open color picker
        check = pick_color.get()
        if check != None:
            self.current_color = check # set the current color
            self.color_picker_button.configure(fg_color=self.current_color)
        else:
            self.current_color = self.current_color
        



