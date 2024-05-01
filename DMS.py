import tkinter as tk
from tkinter import *
import tkinter as tk
import mysql.connector
import tkinter.messagebox
from tkinter import messagebox
from datetime import datetime


# Global Variables
global strikes
strikes = 0


global databaseUsername
global databasePassword

global db   
global cursor


global Creator_ID
global Diary_ID
global Planner_ID

global username

"""""
Corrections

Group, Diary & Planner related queries are user specific
- Utilize global variables of Creator, Diary, & Planner ID to fix

Provide legitimate manner for admin to log in

"""""

def login():
    # Window Setup
    global loginWindow, strikes
    loginWindow = tk.Tk()
    loginWindow.title('Login')
    loginWindow.geometry('800x550')
    loginWindow.configure(bg='light blue')

    # Functions
    # The user gets three tries to enter the password. However, once they reach three strikes, the window will close

    def submit():
        global cursor, Creator_ID, username, strikes
        # Python won't let you use a variable from outside the function unless you use this 'global' declaration in the function
        # You can't measure an entry's length by itself, but you can take it and apply it to another variable
        # Then you can measure, use, apply, etc the variable
        username = usernameInput.get()
        password = passwordInput.get()
        if len(username) == 0 or len(password) == 0:
            # The .config is how you change the labels after they are initially created
            blankSpace.config(bg='skyblue', fg='black', text='Please enter a username and password')
            warning.config(bg='#F0F0F0', fg='#F0F0F0')
            warningTitle.config(bg='#F0F0F0', fg='#F0F0F0')
        else:
            print(username)
            print(password)
            blankSpace.config(bg='#F0F0F0', fg='#F0F0F0')
            cursor.execute("""SELECT username, password FROM Users WHERE username=%s AND password=%s""",
                           (username, password))
            # .fetchall prints all the results that cursor returned
            found = cursor.fetchall()
            # The user has three tries, then the application closes.
            if len(found) == 0:
                if strikes <= 1:
                    warning.config(bg='red', fg='black')
                    warningTitle.config(bg='red', fg='black')
                    strikes = strikes + 1
                    print(strikes)
                elif strikes == 2:
                    warning.config(text='The username or password\n is incorrect.\nYou have one attempt remaining.',
                                   bg='red', fg='black')
                    warningTitle.config(bg='red', fg='black')
                    strikes = strikes + 1
                    print(strikes)
                elif strikes == 3:
                    loginWindow.destroy();
                    quit()
            else:
                strikes = 0
                # Code to go to the main menu
                loginWindow.destroy();
                print("Made it past loginWindow.destroy")
                cursor.execute("""SELECT username FROM Users WHERE username=%s AND has_Admin = 'Yes'""", (username,))
                print("Made it past select")
                found = cursor.fetchall()
                if len(found) == 0:
                    userMainMenuFunction()
                    cursor.execute("""SELECT User_ID FROM Users WHERE username=%s""",(username))
                    Creator_ID = cursor.fetchall()
                elif len(found) == 1:
                    # AdminMenu.mainloop()
                    adminMenuFunction()
                else:
                    print('There has been an unexpected error. Please try again.')

    def databaseSubmit():
        global db, cursor, databaseUsername, databasePassword, strikes
        databaseUsername = usernameInput.get()
        databasePassword = passwordInput.get()

        if len(databaseUsername) == 0 or len(databasePassword) == 0:
            blankSpace.config(bg='skyblue', fg='black')
            warningTitle.config(bg='#F0F0F0', fg='#F0F0F0')
            warning.config(bg='#F0F0F0', fg='#F0F0F0')
        else:
            if databaseUsername == 'diary_management' and databasePassword == 'root':
                strikes = 0
                databaseSubmitButton.destroy()
                blankSpace.config(bg='#F0F0F0', fg='#F0F0F0')
                warningTitle.config(bg='#F0F0F0', fg='#F0F0F0')
                warning.config(bg='#F0F0F0', fg='#F0F0F0')

                # submitButton = tk.Button(loginWindow, text = 'Submit', width = 20, padx = 30, bg = 'blue', fg = 'white', command = submit).place(x = 280, y = 210)
                submitButton.place(x=280, y=210)
                title.config(text='Login', fg='black', bg='lightgrey')
                usernameLabel.config(text='Username')
                usernameLabel.place(x=220, y=120)
                createAccountButton.place(x=280, y=460)
                # Clears the usernameInput and passwordInput fields
                usernameInput.delete(0, END)
                passwordInput.delete(0, END)

                # If having trouble connecting, check that the user and password are correct
                db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )
                cursor = db.cursor()
            else:
                blankSpace.config(bg='#F0F0F0', fg='#F0F0F0')
                if strikes <= 1:
                    warningTitle.config(bg='red', fg='black')
                    warning.config(bg='red', fg='black')
                    strikes = strikes + 1
                    print(strikes)
                elif strikes == 2:
                    warningTitle.config(bg='red', fg='black')
                    warning.config(text='The username or password\n is incorrect.\nYou have one attempt remaining.',
                                   bg='red', fg='black')
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

        passwordCheckLabel.place(x=220, y=200)
        passwordCheckInput.place(x=320, y=200)
        submitAccountButton.place(x=280, y=250)
        backButton.place(x=280, y=460)

    def createAccount():
        username = usernameInput.get()
        password = passwordInput.get()
        passwordCheck = passwordCheckInput.get()

        cursor.execute("""SELECT username FROM Users WHERE username=%s""", (username,))
        found = cursor.fetchall()

        if len(username) == 0 or len(password) == 0 or len(passwordCheck) == 0:
            createAccountNotification.place(x=275, y=300)
            createAccountNotification.config(text='Please enter information\n into all three fields.')
        elif len(found) != 0:
            createAccountNotification.place(x=275, y=300)
            createAccountNotification.config(
                text='Unfortunately, this username\n has already been taken.\nPlease select a different one.')
        elif len(found) == 0:
            if password != passwordCheck:
                createAccountNotification.place(x=275, y=300)
                createAccountNotification.config(text='The entered passwords do not match.')
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
                cursor.execute(
                    """INSERT into users(user_id, username, password, has_admin, admin_id, creation_date, account_age) value (%s, %s, %s, 'No', null, %s, 0)""",
                    (num, username, password, date))
                cursor.execute(
                    """SELECT user_id, username, password, has_admin, admin_id, creation_date, account_age FROM Users WHERE username=%s""",
                    (username,))
                found = cursor.fetchall()
                print(found)

                db.commit()
                db.close()

                # Go to user main page here
                loginWindow.destroy();
                userMainMenuFunction()

    def backToLogin():
        usernameInput.delete(0, END)
        passwordInput.delete(0, END)
        passwordCheckInput.delete(0, END)

        submitButton.place(x=280, y=210)
        createAccountButton.place(x=280, y=460)
        blankSpace.place(x=255, y=250)
        blankSpace.config(bg='#F0F0F0', fg='#F0F0F0')

        warning.place(x=275, y=320)
        warningTitle.place(x=275, y=300)
        warningTitle.config(bg='#F0F0F0', fg='#F0F0F0')
        warning.config(bg='#F0F0F0', fg='#F0F0F0')

        passwordCheckLabel.place_forget()
        passwordCheckInput.place_forget()
        submitAccountButton.place_forget()
        backButton.place_forget()
        createAccountNotification.place_forget()

    def exitFunction():
        loginWindow.destroy()
        quit()

    # Visuals Setup
    # Note: It is important to separate .grid and .place from the original section, otherwise we cannot get the values from the Entry objects
    exitButton = tk.Button(loginWindow, text='Exit', width=10, padx=10, bg='darkred', fg='white', command=exitFunction)
    exitButton.pack(side=TOP, anchor=NE)

    whiteSection = tk.Label(loginWindow, width=50, height=26, text='', bg='#F0F0F0')
    whiteSection.place(x=200, y=50)

    title = tk.Label(loginWindow, width=35, height=2, text='Enter Database Credentials', font=('Arial', 12, 'bold'),
                     fg='white', bg='black')
    title.place(x=200, y=50)

    usernameLabel = tk.Label(loginWindow, width=15, height=1, text='Database Name')
    usernameLabel.place(x=210, y=120)
    passwordLabel = tk.Label(loginWindow, width=10, height=1, text='Password')
    passwordLabel.place(x=240, y=160)

    usernameInput = tk.Entry(loginWindow, width=30)
    usernameInput.place(x=320, y=120)
    passwordInput = tk.Entry(loginWindow, width=30, show='*')
    passwordInput.place(x=320, y=160)

    databaseSubmitButton = tk.Button(loginWindow, text='Submit', width=20, bg='grey', padx=30, command=databaseSubmit)
    # This button needs to use .pack() so that it can be destroyed later on
    databaseSubmitButton.pack(side=TOP, anchor=NW, padx=280, pady=185)

    submitButton = tk.Button(loginWindow, text='Submit', width=20, padx=30, bg='blue', fg='white', command=submit)
    submitButton.place(x=280, y=210)
    submitButton.place_forget()

    # bg = 'skyblue', fg = 'black'
    blankSpace = tk.Label(loginWindow, text='Please enter a database name and password', width=35, height=2,
                          bg='#F0F0F0', fg='#F0F0F0')
    blankSpace.place(x=255, y=250)

    warning = tk.Label(loginWindow, width=30, height=6,
                       text='The username or password\n is incorrect.\nPlease try again.', bg='#F0F0F0', fg='#F0F0F0')
    warning.place(x=275, y=320)
    warningTitle = tk.Label(loginWindow, width=14, height=1, text='Warning', font=('Arial', 18, 'bold'), bg='#F0F0F0',
                            fg='#F0F0F0')
    warningTitle.place(x=275, y=300)

    # Create Account
    createAccountButton = tk.Button(loginWindow, text="Don't have an account?\nCreate one now!", width=20, bg='green',
                                    fg='white', padx=30, command=createAccountPage)
    createAccountButton.place(x=280, y=460)
    createAccountButton.place_forget()

    backButton = tk.Button(loginWindow, text="Back", width=20, bg='blue', fg='white', padx=30, command=backToLogin)
    backButton.place(x=280, y=460)
    backButton.place_forget()

    passwordCheckLabel = tk.Label(loginWindow, width=12, height=1, text='Check Password')
    passwordCheckLabel.place(x=200, y=200)
    passwordCheckLabel.place_forget()

    passwordCheckInput = tk.Entry(loginWindow, width=30, show='*')
    passwordCheckInput.place(x=320, y=200)
    passwordCheckInput.place_forget()

    submitAccountButton = tk.Button(loginWindow, text="Submit", width=20, bg='blue', fg='white', padx=30,
                                    command=createAccount)
    submitAccountButton.place(x=280, y=250)
    submitAccountButton.place_forget()

    createAccountNotification = tk.Label(loginWindow, width=30, height=6,
                                         text='Unfortunately, this username\n has already been taken.\nPlease select a different one.',
                                         bg='skyblue')
    createAccountNotification.place(x=275, y=300)
    createAccountNotification.place_forget()


