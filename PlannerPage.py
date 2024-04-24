import tkinter as tk
from tkinter import messagebox
import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        # initialize mySQL connection
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, values=None):
        # execute query that doesn't return results
        self.cursor.execute(query, values)
        self.connection.commit()

    def fetch_query(self, query, values=None):
        # execute query that returns results
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def close_connection(self):
        # close DB connection
        self.cursor.close()
        self.connection.close()

class PlannerApp:
    def __init__(self, master, db_connector):
        # initialize the main application window
        self.master = master
        self.master.title("Planner")
        self.master.geometry("1920x1080")  

        self.master.configure(bg="light blue")
        
        # connect to the MySQL database
        self.db_connector = db_connector
        
        # lists to store tasks and checklists
        self.tasks = []
        self.checklists = []

        # create GUI widgets
        self.create_widgets()
        # fetch planner information from the DB
        self.fetch_planner_info()

    def fetch_planner_info(self):
        # fetch planner information from the DB using the Planner_Info view
        query = "SELECT * FROM Planner_Info"
        planner_info = self.db_connector.fetch_query(query)
        for row in planner_info:
            # each row contains information about a planner, task, and checklist
            creator_id, planner_id, owner_id, task_id, checklist_id = row
            # here you can process the retrieved data as needed

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Planner Page", font=("Arial", 18))
        self.label.pack(pady=10)

        self.checklist_button = tk.Button(self.master, text="Create Checklist", command=self.create_checklist, font=("Arial", 12), padx=10, pady=5)
        self.checklist_button.pack()

        self.edit_button = tk.Button(self.master, text="Edit Checklists", command=self.edit_checklist, font=("Arial", 12), padx=10, pady=5)
        self.edit_button.pack()

        self.home_button = tk.Button(self.master, text="Home", command=self.go_home, font=("Arial", 12), padx=10, pady=5)
        self.home_button.pack()

    def create_checklist(self):
        # create a new checklist
        checklist_window = tk.Toplevel(self.master)
        checklist_window.title("Create Checklist")
        checklist_window.geometry("1920x1080")  # set window size
        checklist_window.configure(bg="light blue")

        label = tk.Label(checklist_window, text="Enter Checklist Name:")
        label.pack()

        checklist_entry = tk.Entry(checklist_window)
        checklist_entry.pack()

        def save_checklist():
            # save the new checklist to the DB
            name = checklist_entry.get()
            if name:
                # fetch the maximum Checklist_ID from the Checklists table
                max_checklist_id_query = "SELECT MAX(Checklist_ID) FROM Checklists"
                max_checklist_id = self.db_connector.fetch_query(max_checklist_id_query)[0][0] or 0
                checklist_id = max_checklist_id + 1
                
                # fetch the maximum Planner_ID from the Planners table
                max_planner_id_query = "SELECT MAX(Planner_ID) FROM Planners"
                max_planner_id = self.db_connector.fetch_query(max_planner_id_query)[0][0] or 0
                planner_id = max_planner_id + 1
                
                # fetch the maximum Task_Num for the given Planner_ID
                max_task_num_query = "SELECT MAX(Task_Num) FROM Planners WHERE Planner_ID = %s"
                max_task_num = self.db_connector.fetch_query(max_task_num_query, (planner_id,))[0][0] or 0
                task_num = max_task_num + 1

                # insert checklist into the Checklists table
                self.db_connector.execute_query("INSERT INTO Checklists (Checklist_ID, Planner_ID, Checklist_Name, Creation_Date, Checklist_Age, Task_Num) VALUES (%s, %s, %s, NOW(), 0, %s)", (checklist_id, planner_id, name, task_num))
                
                messagebox.showinfo("Success", "Checklist created successfully")
                checklist_window.destroy()
            else:
                messagebox.showerror("Error", "Checklist name cannot be empty")

        save_button = tk.Button(checklist_window, text="Save", command=save_checklist, font=("Arial", 12), padx=10, pady=5)
        save_button.pack()

        back_button = tk.Button(checklist_window, text="Back", command=checklist_window.destroy, font=("Arial", 12), padx=10, pady=5)
        back_button.pack()

    def edit_checklist(self):
        # create a window to select the checklist to edit
        edit_window = tk.Toplevel(self.master)
        edit_window.title("Edit Checklists")
        edit_window.geometry("1920x1080")

        edit_window.configure(bg="light blue")

        # fetch existing checklists from the DB
        query = "SELECT Checklist_ID, Checklist_Name FROM Checklists"
        checklists = self.db_connector.fetch_query(query)

        # create listbox to display existing checklists
        checklist_listbox = tk.Listbox(edit_window)
        for checklist in checklists:
            checklist_listbox.insert(tk.END, f"{checklist[0]}: {checklist[1]}")
        checklist_listbox.pack(padx=10, pady=10)

        def edit_selected_checklist():
            # Get the ID of the selected checklist
            selected_index = checklist_listbox.curselection()
            if selected_index:
                checklist_id = checklists[selected_index[0]][0]

                # open a window to edit the selected checklist
                edit_checklist_window = tk.Toplevel(self.master)
                edit_checklist_window.title("Edit Checklist")
                edit_checklist_window.geometry("1920x1080")

                # fetch the checklist details from the database
                query = "SELECT Checklist_Name FROM Checklists WHERE Checklist_ID = %s"
                checklist_name = self.db_connector.fetch_query(query, (checklist_id,))[0][0]

                # create an entry field to edit the checklist name
                label = tk.Label(edit_checklist_window, text="Enter New Checklist Name:")
                label.pack()

                checklist_entry = tk.Entry(edit_checklist_window)
                checklist_entry.insert(tk.END, checklist_name)
                checklist_entry.pack()

                def save_changes():
                    # save the edited checklist to the DB
                    new_name = checklist_entry.get()
                    if new_name:
                        self.db_connector.execute_query("UPDATE Checklists SET Checklist_Name = %s WHERE Checklist_ID = %s", (new_name, checklist_id))
                        messagebox.showinfo("Success", "Checklist updated successfully")
                        edit_checklist_window.destroy()
                    else:
                        messagebox.showerror("Error", "Checklist name cannot be empty")

                save_button = tk.Button(edit_checklist_window, text="Save", command=save_changes, font=("Arial", 12), padx=10, pady=5)
                save_button.pack()

            else:
                messagebox.showerror("Error", "Please select a checklist to edit")

        edit_button = tk.Button(edit_window, text="Edit Selected Checklist", command=edit_selected_checklist, font=("Arial", 12), padx=10, pady=5)
        edit_button.pack(pady=10)

        back_button = tk.Button(edit_window, text="Back", command=edit_window.destroy, font=("Arial", 12), padx=10, pady=5)
        back_button.pack()

    def go_home(self):
        # Placeholder for going to the home page
        print("Going to home page")

    def run(self):
        # run the main application loop
        self.master.mainloop()

if __name__ == "__main__":
    # initialize the DB connector
    db_connector = Database(host="localhost", user="root", password="root", database="diary_management")

    # create main application window
    root = tk.Tk()
    root.geometry("1920x1080")
    app = PlannerApp(root, db_connector)
    app.run()
