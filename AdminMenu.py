def adminMenuFunction():
    class AdminMenu:
        def __init__(self, master, db_connection):
            self.master = master
            self.db_connection = db_connection

            self.master.title("Administrator's Main Menu")
            self.master.geometry("1920x1080")
            self.master.configure(bg="light blue")

            self.admin_menu_label = tk.Label(master, text="Administrator's Main Menu", font=("Helvetica", 16), bg="#ADD8E6")
            self.admin_menu_label.pack(pady=10)

            self.adminee_requests_button = tk.Button(master, text="Browse Adminee Requests", command=self.browse_requests)
            self.adminee_requests_button.pack(pady=5)

            self.view_adminees_button = tk.Button(master, text="View Established Adminees", command=self.view_adminees)
            self.view_adminees_button.pack(pady=5)

            self.logout_button = tk.Button(master, text="Logout", command=self.logout)
            self.logout_button.pack(pady=5)

            # Text widget to display fetched data
            self.data_text = tk.Text(master, width=50, height=10)
            self.data_text.pack()

        def browse_requests(self):
            # Fetch adminee requests from DB
            query = "SELECT * FROM Admin_Adminee_Requests"
            cursor = self.db_connection.cursor()
            cursor.execute(query)
            adminee_requests = cursor.fetchall()
            cursor.close()

            # Clear old data
            self.data_text.delete(1.0, tk.END)
            
            # Display fetched data with accept and deny buttons
            for request in adminee_requests:
                if len(request) == 2:  # Check if request contains admin_id and creator_id only
                    admin_id, creator_id = request
                    
                    # Display request details and buttons
                    self.data_text.insert(tk.END, f"Admin ID: {admin_id}, Creator ID: {creator_id}\n")
                    accept_button = tk.Button(self.master, text="Accept", command=lambda admin=admin_id, creator=creator_id: self.accept_request(admin, creator))
                    accept_button.pack(side=tk.LEFT, padx=5)
                    deny_button = tk.Button(self.master, text="Deny", command=lambda admin=admin_id, creator=creator_id: self.deny_request(admin, creator))
                    deny_button.pack(side=tk.LEFT, padx=5)
                    self.data_text.window_create(tk.END, window=accept_button)
                    self.data_text.window_create(tk.END, window=deny_button)
                else:
                    self.data_text.insert(tk.END, "Error\n")

        def view_adminees(self):
            # Fetches established adminees from the DB
            query = "SELECT * FROM Admin_Adminee_Established"
            cursor = self.db_connection.cursor()
            cursor.execute(query)
            adminees = cursor.fetchall()
            cursor.close()

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
            self.master.destroy()

        def accept_request(self, admin_id, creator_id):
            # Execute query to accept the request
            query = f"UPDATE Admin_Users SET Adminee_Status = 'Established' WHERE Admin_ID = {admin_id} AND Creator_ID = {creator_id}"
            cursor = self.db_connection.cursor()
            cursor.execute(query)
            self.db_connection.commit()
            cursor.close()
            messagebox.showinfo("Success", "Request accepted successfully")
            self.browse_requests()  # Refresh the request list after accepting

        def deny_request(self, admin_id, creator_id):
            # Execute query to deny the request
            query = f"DELETE FROM Admin_Users WHERE Admin_ID = {admin_id} AND Creator_ID = {creator_id}"
            cursor = self.db_connection.cursor()
            cursor.execute(query)
            self.db_connection.commit()
            cursor.close()
            messagebox.showinfo("Success", "Request denied successfully")
            self.browse_requests()  # Refresh the request list after denying

    def main():
        # Establish connection to the MySQL DB
        db_connection = mysql.connector.connect(host="localhost", user="root", password=databasePassword, database=databaseUsername)

        root = tk.Tk()
        app = AdminMenu(root, db_connection)
        root.mainloop()

    if __name__ == "__main__":
        main()