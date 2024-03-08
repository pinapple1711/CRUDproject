from tkinter import*
from tkinter import messagebox
import mysql.connector

window = Tk()
window.geometry("600x270")
window.title("Employee CRUD App")


empId = Label(window,text="Employee ID:",font=("Arial",12))
empId.place(x=20,y=30)

empName=Label(window,text="Employee name: ",font=("Serif",12))
empName.place(x=20,y=60)

empDept = Label(window,text="Employee dept",font=("Serif",12))
empDept.place(x=20,y=90)

enterId =Entry(window)
enterId.place(x=170,y=30)

enterName = Entry(window)
enterName.place(x=170,y=60)

enterDept = Entry(window)
enterDept.place(x=170,y=90)

def insertData():

    id = enterId.get()
    name = enterName.get()
    dept= enterDept.get()

    if(id==""or name=="" or dept ==""):
        messagebox.showwarning("Cannot Insert","All the feilds are required")
    else:
        myDB = mysql.connector.connect(host="localhost",user="root",passwd="Mzn95188?",database="employee")
        myCur = myDB.cursor()
        myCur.execute("insert into empDetails values('"+id+"','"+name+"','"+dept+"')")
        myDB.commit()

        enterId.delete(0,"end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")

        messagebox.showinfo("Insert Statues","Data inserted successfully")
        myDB.close()
        show()


def updateData():

    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()

    if (id =="" or name=="" or dept==""):
        messagebox.showwarning("Cannot Update","All the felid are required")
    else:
        myDB = mysql.connector.connect(host = "localhost", user="root",passwd="Mzn95188?", database="employee")
        myCur = myDB.cursor()
        myCur.execute("update empDetails set empName ='"+name+"', empDept ='"+dept+"' where empId = '"+id+"'")
        myDB.commit()
        enterId.delete(0,"end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")
        show()
        messagebox.showinfo("Update Status","Data Updated successfully")
        myDB.close()
       

def getData():
    
    if(enterId.get() == ""):
        messagebox.showwarning("Fetch Status ","Please provide the id to fetch the data")
    else:
        myDb = mysql.connector.connect(host="localhost",user="root",passwd="Mzn95188?", database="employee")
        myCur = myDb.cursor()
        myCur.execute("select*from empDetails where empId='"+enterId.get()+"'")
        rows = myCur.fetchall()

        for row in rows:
            enterName.insert(0,row[1])
            enterDept.insert(0,row[2])
        myDb.close()  

def deleteData():
    
    if(enterId.get() ==""):
        messagebox.showwarning("Cannot Delete","Emplyee Id is needed")
    else:
        myDB = mysql.connector.connect(host="localhost",user ="root",passwd ="Mzn95188?", database="employee")
        myCur = myDB.cursor()
        myCur.execute("delete from empDetails where empId = '"+enterId.get()+"'")
        myDB.commit()

        enterDept.delete(0,"end")
        enterId.delete(0,"end")
        enterName.delete(0,"end")
        messagebox.showinfo("Delete Status","you deleted the information succesfully")
        show()        
        myDB.close()


def show():
    myDB = mysql.connector.connect(host="localhost",user="root",passwd = "Mzn95188?", database="employee")
    mycur = myDB.cursor()
    mycur.execute("select*from empDetails")
    rows = mycur.fetchall()
    showData.delete(0,showData.size())

    for i in rows:
        addData = str(i[0])+'  '+i[1]+'  '+i[2]
        showData.insert(showData.size()+1,addData)

    myDB.close()     

def resetFields():
    enterId.delete(0,"end")
    enterDept.delete(0,"end")
    enterName.delete(0,"end")


insertBtn = Button(window,text="Insert",font=("sans",12),bg="white",command=insertData)
insertBtn.place(x=20,y=160)

updateBtn = Button(window,text="Update",font=("Sans",12),bg="white",command=updateData)
updateBtn.place(x=80,y=160)

getBtn =Button(window,text="Fetch",font=("Sans",12),bg="white",command=getData)
getBtn.place(x=150,y=160)

deleteBtn = Button(window,text="Delete",font=("Sans",12),bg="White",command=deleteData)
deleteBtn.place(x=210,y=160)

resetBtn = Button(window,text="Reset",font=("Sans",12),bg="White",command=resetFields)
resetBtn.place(x=20,y=210)

showData = Listbox(window)
showData.place(x=330,y=30)
show()

window.mainloop()









        