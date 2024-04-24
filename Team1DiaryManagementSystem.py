import tkinter as tk
from tkinter import *
import tkinter as tk
import mysql.connector
import tkinter.messagebox
from datetime import datetime

strikes = 0

def login():
    #Window Setup
    loginWindow = tk.Tk()
    loginWindow.title('Login')
    loginWindow.geometry('800x550')
    loginWindow.configure(bg = 'light blue')


    #Functions
    #The user gets three tries to enter the password. However, once they reach three strikes, the window will close

    def submit():
        #Python won't let you use a variable from outside the function unless you use this 'global' declaration in the function
        global strikes
        #You can't measure an entry's length by itself, but you can take it and apply it to another variable
        #Then you can measure, use, apply, etc the variable
        global username
        username = usernameInput.get()
        password = passwordInput.get()
        if len(username) == 0 or len(password) == 0:
            #The .config is how you change the labels after they are initially created
            blankSpace.config(bg = 'skyblue', fg = 'black', text = 'Please enter a username and password')
            warning.config(bg = '#F0F0F0', fg = '#F0F0F0')
            warningTitle.config(bg = '#F0F0F0', fg = '#F0F0F0')
        else:
            print(username)
            print(password)
            blankSpace.config(bg = '#F0F0F0', fg = '#F0F0F0')
            cursor.execute("""SELECT username, password FROM Users WHERE username=%s AND password=%s""", (username, password))
            #.fetchall prints all the results that cursor returned
            found = cursor.fetchall()
            #The user has three tries, then the application closes.
            if len(found) == 0:
                if strikes <= 1:
                    warning.config(bg = 'red', fg = 'black')
                    warningTitle.config(bg = 'red', fg = 'black')
                    strikes = strikes + 1
                    print(strikes)
                elif strikes == 2:
                    warning.config(text = 'The username or password\n is incorrect.\nYou have one attempt remaining.', bg = 'red', fg = 'black')
                    warningTitle.config(bg = 'red', fg = 'black')
                    strikes = strikes + 1
                    print(strikes)
                elif strikes == 3:
                    loginWindow.destroy();
                    quit()
            else:
                strikes = 0
                #Code to go to the main menu
                loginWindow.destroy();
                print("Made it past loginWindow.destroy")
                cursor.execute("""SELECT username FROM Users WHERE username=%s AND has_Admin = 'Yes'""", (username,))
                print("Made it past select")
                found = cursor.fetchall()
                if len(found) == 0:
                    userMainMenuFunction()
                elif len(found) == 1:
                    #AdminMenu.mainloop()
                    adminMenuFunction()
                else:
                    print('There has been an unexpected error. Please try again.')

    def databaseSubmit():
        global databaseUsername
        global databasePassword
        databaseUsername = usernameInput.get()
        databasePassword = passwordInput.get()

        global strikes
        
        if len(databaseUsername) == 0 or len(databasePassword) == 0:
            blankSpace.config(bg = 'skyblue', fg = 'black')
            warningTitle.config(bg = '#F0F0F0', fg = '#F0F0F0')
            warning.config(bg = '#F0F0F0', fg = '#F0F0F0')
        else:
            if databaseUsername == 'diary_management' and databasePassword == 'C0mput3r$c13nc3':
                strikes = 0
                databaseSubmitButton.destroy()
                blankSpace.config(bg = '#F0F0F0', fg = '#F0F0F0')
                warningTitle.config(bg = '#F0F0F0', fg = '#F0F0F0')
                warning.config(bg = '#F0F0F0', fg = '#F0F0F0')
        
                #submitButton = tk.Button(loginWindow, text = 'Submit', width = 20, padx = 30, bg = 'blue', fg = 'white', command = submit).place(x = 280, y = 210)
                submitButton.place(x = 280, y = 210)
                title.config(text = 'Login', fg = 'black', bg = 'lightgrey')
                usernameLabel.config(text = 'Username')
                usernameLabel.place(x = 220, y = 120)
                createAccountButton.place(x = 280, y = 460)
                #Clears the usernameInput and passwordInput fields
                usernameInput.delete(0, END)
                passwordInput.delete(0, END)

                #If having trouble connecting, check that the user and password are correct
                global db
                global cursor
                db = mysql.connector.connect (
                    host = "localhost",
                    #Username and password must be the same as in mySQL
                    user = "root",
                    password = databasePassword,
                    database = databaseUsername
                    #password = "C0mput3r$c13nc3",
                    #database = "diary_management"
                    )

                cursor = db.cursor()
            else:
                blankSpace.config(bg = '#F0F0F0', fg = '#F0F0F0')
                if strikes <= 1:
                    warningTitle.config(bg = 'red', fg = 'black')
                    warning.config(bg = 'red', fg = 'black')
                    strikes = strikes + 1
                    print(strikes)
                elif strikes == 2:
                    warningTitle.config(bg = 'red', fg = 'black')
                    warning.config(text = 'The username or password\n is incorrect.\nYou have one attempt remaining.', bg = 'red', fg = 'black')
                    strikes = strikes + 1
                    print(strikes)
                elif strikes == 3:
                    loginWindow.destroy();
                    quit()
        
    def createAccountPage():
        usernameInput.delete(0, END)
        passwordInput.delete(0, END)
    
        submitButton.place_forget()
        createAccountButton.place_forget()
        warningTitle.place_forget()
        warning.place_forget()
        blankSpace.place_forget()
    
        passwordCheckLabel.place(x = 220, y = 200)
        passwordCheckInput.place(x = 320, y = 200)
        submitAccountButton.place(x = 280, y = 250)
        backButton.place(x = 280, y = 460)
        
    def createAccount():
        global username
        username = usernameInput.get()
        password = passwordInput.get()
        passwordCheck = passwordCheckInput.get()

        cursor.execute("""SELECT username FROM Users WHERE username=%s""", (username,))
        found = cursor.fetchall()

        if len(username) == 0 or len(password) == 0 or len(passwordCheck) == 0:
            createAccountNotification.place(x = 275, y = 300)
            createAccountNotification.config(text = 'Please enter information\n into all three fields.')
        elif len(found) != 0:
            createAccountNotification.place(x = 275, y = 300)
            createAccountNotification.config(text = 'Unfortunately, this username\n has already been taken.\nPlease select a different one.')
        elif len(found) == 0:
            if password != passwordCheck:
                createAccountNotification.place(x = 275, y = 300)
                createAccountNotification.config(text = 'The entered passwords do not match.')
            else:
                from random import randint
                num = randint(1, 100) 
                print(num)
            
                cursor.execute("""SELECT username FROM Users WHERE user_id=%s""", (num,))
                found = cursor.fetchall()
                while len(found) != 0:
                    num = randint(1, 100)
                    print(num)

                    cursor.execute("""SELECT username FROM Users WHERE user_id=%s""", (num,))
                    found = cursor.fetchall()
                    if len(found) == 0:
                        break;
                date = datetime.today().strftime('%Y-%m-%d')
                print(date)

                cursor.execute("""INSERT into Creators(Creator_ID, Creator_Type) value (%s, 'User')""", (num,))
                cursor.execute("""INSERT into users(user_id, username, password, has_admin, admin_id, creation_date, account_age) value (%s, %s, %s, 'No', null, %s, 0)""", (num, username, password, date))
                cursor.execute("""SELECT user_id, username, password, has_admin, admin_id, creation_date, account_age FROM Users WHERE username=%s""", (username,))
                found = cursor.fetchall()
                print(found)

                #Go to user main page here
                loginWindow.destroy();
                userMainMenuFunction()
                #exec(open("Team1UserMainPage.py").read())

    def backToLogin():
        usernameInput.delete(0, END)
        passwordInput.delete(0, END)
        passwordCheckInput.delete(0, END)
    
        submitButton.place(x = 280, y = 210)
        createAccountButton.place(x = 280, y = 460)
        blankSpace.place(x = 255, y = 250)
        blankSpace.config(bg = '#F0F0F0', fg = '#F0F0F0')
    
        warning.place(x = 275, y = 320)
        warningTitle.place(x = 275, y = 300)
        warningTitle.config(bg = '#F0F0F0', fg = '#F0F0F0')
        warning.config(bg = '#F0F0F0', fg = '#F0F0F0')
    
        passwordCheckLabel.place_forget()
        passwordCheckInput.place_forget()
        submitAccountButton.place_forget()
        backButton.place_forget()
        createAccountNotification.place_forget()

    def exitFunction():
        loginWindow.destroy()
        quit()

    
    #Visuals Setup
        #Note: It is important to separate .grid and .place from the original section, otherwise we cannot get the values from the Entry objects
    exitButton = tk.Button(loginWindow, text = 'Exit', width = 10, padx = 10, bg = 'darkred', fg = 'white', command = exitFunction)
    exitButton.pack(side = TOP, anchor = NE)

    whiteSection = tk.Label(loginWindow, width = 50, height = 26, text = '', bg = '#F0F0F0')
    whiteSection.place(x =200, y = 50)

    title = tk.Label(loginWindow, width = 35, height = 2, text = 'Enter Database Credentials', font=('Arial', 12, 'bold'), fg = 'white', bg = 'black')
    title.place(x = 200, y = 50)

    usernameLabel = tk.Label(loginWindow, width = 15, height = 1, text = 'Database Name')
    usernameLabel.place(x = 210, y = 120)
    passwordLabel = tk.Label(loginWindow, width = 10, height = 1, text = 'Password')
    passwordLabel.place(x = 240, y = 160)

    usernameInput = tk.Entry(loginWindow, width = 30)
    usernameInput.place(x = 320, y = 120)
    passwordInput = tk.Entry(loginWindow, width = 30, show = '*')
    passwordInput.place(x = 320, y = 160)

    databaseSubmitButton = tk.Button(loginWindow, text = 'Submit', width = 20, bg = 'grey', padx = 30, command = databaseSubmit)
    #This button needs to use .pack() so that it can be destroyed later on
    databaseSubmitButton.pack(side=TOP, anchor=NW, padx = 280, pady = 185)

    submitButton = tk.Button(loginWindow, text = 'Submit', width = 20, padx = 30, bg = 'blue', fg = 'white', command = submit)
    submitButton.place(x = 280, y = 210)
    submitButton.place_forget()

    #bg = 'skyblue', fg = 'black'
    blankSpace = tk.Label(loginWindow, text = 'Please enter a database name and password', width = 35, height = 2, bg = '#F0F0F0', fg = '#F0F0F0')
    blankSpace.place(x = 255, y = 250)

    warning = tk.Label(loginWindow, width = 30, height = 6, text = 'The username or password\n is incorrect.\nPlease try again.', bg = '#F0F0F0', fg = '#F0F0F0')
    warning.place(x = 275, y = 320)
    warningTitle = tk.Label(loginWindow, width = 14, height = 1, text = 'Warning', font=('Arial', 18, 'bold'), bg = '#F0F0F0', fg = '#F0F0F0')
    warningTitle.place(x = 275, y = 300)

    #Create Account
    createAccountButton = tk.Button(loginWindow, text = "Don't have an account?\nCreate one now!", width = 20, bg = 'green', fg = 'white', padx = 30, command = createAccountPage)
    createAccountButton.place(x = 280, y = 460)
    createAccountButton.place_forget()

    backButton = tk.Button(loginWindow, text = "Back", width = 20, bg = 'blue', fg = 'white', padx = 30, command = backToLogin)
    backButton.place(x = 280, y = 460)
    backButton.place_forget()

    passwordCheckLabel = tk.Label(loginWindow, width = 12, height = 1, text = 'Check Password')
    passwordCheckLabel.place(x = 200, y = 200)
    passwordCheckLabel.place_forget()

    passwordCheckInput = tk.Entry(loginWindow, width = 30, show = '*')
    passwordCheckInput.place(x = 320, y = 200)
    passwordCheckInput.place_forget()

    submitAccountButton = tk.Button(loginWindow, text = "Submit", width = 20, bg = 'blue', fg = 'white', padx = 30, command = createAccount)
    submitAccountButton.place(x = 280, y = 250)
    submitAccountButton.place_forget()

    createAccountNotification = tk.Label(loginWindow, width = 30, height = 6, text = 'Unfortunately, this username\n has already been taken.\nPlease select a different one.', bg = 'skyblue')
    createAccountNotification.place(x = 275, y = 300)
    createAccountNotification.place_forget()


