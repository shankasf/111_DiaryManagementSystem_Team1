import tkinter as tk
from tkinter import *
import mysql.connector

#Window Setup
loginWindow = tk.Tk()
loginWindow.title('Login')
loginWindow.geometry('800x500')
loginWindow.configure(bg = 'light blue')


#Functions
#If having trouble connecting, check that the user and password are correct
db = mysql.connector.connect (
    host = "localhost",
    #Username and password must be the same as in mySQL
    user = "root",
    password = "C0mput3r$c13nc3",
    database = "diary_management"
    )

cursor = db.cursor()
#The user gets three tries to enter the password. However, once they reach three strikes, the window will close
strikes = 0

def submit():
    #Python won't let you use a variable from outside the function unless you use this 'global' declaration in the function
    global strikes
    #You can't measure an entry's length by itself, but you can take it and apply it to another variable
    #Then you can measure, use, apply, etc the variable
    username = usernameInput.get()
    password = passwordInput.get()
    if len(username) == 0 or len(password) == 0:
        #The .config is how you change the labels after they are initially created
        blankSpace.config(bg = 'skyblue', fg = 'black')
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
        #else:
            #Code to go to the main menu
        #print (found)


#Visuals Setup
    #Note: It is important to separate .grid and .place from the original section, otherwise we cannot get the values from the Entry objects
whiteSection = tk.Label(loginWindow, width = 50, height = 25, text = '', bg = '#F0F0F0')
whiteSection.grid(padx=(200, 0), pady=(50, 0))

title = tk.Label(loginWindow, width = 35, height = 2, text = 'Login', font=('Arial', 12, 'bold'), bg = 'lightgrey')
title.place(x = 200, y = 50)

usernameLabel = tk.Label(loginWindow, width = 10, height = 1, text = 'Username')
usernameLabel.place(x = 240, y = 120)
passwordLabel = tk.Label(loginWindow, width = 10, height = 1, text = 'Password')
passwordLabel.place(x = 240, y = 160)

usernameInput = tk.Entry(loginWindow, width = 30)
usernameInput.place(x = 320, y = 120)
passwordInput = tk.Entry(loginWindow, width = 30, show = '*')
passwordInput.place(x = 320, y = 160)

submitButton = tk.Button(loginWindow, text = 'Submit', width = 20, padx = 30, bg = 'blue', fg = 'white', command = submit).place(x = 280, y = 210)

#bg = 'skyblue', fg = 'black'
blankSpace = tk.Label(loginWindow, text = 'Please enter a username and password', width = 30, height = 2, bg = '#F0F0F0', fg = '#F0F0F0')
blankSpace.place(x = 275, y = 250)

warning = tk.Label(loginWindow, width = 30, height = 6, text = 'The username or password\n is incorrect.\nPlease try again.', bg = '#F0F0F0', fg = '#F0F0F0')
warning.place(x = 275, y = 320)
warningTitle = tk.Label(loginWindow, width = 14, height = 1, text = 'Warning', font=('Arial', 18, 'bold'), bg = '#F0F0F0', fg = '#F0F0F0')
warningTitle.place(x = 275, y = 300)
