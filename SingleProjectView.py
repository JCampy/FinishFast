import customtkinter as ctk
from ProjectsModel import ProjectsModel, Projects
from Testing import Testing

class SingleProjectView:

    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')

    def __init__(self, window, database, curr_user, project_id):
        
        self.window = window
        self.db = database
        self.curr_user = curr_user
        self.p_id = project_id
        self.test = Testing()

    def single_project_data(self):

        print("Called sp")
        # Fetch project data from the database
        with self.db.get_session() as session:
            project = session.query(Projects).filter_by(projectID=self.p_id).first()
            if not project:
                error_label = ctk.CTkLabel(self.window, text="Project not found!", text_color="red", font=('', 20, 'bold'))
                error_label.grid(row=0, column=0, columnspan=4, sticky='nsew')
                return
            
            #self.test.fill_grid(self.window, 5, 4)

            # Project Name
            project_name_label = ctk.CTkLabel(self.window, text=project.project_name,
                                              text_color=self.TEXT_COLOR, font=('', 20, 'bold'))
            project_name_label.grid(row=0, column=0, columnspan=2, sticky='nw', padx=10, pady=10)

            # Project ID
            project_id_label = ctk.CTkLabel(self.window, text=f"{self.p_id}",
                                            text_color=self.TEXT_COLOR, font=('', 16))
            project_id_label.grid(row=4, column=2, columnspan=2, sticky='se', padx=5, pady=0)

            # Creation Date
            created_date = project.date_created[:10]
            year = created_date[:4]
            month = created_date[5:7]
            day = created_date[8:10]
            corrected_date = month + '-' + day + '-' + year

            creation_date_label = ctk.CTkLabel(self.window, text=f"Created On: {corrected_date}",
                                               text_color=self.TEXT_COLOR, font=('', 16))
            creation_date_label.grid(row=0, column=0, columnspan=2, sticky='sw', padx=10, pady=5)

            # Tasks Label
            tasks_label = ctk.CTkLabel(self.window, text="Tasks:", text_color=self.TEXT_COLOR, font=('', 18, 'bold'))
            tasks_label.grid(row=2, column=0, columnspan=4, sticky='', padx=10, pady=10)

            # Scrollable Frame for Tasks
            tasks_frame = ctk.CTkScrollableFrame(self.window, fg_color='black')
            tasks_frame.grid(row=3, column=0, columnspan=4, rowspan=2, sticky='nsew', padx=10, pady=(0, 25))

            # Configure rows and columns for tasks_frame
            tasks_frame.rowconfigure(list(range(10)), weight=1)  # Adjust the range based on the number of tasks
            tasks_frame.columnconfigure(0, weight=1)

            # Fetch tasks associated with the project
            #tasks = self.get_project_tasks(self.p_id)  # Replace with your method to fetch tasks
            #if not tasks:
            #    no_tasks_label = ctk.CTkLabel(tasks_frame, text="No tasks available.", text_color=self.TEXT_COLOR)
            #    no_tasks_label.grid(row=0, column=0, sticky='nsew', padx=10, pady=5)
            #else:
            #    for i, task in enumerate(tasks):
            #        task_label = ctk.CTkLabel(tasks_frame, text=f"{i + 1}. {task['name']}",
            #                                  text_color=self.TEXT_COLOR, font=('', 14))
            #        task_label.grid(row=i, column=0, sticky='nsew', padx=10, pady=5)
            


            # FIGURE OUT WHY GRID IS NOT EXPANDING TO THE ENTIRE FRAME