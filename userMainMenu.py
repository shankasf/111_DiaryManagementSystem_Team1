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

# temp for testing until i can connect to login user
username = "jakie"

db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

cursor = db.cursor()

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


# user_id
def get_userID():
    user_id = cursor.execute("""Select User_ID from Users where Username = %s""", (username,))
    userIdResult = cursor.fetchall()

    LT1 = tk.Label(userMainMenu, text=userIdResult, font=('Times', 20))
    # LT1.pack(side=tk.TOP, expand=False, fill=None)
    LT1.config(bg="light blue", fg="White")


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
viewRecordsBtn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


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
createRecordsBtn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


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
viewAdminsBtn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


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

# logout button
logoutButton = tk.Button(text="Logout", width=15, height=2, bg="blue", fg="black")
# logoutButton.pack(side=tk.BOTTOM, expand=False, fill=None)
logoutButton.grid(row=10, column=0)

print(db.is_connected())
userMainMenu.mainloop()

# # Group
# groupValues = ["View Groups", "Group Requests", "Create Group"]
#
# variable2 = StringVar(userMainMenu)
# variable2.set("Group")
#
# g = OptionMenu(userMainMenu, variable2, *groupValues)
# # g.pack(side=tk.TOP, expand=False, fill=None)
# g.grid(row=8, column=0)
# g.config(width=34, height=4, bg="light blue", fg="black")

# Admin
# adminValues = ["View Admins", "Admin Requests"]
#
# variable3 = StringVar(userMainMenu)
# variable3.set("Admin")
#
# a = OptionMenu(userMainMenu, variable3, *adminValues)
# # a.pack(side=tk.TOP, expand=False, fill=None)
# a.grid(row=9, column=0)
# a.config(width=34, height=4, bg="light blue", fg="black")

# # Planner
# plannerValues = ["Planner Page"]
#
# variable1 = StringVar(userMainMenu)
# variable1.set("Planner")
#
# p = OptionMenu(userMainMenu, variable1, *plannerValues)
# # p.pack(side=tk.TOP, expand=False, fill=None)
# p.grid(row=7, column=0)
# p.config(width=33, height=4, bg="light blue", fg="black")

# admin status
# def get_adminStatus():
#     adminQuery = cursor.execute("""select Has_Admin from Users where Username = %s""", (username,))
#     adminResult = cursor.fetchall()
#
#     if adminResult == 'yes':
#         findAdminQuery = cursor.execute(
#             """select Admin_Name from Admins where admin_ID =(Select admin_id from Users where Username = %s""",
#             (username,))
#
#         LT3 = tk.Button(userMainMenu, text=findAdminQuery, font=('Times', 20))
#         LT3.pack(side=tk.TOP, expand=False, fill=None)
#         LT3.config(bg="light blue", fg="White")
#         # adminLabel = Label(userMainMenu, text=str(findAdminQuery))
#
#     else:
#         LT4 = tk.Button(userMainMenu, text='none', font=('Times', 20))
#         LT4.pack(side=tk.TOP, expand=False, fill=None)
#         LT4.config(bg="light blue", fg="White")

# def get_username():
#     username_query = cursor.execute("""Select Username from Users where User_ID = pass""", (username,))
#     usernameResult = cursor.fetchall()

# recordValues = ["View Records", "Archive Records"]
# variable = StringVar(userMainMenu)
# variable.set("Records")

# r = OptionMenu(userMainMenu, variable, *recordValues)
# # r.pack(side=tk.TOP, expand=False, fill=None)
# r.grid(row=6, column=0)
# r.config(width=33, height=4, bg="light blue", fg="black")
