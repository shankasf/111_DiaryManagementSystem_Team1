import tkinter as tk
from tkinter import *
import mysql.connector
from Team1UserMainPage import *
from AdminMainMenuPage import *

#Window Setup
loginWindow = tk.Tk()
loginWindow.title('Login')
loginWindow.geometry('800x550')
loginWindow.configure(bg = 'light blue')


#Functions
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
        else:
            strikes = 0
            #Code to go to the main menu
            loginWindow.destroy();
            print("Made it past loginWindow.destroy")
            cursor.execute("""SELECT username FROM Users WHERE username=%s AND has_Admin = 'Yes'""", (username,))
            print("Made it past select")
            found = cursor.fetchall()
            if len(found) == 0:
                userMainMenu.mainloop()
                #exec(open("Team1UserMainPage.py").read())
                
                #from subprocess import call;
                #call(["python", "Team1UserMainPage.py"]);
            elif len(found) == 1:
                #AdminMenu.mainloop()
                exec(open("AdminMainMenuPage.py").read())
            else:
                print('There has been an unexpected error. Please try again.')
        #print (found)

def databaseSubmit():
    global strikes
    username = usernameInput.get()
    password = passwordInput.get()
    if len(username) == 0 or len(password) == 0:
        blankSpace.config(bg = 'skyblue', fg = 'black')
        warningTitle.config(bg = '#F0F0F0', fg = '#F0F0F0')
        warning.config(bg = '#F0F0F0', fg = '#F0F0F0')
    else:
        if username == 'diary_management' and password == 'C0mput3r$c13nc3':
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
                password = password,
                database = username
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
            from datetime import datetime
            date = datetime.today().strftime('%Y-%m-%d')
            print(date)

            cursor.execute("""INSERT into Creators(Creator_ID, Creator_Type) value (%s, 'User')""", (num,))
            cursor.execute("""INSERT into users(user_id, username, password, has_admin, admin_id, creation_date, account_age) value (%s, %s, %s, 'No', null, %s, 0)""", (num, username, password, date))
            cursor.execute("""SELECT user_id, username, password, has_admin, admin_id, creation_date, account_age FROM Users WHERE username=%s""", (username,))
            found = cursor.fetchall()
            print(found)

            #Go to user main page here
            loginWindow.destroy();
            userMainMenu.mainloop()
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

loginWindow.mainloop()
