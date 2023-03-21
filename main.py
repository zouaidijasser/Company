# libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database


# Database
db = Database("company.db")




# company informations
root = Tk()
root.title('Company')
root.geometry('1350x690+0+40')
root.resizable(True,True)
root.configure(bg='#253237')


# champs
name = StringVar()
age = StringVar()
job = StringVar()
gender = StringVar()
email = StringVar()
mobile = StringVar()


# entries frame
entries_frame = Frame(root, bg='#2c7da0')
entries_frame.place(x=20,y=10,width=400,height=670)
title = Label(entries_frame,text='COMPANY',font=('Cursive',25,'bold'),bg='#2c7da0',fg='white')
title.place(x=10,y=10)

# name
label_name = Label(entries_frame,text='Name :',bg='#2c7da0',font=('Calibri',16),fg='white')
label_name.place(x=10,y=60)
input_name = Entry(entries_frame,textvariable=name,width=20,font=('Calibri',16))
input_name.place(x=120,y=60)


# job
label_job = Label(entries_frame,text='Job :',bg='#2c7da0',font=('Calibri',16),fg='white')
label_job.place(x=10,y=110)
input_job = Entry(entries_frame,textvariable=job,width=20,font=('Calibri',16))
input_job.place(x=120,y=110)


# gender
label_gender = Label(entries_frame,text='Gender :',bg='#2c7da0',font=('Calibri',16),fg='white')
label_gender.place(x=10,y=160)
combo_gender = ttk.Combobox(entries_frame,textvariable=gender,width=18,state='readonly',font=('Calibri',16))
combo_gender['values'] = ("Male","Female")
combo_gender.place(x=120,y=160)


# age
label_age = Label(entries_frame,text='Age :',bg='#2c7da0',font=('Calibri',16),fg='white')
label_age.place(x=10,y=210)
input_age = Entry(entries_frame,textvariable=age,width=20,font=('Calibri',16))
input_age.place(x=120,y=210)

# email
label_email = Label(entries_frame,text='Email :',bg='#2c7da0',font=('Calibri',16),fg='white')
label_email.place(x=10,y=260)
input_email = Entry(entries_frame,textvariable=email,width=20,font=('Calibri',16))
input_email.place(x=120,y=260)

# mobile
label_mobile = Label(entries_frame,text='Mobile :',bg='#2c7da0',font=('Calibri',16),fg='white')
label_mobile.place(x=10,y=310)
input_mobile = Entry(entries_frame,textvariable=mobile,width=20,font=('Calibri',16))
input_mobile.place(x=120,y=310)

# address
label_adr = Label(entries_frame,text='Address :',bg='#2c7da0',font=('Calibri',16),fg='white')
label_adr.place(x=10,y=360)
input_adr = Text(entries_frame,width=30,height=2,font=('Calibri',16))
input_adr.place(x=10,y=410)


# hide and show functions
def hide ():
    root.geometry('400x690+0+40')
def show ():
    root.geometry('1350x690+0+40')


# hide and show buttons
btnhide = Button(entries_frame,text='HIDE',cursor='hand2',bg='red',fg='white',bd="5",relief=SOLID,command=hide)
btnhide.place(x=270,y=10)
btnShow = Button(entries_frame,text='SHOW',cursor='hand2',bg='green',fg="white",bd="5",relief=SOLID,command=show)
btnShow.place(x=310,y=10)

# functions

# get function
def getData(event) :
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data['values']
    name.set(row[1])
    age.set(row[2])
    job.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    mobile.set(row[6])
    input_adr.delete(1.0,END)
    input_adr.insert(END,row[7])


# display function
def displayAll() :
    tv.delete(*tv.get_children())
    for row in db.fetch() :
        tv.insert("",END,values=row)


# delete function
def delete () :
    db.remove(row[0])
    Clear()
    displayAll()


# clear function
def Clear () :
    name.set("")
    age.set("")
    job.set("")
    gender.set("")
    mobile.set("")
    email.set("")
    input_adr.delete(1.0,END)

# add functions
def add () :
    if input_name.get() == '' or input_age.get() == '' or input_adr.get(1.0,END) == "":
        messagebox.showerror('error','please fill all th blanks')
        return
    db.insert(
        input_name.get(),
        input_age.get(),
        input_job.get(),
        input_email.get(),
        combo_gender.get(),
        input_mobile.get(),
        input_adr.get(1.0,END))
    messagebox.showinfo('success','Added')
    Clear()
    displayAll()

# update function
def update () :
    if input_name.get() == '' or input_age.get() == '' or input_adr.get(1.0,END) == "":
        messagebox.showerror('error','please fill all the blanks')
        return
    db.update(row[0],input_name.get(),input_age.get(),input_job.get(),input_email.get(),combo_gender.get(),input_mobile.get(),input_adr.get(1.0,END)
            )
    messagebox.showinfo('successs','Updated')
    Clear()
    displayAll()

# buttons frame
btns_frame = Frame(entries_frame,bg="#2c7da0")
btns_frame.place(x=0,y=480,width=390,height=190)

# add button
btnAdd = Button(btns_frame,
                text='ADD',
                width=20,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#16a085',
                bd=0,
                command=add
                ).place(x=75,y=5)

# edit button
btnEdit = Button(btns_frame,
                text='EDIT',
                width=20,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#003f88',
                bd=0,
                command=update
                ).place(x=75,y=50)

# delete button
btnDelete = Button(btns_frame,
                text='DELETE',
                width=20,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#c0392b',
                bd=0,
                command=delete
                ).place(x=75,y=95)

# clear button
btnClear = Button(btns_frame,
                text='CLEAR',
                width=20,
                height=1,
                font=('Calibri',16),
                fg='white',
                bg='#f39c12',
                bd=0,
                command=Clear
                ).place(x=75,y=140)

# treeview
tree_frame = Frame(root,bg='white')
tree_frame.place(x=450,y=10,width=875,height=610)
style = ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',13),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=('Calibri',13))
tv = ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style='mystyle.Treeview')
tv.heading("1",text="ID")
tv.column("1",width="40")
tv.heading("2",text="NAME")
tv.column("2",width="140")
tv.heading("3",text="AGE")
tv.column("3",width="50")
tv.heading("4",text="JOB")
tv.column("4",width="120")
tv.heading("5",text="EMAIL")
tv.column("5",width="150")
tv.heading("6",text="GENDRE")
tv.column("6",width="90")
tv.heading("7",text="MOBILE")
tv.column("7",width="150")
tv.heading("8",text="ADDRESS")
tv.column("8",width="150")
tv['show'] = 'headings'
tv.bind('<ButtonRelease-1>',getData)
tv.place(x=1,y=1,height=610,width=875)




displayAll()
root.mainloop()