def userMainMenuFunction():

    #from loginPage import *
    #from records import *
    #from planner import *

    userMainMenu = tk.Tk()
    userMainMenu.title('User Main Menu')
    userMainMenu.geometry('1500x700')
    userMainMenu.config(bg='light blue')

    # temp for testing until i can connect to login user
    #username = "jakie"

    userMainMenu.grid_rowconfigure(0, weight=1)
    userMainMenu.grid_columnconfigure(0, weight=1)

    #db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

    #cursor = db.cursor()


    # Welcome
    LT = tk.Label(userMainMenu, text="Welcome!", font=('Times', 50))
    LT.grid(row=0, column=0)
    # LT.pack(side=TOP, expand=True, fill=None)
    # LT.pack(expand=True)
    LT.config(bg="light blue", fg="white")

    # Menu Intro
    LT0 = tk.Label(userMainMenu, text="Main Menu", font=('Times', 25))
    # LT0.pack(side=TOP, expand=True)
    LT0.grid(row=1, column=0)
    LT0.config(bg="light blue", fg="white")

    # Profile display

    # username
    LT2 = tk.Label(userMainMenu, text=username, font=('Times', 20))
    # LT2.pack(side=tk.TOP, expand=False, fill=None)
    LT2.grid(row=2, column=0)
    LT2.config(bg="light blue", fg="White")


    # # user_id
    # def get_userID():
    #     user_id = cursor.execute("""Select User_ID from Users where Username = %s""", (username,))
    #     userIdResult = cursor.fetchall()
    #
    #     LT1 = tk.Label(userMainMenu, text=userIdResult, font=('Times', 20))
    #     # LT1.pack(side=tk.TOP, expand=False, fill=None)
    #     LT1.config(bg="light blue", fg="White")

    def diary():
        # connect ot the database
        db = mysql.connector.connect(host="localhost", user="root", password=databasePassword, database=databaseUsername)

        # create cursor
        cursor = db.cursor()

        userMainMenu.destroy()
        print('made it past userMainMenu.destroy()')
        diaryFunction()
        print('opened diary.py')

        # Commit Changes
        db.commit()
        # Close Connection
        db.close()


    # diary button
    diaryBtn = Button(userMainMenu, text="Open Diary", command=diary)
    diaryBtn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # Record function
    def viewRecords():
        # connect ot the database
        db = mysql.connector.connect(host="localhost", user="root", password=databasePassword, database=databaseUsername)

        # create cursor
        cursor = db.cursor()

        recordWindow = Toplevel(userMainMenu)
        recordWindow.title("Records")
        recordWindow.geometry("1500x700")

        # view records
        cursor.execute("SELECT * FROM Records")
        recordsFetch = cursor.fetchall()
        print(recordsFetch)

        print_records = ' '

        # loop through records
        for record in recordsFetch:
            print_records += str('Record Name: ' + record[6] + '\n' + 'Record Description: ' + record[7]) + '\n'

        record_label = Label(recordWindow, text=print_records)
        record_label.grid(row=5, column=2, columnspan=2)
        record_label.grid_rowconfigure(1, weight=1)
        record_label.grid_columnconfigure(1, weight=1)

        # Commit Changes
        db.commit()

        # Close Connection
        db.close()


    # record button
    viewRecordsBtn = Button(userMainMenu, text="View Records", command=viewRecords)
    viewRecordsBtn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    # create record function
    def createRecords():
        # connect ot the database
        db = mysql.connector.connect(host="localhost", user="root", password=databasePassword, database=databaseUsername)

        # create cursor
        cursor = db.cursor()

        userMainMenu.destroy()
        print('made it past userMainMenu.destroy()')
        recordsFunction()
        print('opened records.py')

        # Commit Changes
        db.commit()
        # Close Connection
        db.close()


    # create record button
    createRecordsBtn = Button(userMainMenu, text="Create Records", command=createRecords)
    createRecordsBtn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    # admin function
    def viewAdmins():
        # connect ot the database
        db = mysql.connector.connect(host="localhost", user="root", password=databasePassword, database=databaseUsername)

        # create cursor
        cursor = db.cursor()

        adminWindow = Toplevel(userMainMenu)
        adminWindow.title("Admins")
        adminWindow.geometry("200x200")

        # view records
        cursor.execute("SELECT * FROM Admins")
        admins = cursor.fetchall()
        print(admins)

        print_admins = ' '

        # loop through records
        for admin in admins:
            print_admins += str('Admin Name: ' + admin[1]) + '\n'
        admin_label = Label(adminWindow, text=print_admins)
        admin_label.grid(row=4, column=3, columnspan=2)

        # Commit Changes
        db.commit()
        # Close Connection
        db.close()


    # admin button
    viewAdminsBtn = Button(userMainMenu, text="View Admins", command=viewAdmins)
    viewAdminsBtn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    # planner function
    def viewPlanner():
        # connect ot the database
        db = mysql.connector.connect(host="localhost", user="root", password=databasePassword, database=databaseUsername)

        # create cursor
        cursor = db.cursor()

        userMainMenu.destroy()
        print('made it past userMainMenu.destroy()')
        galleriesFunction()
        print('opened galleries.py')


    # planner button
    viewPlannerBtn = Button(userMainMenu, text="View Planner", command=viewPlanner)
    viewPlannerBtn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    # group function

    def viewGroups():
        # connect ot the database
        db = mysql.connector.connect(host="localhost", user="root", password=databasePassword, database=databaseUsername)

        # create cursor
        cursor = db.cursor()

        groupsWindow = Toplevel(userMainMenu)
        groupsWindow.title("Groups")
        groupsWindow.geometry("200x200")

        # view records
        cursor.execute("SELECT * FROM _groups")
        _groups = cursor.fetchall()
        print(_groups)

        print_groups = 0

        # loop through records
        for group in _groups:
            print_groups += group[0]
            # print_groups += str('Group Name: ') + '\n'
        groupID_label = Label(groupsWindow, text='Group IDS: ')
        groupID_label.grid(row=7, column=0, columnspan=2)
        group_label = Label(groupsWindow, text=print_groups)
        group_label.grid(row=8, column=0, columnspan=2)

        # Commit Changes
        db.commit()
        # Close Connection
        db.close()


    # view group button
    viewPlannerBtn = Button(userMainMenu, text="View Groups", command=viewGroups)
    viewPlannerBtn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    def createGroups():
        # connect ot the database
        db = mysql.connector.connect(host="localhost", user="root", password=databasePassword, database=databaseUsername)

        # create cursor
        cursor = db.cursor()

        userMainMenu.destroy()
        print('made it past userMainMenu.destroy()')
        groupMainMenuFunction()
        print('opened groups.py')

        # Commit Changes
        db.commit()
        # Close Connection
        db.close()

    # create group button
    createGroupsBtn = Button(userMainMenu, text="Create Groups", command=createGroups)
    createGroupsBtn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # logout function
    def logout():
        # connect ot the database
        #db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

        # create cursor
        #cursor = db.cursor()

        userMainMenu.destroy()
        login()
        print('made it past userMainMenu.destroy()')
        print('opened loginPage.py')


    # logout button
    logoutButton = Button(userMainMenu, text="Logout", command=logout)
    logoutButton.grid(row=10, column=0)

    # logoutButton = tk.Button(text="Logout", width=15, height=2, bg="blue", fg="black")
    # logoutButton.pack(side=tk.BOTTOM, expand=False, fill=None)


    print(db.is_connected())
    userMainMenu.mainloop()


