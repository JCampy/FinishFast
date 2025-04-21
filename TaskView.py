import customtkinter as ctk
from TasksModel import TasksModel
from Methods import Methods


class TaskView():

    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')

    def __init__(self, db, curr_user, proj_id, proj_win):

        self.db = db
        self.curr_user = curr_user
        self.proj_id = proj_id
        self.proj_win = proj_win
        self.rows = 2
        self.cols = 5

        self.num_of_task = TasksModel.get_num_of_task(self.db, self.proj_id)
        self.m = Methods()
    
    def task_window(self):

        # get current dark or light mode for variables 
        current_color = self.m.color_choice()

        # Scrollable Frame for Tasks
        self.tasks_frame = ctk.CTkScrollableFrame(self.proj_win, fg_color='#cccbc8')
        self.tasks_frame.grid(row=3, column=0, columnspan=4, rowspan=3, sticky='nsew', padx=10, pady=(0, 25))

        # Configure rows and columns for tasks_frame
        self.m.grid_configure(self.tasks_frame, self.rows, self.cols)
        
        # Tasks Label
        tasks_label = ctk.CTkLabel(self.proj_win, text="Tasks:", text_color=None, font=('', 18, 'bold'))
        tasks_label.grid(row=2, column=0, columnspan=1, sticky='sw', padx=10, pady=10)

        # add task button
        add_task = ctk.CTkButton(self.proj_win, text='Add Task', fg_color=self.MAIN_COLOR,
                                    width=12, height=8, command=lambda: self.task_popup_window())
        add_task.grid(row=2, column=3, columnspan=1, sticky='se', padx=10, pady=10)

        
        # sort task combobox
        sort_task = ctk.CTkComboBox(self.proj_win, width=110, height=12,fg_color=self.MAIN_COLOR, bg_color=self.MAIN_COLOR, values=["Date Created", "Priority",  
                                    "Difficulty", "Completed", "Search Specific"], dropdown_fg_color=current_color,
                                    command= self.sort_task_combobox, text_color=self.TEXT_COLOR, state="readonly", corner_radius=0)
        sort_task.grid(row=2, column=3, sticky='sw', padx=10 , pady=10)
        sort_task.set("Date Created")

    # Create a popup window
    def task_popup_window(self):

        popup = ctk.CTkToplevel(self.proj_win)
        popup.title("Add Task")
        popup.geometry("400x350")
        self.m.center_window(popup, 400, 350)
        popup.resizable(False, False)
        popup.lift()
        popup.focus_force()

        self.m.grid_configure(popup, 5, 2)

        # Task Name Input
        task_name_label = ctk.CTkLabel(popup, text="Task Name:", font=('', 14))
        task_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        task_name_entry = ctk.CTkEntry(popup, width=150)
        task_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Task Description Input
        task_desc_label = ctk.CTkLabel(popup, text="Task Description:", font=('', 14))
        task_desc_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        task_desc_entry = ctk.CTkEntry(popup, width=150, height=75)
        task_desc_entry.grid(row=1, column=1, padx=10, pady=10)

        # Task Priority Slider
        priority_label = ctk.CTkLabel(popup, text="Priority (1-10):", font=('', 14))
        priority_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        priority_slider = ctk.CTkSlider(popup, from_=1, to=10, number_of_steps=9)
        priority_slider.grid(row=2, column=1, padx=10, pady=10)

        # Task Difficulty Slider
        difficulty_label = ctk.CTkLabel(popup, text="Difficulty (1-10):", font=('', 14))
        difficulty_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        difficulty_slider = ctk.CTkSlider(popup, from_=1, to=10, number_of_steps=9)
        difficulty_slider.grid(row=3, column=1, padx=10, pady=10)

        # Done Button
        def on_done():

            #with self.db.get_session() as session:
                
            task_name = task_name_entry.get()
            task_desc = task_desc_entry.get()
            task_priority = priority_slider.get()
            task_difficulty = difficulty_slider.get()
            new_task = TasksModel.create_task(self.db, self.proj_id, task_name, task_desc, 
                                              task_priority, task_difficulty)
            print(f"Task Name: {task_name}")
            print(f"Task Description: {task_desc}")
            print(f"Priority: {task_priority}")
            print(f"Difficulty: {task_difficulty}")
            popup.destroy()

        done_button = ctk.CTkButton(popup, text="Done", command=on_done, fg_color=self.MAIN_COLOR)
        done_button.grid(row=4, column=0, padx=10, pady=20)

        # Cancel Button
        def on_cancel():
            popup.destroy()

        cancel_button = ctk.CTkButton(popup, text="Cancel", command=on_cancel, fg_color="gray")
        cancel_button.grid(row=4, column=1, padx=10, pady=20)
        
    # Check grid at start of app when loading projects
    def check_task_grid(self, window):
        if self.num_of_task == (self.rows*self.cols):
            self.rows += 1
            self.updateGrid(window)
        elif self.num_of_task > (self.rows*self.cols):
            while self.num_of_projects > (self.rows*self.cols):
                self.rows += 1
                self.updateGrid(window)  

    def sort_task_combobox(self, value):
        print(value)
            # FIGURE OUT WHY GRID IS NOT EXPANDING TO THE ENTIRE FRAME