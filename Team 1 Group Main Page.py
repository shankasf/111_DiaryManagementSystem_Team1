import mysql.connector
import tkinter as tk
from tkinter import *

groupMainMenu = tk.Tk()
groupMainMenu.title('Group Main Menu')
groupMainMenu.geometry('1920x1080')
groupMainMenu.config(bg='light blue')

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jackie2013",
    database="diary_management"
)

cursor = db.cursor()

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
logoutButton = tk.Button(text="Logout", width=15, height=2, bg="blue", fg="black")
logoutButton.pack(side=tk.BOTTOM, expand=False, fill=None)



groupMainMenu.mainloop()
