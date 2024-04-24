import mysql.connector
import tkinter as tk
from tkinter import *
from loginPage import *
from userMainMenu import *

createrecordPage = tk.Tk()
createrecordPage.title('Records Page')
createrecordPage.geometry('1920x1080')
createrecordPage.config(bg='light blue')

createrecordPage.grid_rowconfigure(0, weight=1)
createrecordPage.grid_columnconfigure(0, weight=1)

db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

cursor = db.cursor()


# create function

def create():
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

    cursor = db.cursor()

    record_ID1 = recordID.get()
    record_name1 = recordName.get()
    diary_ID1 = diaryID.get()
    in_gallery1 = inGallery.get()
    # creation_date1 = creationDate.get()
    # record_age1 = recordAge.get()
    record_description1 = recordDescription.get()
    # gallery_ID1 = galleryID.get()

    # set foriegn keys = 0

    cursor.execute('SET FOREIGN_KEY_CHECKS = 0;')
    print('SET FOREIGN_KEY_CHECKS = 0;')

    cursor.execute(
        """insert into records(record_id, diary_id, in_gallery, gallery_id, creation_date, record_age, record_name, record_description) value (%s, %s, %s, null, current_date , 0, %s, %s)""",
        (record_ID1, diary_ID1, in_gallery1, record_name1,
         record_description1))

    db.commit()
    db.close()

    # Clear textbox
    recordName.delete(0, END)
    recordID.delete(0, END)
    diaryID.delete(0, END)
    inGallery.delete(0, END)
    # galleryID.delete(0, END)
    #creationDate.delete(0, END)
    # recordAge.delete(0, END)
    recordDescription.delete(0, END)


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

# galleryID = Entry(createrecordPage, width=10)
# galleryID.grid(row=6, column=0, padx=20)

recordName = Entry(createrecordPage, width=15)
recordName.grid(row=8, column=0, padx=20)

# creationDate = Entry(createrecordPage, width=15)
# creationDate.grid(row=10, column=0, padx=20)

# recordAge = Entry(createrecordPage, width=15)
# recordAge.grid(row=12, column=0, padx=20)

inGallery = Entry(createrecordPage, width=15)
inGallery.grid(row=14, column=0, padx=20)

recordDescription = Entry(createrecordPage, width=20)
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

# creationDateLabel = Label(createrecordPage, text="Creation Date:")
# creationDateLabel.grid(row=9, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

# recordAgeLabel = Label(createrecordPage, text="Record Age:")
# recordAgeLabel.grid(row=11, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

inGalleryLabel = Label(createrecordPage, text="In Gallery:")
inGalleryLabel.grid(row=13, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

recordDescriptionLabel = Label(createrecordPage, text="Record Description:")
recordDescriptionLabel.grid(row=15, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

# create button
createBtn = Button(createrecordPage, text="Create", command=create)
createBtn.grid(row=17, column=0, columnspan=3, pady=10, padx=10, ipadx=100)


# back btn funcionality
def backToUserMenu():
    db = mysql.connector.connect(host="localhost", user="root", password="Jackie2013", database="diary_management")

    cursor = db.cursor()

    # record page closed
    createrecordPage.destroy()
    print('record page closed')

    # opened userMainMenu
    exec(open("userMainMenu.py").read())
    print('opened userMainMenu.py')

    db.commit()
    db.close()


# back btn
backBtn = Button(createrecordPage, text='Back', command=backToUserMenu)
backBtn.grid(row=18, column=0, columnspan=3, pady=10, padx=10, ipadx=100)


createrecordPage.mainloop()

db.commit()
db.close()