def userMainMenuFunction():
    global username
    userMainMenu = tk.Tk()
    userMainMenu.title('User Main Menu')
    userMainMenu.geometry('1500x700')
    userMainMenu.config(bg='light blue')

    userMainMenu.grid_rowconfigure(0, weight=1)
    userMainMenu.grid_columnconfigure(0, weight=1)

    # Welcome
    LT = tk.Label(userMainMenu, text="Welcome " + username + "!", font=('Times', 50))
    LT.grid(row=0, column=0)
    LT.config(bg="light blue", fg="white")

    # Menu Intro
    LT0 = tk.Label(userMainMenu, text="Main Menu", font=('Times', 25))
    LT0.grid(row=1, column=0)
    LT0.config(bg="light blue", fg="white")

    # # username
    # LT2 = tk.Label(userMainMenu, text=username, font=('Times', 20))
    # LT2.grid(row=2, column=0)
    # LT2.config(bg="light blue", fg="White")

    def diary():
    # connect to the database
        db = mysql.connector.connect(
            host="localhost",
            # Username and password must be the same as in mySQL
            user="root",
            password=databasePassword,
            database=databaseUsername
        )

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
        # connect to the database
        db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )

        # create cursor
        cursor = db.cursor()

        recordWindow = Toplevel(userMainMenu)
        recordWindow.title("Records")
        recordWindow.geometry("750x300")

        # view records
        cursor.execute("SELECT * FROM Records")
        recordsFetch = cursor.fetchall()
        print(recordsFetch)

        print_records = ' '

        # loop through records
        for record in recordsFetch:
            print_records += str('Record Name: ' + record[6] + '\n' + 'Record Description: ' + record[7]) + '\n'

        record_label1 = Label(recordWindow, text=print_records)
        record_label1.grid(row=3, column=0, columnspan=1)
        record_label1.grid_rowconfigure(1, weight=1)
        record_label1.grid_columnconfigure(1, weight=1)

        def searchRecords():
            db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )
            cursor = db.cursor()

            search1 = search.get()

            cursor.execute("""Select * from Records where record_name = %s """, (search1,))
            results = cursor.fetchall()
            print('past results')
            print(results)
            print('past results2 ')

            print_result = ' '

            for result in results:
                print_result += str('Record: ' + result[6]) + '\n'
            result_label = Label(recordWindow, text=print_result)
            result_label.grid(row=10, column=3, columnspan=1)
            result_label.grid_columnconfigure(1, weight=1)
            result_label.grid_rowconfigure(1, weight=1)
            result_label.delete(0, END)
            db.commit()
            db.close()

        # Commit Changes
        db.commit()

        # Close Connection
        db.close()

        # search textbox
        search = Entry(recordWindow, width=10)
        search.grid(row=3, column=2, padx=20)

        # search label
        searchLabel = Label(recordWindow, text="Search:")
        searchLabel.grid(row=3, column=1)

        # search btn
        searchBtn = Button(recordWindow, text="Search Records", command=searchRecords)
        searchBtn.grid(row=3, column=3, columnspan=1, pady=10, padx=10, ipadx=100)

    # record button
    viewRecordsBtn = Button(userMainMenu, text="View Records", command=viewRecords)
    viewRecordsBtn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # create record function
    def createRecords():
        # connect to the database
        db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )

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

    # admin button
    viewAdminsBtn = Button(userMainMenu, text="View Admins", command=viewAdmins)
    viewAdminsBtn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # planner function
    def viewPlanner():
        # connect to the database
        db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )

        # create cursor
        cursor = db.cursor()

        userMainMenu.destroy()
        print('made it past userMainMenu.destroy()')
        plannerFunction()
        print('opened galleries.py')

    # planner button
    viewPlannerBtn = Button(userMainMenu, text="View Planner", command=viewPlanner)
    viewPlannerBtn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # group function

    def viewGroups():
        # connect to the database
        db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )

        # create cursor
        cursor = db.cursor()

        groupsWindow = Toplevel(userMainMenu)
        groupsWindow.title("Groups")
        groupsWindow.geometry("200x200")

        # view records
        cursor.execute("SELECT * FROM _groups")
        _groups = cursor.fetchall()
        print(_groups)

        print_groups = ''

        # loop through groups
        for group in _groups:
            print_groups += str('Group ID: ' + str(group[0]) + ' | ' + 'Creator_ID: ' + str(group[1])) + '\n\n'
        groupID_label = Label(groupsWindow, text='Groups: ')
        groupID_label.grid(row=2, column=0, columnspan=1)
        group_label = Label(groupsWindow, text=print_groups)
        group_label.grid(row=3, column=0, columnspan=1)
        group_label.grid_rowconfigure(1, weight=1)
        group_label.grid_columnconfigure(1, weight=1)

        def searchGroups():
            global Creator_ID
            db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )
            cursor = db.cursor()

            # global recordID
            # recordID = recordID.get()

            search2 = searchG.get()

            cursor.execute("""Select * from _groups where group_id = %s """, (search2,))
            results = cursor.fetchall()
            print('past results')
            print(results)
            print('past results2 ')

            if(len(results) != 0):
                Creator_ID = results[0]
                groupMainMenuFunction()

            # Commit Changes
        db.commit()

        # Close Connection
        db.close()

        # search textbox
        searchG = Entry(groupsWindow, width=10)
        searchG.grid(row=3, column=2, padx=20)

        # search label
        searchGLabel = Label(groupsWindow, text="Search:")
        searchGLabel.grid(row=3, column=1)

        # search btn
        searchGBtn = Button(groupsWindow, text="Search Groups", command=searchGroups)
        searchGBtn.grid(row=3, column=3, columnspan=1, pady=10, padx=10, ipadx=100)

    # view group button
    viewPlannerBtn = Button(userMainMenu, text="View Groups", command=viewGroups)
    viewPlannerBtn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    def createGroups():
        # connect to the database
        db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )
        # create cursor
        cursor = db.cursor()
        groupCreation()
        userMainMenu.destroy()
        print('made it past userMainMenu.destroy()')

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
        userMainMenu.destroy()
        login()
        print('made it past userMainMenu.destroy()')
        print('opened loginPage.py')

    # logout button
    logoutButton = Button(userMainMenu, text="Logout", command=logout)
    logoutButton.grid(row=10, column=0)

    print(db.is_connected())
    userMainMenu.mainloop()

