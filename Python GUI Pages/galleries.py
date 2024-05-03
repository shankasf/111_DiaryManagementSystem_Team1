import mysql.connector
import tkinter as tk
from tkinter import *

from loginPage import *
from userMainMenu import *


creategalleriePage = tk.Tk()
creategalleriePage.title('Gallery Page')
creategalleriePage.geometry('1920x1080')
creategalleriePage.config(bg='light blue')

creategalleriePage.grid_rowconfigure(0, weight=1)
creategalleriePage.grid_columnconfigure(0, weight=1)

db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

cursor = db.cursor()


# create function

def createGallery():
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

    cursor = db.cursor()

    galleryId2 = galleryID.get()
    diaryID2 = diaryID.get()
    # creationDate2 = creationDate.get()
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


# Intro
intro = tk.Label(creategalleriePage, text="Create Gallery", font=('Helvetica', 40))
intro.grid(row=0, column=0, columnspan=3, pady=10, padx=10, ipadx=100)
intro.config(bg="light blue", fg="white")

# create textboxes
galleryID = Entry(creategalleriePage, width=10)
galleryID.grid(row=2, column=0, padx=20)

diaryID = Entry(creategalleriePage, width=10)
diaryID.grid(row=4, column=0, padx=20)

# creationDate = Entry(creategalleriePage, width=10)
# creationDate.grid(row=6, column=0, padx=20)

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

# creationDateLabel = Label(creategalleriePage, text="Creation Date:")
# creationDateLabel.grid(row=5, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

galleryNameLabel = Label(creategalleriePage, text="Gallery Name:")
galleryNameLabel.grid(row=7, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

# galleryAgeLabel = Label(creategalleriePage, text="Gallery Age:")
# galleryAgeLabel.grid(row=9, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

recordNumLabel = Label(creategalleriePage, text="Record Number:")
recordNumLabel.grid(row=11, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

# create button
createBtn = Button(creategalleriePage, text="Create", command=createGallery)
createBtn.grid(row=17, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

creategalleriePage.mainloop()

db.commit()
db.close()