def adminMenuFunction():
    class Database:
        #def __init__(self, host, user, password, database):
            # Create connection to MySQL DB
            #self.connection = mysql.connector.connect(
                #host= "localhost",
                #user= "root",
                #password="C0mput3r$c13nc3",
                #database='diary_management'
            #)
            #self.cursor = self.connection.cursor()

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
            login()

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
        #db = Database(host="localhost", user="root", password="root", database="diary_management")
        app = AdminMenu(database=db)
        app.mainloop()


def groupMainMenuFunction():
    groupMainMenu = tk.Tk()
    groupMainMenu.title('Group Main Menu')
    groupMainMenu.geometry('1500x700')
    groupMainMenu.config(bg='light blue')

    #db = mysql.connector.connect(
        #host="localhost",
        #user="root",
        #password="Jackie2013",
        #database="diary_management"
    #)

    #cursor = db.cursor()

    def logout():
        groupMainMenu.destroy()
        login()

    def backToMainMenu():
        groupMainMenu.destroy()
        userMainMenuFunction()

    backButton = tk.Button(groupMainMenu, text = 'Back', width = 10, padx = 10, bg = 'darkred', fg = 'white', command = backToMainMenu)
    backButton.pack(side = TOP, anchor = NW)

    #Welcome
    LT = tk.Label(groupMainMenu, text="Group Main Page", font=('Times', 50))
    # LT.pack(side=TOP, expand=True, fill=None)
    LT.pack(expand=True)
    LT.config(bg="light blue", fg="white")

    #Profile
    LT2 = tk.Label(groupMainMenu, text="GroupName = Team1", font=('Times', 20))
    LT2.pack(side=tk.TOP, expand=False, fill=None)
    LT2.config(bg="light blue", fg="White")

    LT1 = tk.Label(groupMainMenu, text="Member Count = 3", font=('Times', 20))
    LT1.pack(side=tk.TOP, expand=False, fill=None)
    LT1.config(bg="light blue", fg="White")

    LT3 = tk.Label(groupMainMenu, text="Group Members = Karina01, Jay02, Fin20", font=('Times', 20))
    LT3.pack(side=tk.TOP, expand=False, fill=None)
    LT3.config(bg="light blue", fg="White")

    #Menu Intro
    LT0 = tk.Label(groupMainMenu, text="Main Menu", font=('Times', 25))
    LT0.pack(side=TOP, expand=True)
    LT0.config(bg="light blue", fg="white")

    #Planner
    plannerValues=["View Group Planner"]

    variable1 = StringVar(groupMainMenu)
    variable1.set("Planner")

    p = OptionMenu(groupMainMenu, variable1, *plannerValues)
    p.pack(side=tk.TOP, expand=False, fill=None)
    p.config(width=33, height=4, bg="light blue", fg="black")

    #Group Diary
    groupValues=["View Group Diary"]

    variable2 = StringVar(groupMainMenu)
    variable2.set("Group")

    g = OptionMenu(groupMainMenu, variable2, *groupValues)
    g.pack(side=tk.TOP, expand=False, fill=None)
    g.config(width=34, height=4, bg="light blue", fg="black")


    #Admin
    adminValues=["View Admins", "Admin Requests"]

    variable3 = StringVar(groupMainMenu)
    variable3.set("Admin")

    a = OptionMenu(groupMainMenu, variable3, *adminValues)
    a.pack(side=tk.TOP, expand=False, fill=None)
    a.config(width=34, height=4, bg="light blue", fg="black")

    #logout button
    logoutButton = tk.Button(text="Logout", width=15, height=2, bg="blue", fg="black", command = logout)
    logoutButton.pack(side=tk.BOTTOM, expand=False, fill=None)


