import mysql.connector
import tkinter as tk
from tkinter import *
import tkinter.messagebox

from loginPage import *
from records import *
from planner import *

userMainMenu = tk.Tk()
userMainMenu.title('User Main Menu')
userMainMenu.geometry('1920x1080')
userMainMenu.config(bg='light blue')

print('test username' + username)

userMainMenu.grid_rowconfigure(0, weight=1)
userMainMenu.grid_columnconfigure(0, weight=1)

db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

cursor = db.cursor()

# Welcome
LT = tk.Label(userMainMenu, text=f"Welcome {username}! ", font=('Times', 50))
LT.grid(row=0, column=0)
LT.config(bg="light blue", fg="white")


# Menu Intro
LT0 = tk.Label(userMainMenu, text="Main Menu", font=('Times', 25))
LT0.grid(row=1, column=0)
LT0.config(bg="light blue", fg="white")

# Diary function
def diary():
    # connect ot the database
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

    # create cursor
    cursor = db.cursor()

    userMainMenu.destroy()
    print('made it past userMainMenu.destroy()')
    exec(open("diary.py").read())
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
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

    # create cursor
    cursor = db.cursor()

    recordWindow = Toplevel(userMainMenu)
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
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

    # create cursor
    cursor = db.cursor()

    userMainMenu.destroy()
    print('made it past userMainMenu.destroy()')
    exec(open("records.py").read())
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
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

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
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

    # create cursor
    cursor = db.cursor()

    userMainMenu.destroy()
    print('made it past userMainMenu.destroy()')
    exec(open("planner.py").read())
    print('opened planner.py')


# planner button
viewPlannerBtn = Button(userMainMenu, text="View Planner", command=viewPlanner)
viewPlannerBtn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# group function

def viewGroups():
    # connect ot the database
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

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
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

    # create cursor
    cursor = db.cursor()

    userMainMenu.destroy()
    print('made it past userMainMenu.destroy()')
    exec(open("groups.py").read())
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
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

    # create cursor
    cursor = db.cursor()

    userMainMenu.destroy()
    print('made it past userMainMenu.destroy()')
    exec(open("loginPage.py").read())
    print('opened loginPage.py')


# logout button
logoutButton = Button(userMainMenu, text="Logout", command=logout)
logoutButton.grid(row=10, column=0)

print(db.is_connected())
userMainMenu.mainloop()
