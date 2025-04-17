import customtkinter as ctk
from Methods import Methods


class TaskView():

    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')

    def __init__(self, db, curr_user, proj_id, proj_win, task_win):

        self.db = db
        self.curr_user = curr_user
        self.proj_id = proj_id
        self.proj_win = proj_win
        self.task_win = task_win

        self.m = Methods()
    
    # Create a popup window
    def task_popup_window(self):

        popup = ctk.CTkToplevel(self.proj_win)
        popup.title("Add Task")
        popup.geometry("400x350")
        self.m.center_window(popup, 400, 350)
        popup.resizable(False, False)
        popup.lift()

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
        