def recordsFunction():
    createrecordPage = tk.Tk()
    createrecordPage.title('Records Page')
    createrecordPage.geometry('1500x700')
    createrecordPage.config(bg='light blue')

    createrecordPage.grid_rowconfigure(0, weight=1)
    createrecordPage.grid_columnconfigure(0, weight=1)

    #db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

    #cursor = db.cursor()


    # create function

    def create():
        #db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

        #cursor = db.cursor()

        record_ID1 = recordID.get()
        record_name1 = recordName.get()
        diary_ID1 = diaryID.get()
        in_gallery1 = inGallery.get()
        creation_date1 = creationDate.get()
        record_age1 = recordAge.get()
        record_description1 = recordDescription.get()
        gallery_ID1 = galleryID.get()

        cursor.execute("""insert into records(record_id, diary_id, in_gallery, gallery_id, creation_date, record_age, record_name, record_decription)values"
                   "(%s, %s, %s, %s, %s, %s, %s, %s)""",
                   (record_ID1, diary_ID1, in_gallery1, gallery_ID1, date, record_age1, record_name1,
                    record_description1))

        db.commit()
        db.close()

        # Clear textbox
        recordName.delete(0, END)
        recordID.delete(0, END)
        diaryID.delete(0, END)
        inGallery.delete(0, END)
        galleryID.delete(0, END)
        creationDate.delete(0, END)
        recordAge.delete(0, END)
        recordDescription.delete(0, END)

    def backToMainMenu():
        createrecordPage.destroy()
        userMainMenuFunction()

    # Intro
    intro = tk.Label(createrecordPage, text="Create Record", font=('Helvetica', 40))
    # intro.rowconfigure(1, weight=1)
    # intro.columnconfigure(1, weight=1)
    intro.grid(row=0, column=0, columnspan=3, pady=10, padx=10, ipadx=100)
    intro.config(bg="light blue", fg="white")

    # create textboxes
    recordID = Entry(createrecordPage, width=10)
    recordID.grid(row=2, column=0, padx=20)

    diaryID = Entry(createrecordPage, width=10)
    diaryID.grid(row=4, column=0, padx=20)

    galleryID = Entry(createrecordPage, width=10)
    galleryID.grid(row=6, column=0, padx=20)

    recordName = Entry(createrecordPage, width=15)
    recordName.grid(row=8, column=0, padx=20)

    #creationDate = Entry(createrecordPage, width=15)
    #creationDate.grid(row=10, column=0, padx=20)

    recordAge = Entry(createrecordPage, width=15)
    recordAge.grid(row=12, column=0, padx=20)

    inGallery = Entry(createrecordPage, width=15)
    inGallery.grid(row=14, column=0, padx=20)

    recordDescription = Entry(createrecordPage, width=30)
    recordDescription.grid(row=16, column=0, padx=20)

    # create textbox labels
    recordIDLabel = Label(createrecordPage, text="Record ID:")
    recordIDLabel.grid(row=1, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    diaryIDLabel = Label(createrecordPage, text="Diary ID:")
    diaryIDLabel.grid(row=3, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    galleryIDLabel = Label(createrecordPage, text="Gallery ID:")
    galleryIDLabel.grid(row=5, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    recordNameLabel = Label(createrecordPage, text="Record Name:")
    recordNameLabel.grid(row=7, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    date = datetime.today().strftime('%Y-%m-%d')
    #creationDateLabel = Label(createrecordPage, text="Creation Date:")
    #creationDateLabel.grid(row=9, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    recordAgeLabel = Label(createrecordPage, text="Record Age:")
    recordAgeLabel.grid(row=11, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    inGalleryLabel = Label(createrecordPage, text="In Gallery:")
    inGalleryLabel.grid(row=13, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    recordDescriptionLabel = Label(createrecordPage, text="Record Description:")
    recordDescriptionLabel.grid(row=15, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    # create button
    createBtn = Button(createrecordPage, text="Create", command=create)
    createBtn.grid(row=17, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    backButton = tk.Button(createrecordPage, text = 'Back', width = 10, padx = 10, bg = 'darkred', fg = 'white', command = backToMainMenu)
    backButton.grid(row=0, column=0, sticky = 'nw')

    createrecordPage.mainloop()

    db.commit()
    db.close()


def galleriesFunction():
    creategalleriePage = tk.Tk()
    creategalleriePage.title('Records Page')
    creategalleriePage.geometry('1500x700')
    creategalleriePage.config(bg='light blue')

    creategalleriePage.grid_rowconfigure(0, weight=1)
    creategalleriePage.grid_columnconfigure(0, weight=1)

    #db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

    #cursor = db.cursor()


    # create function

    def create():
        #db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

        #cursor = db.cursor()


        galleryId2 = galleryID.get()
        diaryID2 = diaryID.get()
        creationDate2 = creationDate.get()
        galleryName2 = galleryName.get()
        galleryAge2 = galleryAge.get()
        galleryNum2 = galleryNum.get()

    def backToMainMenu():
        creategalleriePage.destroy()
        userMainMenuFunction()

                #not done yet
    #####################################################


    # Intro
    intro = tk.Label(creategalleriePage, text="Create Gallery", font=('Helvetica', 40))
    # intro.rowconfigure(1, weight=1)
    # intro.columnconfigure(1, weight=1)
    intro.grid(row=0, column=0, columnspan=3, pady=10, padx=10, ipadx=100)
    intro.config(bg="light blue", fg="white")

    # create textboxes
    galleryID = Entry(creategalleriePage, width=10)
    galleryID.grid(row=2, column=0, padx=20)

    diaryID = Entry(creategalleriePage, width=10)
    diaryID.grid(row=4, column=0, padx=20)

    creationDate = Entry(creategalleriePage, width=10)
    creationDate.grid(row=6, column=0, padx=20)

    galleryName = Entry(creategalleriePage, width=15)
    galleryName.grid(row=8, column=0, padx=20)

    galleryAge = Entry(creategalleriePage, width=15)
    galleryAge.grid(row=10, column=0, padx=20)

    recordNum = Entry(creategalleriePage, width=15)
    recordNum.grid(row=12, column=0, padx=20)

    # create textbox labels
    galleryIDLabel = Label(creategalleriePage, text="Gallery ID:")
    galleryIDLabel.grid(row=1, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    diaryIDLabel = Label(creategalleriePage, text="Diary ID:")
    diaryIDLabel.grid(row=3, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    creationDateLabel = Label(creategalleriePage, text="Creation Date:")
    creationDateLabel.grid(row=5, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    galleryNameLabel = Label(creategalleriePage, text="Gallery Name:")
    galleryNameLabel.grid(row=7, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    galleryAgeLabel = Label(creategalleriePage, text="Gallery Age:")
    galleryAgeLabel.grid(row=9, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    recordNumLabel = Label(creategalleriePage, text="Record Number:")
    recordNumLabel.grid(row=11, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    # create button
    createBtn = Button(creategalleriePage, text="Create", command=create)
    createBtn.grid(row=17, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    backButton = tk.Button(creategalleriePage, text = 'Back', width = 10, padx = 10, bg = 'darkred', fg = 'white', command = backToMainMenu)
    backButton.grid(row=0, column=0, sticky = 'nw')

    creategalleriePage.mainloop()

    db.commit()
    db.close()


def diaryFunction():
    diaryPage = tk.Tk()
    diaryPage.title('Diary Page')
    diaryPage.geometry('1500x700')
    diaryPage.config(bg='light blue')

    #db = mysql.connector.connect(
        #host="localhost",
        #user="root",
        #password="Jackie2013",
        #database="diary_management"
    #)

    #cursor = db.cursor()

    diaryPage.grid_rowconfigure(0, weight=1)
    diaryPage.grid_columnconfigure(0, weight=1)

    # Welcome
    intro = tk.Label(diaryPage, text="Welcome to your Diary!", font=('Helvetica', 45))
    intro.rowconfigure(1, weight=1)
    intro.columnconfigure(1, weight=1)
    intro.grid(row=0, column=0)
    intro.config(bg="light blue", fg="white")


    # view records function
    def viewRecords():
        # connect ot the database
        db = mysql.connector.connect(host="localhost", user="root", password=databasePassword, database=databaseUsername)

        # create cursor
        cursor = db.cursor()

        recordWindow = Toplevel(diaryPage)
        recordWindow.title("Records")
        recordWindow.geometry("200x200")

        # view records
        cursor.execute("SELECT * FROM Records")
        _records = cursor.fetchall()
        print(_records)

        print_records = ' '

        # loop through records
        for record in _records:
            print_records += str('Record Name: ' + record[6] + '\n' + 'Record Description: ' + record[7]) + '\n'

        record_label = Label(recordWindow, text=print_records)
        record_label.grid(row=1, column=0, columnspan=2)

        # Commit Changes
        db.commit()
        # Close Connection
        db.close()


    # record button
    viewRecordsBtn = Button(diaryPage, text="View Records", command=viewRecords)
    viewRecordsBtn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    # create records function
    def createRecords():
        # connect ot the database
        db = mysql.connector.connect(host="localhost", user="root", password=databasePassword, database=databaseUsername)

        # create cursor
        cursor = db.cursor()

        diaryPage.destroy()
        print('made it past diary.destroy()')
        recordsFunction()
        print('opened records.py')

        # Commit Changes
        db.commit()
        # Close Connection
        db.close()


    # create record button
    createRecordsBtn = Button(diaryPage, text="Create Records", command=createRecords)
    createRecordsBtn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    # view galleries function
    def viewGalleries():
        # connect ot the database
        db = mysql.connector.connect(host="localhost", user="root", password=databasePassword, database=databaseUsername)

        # create cursor
        cursor = db.cursor()

        galleryWindow = Toplevel(diaryPage)
        galleryWindow.title("Galleries")
        galleryWindow.geometry("200x200")

        # view records
        cursor.execute("SELECT * FROM Galleries")
        _galleries = cursor.fetchall()
        print(_galleries)

        print_records = ' '

        # loop through records
        for record in _galleries:
            print_records += str('Record Name: ' + record[5] + '\n' + 'Record Description: ' + record[6]) + '\n'

        record_label = Label(galleryWindow, text=print_records)
        record_label.grid(row=1, column=0, columnspan=2)

        # Commit Changes
        db.commit()
        # Close Connection
        db.close()


    # galleries button
    viewGalleriesBtn = Button(diaryPage, text="View Galleries", command=viewGalleries)
    viewGalleriesBtn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # create galleries function
    def createGalleries():
        # connect ot the database
        db = mysql.connector.connect(host="localhost", user="root", password=databasePassword, database=databaseUsername)

        # create cursor
        cursor = db.cursor()

        diaryPage.destroy()
        print('made it past diary.destroy()')
        galleriesFunction()
        print('opened galleries.py')

        # Commit Changes
        db.commit()
        # Close Connection
        db.close()


    # galleries button
    createGalleriesBtn = Button(diaryPage, text="Create Galleries", command=createGalleries)
    createGalleriesBtn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    # logout function

    def logout():
        # connect ot the database
        db = mysql.connector.connect(host="localhost", user="root", password=databasePassword, database=databaseUsername)

        # create cursor
        cursor = db.cursor()

        diaryPage.destroy()
        print('made it past diaryPpage.destroy()')
        exec(open("loginPage.py").read())
        print('opened loginPage.py')

    def backToMainMenu():
        diaryPage.destroy()
        userMainMenuFunction()
        
    # logout button
    logoutButton = Button(diaryPage, text="Logout", command=logout)
    logoutButton.grid(row=5, column=0)

    backButton = tk.Button(diaryPage, text = 'Back', width = 10, padx = 10, bg = 'darkred', fg = 'white', command = backToMainMenu)
    backButton.grid(row=0, column=0, sticky = 'nw')

    diaryPage.mainloop()

    
login()
