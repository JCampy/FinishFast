import customtkinter as ctk
from ProjectsModel import ProjectsModel, Projects
from Testing import Testing
import awesometkinter as atk
from Methods import Methods
from TaskView import TaskView
from TasksModel import TasksModel

class SingleProjectView:

    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')

    def __init__(self, window, database, curr_user, project_id, prev_frame, projects_view, proj_button):

        self.window = window
        self.db = database
        self.curr_user = curr_user
        self.p_id = project_id
        self.pf = prev_frame
        self.pv = projects_view
        self.proj_button = proj_button
        
        self.test = Testing()
        self.m = Methods()


    def single_project_data(self):
        # import necessary for method call
        from ProjectsView import ProjectsView
        

        # individual project s_project_frame
        self.s_project_frame = ctk.CTkFrame(self.window, bg_color='transparent',
                                            fg_color='transparent')
        self.s_project_frame.grid(row=0, column=3, rowspan=9, columnspan=6, sticky='news', pady=(35,5), padx=5)
        self.s_project_frame.grid_propagate(False)
        # new grid for project s_project_frame
        self.m.grid_configure(self.s_project_frame, 6, 4, 50)
    
        print("Called sp")
        # Fetch project data from the database
        with self.db.get_session() as session:
            project = session.query(Projects).filter_by(projectID=self.p_id).first()
            if not project:
                error_label = ctk.CTkLabel(self.s_project_frame, text="Project not found!", text_color="red", font=('', 20, 'bold'))
                error_label.grid(row=0, column=0, columnspan=4, sticky='nsew')
                return
            
            #self.test.fill_grid(self.s_project_frame, 6, 4)

            # Project Name
            project_name_label = ctk.CTkLabel(self.s_project_frame, text=project.project_name,
                                              text_color=self.TEXT_COLOR, font=('', 20, 'bold'),
                                              wraplength=315)
            project_name_label.grid(row=0, column=0, columnspan=2, sticky='nw', padx=10, pady=10)

            # Project ID
            project_id_label = ctk.CTkLabel(self.s_project_frame, text=f"{self.p_id}",
                                            text_color=self.TEXT_COLOR, font=('', 16))
            project_id_label.grid(row=5, column=2, columnspan=2, sticky='se', padx=5, pady=0)

            # Creation Date
            corrected_date = self.m.reformat_date(project.date_created)

        # initialize task_view 
        self.task_view = TaskView(self.db, self.curr_user, self.p_id, self.s_project_frame)

        creation_date_label = ctk.CTkLabel(self.s_project_frame, text=f"Created On: {corrected_date}",
                                            text_color=self.TEXT_COLOR, font=('', 16))
        creation_date_label.grid(row=0, column=0, columnspan=2, sticky='sw', padx=10, pady=5)

        # get current dark or light mode for variables 
        current_color = Methods().color_choice()

        # Radial Progress bar using ATK
        r_progress_bar = atk.RadialProgressbar(self.s_project_frame, size=190, bg=self.MAIN_COLOR, fg='green', text_fg=self.MAIN_COLOR,
                                                parent_bg=current_color, font_size_ratio=.2 )
        r_progress_bar.grid(row=0, column=2, columnspan=2, rowspan=2, sticky='news', padx=20, pady=10)

        r_progress_bar.set(self.task_view.get_progress()) # percentage = (Completed_Task / Task) * 100
        # Close single project s_project_frame view
        close_single_project_button = ctk.CTkButton(self.s_project_frame,width=12, height=8, text='close', fg_color=current_color, hover_color=current_color,
                                                    bg_color=current_color, text_color=self.MAIN_COLOR, command= self.close_project_frame)
        close_single_project_button.grid(row=0, column=3, sticky='ne', padx=3, pady=3)

        # delete current project and all associated task
        delete_project = ctk.CTkButton(self.s_project_frame, text='Delete Project', fg_color='red',
                                    width=12, height=8, command=lambda: self.m.are_you_sure(
                                        self.s_project_frame, self.pf, ProjectsModel.delete_project, # method in methods that calls
                                        TasksModel.delete_all_tasks, lambda: self.pv.shift_projects(self.proj_button),   # delete methods for both project
                                        m_args=(self.db, self.p_id), m_two_args=(self.db, self.p_id),  # and task. Then restore previous frame
                                        restore_frame_kwargs={
                                            'row': 0, 'column': 3, 'rowspan': 9, 'columnspan': 6,
                                            'sticky': 'news', 'pady': (35, 5), 'padx': 5
                                        }
                                    )
                                )
        delete_project.grid(row=5, column=0, columnspan=2, sticky='sw', padx=10, pady=0)

        # task view methods
        self.task_view.task_frame()
        self.task_view.get_current_task()

        # DELETE THIS 
        frame_width = self.s_project_frame.winfo_width()
        frame_height=self.s_project_frame.winfo_height()
        print(f'Frame Size: {frame_width}x{frame_height}')
       
    def close_project_frame(self):
        self.s_project_frame.destroy()
        self.pf.grid(row=0, column=3, rowspan=9, columnspan=6, sticky='news', pady=(35,5), padx=5)

