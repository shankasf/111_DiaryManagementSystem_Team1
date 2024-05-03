import mysql.connector
import tkinter as tk
from tkinter import *

diaryPage = tk.Tk()
diaryPage.title('Diary Page')
diaryPage.geometry('1920x1080')
diaryPage.config(bg='light blue')

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jackie2013",
    database="diary_management"
)

cursor = db.cursor()

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
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

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
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

    # create cursor
    cursor = db.cursor()

    diaryPage.destroy()
    print('made it past diary.destroy()')
    exec(open("records.py").read())
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
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

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
        print_records += str('Record Name: ' + record[6] + '\n' + 'Record Description: ' + record[7]) + '\n'

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
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

    # create cursor
    cursor = db.cursor()

    diaryPage.destroy()
    print('made it past diary.destroy()')
    exec(open("galleries.py").read())
    print('opened galleries.py')

    # Commit Changes
    db.commit()
    # Close Connection
    db.close()


# galleries button
createGalleriesBtn = Button(diaryPage, text="Create Records", command=createGalleries)
createGalleriesBtn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# logout function

def logout():
    # connect ot the database
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

    # create cursor
    cursor = db.cursor()

    diaryPage.destroy()
    print('made it past diaryPpage.destroy()')
    exec(open("loginPage.py").read())
    print('opened loginPage.py')


# logout button
logoutButton = Button(diaryPage, text="Logout", command=logout)
logoutButton.grid(row=5, column=0)




diaryPage.mainloop()
