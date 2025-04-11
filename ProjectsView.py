import customtkinter as ctk
from ProjectsModel import ProjectsModel, Projects
from Methods import Methods
from SingleProjectView import SingleProjectView
from Testing import Testing

class ProjectsView:
    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')

    def __init__(self, window, database, curr_user):
        self.window = window
        self.db = database
        self.curr_user = curr_user
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
                                    width=100, height=100, fg_color='black',
                                    command = lambda p_id=project.projectID: self.single_project_frame(p_id))
                button._text_label.configure(wraplength=100, justify="center", padx=2, pady=2)
                button.grid(row=row_pos, column=col_pos)

    def create_projects_frame(self):

        # project Label
        curr_project = ctk.CTkLabel(self.window, text='Projects',
                                     text_color=self.TEXT_COLOR, font=('',20,'bold'))
        curr_project.grid(row=0, column=3, columnspan=6, sticky='nw',pady=(3,0), padx=(5,0))

        # project name entry
        proj_name = ctk.CTkEntry(self.window, fg_color='#cccbc8', corner_radius=8, height=8)
        proj_name.grid(row=0, column=4, columnspan=4, sticky='new', pady=(5,5), padx=(3,3))

        # add project button
        add_project = ctk.CTkButton(self.window, text='Add Project', fg_color=self.MAIN_COLOR,
                                     width=12, height=8, command=lambda: self.add_project(proj_name))
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
        self.update_grid(self.projects_frame)

    
    # Single Project Frame
    def single_project_frame(self, project_id):

        # Hide old frame
        self.projects_frame.grid_forget()

         # individual project frame
        self.project_frame = ctk.CTkFrame(self.window, bg_color='transparent',
                                            fg_color='transparent')
        self.project_frame.grid(row=0, column=3, rowspan=9, columnspan=6, sticky='news', pady=(35,5), padx=5)

        # new grid for project frame
        self.methods.grid_configure(self.project_frame, 6, 4, 50)

        print(f'Open Project: {project_id}')
        
        # create instance of single project view and pass window layout    
        spv = SingleProjectView(self.project_frame, self.db, self.curr_user, project_id)
        spv.single_project_data()
            


    # Add Project to database and GUI
    def add_project(self, proj_name):
        
        new_project_obj = ProjectsModel.create_project(self.db, proj_name.get(), self.curr_user)
        row_pos = self.num_of_projects // self.cols
        col_pos = self.num_of_projects % self.cols

        button = ctk.CTkButton(self.projects_frame, text=new_project_obj["project_name"],
                              width=100, height=100, fg_color='black',
                              command = lambda: self.single_project_frame(new_project_obj["projectID"]))
        button._text_label.configure(wraplength=100, justify="center", padx=2, pady=2)
        button.grid(row=row_pos, column=col_pos)

        if self.num_of_projects == (self.rows*self.cols):
            self.rows += 1
            self.update_grid(self.projects_frame)
        self.num_of_projects += 1

    def update_grid(self, window):
        
        # Update rows
        for row in range(self.rows):
            window.rowconfigure(row, weight=1, uniform='a', minsize=125)
        # Update columns
        for col in range(self.cols):
            window.columnconfigure(col, weight=1, uniform='a', minsize=125)

    # Check grid
    def check_grid(self, window):
        if self.num_of_projects == (self.rows*self.cols):
            self.rows += 1
            self.updateGrid(window)
        elif self.num_of_projects > (self.rows*self.cols):
            while self.num_of_projects > (self.rows*self.cols):
                self.rows += 1
                self.updateGrid(window)

