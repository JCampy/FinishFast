import customtkinter as ctk
from ProjectsModel import ProjectsModel, Projects
from Testing import Testing
import awesometkinter as atk
from Methods import Methods

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
            
            #self.test.fill_grid(self.window, 6, 4)

            # Project Name
            project_name_label = ctk.CTkLabel(self.window, text=project.project_name,
                                              text_color=self.TEXT_COLOR, font=('', 20, 'bold'))
            project_name_label.grid(row=0, column=0, columnspan=2, sticky='nw', padx=10, pady=10)

            # Project ID
            project_id_label = ctk.CTkLabel(self.window, text=f"{self.p_id}",
                                            text_color=self.TEXT_COLOR, font=('', 16))
            project_id_label.grid(row=5, column=2, columnspan=2, sticky='se', padx=5, pady=0)

            # Creation Date
            created_date = project.date_created[:10]
            year = created_date[:4]
            month = created_date[5:7]
            day = created_date[8:10]
            corrected_date = month + '-' + day + '-' + year

            creation_date_label = ctk.CTkLabel(self.window, text=f"Created On: {corrected_date}",
                                               text_color=self.TEXT_COLOR, font=('', 16))
            creation_date_label.grid(row=0, column=0, columnspan=2, sticky='sw', padx=10, pady=5)

            # get current dark or light mode for variables 
            current_color = Methods().color_choice()

            # Radial Progress bar using ATK
            r_progress_bar = atk.RadialProgressbar(self.window, size=190, bg=self.MAIN_COLOR, fg='green', text_fg=self.MAIN_COLOR,
                                                  parent_bg=current_color, font_size_ratio=.2 )
            r_progress_bar.grid(row=0, column=2, columnspan=2, rowspan=2, sticky='news', padx=20, pady=10)

            # Close single project window view
            close_single_project_button = ctk.CTkButton(self.window,width=12, height=8, text='close', fg_color=current_color, hover_color=current_color,
                                                        bg_color=current_color, text_color=self.MAIN_COLOR)
            close_single_project_button.grid(row=0, column=3, sticky='ne', padx=3, pady=3)

            # Tasks Label
            tasks_label = ctk.CTkLabel(self.window, text="Tasks:", text_color=None, font=('', 18, 'bold'))
            tasks_label.grid(row=2, column=0, columnspan=1, sticky='sw', padx=10, pady=10)

            # add task button
            add_task = ctk.CTkButton(self.window, text='Add Task', fg_color=self.MAIN_COLOR,
                                     width=12, height=8)
            add_task.grid(row=2, column=3, columnspan=1, sticky='se', padx=10, pady=10)

            
            # sort task combobox
            sort_task = ctk.CTkComboBox(self.window, width=110, height=12,fg_color=self.MAIN_COLOR, bg_color=self.MAIN_COLOR, values=["Date Created", "Priority",  
                                        "Difficulty", "Completed", "Search Specific"], dropdown_fg_color=current_color,
                                        command= self.sort_task_combobox, text_color=self.TEXT_COLOR, state="readonly", corner_radius=0)
            sort_task.grid(row=2, column=3, sticky='sw', padx=10 , pady=10)
            sort_task.set("Date Created")
            

            # Scrollable Frame for Tasks
            tasks_frame = ctk.CTkScrollableFrame(self.window, fg_color='#cccbc8')
            tasks_frame.grid(row=3, column=0, columnspan=4, rowspan=3, sticky='nsew', padx=10, pady=(0, 25))

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
            

    def sort_task_combobox(self, value):
        print(value)
            # FIGURE OUT WHY GRID IS NOT EXPANDING TO THE ENTIRE FRAME