def viewAdmins():
    # connect to the database
    db = mysql.connector.connect(
                host="localhost",
                # Username and password must be the same as in mySQL
                user="root",
                password=databasePassword,
                database=databaseUsername
            )

    # create cursor
    cursor = db.cursor()

    adminWindow = tk.Tk()
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


def recordsFunction():
    createrecordPage = tk.Tk()
    createrecordPage.title('Records Page')
    createrecordPage.geometry('1500x700')
    createrecordPage.config(bg='light blue')

    createrecordPage.grid_rowconfigure(0, weight=1)
    createrecordPage.grid_columnconfigure(0, weight=1)

    # create function

    def create():
        db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )
        cursor = db.cursor()

        Group_ID = groupIDinput.get()
        record_name1 = recordName.get()
        Creator_ID = diaryID.get()
        in_gallery1 = inGallery.get()
        # record_age1 = recordAge.get()
        record_description1 = recordDescription.get()
        # gallery_ID1 = galleryID.get()

        # set foriegn keys = 0
        cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
        print('SET FOREIGN_KEY_CHECKS = 0;')

        cursor.execute(
            """insert into records(record_id, diary_id, in_gallery, gallery_id, creation_date, record_age, record_name, record_description)value (%s, %s, %s, null, current_date , 0, %s, %s)""",
            (Group_ID, Creator_ID, in_gallery1, record_name1, record_description1))

        db.commit()
        db.close()

        # Clear textbox
        recordName.delete(0, END)
        groupIDinput.delete(0, END)
        diaryID.delete(0, END)
        inGallery.delete(0, END)
        # galleryID.delete(0, END)
        # recordAge.delete(0, END)
        recordDescription.delete(0, END)

    def backToMainMenu():
        createrecordPage.destroy()
        userMainMenuFunction()

    # Intro
    intro = tk.Label(createrecordPage, text="Create Record", font=('Helvetica', 40))
    intro.grid(row=0, column=0, columnspan=3, pady=10, padx=10, ipadx=100)
    intro.config(bg="light blue", fg="white")

    # create textboxes
    groupIDinput = Entry(createrecordPage, width=10)
    groupIDinput.grid(row=2, column=0, padx=20)

    diaryID = Entry(createrecordPage, width=10)
    diaryID.grid(row=4, column=0, padx=20)

    # galleryID = Entry(createrecordPage, width=10)
    # galleryID.grid(row=6, column=0, padx=20)

    recordName = Entry(createrecordPage, width=15)
    recordName.grid(row=8, column=0, padx=20)

    # recordAge = Entry(createrecordPage, width=15)
    # recordAge.grid(row=12, column=0, padx=20)

    inGallery = Entry(createrecordPage, width=15)
    inGallery.grid(row=14, column=0, padx=20)

    recordDescription = Entry(createrecordPage, width=30)
    recordDescription.grid(row=16, column=0, padx=20)

    # create textbox labels
    recordIDLabel = Label(createrecordPage, text="Record ID:")
    recordIDLabel.grid(row=1, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    diaryIDLabel = Label(createrecordPage, text="Diary ID:")
    diaryIDLabel.grid(row=3, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    # galleryIDLabel = Label(createrecordPage, text="Gallery ID:")
    # galleryIDLabel.grid(row=5, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    recordNameLabel = Label(createrecordPage, text="Record Name:")
    recordNameLabel.grid(row=7, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    # date = datetime.today().strftime('%Y-%m-%d')

    # recordAgeLabel = Label(createrecordPage, text="Record Age:")
    # recordAgeLabel.grid(row=11, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    inGalleryLabel = Label(createrecordPage, text=" (Yes or No):")
    inGalleryLabel.grid(row=13, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    recordDescriptionLabel = Label(createrecordPage, text="Record Description:")
    recordDescriptionLabel.grid(row=15, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    # create button
    createBtn = Button(createrecordPage, text="Create", command=create)
    createBtn.grid(row=17, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    backButton = tk.Button(createrecordPage, text='Back', width=10, padx=10, bg='darkred', fg='white',
                           command=backToMainMenu)
    backButton.grid(row=0, column=0, sticky='nw')

    createrecordPage.mainloop()

    db.commit()
    db.close()

def groupCreation():
    creategroupPage = tk.Tk()
    creategroupPage.title('Group Creation Page')
    creategroupPage.geometry('1500x700')
    creategroupPage.config(bg='light blue')

    creategroupPage.grid_rowconfigure(0, weight=1)
    creategroupPage.grid_columnconfigure(0, weight=1)

    # create function

    def create():
        
        global Creator_ID
        db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )
        cursor = db.cursor()

        Group_ID = groupIDinput.get()

        # set foriegn keys = 0
        cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
        print('SET FOREIGN_KEY_CHECKS = 0;')

        cursor.execute(
            """insert into _groups(Group_ID, Creator_ID, Creation_Date, Group_Age, Member_Num) value (%s, %s, current_date , 0, 0)""",
            (Group_ID, 5))

        db.commit()
        db.close()

        # Clear textbox
        groupIDinput.delete(0, END)


    def backToMainMenu():
        creategroupPage.destroy()
        userMainMenuFunction()

    # Intro
    intro = tk.Label(creategroupPage, text="Create Group", font=('Helvetica', 40))
    intro.grid(row=0, column=0, columnspan=3, pady=10, padx=10, ipadx=100)
    intro.config(bg="light blue", fg="white")

    # create textboxes
    groupIDinput = Entry(creategroupPage, width=10)
    groupIDinput.grid(row=2, column=0, padx=20)

 
    # create textbox labels
    groupIDLabel = Label(creategroupPage, text="Group ID:")
    groupIDLabel.grid(row=1, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    # create button
    createBtn = Button(creategroupPage, text="Create", command=create)
    createBtn.grid(row=17, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    backButton = Button(creategroupPage, text='Back', width=10, padx=10, bg='darkred', fg='white',
                           command=backToMainMenu)
    backButton.grid(row=0, column=0, sticky='nw')

    creategroupPage.mainloop()

    db.commit()
    db.close()


def galleriesFunction():
    creategalleriePage = tk.Tk()
    creategalleriePage.title('Gallery Page')
    creategalleriePage.geometry('1500x700')
    creategalleriePage.config(bg='light blue')

    creategalleriePage.grid_rowconfigure(0, weight=1)
    creategalleriePage.grid_columnconfigure(0, weight=1)

    # create function

    def createGallery():
        db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )
        cursor = db.cursor()

        date = datetime.today().strftime('%Y-%m-%d')

        galleryId2 = galleryID.get()
        diaryID2 = diaryID.get()
        galleryName2 = galleryName.get()
        # galleryAge2 = galleryAge.get()
        recordNum2 = recordNum.get()

        cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
        print('SET FOREIGN_KEY_CHECKS = 0;')

        cursor.execute(
            """insert into galleries(gallery_id, diary_id, creation_date, gallery_name, gallery_age, record_num) value (%s, %s, current_date , %s, 0, %s)""",
            (galleryId2, diaryID2, galleryName2, recordNum2))

        db.commit()
        db.close()

        galleryID.delete(0, END)
        diaryID.delete(0, END)
        galleryName.delete(0, END)
        recordNum.delete(0, END)

    def backToMainMenu():
        creategalleriePage.destroy()
        userMainMenuFunction()

    # Intro
    intro = tk.Label(creategalleriePage, text="Create Gallery", font=('Helvetica', 40))
    intro.grid(row=0, column=0, columnspan=3, pady=10, padx=10, ipadx=100)
    intro.config(bg="light blue", fg="white")

    # create textboxes
    galleryID = Entry(creategalleriePage, width=10)
    galleryID.grid(row=2, column=0, padx=20)

    diaryID = Entry(creategalleriePage, width=10)
    diaryID.grid(row=4, column=0, padx=20)

    galleryName = Entry(creategalleriePage, width=15)
    galleryName.grid(row=8, column=0, padx=20)

    # galleryAge = Entry(creategalleriePage, width=15)
    # galleryAge.grid(row=10, column=0, padx=20)

    recordNum = Entry(creategalleriePage, width=15)
    recordNum.grid(row=12, column=0, padx=20)

    # create textbox labels
    galleryIDLabel = Label(creategalleriePage, text="Gallery ID:")
    galleryIDLabel.grid(row=1, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    diaryIDLabel = Label(creategalleriePage, text="Diary ID:")
    diaryIDLabel.grid(row=3, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    galleryNameLabel = Label(creategalleriePage, text="Gallery Name:")
    galleryNameLabel.grid(row=7, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    # galleryAgeLabel = Label(creategalleriePage, text="Gallery Age:")
    # galleryAgeLabel.grid(row=9, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    recordNumLabel = Label(creategalleriePage, text="Record Number:")
    recordNumLabel.grid(row=11, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    # create button
    createBtn = Button(creategalleriePage, text="Create", command=createGallery)
    createBtn.grid(row=17, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

    backButton = tk.Button(creategalleriePage, text='Back', width=10, padx=10, bg='darkred', fg='white',
                           command=backToMainMenu)
    backButton.grid(row=0, column=0, sticky='nw')

    creategalleriePage.mainloop()

    db.commit()
    db.close()


def diaryFunction():
    diaryPage = tk.Tk()
    diaryPage.title('Diary Page')
    diaryPage.geometry('1500x700')
    diaryPage.config(bg='light blue')

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
        db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )

        # create cursor
        cursor = db.cursor()

        recordWindow = Toplevel(diaryPage)
        recordWindow.title("Records")
        recordWindow.geometry("750x300")

        # view records
        cursor.execute("SELECT * FROM Records")
        _records = cursor.fetchall()
        print(_records)

        print_records = ' '

        # loop through records
        for record in _records:
            print_records += str('Record Name: ' + record[6] + '\n' + 'Record Description: ' + record[7]) + '\n' + '\n'

        record_label = Label(recordWindow, text=print_records)
        record_label.grid(row=3, column=0, columnspan=1)
        record_label.grid_rowconfigure(1, weight=1)
        record_label.grid_columnconfigure(1, weight=1)

        def searchRecords():
            db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )
            cursor = db.cursor()

            # global recordID
            # recordID = recordID.get()

            search1 = search.get()

            cursor.execute("""Select * from Records where record_id = %s """, (search1,))
            results = cursor.fetchall()
            print('past results')
            print(results)
            print('past results2 ')

            print_result = ' '

            for result in results:
                print_result += str('Record: ' + result[6]) + '\n'
            result_label = Label(recordWindow, text=print_result)
            result_label.grid(row=10, column=3, columnspan=1)

            # groupIDinput.delete(0, END)
            db.commit()
            db.close()

        # Commit Changes
        db.commit()
        # Close Connection
        db.close()

        # search textbox
        search = Entry(recordWindow, width=10)
        search.grid(row=3, column=2, padx=20)

        # search label
        searchLabel = Label(recordWindow, text="Search:")
        searchLabel.grid(row=3, column=1)

        # search btn
        searchBtn = Button(recordWindow, text="Search Records", command=searchRecords)
        searchBtn.grid(row=3, column=3, columnspan=1, pady=10, padx=10, ipadx=100)

    # record button
    viewRecordsBtn = Button(diaryPage, text="View Records", command=viewRecords)
    viewRecordsBtn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # create records function
    def createRecords():
        # connect ot the database
        db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )
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
        # connect to the database
        db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )

        # create cursor
        cursor = db.cursor()

        galleryWindow = Toplevel(diaryPage)
        galleryWindow.title("Galleries")
        galleryWindow.geometry("200x200")

        # view records
        cursor.execute("SELECT * FROM Galleries")
        _galleries = cursor.fetchall()
        print(_galleries)

        print_galleries = ' '

        # loop through records
        for gallery in _galleries:
            print_galleries += str('Gallery Name: ' + gallery[3]) + '\n'  # + 'Record Description: ' + record[6]) + '\n'

        gallery_label = Label(galleryWindow, text=print_galleries)
        gallery_label.grid(row=1, column=0, columnspan=2)

        # Commit Changes
        db.commit()
        # Close Connection
        db.close()

    # galleries button
    viewGalleriesBtn = Button(diaryPage, text="View Galleries", command=viewGalleries)
    viewGalleriesBtn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # create galleries function
    def createGalleries():
        # connect to the database
        db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )
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
        # connect to the database
        db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )

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

    backButton = tk.Button(diaryPage, text='Back', width=10, padx=10, bg='darkred', fg='white', command=backToMainMenu)
    backButton.grid(row=0, column=0, sticky='nw')

    diaryPage.mainloop()


def plannerFunction():
    class PlannerPage:
        def __init__(self, master, db_connection):
            self.master = master
            self.db_connection = db_connection
            self.last_task_id = self.get_last_task_id()  # initialize the last task ID

            self.master.title("Planner Page")
            self.master.geometry("1500x700")
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
            create_checklist_window.geometry("1500x700")
            create_checklist_window.configure(bg="light blue")

            # title label for the Create Checklist page
            title_label = tk.Label(create_checklist_window, text="Checklist Creation", font=("Arial", 20),
                                   bg="light blue")
            title_label.pack(pady=20)

            checklist_name_label = tk.Label(create_checklist_window, text="Enter Checklist Name:", bg="light blue")
            checklist_name_label.pack()

            self.checklist_name_entry = tk.Entry(create_checklist_window)
            self.checklist_name_entry.pack()

            planner_id = 1

            save_button = tk.Button(create_checklist_window, text="Save",
                                    command=lambda: self.save_checklist(planner_id, create_checklist_window))
            save_button.pack(pady=5)

            back_button = tk.Button(create_checklist_window, text="Back", command=create_checklist_window.destroy)
            back_button.pack(pady=5)

        def add_task(self, planner_id, checklist_id):
            add_task_window = tk.Toplevel(self.master)
            add_task_window.title("Add Task")
            add_task_window.geometry("1500x700")
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

            save_task_button = tk.Button(add_task_window, text="Save Task",
                                         command=lambda: self.save_task(planner_id, checklist_id, add_task_window))
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
            edit_checklist_window.geometry("1500x700")
            edit_checklist_window.configure(bg="light blue")

            # title label for the Edit Checklist page
            title_label = tk.Label(edit_checklist_window, text="Checklist Editor", font=("Arial", 20), bg="light blue")
            title_label.pack(pady=20)

            checklist_label = tk.Label(edit_checklist_window, text="Select Checklist:", bg="light blue")
            checklist_label.pack()

            self.selected_checklist = tk.StringVar()
            self.selected_checklist.set("")  # set default value

            checklist_option_menu = tk.OptionMenu(edit_checklist_window, self.selected_checklist,
                                                  *[""] + [checklist[1] for checklist in checklists])
            checklist_option_menu.pack()

            edit_checklist_button = tk.Button(edit_checklist_window, text="Edit Checklist",
                                              command=self.open_edit_checklist_window)
            edit_checklist_button.pack(pady=5)

            delete_checklist_button = tk.Button(edit_checklist_window, text="Delete Checklist",
                                                command=self.delete_checklist)
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
            edit_checklist_window.geometry("1500x700")
            edit_checklist_window.configure(bg="light blue")

            # Title label for the Edit Checklist options
            title_label = tk.Label(edit_checklist_window, text="Click on one of these two options or go back",
                                   font=("Arial", 16), bg="light blue")
            title_label.pack(pady=20)

            edit_name_button = tk.Button(edit_checklist_window, text="Edit Checklist Name",
                                         command=lambda: self.edit_checklist_name(checklist_id, checklist_name))
            edit_name_button.pack(pady=5)

            add_task_button = tk.Button(edit_checklist_window, text="Add Task",
                                        command=lambda: self.add_task(1, checklist_id))  # Hardcoded Planner_ID for now
            add_task_button.pack(pady=5)

            back_button = tk.Button(edit_checklist_window, text="Back", command=edit_checklist_window.destroy)
            back_button.pack(pady=5)

        def edit_checklist_name(self, checklist_id, old_name):
            edit_name_window = tk.Toplevel(self.master)
            edit_name_window.title("Edit Checklist Name")
            edit_name_window.geometry("1500x700")
            edit_name_window.configure(bg="light blue")

            new_name_label = tk.Label(edit_name_window, text="Enter New Checklist Name:", bg="light blue")
            new_name_label.pack()

            self.new_name_entry = tk.Entry(edit_name_window)
            self.new_name_entry.pack()

            save_button = tk.Button(edit_name_window, text="Save",
                                    command=lambda: self.save_checklist_name(checklist_id, old_name, edit_name_window))
            save_button.pack(pady=5)

            back_button = tk.Button(edit_name_window, text="Back", command=edit_name_window.destroy)
            back_button.pack(pady=5)

        def view_checklists(self):
            view_checklists_window = tk.Toplevel(self.master)
            view_checklists_window.title("View Checklists")
            view_checklists_window.geometry("1500x700")
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

            checklist_option_menu = tk.OptionMenu(view_checklists_window, self.selected_checklist_id,
                                                  *[""] + [str(checklist[0]) + " - " + checklist[1] for checklist in
                                                           checklists])
            checklist_option_menu.pack()

            view_selected_checklist_button = tk.Button(view_checklists_window, text="View Selected Checklist",
                                                       command=self.view_selected_checklist)
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
            view_selected_checklist_window.geometry("1500x700")
            view_selected_checklist_window.configure(bg="light blue")

            checklist_label = tk.Label(view_selected_checklist_window, text="Checklist: " + checklist_name,
                                       bg="light blue")
            checklist_label.pack()

            tasks_label = tk.Label(view_selected_checklist_window, text="Tasks:", bg="light blue")
            tasks_label.pack()

            for task in tasks:
                task_name = task[0]
                task_label = tk.Label(view_selected_checklist_window, text=task_name, bg="light blue")
                task_label.pack()

            back_button = tk.Button(view_selected_checklist_window, text="Back",
                                    command=view_selected_checklist_window.destroy)
            back_button.pack(pady=5)

        def save_checklist_name(self, checklist_id, old_name, edit_name_window):
            new_name = self.new_name_entry.get()
            if not new_name:
                messagebox.showerror("Error", "Please enter a new checklist name.")
                return

            # update checklist name in the DB
            cursor = self.db_connection.cursor()
            cursor.execute("UPDATE Checklists SET Checklist_Name = %s WHERE Checklist_ID = %s",
                           (new_name, checklist_id))
            self.db_connection.commit()
            cursor.close()

            messagebox.showinfo("Success", "Checklist name updated successfully.")
            edit_name_window.destroy()

        def delete_checklist(self):
            checklist_name = self.selected_checklist.get()

            if not checklist_name:
                messagebox.showerror("Error", "Please select a checklist.")
                return

            confirm = messagebox.askyesno("Delete Checklist",
                                          f"Are you sure you want to delete the checklist '{checklist_name}'? This action cannot be undone.")

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
            cursor.execute(
                "INSERT INTO Tasks (Task_ID, Task_Name, Checklist_ID, Planner_ID, Creation_Date) VALUES (%s, %s, %s, %s, CURDATE())",
                (self.last_task_id, task_name, checklist_id, planner_id))
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
            cursor.execute(
                "INSERT INTO Checklists (Checklist_Name, Creation_Date, Checklist_Age, Task_Num, Planner_ID) VALUES (%s, CURDATE(), 1, 0, %s)",
                (checklist_name, planner_id))
            self.db_connection.commit()
            cursor.close()
            create_checklist_window.destroy()  # close the create checklist window
            self.edit_checklist()  # open the edit checklist window

        def return_to_main_menu(self):
            self.master.destroy()
            userMainMenuFunction()

    def main():
        # establish connection to the MySQL DB
        db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )

        root = tk.Tk()
        app = PlannerPage(root, db)
        root.mainloop()

    if __name__ == "__main__":
        main()


def adminMenuFunction():
    class AdminMenu:
        def __init__(self, master, db_connection):
            self.master = master
            self.db_connection = db_connection

            self.master.title("Administrator's Main Menu")
            self.master.geometry("1920x1080")
            self.master.configure(bg="light blue")

            self.admin_menu_label = tk.Label(master, text="Administrator's Main Menu", font=("Helvetica", 16),
                                             bg="#ADD8E6")
            self.admin_menu_label.pack(pady=10)

            self.adminee_requests_button = tk.Button(master, text="Browse Adminee Requests",
                                                     command=self.browse_requests)
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
                    accept_button = tk.Button(self.master, text="Accept",
                                              command=lambda admin=admin_id, creator=creator_id: self.accept_request(
                                                  admin, creator))
                    accept_button.pack(side=tk.LEFT, padx=5)
                    deny_button = tk.Button(self.master, text="Deny",
                                            command=lambda admin=admin_id, creator=creator_id: self.deny_request(admin,
                                                                                                                 creator))
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
        db = mysql.connector.connect(
                    host="localhost",
                    # Username and password must be the same as in mySQL
                    user="root",
                    password=databasePassword,
                    database=databaseUsername
                )

        root = tk.Tk()
        app = AdminMenu(root, db)
        root.mainloop()

    if __name__ == "__main__":
        main()


def groupMainMenuFunction():
    groupMainMenu = tk.Tk()
    groupMainMenu.title('Group Main Menu')
    groupMainMenu.geometry('1500x700')
    groupMainMenu.config(bg='light blue')

    def viewPlanner():
        pass

    def viewDiary():
        pass
    def viewAdmin():
        pass
    def logout():
        groupMainMenu.destroy()
        login()

    def backToMainMenu():
        groupMainMenu.destroy()
        userMainMenuFunction()


    backButton = tk.Button(groupMainMenu, text='Back', width=10, padx=10, bg='darkred', fg='white',
                           command=backToMainMenu)
    backButton.pack(side=TOP, anchor=NW)

    # Welcome
    LT = tk.Label(groupMainMenu, text="Group Main Page", font=('Times', 50))
    LT.pack(expand=True)
    LT.config(bg="light blue", fg="white")

    # Profile
    LT2 = tk.Label(groupMainMenu, text="GroupName = Team1", font=('Times', 20))
    LT2.pack(side=tk.TOP, expand=False, fill=None)
    LT2.config(bg="light blue", fg="White")

    LT1 = tk.Label(groupMainMenu, text="Member Count = 3", font=('Times', 20))
    LT1.pack(side=tk.TOP, expand=False, fill=None)
    LT1.config(bg="light blue", fg="White")

    LT3 = tk.Label(groupMainMenu, text="Group Members = Karina01, Jay02, Fin20", font=('Times', 20))
    LT3.pack(side=tk.TOP, expand=False, fill=None)
    LT3.config(bg="light blue", fg="White")

    # Menu Intro
    LT0 = tk.Label(groupMainMenu, text="Main Menu", font=('Times', 25))
    LT0.pack(side=TOP, expand=True)
    LT0.config(bg="light blue", fg="white")

    # Planner  
    p = Button(groupMainMenu,text = "View Group Planner",command=plannerFunction)
    p.pack(side=tk.TOP, expand=False, fill=None)
    p.config(width=33, height=4, bg="light blue", fg="black")

    # Group Diary
    g = Button(groupMainMenu, text="View Group Diary", command=diaryFunction)
    g.pack(side=tk.TOP, expand=False, fill=None)
    g.config(width=34, height=4, bg="light blue", fg="black")

    # Admin

    a = Button(groupMainMenu,text="View Admins",command=viewAdmins)
    a.pack(side=tk.TOP, expand=False, fill=None)
    a.config(width=34, height=4, bg="light blue", fg="black")




login()
loginWindow.mainloop()
