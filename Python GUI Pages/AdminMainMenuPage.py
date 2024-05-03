import tkinter as tk
from tkinter import messagebox
from Team1LoginPageTesting import *

import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        # Create connection to MySQL DB
        self.connection = mysql.connector.connect(
            host= "localhost",
            user= "root",
            password="C0mput3r$c13nc3",
            database='diary_management'
        )
        self.cursor = self.connection.cursor()

    def fetch_data(self, query):
        # Executes select query and fetches the data from DB
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute_query(self, query):
        # Executes query that modifies the DB
        self.cursor.execute(query)
        self.connection.commit()

    def close_connection(self):
        # Closes DB connection and cursor
        self.cursor.close()
        self.connection.close()

class AdminMenu(tk.Tk):
    def __init__(self, database):
        super().__init__()
        self.title("Administrator's Main Menu")
        self.geometry("1920x1080")
        self.db = database

        self.configure(bg="light blue")

        self.admin_menu_label = tk.Label(self, text="Administrator's Main Menu", font=("Helvetica", 16), bg="#ADD8E6")
        self.admin_menu_label.pack(pady=10)

        self.adminee_requests_button = tk.Button(self, text="Browse Adminee Requests", command=self.browse_requests)
        self.adminee_requests_button.pack(pady=5)

        self.view_adminees_button = tk.Button(self, text="View Established Adminees", command=self.view_adminees)
        self.view_adminees_button.pack(pady=5)

        self.logout_button = tk.Button(self, text="Logout", command=self.logout)
        self.logout_button.pack(pady=5)

        # Text widget to display fetched data
        self.data_text = tk.Text(self, width=50, height=10)
        self.data_text.pack()

    def browse_requests(self):
        # Fetch adminee requests from DB
        query = "SELECT * FROM Admin_Adminee_Requests"
        adminee_requests = self.db.fetch_data(query)
        
        # Clear old data
        self.data_text.delete(1.0, tk.END)
        
        # Display fetched data with accept and deny buttons
        for request in adminee_requests:
            if len(request) == 2:  # Check if request contains admin_id and creator_id only
                admin_id, creator_id = request
                
                # Display request details and buttons
                self.data_text.insert(tk.END, f"Admin ID: {admin_id}, Creator ID: {creator_id}\n")
                accept_button = tk.Button(self, text="Accept", command=lambda admin=admin_id, creator=creator_id: self.accept_request(admin, creator))
                accept_button.pack(side=tk.LEFT, padx=5)
                deny_button = tk.Button(self, text="Deny", command=lambda admin=admin_id, creator=creator_id: self.deny_request(admin, creator))
                deny_button.pack(side=tk.LEFT, padx=5)
                self.data_text.window_create(tk.END, window=accept_button)
                self.data_text.window_create(tk.END, window=deny_button)
            else:
                self.data_text.insert(tk.END, "Error\n")

    def view_adminees(self):
        # Fetches established adminees from the DB
        query = "SELECT * FROM Admin_Adminee_Established"
        adminees = self.db.fetch_data(query)

        # Clear old data
        self.data_text.delete(1.0, tk.END)
        
        for adminee in adminees:
            if len(adminee) >= 2:  # Check if adminee data contains admin_id and creator_id
                admin_id, creator_id = adminee[:2]  # Extract Admin ID and Creator ID
                self.data_text.insert(tk.END, f"Admin ID: {admin_id}, Creator ID: {creator_id}\n")
            else:
                self.data_text.insert(tk.END, "Error\n")


    def logout(self):
        # Closes window
        self.destroy()

    def accept_request(self, admin_id, creator_id):
        # Execute query to accept the request
        query = f"UPDATE Admin_Users SET Adminee_Status = 'Established' WHERE Admin_ID = {admin_id} AND Creator_ID = {creator_id}"
        self.db.execute_query(query)
        messagebox.showinfo("Success", "Request accepted successfully")
        self.browse_requests()  # Refresh the request list after accepting

    def deny_request(self, admin_id, creator_id):
        # Execute query to deny the request
        query = f"DELETE FROM Admin_Users WHERE Admin_ID = {admin_id} AND Creator_ID = {creator_id}"
        self.db.execute_query(query)
        messagebox.showinfo("Success", "Request denied successfully")
        self.browse_requests()  # Refresh the request list after denying

if __name__ == "__main__":
    # Connect to MySQL DB and put your own info
    db = Database(host="localhost", user="root", password="root", database="diary_management")
    app = AdminMenu(database=db)
    app.mainloop()

#AdminMenu.mainloop()
