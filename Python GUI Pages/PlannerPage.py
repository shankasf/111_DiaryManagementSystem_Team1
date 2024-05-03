import tkinter as tk
from tkinter import messagebox
import mysql.connector

class PlannerPage:
    def __init__(self, master, db_connection):
        self.master = master
        self.db_connection = db_connection
        self.last_task_id = self.get_last_task_id()  # initialize the last task ID

        self.master.title("Planner Page")
        self.master.geometry("1920x1080")
        self.master.configure(bg="light blue")

        self.title_label = tk.Label(master, text="Planner Page", font=("Arial", 24), bg="light blue")
        self.title_label.pack(pady=20)

        self.create_checklist_button = tk.Button(master, text="Create Checklist", command=self.create_checklist)
        self.create_checklist_button.pack(pady=5)

        self.edit_checklist_button = tk.Button(master, text="Edit Checklist", command=self.edit_checklist)
        self.edit_checklist_button.pack(pady=5)

        self.view_checklists_button = tk.Button(master, text="View Checklists", command=self.view_checklists)
        self.view_checklists_button.pack(pady=5)

        self.main_menu_button = tk.Button(master, text="Main Menu", command=self.return_to_main_menu)
        self.main_menu_button.pack(pady=5)

    def get_last_task_id(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT MAX(Task_ID) FROM Tasks")
        last_task_id = cursor.fetchone()[0]
        cursor.close()
        return last_task_id if last_task_id else 0

    def create_checklist(self):
        create_checklist_window = tk.Toplevel(self.master)
        create_checklist_window.title("Create Checklist")
        create_checklist_window.geometry("1920x1080")
        create_checklist_window.configure(bg="light blue")

        # title label for the Create Checklist page
        title_label = tk.Label(create_checklist_window, text="Checklist Creation", font=("Arial", 20), bg="light blue")
        title_label.pack(pady=20)

        checklist_name_label = tk.Label(create_checklist_window, text="Enter Checklist Name:", bg="light blue")
        checklist_name_label.pack()

        self.checklist_name_entry = tk.Entry(create_checklist_window)
        self.checklist_name_entry.pack()

        planner_id = 1

        save_button = tk.Button(create_checklist_window, text="Save", command=lambda: self.save_checklist(planner_id, create_checklist_window))
        save_button.pack(pady=5)

        back_button = tk.Button(create_checklist_window, text="Back", command=create_checklist_window.destroy)
        back_button.pack(pady=5)

    def add_task(self, planner_id, checklist_id):
        add_task_window = tk.Toplevel(self.master)
        add_task_window.title("Add Task")
        add_task_window.geometry("1920x1080")
        add_task_window.configure(bg="light blue")

        task_label = tk.Label(add_task_window, text="Enter Task:", bg="light blue")
        task_label.pack()

        self.task_entry = tk.Entry(add_task_window)
        self.task_entry.pack()

        # fetch existing tasks for the checklist
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT Task_Name FROM Tasks WHERE Checklist_ID = %s", (checklist_id,))
        existing_tasks = cursor.fetchall()
        cursor.close()

        tasks_label = tk.Label(add_task_window, text="Existing Tasks:", bg="light blue")
        tasks_label.pack()

        for task in existing_tasks:
            task_name = task[0]
            existing_task_label = tk.Label(add_task_window, text=task_name, bg="light blue")
            existing_task_label.pack()

        save_task_button = tk.Button(add_task_window, text="Save Task", command=lambda: self.save_task(planner_id, checklist_id, add_task_window))
        save_task_button.pack(pady=5)

        back_button = tk.Button(add_task_window, text="Back", command=add_task_window.destroy)
        back_button.pack(pady=5)

    def edit_checklist(self):
        # fetch the list of checklists from the database
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT Checklist_ID, Checklist_Name FROM Checklists")
        checklists = cursor.fetchall()
        cursor.close()

        edit_checklist_window = tk.Toplevel(self.master)
        edit_checklist_window.title("Edit Checklist")
        edit_checklist_window.geometry("1920x1080")
        edit_checklist_window.configure(bg="light blue")

        # title label for the Edit Checklist page
        title_label = tk.Label(edit_checklist_window, text="Checklist Editor", font=("Arial", 20), bg="light blue")
        title_label.pack(pady=20)

        checklist_label = tk.Label(edit_checklist_window, text="Select Checklist:", bg="light blue")
        checklist_label.pack()

        self.selected_checklist = tk.StringVar()
        self.selected_checklist.set("")  # set default value

        checklist_option_menu = tk.OptionMenu(edit_checklist_window, self.selected_checklist, *[""] + [checklist[1] for checklist in checklists])
        checklist_option_menu.pack()

        edit_checklist_button = tk.Button(edit_checklist_window, text="Edit Checklist", command=self.open_edit_checklist_window)
        edit_checklist_button.pack(pady=5)

        delete_checklist_button = tk.Button(edit_checklist_window, text="Delete Checklist", command=self.delete_checklist)
        delete_checklist_button.pack(pady=5)

        back_button = tk.Button(edit_checklist_window, text="Back", command=edit_checklist_window.destroy)
        back_button.pack(pady=5)

    def open_edit_checklist_window(self):
        checklist_name = self.selected_checklist.get()

        if not checklist_name:
            messagebox.showerror("Error", "Please select a checklist.")
            return

        cursor = self.db_connection.cursor()
        cursor.execute("SELECT Checklist_ID FROM Checklists WHERE Checklist_Name = %s", (checklist_name,))
        checklist_id = cursor.fetchone()[0]
        cursor.close()

        edit_checklist_window = tk.Toplevel(self.master)
        edit_checklist_window.title("Edit Checklist - " + checklist_name)
        edit_checklist_window.geometry("1920x1080")
        edit_checklist_window.configure(bg="light blue")

        # Title label for the Edit Checklist options
        title_label = tk.Label(edit_checklist_window, text="Click on one of these two options or go back", font=("Arial", 16), bg="light blue")
        title_label.pack(pady=20)

        edit_name_button = tk.Button(edit_checklist_window, text="Edit Checklist Name", command=lambda: self.edit_checklist_name(checklist_id, checklist_name))
        edit_name_button.pack(pady=5)

        add_task_button = tk.Button(edit_checklist_window, text="Add Task", command=lambda: self.add_task(1, checklist_id))  # Hardcoded Planner_ID for now
        add_task_button.pack(pady=5)

        back_button = tk.Button(edit_checklist_window, text="Back", command=edit_checklist_window.destroy)
        back_button.pack(pady=5)

    def edit_checklist_name(self, checklist_id, old_name):
        edit_name_window = tk.Toplevel(self.master)
        edit_name_window.title("Edit Checklist Name")
        edit_name_window.geometry("1920x1080")
        edit_name_window.configure(bg="light blue")

        new_name_label = tk.Label(edit_name_window, text="Enter New Checklist Name:", bg="light blue")
        new_name_label.pack()

        self.new_name_entry = tk.Entry(edit_name_window)
        self.new_name_entry.pack()

        save_button = tk.Button(edit_name_window, text="Save", command=lambda: self.save_checklist_name(checklist_id, old_name, edit_name_window))
        save_button.pack(pady=5)

        back_button = tk.Button(edit_name_window, text="Back", command=edit_name_window.destroy)
        back_button.pack(pady=5)

    def view_checklists(self):
        view_checklists_window = tk.Toplevel(self.master)
        view_checklists_window.title("View Checklists")
        view_checklists_window.geometry("1920x1080")
        view_checklists_window.configure(bg="light blue")

        # Title label for the View Checklists page
        title_label = tk.Label(view_checklists_window, text="Checklist Viewer", font=("Arial", 20), bg="light blue")
        title_label.pack(pady=20)

        # Fetch all checklists
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT Checklist_ID, Checklist_Name FROM Checklists")
        checklists = cursor.fetchall()
        cursor.close()

        self.selected_checklist_id = tk.StringVar(view_checklists_window)
        self.selected_checklist_id.set("")  # set default value

        checklist_option_menu = tk.OptionMenu(view_checklists_window, self.selected_checklist_id, *[""] + [str(checklist[0]) + " - " + checklist[1] for checklist in checklists])
        checklist_option_menu.pack()

        view_selected_checklist_button = tk.Button(view_checklists_window, text="View Selected Checklist", command=self.view_selected_checklist)
        view_selected_checklist_button.pack(pady=5)

        back_button = tk.Button(view_checklists_window, text="Back", command=view_checklists_window.destroy)
        back_button.pack(pady=5)

    def view_selected_checklist(self):
        selected_checklist_id = int(self.selected_checklist_id.get().split(" - ")[0])

        # Fetch checklist name
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT Checklist_Name FROM Checklists WHERE Checklist_ID = %s", (selected_checklist_id,))
        checklist_name = cursor.fetchone()[0]
        
        # Fetch tasks for the selected checklist
        cursor.execute("SELECT Task_Name FROM Tasks WHERE Checklist_ID = %s", (selected_checklist_id,))
        tasks = cursor.fetchall()
        cursor.close()

        # Display checklist and tasks
        view_selected_checklist_window = tk.Toplevel(self.master)
        view_selected_checklist_window.title("View Selected Checklist")
        view_selected_checklist_window.geometry("1920x1080")
        view_selected_checklist_window.configure(bg="light blue")

        checklist_label = tk.Label(view_selected_checklist_window, text="Checklist: " + checklist_name, bg="light blue")
        checklist_label.pack()

        tasks_label = tk.Label(view_selected_checklist_window, text="Tasks:", bg="light blue")
        tasks_label.pack()

        for task in tasks:
            task_name = task[0]
            task_label = tk.Label(view_selected_checklist_window, text=task_name, bg="light blue")
            task_label.pack()

        back_button = tk.Button(view_selected_checklist_window, text="Back", command=view_selected_checklist_window.destroy)
        back_button.pack(pady=5)

    def save_checklist_name(self, checklist_id, old_name, edit_name_window):
        new_name = self.new_name_entry.get()
        if not new_name:
            messagebox.showerror("Error", "Please enter a new checklist name.")
            return

        # update checklist name in the DB
        cursor = self.db_connection.cursor()
        cursor.execute("UPDATE Checklists SET Checklist_Name = %s WHERE Checklist_ID = %s", (new_name, checklist_id))
        self.db_connection.commit()
        cursor.close()

        messagebox.showinfo("Success", "Checklist name updated successfully.")
        edit_name_window.destroy()

    def delete_checklist(self):
        checklist_name = self.selected_checklist.get()

        if not checklist_name:
            messagebox.showerror("Error", "Please select a checklist.")
            return

        confirm = messagebox.askyesno("Delete Checklist", f"Are you sure you want to delete the checklist '{checklist_name}'? This action cannot be undone.")

        if confirm:
            cursor = self.db_connection.cursor()
            cursor.execute("DELETE FROM Checklists WHERE Checklist_Name = %s", (checklist_name,))
            self.db_connection.commit()
            cursor.close()

            messagebox.showinfo("Success", "Checklist deleted successfully.")

    def save_task(self, planner_id, checklist_id, add_task_window):
        task_name = self.task_entry.get()
        if not task_name:
            messagebox.showerror("Error", "Please enter a task.")
            return

        # increment the task ID
        self.last_task_id += 1

        # insert the new task into the DB with the current date
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO Tasks (Task_ID, Task_Name, Checklist_ID, Planner_ID, Creation_Date) VALUES (%s, %s, %s, %s, CURDATE())", (self.last_task_id, task_name, checklist_id, planner_id))
        self.db_connection.commit()
        cursor.close()

        messagebox.showinfo("Success", "Task added successfully.")
        add_task_window.destroy()

    def save_checklist(self, planner_id, create_checklist_window):
        checklist_name = self.checklist_name_entry.get()
        if not checklist_name:
            messagebox.showerror("Error", "Please enter a checklist name.")
            return

        # insert the new checklist into the DB
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO Checklists (Checklist_Name, Creation_Date, Checklist_Age, Task_Num, Planner_ID) VALUES (%s, CURDATE(), 1, 0, %s)", (checklist_name, planner_id))
        self.db_connection.commit()
        cursor.close()
        create_checklist_window.destroy()  # close the create checklist window
        self.edit_checklist()  # open the edit checklist window

    def return_to_main_menu(self):
        self.master.destroy()  # close the Planner Page window

def main():
    # establish connection to the MySQL DB
    db_connection = mysql.connector.connect(host="localhost", user="root", password="root", database="diary_management")

    root = tk.Tk()
    app = PlannerPage(root, db_connection)
    root.mainloop()

if __name__ == "__main__":
    main()
