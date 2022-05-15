from tkinter import *
from tkinter import messagebox
import mysql.connector



# Start of Back-end

# Insertion of data func.
def insertData():
    id = enterId.get()
    name = enterName.get()
    album = enterAlbum.get()

    if (id == "" or name == "" or dept == ""):
        messagebox.showwarning("Cannot insert", "All the fields are required!")
    else:
        f = open("password.txt", "r")
        lines = f.readlines()
        secret_password = lines[0]
        f.close()

        myDB = mysql.connector.connect(
        host="localhost",
        user="Artem",
        password=secret_password,
        database="artebomba_world"
        )
        myCur = myDB.cursor()
        myCur.execute("insert into empDetails values('" + id +
                      "', '" + name + "', '" + album + "' ) ")
        myDB.commit()

        # Clear out the entries from the fields filled by user
        enterId.delete(0,"end")
        enterName.delete(0, "end")
        enterAlbum.delete(0, "end")

        messagebox.showinfo("Insert Status", "Data inserted successfully!")
        myDB.close()


# Updating of data func.
def updateData():
    id = enterId.get()
    name = enterName.get()
    album = enterAlbum.get()

    if (id == "" or name == "" or dept == ""):
        messagebox.showwarning("Cannot update", "All the fields are required!")
    else:
        f = open("password.txt", "r")
        lines = f.readlines()
        secret_password = lines[0]
        f.close()

        myDB = mysql.connector.connect(
        host="localhost",
        user="Artem",
        password=secret_password,
        database="artebomba_world"
        )
        myCur = myDB.cursor()
        myCur.execute("update empDetails set empName='" + name +
                      "', empDept='" + album + "' where empId='" + id + "'")
        myDB.commit()

        # Clear out the entries from the fields filled by user
        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterAlbum.delete(0, "end")

        messagebox.showinfo("Update Status", "Data updated successfully!")
        myDB.close()

# Get data func.      
def getData():
    
    if (enterId.get() == "" ):
        messagebox.showwarning("Cannot fetch", "Please provide correct song ID")
    else:
        f = open("password.txt", "r")
        lines = f.readlines()
        secret_password = lines[0]
        f.close()

        myDB = mysql.connector.connect(
        host="localhost",
        user="Artem",
        password=secret_password,
        database="artebomba_world"
        )
        myCur = myDB.cursor()
        myCur.execute("select * from empDetails where empID='" +
                      enterId.get() + "'")
        rows = myCur.fetchall()
        for row in rows:
            enterName.insert(0, row[1])
            enterAlbum.insert(0, row[2])
        myDB.close()

# Delete data func
def deleteData():
    if (enterId.get() == ""):
        messagebox.showwarning("Cannot delete", "Please provide correct song ID")
    else:
        f = open("password.txt", "r")
        lines = f.readlines()
        secret_password = lines[0]
        f.close()

        myDB = mysql.connector.connect(
            host="localhost",
            user="Artem",
            password=secret_password,
            database="artebomba_world"
        )
        myCur = myDB.cursor()
        myCur.execute("delete from empDetails where empID='" +
                      enterId.get() + "'")
        myDB.commit()

        # Clear out the entries from the fields filled by user
        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterAlbum.delete(0, "end")

        messagebox.showinfo("Delete Status", "Data deleted successfully!")
        myDB.close()

#Show func
def show():
    f = open("password.txt", "r")
    lines = f.readlines()
    secret_password = lines[0]
    f.close()

    myDB = mysql.connector.connect(
        host="localhost",
        user="Artem",
        password=secret_password,
        database="artebomba_world"
    )
    myCursor = myDB.cursor()
    myCursor.execute("SELECT * FROM music")
    rows = myCursor.fetchall()
    showData.delete(0,showData.size())
    for row in rows:
        addData = str(row[0]) + ' ' + row[1] + ' ' + row[2]
        showData.insert(showData.size() + 1, addData)
    myDB.close()

# reset data func.
def resetFields():
    enterId.delete(0, "end")
    enterName.delete(0, "end")
    enterAlbum.delete(0, "end")

# Start of Front-end. Establish main window size and title
window = Tk()
window.geometry("800x400")
window.title("Artebomba's music CRUD app")

# Set labels
songId = Label(window, text="№",font=("Ubuntu", 14))
songId.place(x=20,y=40)

songName = Label(window, text="Song name",font=("Ubuntu", 14))
songName.place(x=20,y=80)

songAlbum = Label(window, text="From album",font=("Ubuntu", 14))
songAlbum.place(x=20,y=120)

# Set entry fields
enterId = Entry(window)
enterId.place(x=200,y=45)

enterName = Entry(window)
enterName.place(x=200,y=85)

enterAlbum = Entry(window)
enterAlbum.place(x=200,y=125)

# Creation of buttons to manage the database
insertBtn = Button(window, text="Insert", font=("Ubuntu", 14), bg="green", command=insertData)
insertBtn.place(x=20, y= 180)

updateBtn = Button(window, text="Update", font=("Ubuntu", 14), bg="green", command=updateData)
updateBtn.place(x=80, y= 180)

getBtn = Button(window, text="Fetch", font=("Ubuntu", 14), bg="green", command=getData)
getBtn.place(x=150, y= 180)

deleteBtn = Button(window, text="Delete", font=("Ubuntu", 14), bg="red", command=deleteData)
deleteBtn.place(x=210, y= 180)

resetBtn = Button(window, text="Reset", font=("Ubuntu", 14), bg="red", command=resetFields)
resetBtn.place(x=270, y= 180)

#Add Listbox
showData = Listbox(window)
showData.place(x=330, y=30)

window.mainloop()







