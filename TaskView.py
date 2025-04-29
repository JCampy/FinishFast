import customtkinter as ctk
from TasksModel import TasksModel
from Methods import Methods
from CTkColorPicker import *


class TaskView():

    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')

    def __init__(self, db, curr_user, proj_id, proj_frame):

        self.db = db
        self.curr_user = curr_user
        self.proj_id = proj_id
        self.proj_frame = proj_frame
        self.rows = 2
        self.cols = 5
        self.current_color = '#000000'

        self.num_of_task = TasksModel.get_num_of_task(self.db, self.proj_id)
        self.m = Methods()
    
    def get_current_task(self):
        
        task_count = 0

        tasks = TasksModel.get_tasks(self.db, self.proj_id)
        with self.db.get_session() as session:
            for task in tasks:
                session.add(task)
                print(f'Task: {task.task_name}')
                row_pos = task_count // self.cols
                col_pos = task_count % self.cols
                task_count += 1
                print(f'Row: {row_pos} and Column: {col_pos}')

                single_task_frame = ctk.CTkFrame(self.tasks_frame, fg_color='#cccbc8', width=75, height=100)  #'#cccbc8'
                single_task_frame.grid(row=row_pos, column=col_pos)
                self.m.grid_configure(single_task_frame, 2, 1)
                
                remove_task = ctk.CTkButton(single_task_frame, text='X', width=10, height=10, 
                                        fg_color="red", command= lambda t_ID = task.taskID,  stf = single_task_frame, 
                                        p_ID = self.proj_id : self.delete_task(stf, p_ID, t_ID)) # temp message
                remove_task.grid(row=1, column=1, sticky='ne', padx= 1, pady=1)
                click_task = ctk.CTkButton(single_task_frame, text=task.task_name, text_color=self.m.get_contrasting_text_color(task.task_color),
                                width=50, height=50, corner_radius=15, fg_color=task.task_color,
                                hover_color=task.task_color, command = lambda t_ID = task.taskID : print(t_ID))
                click_task._text_label.configure(wraplength=100, justify="center", padx=2, pady=2)
                click_task.grid(row=2, column=1, sticky='nsew')

                self.check_task_grid(self.tasks_frame)

    def task_frame(self):

        # get current dark or light mode for variables 
        current_color = self.m.color_choice()

        # Scrollable Frame for Tasks
        self.tasks_frame = ctk.CTkScrollableFrame(self.proj_frame, fg_color='#cccbc8')
        self.tasks_frame.grid(row=3, column=0, columnspan=4, rowspan=3, sticky='nsew', padx=10, pady=(0, 25))

        # Configure rows and columns for tasks_frame
        self.m.grid_configure(self.tasks_frame, self.rows, self.cols)
        
        # Tasks Label
        tasks_label = ctk.CTkLabel(self.proj_frame, text="Tasks:", text_color=None, font=('', 18, 'bold'))
        tasks_label.grid(row=2, column=0, columnspan=1, sticky='sw', padx=10, pady=10)

        # add task button
        add_task = ctk.CTkButton(self.proj_frame, text='Add Task', fg_color=self.MAIN_COLOR,
                                    width=12, height=8, command=lambda: self.task_popup_window())
        add_task.grid(row=2, column=3, columnspan=1, sticky='se', padx=10, pady=10)

        
        # sort task combobox
        sort_task = ctk.CTkComboBox(self.proj_frame, width=110, height=12,fg_color=self.MAIN_COLOR, bg_color=self.MAIN_COLOR, values=["Date Created", "Priority",  
                                    "Difficulty", "Completed", "Search Specific"], dropdown_fg_color=current_color,
                                    command= self.sort_task_combobox, text_color=self.TEXT_COLOR, state="readonly", corner_radius=0)
        sort_task.grid(row=2, column=3, sticky='sw', padx=10 , pady=10)
        sort_task.set("Date Created")

    # Create a popup window
    def task_popup_window(self):

        popup = ctk.CTkToplevel(self.proj_frame)
        popup.title("Add Task")
        popup.geometry("400x350")
        self.m.center_window(popup, 400, 350)
        popup.resizable(False, False)
        popup.attributes("-topmost", True)

        self.m.grid_configure(popup, 6, 2)

        # Task Name Input
        task_name_label = ctk.CTkLabel(popup, text="Task Name:", font=('', 14))
        task_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        task_name_entry = ctk.CTkEntry(popup, width=150)
        task_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Task Description Input
        task_desc_label = ctk.CTkLabel(popup, text="Task Description:", font=('', 14))
        task_desc_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        task_desc_entry = ctk.CTkTextbox(popup, width=150, height=75, wrap='word')
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

            # getting task details and creating a new task                
            task_name = task_name_entry.get()
            task_desc = task_desc_entry.get('1.0', 'end-1c')
            task_priority = priority_slider.get()
            task_difficulty = difficulty_slider.get()
            new_task = TasksModel.create_task(self.db, self.proj_id, task_name, task_desc, 
                                              task_priority, task_difficulty, self.current_color)
            
            # position task
            row_pos = self.num_of_task // self.cols
            col_pos = self.num_of_task % self.cols

            single_task_frame = ctk.CTkFrame(self.tasks_frame, fg_color='#cccbc8', width=75, height=100)  #'#cccbc8'
            single_task_frame.grid(row=row_pos, column=col_pos)
            self.m.grid_configure(single_task_frame, 2, 1)
            
            remove_task = ctk.CTkButton(single_task_frame, text='X', width=10, height=10, 
                                    fg_color="red", command= lambda: self.delete_task(single_task_frame, self.proj_id, new_task["taskID"])) # temp message
            remove_task.grid(row=1, column=1, sticky='ne', padx= 1, pady=1)
            click_task = ctk.CTkButton(single_task_frame, text=new_task["task_name"], text_color=self.m.get_contrasting_text_color(self.current_color),
                              width=50, height=50, corner_radius=15, fg_color=self.current_color,
                              hover_color=self.current_color, command = lambda: print(new_task["taskID"]))
            click_task._text_label.configure(wraplength=100, justify="center", padx=2, pady=2)
            click_task.grid(row=2, column=1, sticky='nsew')

            if self.num_of_task == (self.rows*self.cols):
                self.rows += 1
                self.update_task_grid(self.tasks_frame)
            self.num_of_task += 1

            # temp display of task details
            print(f"Task Name: {task_name}")
            print(f"Task Description: {task_desc}")
            print(f"Priority: {task_priority}")
            print(f"Difficulty: {task_difficulty}")
            popup.destroy()

        self.task_color_picker_button = ctk.CTkButton(popup, text='    ', fg_color=self.current_color,
                                                width=12, height=8, command= self.ask_color)
        self.task_color_picker_button.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

        done_button = ctk.CTkButton(popup, text="Done", command=on_done, fg_color=self.MAIN_COLOR)
        done_button.grid(row=5, column=0, padx=10, pady=20)

        # Cancel Button
        def on_cancel():
            popup.destroy()

        cancel_button = ctk.CTkButton(popup, text="Cancel", command=on_cancel, fg_color="gray")
        cancel_button.grid(row=5, column=1, padx=10, pady=20)
        
    # Check grid at start of app when loading projects
    def check_task_grid(self, window):
        if self.num_of_task == (self.rows*self.cols):
            self.rows += 1
            self.update_task_grid(window)
        elif self.num_of_task > (self.rows*self.cols):
            while self.num_of_task > (self.rows*self.cols):
                self.rows += 1
                self.update_task_grid(window)

    # Updating grid 
    def update_task_grid(self, window):
    
        # Update rows when adding during app usage
        for row in range(self.rows):
            window.rowconfigure(row, weight=1, uniform='a')
        # Update columns
        for col in range(self.cols):
            window.columnconfigure(col, weight=1, uniform='a')

    # simple method to show current combobox selection
    def sort_task_combobox(self, value):
        print(value)
            
    # reset the frame after every change
    def shift_tasks(self):
        task_count = 0
        for widget in self.tasks_frame.winfo_children():
            row_pos = task_count // self.cols
            col_pos = task_count % self.cols
            widget.grid(row=row_pos, column=col_pos)
            task_count += 1
        
        # Adjust the number of rows dynamically
        new_rows = (task_count + self.cols - 1) // self.cols  # Calculate required rows
        if new_rows < self.rows:  # Only shrink the grid if necessary
            self.rows = new_rows
            self.update_task_grid(self.tasks_frame)

    # delete task
    def delete_task(self, window, proj_id, taskID):
        print(f'Deleting from: {window}')
        print(f"Deleting task from database: TaskID={taskID}, ProjectID={proj_id}")
        window.destroy()
        self.shift_tasks()
        self.num_of_task -= 1
        TasksModel.delete_task(self.db, proj_id, taskID)

    # get progress percentage
    def get_progress(self):
        if self.num_of_task == 0:
            percentage = 0
        else:
            percentage = (TasksModel.completed_tasks(self.db, self.proj_id) / self.num_of_task) * 100
        
        return percentage 
        
    # select color for project buttons
    def ask_color(self):

        pick_color= AskColor() # Open color picker
        check = pick_color.get()
        if check != None:
            self.current_color = check # set the current color
            self.task_color_picker_button.configure(fg_color=self.current_color)
        else:
            self.current_color = self.current_color