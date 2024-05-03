import mysql.connector
import tkinter as tk
from tkinter import *
from Team1LoginPageTesting import *

userMainMenu = tk.Tk()
userMainMenu.title('User Main Menu')
userMainMenu.geometry('1500x700')
userMainMenu.config(bg='light blue')

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="C0mput3r$c13nc3",
    database="diary_management"
)

cursor = db.cursor()

def logout():
    userMainMenu.destroy();
    #import subprocess
    #subprocess.run(open["python", "Team1LoginPage - Testing.py"], shell = True)
    #print("Reached the logout function")
    #with open("Team1LoginPage - Testing.py") as file:
        #exec(file.read())
    loginWindow.mainloop()
    
    #from subprocess import call
    #call(["python", "Team1LoginPage.py"])

#Welcome
LT = tk.Label(userMainMenu, text="Welcome!", font=('Times', 50))
#LT.pack(side=TOP, expand=True, fill=None)
LT.pack(expand=True)
LT.config(bg="light blue", fg="white")

#Profile
LT2 = tk.Label(userMainMenu, text="Username = Karina01", font=('Times', 20))
LT2.pack(side=tk.TOP, expand=False, fill=None)
LT2.config(bg="light blue", fg="White")

LT1 = tk.Label(userMainMenu, text="User_ID = 5", font=('Times', 20))
LT1.pack(side=tk.TOP, expand=False, fill=None)
LT1.config(bg="light blue", fg="White")

LT3 = tk.Label(userMainMenu, text="Admin = none", font=('Times', 20))
LT3.pack(side=tk.TOP, expand=False, fill=None)
LT3.config(bg="light blue", fg="White")

#Menu Intro
LT0 = tk.Label(userMainMenu, text="Main Menu", font=('Times', 25))
LT0.pack(side=TOP, expand=True)
LT0.config(bg="light blue", fg="white")

#Record
recordValues=["View Records", "Archive Records"]
variable = StringVar(userMainMenu)
variable.set("Records")

r = OptionMenu(userMainMenu, variable, *recordValues)
r.pack(side=tk.TOP, expand=False, fill=None)
r.config(width=33, height=4, bg="light blue", fg="black")

#Planner
plannerValues=["Planner Page"]

variable1 = StringVar(userMainMenu)
variable1.set("Planner")

p = OptionMenu(userMainMenu, variable1, *plannerValues)
p.pack(side=tk.TOP, expand=False, fill=None)
p.config(width=33, height=4, bg="light blue", fg="black")

#Group
groupValues=["View Groups", "Group Requests", "Create Group"]

variable2 = StringVar(userMainMenu)
variable2.set("Group")

g = OptionMenu(userMainMenu, variable2, *groupValues)
g.pack(side=tk.TOP, expand=False, fill=None)
g.config(width=34, height=4, bg="light blue", fg="black")


#Admin
adminValues=["View Admins", "Admin Requests"]

variable3 = StringVar(userMainMenu)
variable3.set("Admin")

a = OptionMenu(userMainMenu, variable3, *adminValues)
a.pack(side=tk.TOP, expand=False, fill=None)
a.config(width=34, height=4, bg="light blue", fg="black")


#logout button
logoutButton = tk.Button(text="Logout", width=15, height=2, bg="blue", fg="black", command = logout)
logoutButton.pack(side=tk.BOTTOM, expand=False, fill=None)


#User Profile Data
# 'pass' until have user_id variable when connected to log in and sign in page
def get_adminStatus():
    adminQuery = "select Has_Admin from Users where User_ID = pass"

    findAdminQuery = "select Admin_Name from Admins where admin_ID =(Select admin_id from Users where User_ID = pass)"

    if(adminQuery == 'yes'):
        print(findAdminQuery)
    else:
        print('none')

def get_username():
    username_query = "Select Username from Users where User_ID = pass"

def get_userID():
    user_id = "Select User_ID from Users where User_ID = pass"

userMainMenu.mainloop()
