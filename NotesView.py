import customtkinter as ctk
from Methods import Methods
from NotesModel import NotesModel
from ProfileView import ProfileView


class NotesView:

    MAIN_COLOR = '#39BCCE'
    SECONDARY_WHITE = '#f8f2f2'
    THIRD_GRAY = 'gray14'
    TEXT_COLOR = ('black', 'white')

    def __init__(self, window, database, curr_user, profile_view):

        self.window = window
        self.db = database
        self.curr_user = curr_user
        self.pv = profile_view
        self.cols = 1
        self.rows = 5
        self.get_num_notes = NotesModel.get_num_of_notes(self.db, self.curr_user)

        self.m = Methods()

    def get_current_notes(self):
        
        note_count = 0

        notes = NotesModel.get_notes(self.db, self.curr_user)
        with self.db.get_session() as session:
            for note in notes:
                session.add(note)
                print(f'Task: {note.note_name}')
                row_pos = note_count // self.cols
                col_pos = note_count % self.cols
                note_count += 1
                print(f'Row: {row_pos} and Column: {col_pos}')

                single_note_frame = ctk.CTkFrame(self.notes_frame, bg_color='transparent', fg_color='transparent')
                single_note_frame.grid(row=row_pos, column=col_pos, sticky='ew')

                self.m.grid_configure(single_note_frame, 2, 1)

                delete_note = ctk.CTkButton(single_note_frame,  text='X', width=10, height=10, 
                                        fg_color="red", command= lambda snf=single_note_frame, n_u_id= note.userID, 
                                        n_n_id=note.noteID: self.delete_note(snf,n_u_id, n_n_id))
                delete_note.grid(row=0, column=0, sticky='e', padx=5, pady=5)

                note_name = ctk.CTkLabel(single_note_frame, bg_color='transparent', fg_color='transparent',
                                        text=note.note_name, font=('', 14,'bold'))
                note_name.grid(row=0, column=0, sticky='w', padx=5, pady=5)

                #note_created= ctk.CTkLabel(single_note_frame, bg_color='transparent', fg_color='transparent', 
                #                    font=('', 14,'bold'), text=self.m.reformat_date(note.date_created))
                #note_created.grid(row=0, column=0, sticky='w', padx=(75, 0), pady=5)

                note_text = ctk.CTkLabel(single_note_frame, bg_color='transparent', fg_color='transparent',
                                        text=note.note_text, wraplength=370)
                note_text.grid(row=1, column=0, sticky='w', padx=5, pady=5)

                self.check_notes_grid(self.notes_frame)

    def create_notes_frame(self):

        # notes label
        notes_label = ctk.CTkLabel(self.window, text='Notes',
                                    text_color=self.TEXT_COLOR, font=('',20,'bold'))
        notes_label.grid(row=3, column=0, columnspan=3, sticky='news', pady=(15, 0))

        add_note = ctk.CTkButton(self.window, text=' + ', fg_color=self.MAIN_COLOR,
                                     width=12, height=8, command=lambda: self.add_note_popup())
        add_note.grid(row=3, column=0, columnspan=3, sticky='es', padx=(0,5), pady=(5, 0))

        # notes frame outline color
        notes_frame_bg = ctk.CTkFrame(self.window, bg_color='transparent',
                                    fg_color=self.MAIN_COLOR)
        notes_frame_bg.grid(row=4, column=0, rowspan=5, columnspan=3, sticky='news', pady=2, padx=2)

        # notes frame
        self.notes_frame = ctk.CTkScrollableFrame(self.window, bg_color='transparent',
                                    fg_color='transparent')
        self.notes_frame.grid(row=4, column=0, rowspan=5, columnspan=3, sticky='news', pady=5, padx=5)

        self.m.grid_configure(self.notes_frame, self.rows, self.cols, None, None, None)

    def add_note_popup(self):
        # Create the popup window
        popup = ctk.CTkToplevel(self.window)
        popup.title("Add Note")
        popup.geometry("400x300")
        popup.attributes("-topmost", True)
        popup.resizable(False, False)

        self.m.grid_configure(popup, 6, cols=2)
        # Title Label and Entry
        title_label = ctk.CTkLabel(popup, text="Title:", font=('', 14))
        title_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        title_entry = ctk.CTkEntry(popup, width=300)
        title_entry.grid(row=0, column=1, padx=10, pady=10)

        # Text Label and Scrollable Text Box
        text_label = ctk.CTkLabel(popup, text="Text:", font=('', 14))
        text_label.grid(row=2, column=0, padx=10, pady=10, sticky="nw")
        text_box = ctk.CTkTextbox(popup, wrap="word", width=300, height=175)
        text_box.grid(row=2, column=1, rowspan=3, padx=10, pady=10)

        # Done Button
        def on_done():

            title = title_entry.get()
            text = text_box.get('1.0', 'end-1c')  

            new_note = NotesModel.create_note(self.db, self.curr_user, title, text)
            # positioning notes
            row_pos = self.get_num_notes // self.cols
            col_pos = self.get_num_notes % self.cols

            single_note_frame = ctk.CTkFrame(self.notes_frame, bg_color='transparent', fg_color='transparent')
            single_note_frame.grid(row=row_pos, column=col_pos, sticky='ew')

            self.m.grid_configure(single_note_frame, 2, 1)

            delete_note = ctk.CTkButton(single_note_frame,  text='X', width=10, height=10, 
                                    fg_color="red", command= lambda: self.delete_note(single_note_frame,
                                    new_note['userID'], new_note['noteID']))
            delete_note.grid(row=0, column=0, sticky='e', padx=5, pady=5)

            note_name = ctk.CTkLabel(single_note_frame, bg_color='transparent', fg_color='transparent',
                                    text=new_note['note_name'], font=('', 14,'bold'))
            note_name.grid(row=0, column=0, sticky='w', padx=5, pady=5)

            #note_created= ctk.CTkLabel(single_note_frame, bg_color='transparent', fg_color='transparent', 
            #                        font=('', 14,'bold'), text=self.m.reformat_date(new_note['date_created']))
            #note_created.grid(row=0, column=0, sticky='w', padx=(75, 0), pady=5)

            note_text = ctk.CTkLabel(single_note_frame, bg_color='transparent', fg_color='transparent',
                                    text=new_note['note_text'], wraplength=370)
            note_text.grid(row=1, column=0, sticky='w', padx=5, pady=5)

            # check notes frame and update number of notes
            if self.get_num_notes == (self.rows*self.cols):
                self.rows += 1
                self.update_notes_grid(self.notes_frame, None, None)
            self.get_num_notes += 1
            self.pv.update_stats(num_notes=True)


        done_button = ctk.CTkButton(popup, text="Done", fg_color=self.MAIN_COLOR,
                                    command=lambda: self.m.check_text_length_warning(title_entry.get(), 30, 0, on_done, False))
        done_button.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        # Cancel Button
        def on_cancel():
            popup.destroy()  # Close the popup without saving

        cancel_button = ctk.CTkButton(popup, text="Cancel", fg_color="red", command=on_cancel)
        cancel_button.grid(row=5, column=1, padx=10, pady=10, sticky="e")

    # Check grid for needed updating
    def check_notes_grid(self, window):
        if self.get_num_notes == (self.rows*self.cols):
            self.rows += 1
            self.update_notes_grid(window, None, None)
        elif self.get_num_notes > (self.rows*self.cols):
            while self.get_num_notes > (self.rows*self.cols):
                self.rows += 1
                self.update_notes_grid(window, None, None)

    # updating grid
    def update_notes_grid(self, window, weight=1, uniform='a'):
    
        # Update rows when adding during app usage
        for row in range(self.rows):
            window.rowconfigure(row, weight=weight, uniform=uniform)
        # Update columns
        for col in range(self.cols):
            window.columnconfigure(col, weight=weight, uniform=uniform)

    # shift task after deletion
    def shift_tasks(self):
        note_count = 0
        for widget in self.notes_frame.winfo_children():
            row_pos = note_count // self.cols
            col_pos = note_count % self.cols
            widget.grid(row=row_pos, column=col_pos)
            note_count += 1
        
        # Adjust the number of rows dynamically
        new_rows = (note_count + self.cols - 1) // self.cols  # Calculate required rows
        if new_rows < self.rows:  # Only shrink the grid if necessary
            self.rows = new_rows
            self.update_notes_grid(self.notes_frame, None, None)

    # delete task and call helper methods
    def delete_note(self, frame, user_id, note_id):
        print(f'Deleting from: {frame}')
        print(f"Deleting task from database: userID={user_id}, noteID={note_id}")
        frame.destroy()
        self.shift_tasks()
        self.get_num_notes -= 1
        NotesModel.delete_note(self.db, user_id, note_id)
        self.pv.update_stats(num_notes=True)
