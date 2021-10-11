import tkinter as tk
from datetime import date
import tkinter.font as tkFont
import MySql
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # python imaging library


# front presentatin
def DATA(roll=1):
    global password
    global User
    global cur
    cur = roll
    if connected == True:
        data = MySql.get_data(roll, user=User, password=password)
        roll = data[0][0]
        name = data[0][1]
        status = data[0][2]
        if status == '  P  ':
            status = 'Present'
        elif status == '  Ab  ':
            status= "Absent"
    else:
        roll = "EMPTY"
        name = "NOTHING TO SHOW"
        status = "N/A"
    data = tk.Label(rw, text=str(roll) + "  " + str(name), background="#fde871", width=25, font=fontStyle3)
    stat = tk.Label(rw, text=str(status), background="#fde871", width=25, font=fontStyle2)
    stat.place(relx=0.12, rely=0.43, anchor='nw')
    data.place(relx=0.05, rely=0.399, anchor='sw')


# Loading database
def Load():
    global password
    global pwindow
    global User
    global connected
    r = tk.Tk()
    r.configure(bg="#fde871", height="500", width="900")
    label = tk.Label(r, text="USER NAME", background="#fde871", font=fontStyle)
    label.pack()
    usr = tk.Entry(r, font=fontStyle1, textvariable=User)
    usr.pack()

    labelpswd = tk.Label(r, text="Enter Password", background="#fde871", font=fontStyle, textvariable=password)
    labelpswd.pack()
    pswd = tk.Entry(r, font=fontStyle1)
    pswd.pack()
    Enter = tk.Button(r, text="connect", height=1, font=fontStyle1, command=lambda: connection())
    Enter.pack()
    password = pswd
    User = usr
    pwindow = r
    connected = False


def connection():
    global data
    global pwindow
    global password
    global User
    global studentrcd
    global connected
    M = 0
    if connected != True:
        print(password, User)
        password = password.get()
        User = User.get()
        try:
            MySql.addnewdate(password=password, user=User)
            pwindow.destroy()
        except:
            print("Wrong Password or Username")  # ERROR
            connected = False
            password = None
            User = None
            pwindow.destroy()  # DESTROYNG CURRENT WINDOW AS WRONG CREDENTIALS
            messagebox.showerror("ERROR OCCURED", "Wrong username or password")
            Load()
        M = 1  # preventing Data to be called stopping auto refresh on pressing button
    data = MySql.exc("select roll,Name," + MySql.today + " from attendence ", password=password, user=User,get=None)
    tbl = ""
    print(data)
    roll = ""
    name = ""
    status = ""
    for a in range(len(data)):
        roll += str(data[a][0]) + "\n"
        name += str(data[a][1]) + "\n"
        status += str(data[a][2]) + "\n"
    studentrcd = [roll, name, status]
    connected = True
    if M == 1:
        DATA()
    view()
    print(studentrcd)


# PREESENT AND ABSENT
def p_ab(a):
    if a == "p":
        MySql.exc("update  attendence set " + str(MySql.today) + "= '  P  ' where roll =" + str(cur), get="update",
                  password=password, user=User)
    elif a == "ab":
        MySql.exc("update  attendence set " + str(MySql.today) + "= '  Ab  ' where roll =" + str(cur), get="update",
                  password=password, user=User)
    connection()
    DATA(cur)


# def tables():

def view():
    Roll = tk.Label(rw, text=studentrcd[0], background="#fde871", font=fontStyle)
    Roll.place(relx=0.75, rely=0.3, anchor='ne')
    name = tk.Label(rw, text=studentrcd[1], background="#fde871", font=fontStyle, justify="left")
    name.place(relx=0.89, rely=0.3, anchor='ne')
    P_ab = tk.Label(rw, text="  " + studentrcd[2] + " ", background="#fde871", font=fontStyle)
    P_ab.place(relx=1.0, rely=0.3, anchor='ne')


def pvnxt(r):
    global cur
    max = len(data)
    min = 1
    if r == "n" and cur < len(data):
        print("command is here")
        cur += 1
    elif r == "p" and cur > min:
        cur -= 1
    print(cur, cur < len(data))
    DATA(roll=cur)


def search():
    global cur
    global srchen
    roll = srchen.get()
    DATA(roll)
    cur = int(roll)


def add_refresh(Name,data,user,pswd):
    global awindow
    MySql.exc(
        "INSERT INTO attendence (roll,Name) VALUES(" + str(len(data) + 1) + ',' + '"' + Name + '"' + ");",
        user=user, password=pswd, get="update")
    #MySQL command
    p_ab("r") #refreshing
    awindow.destroy()


def newdata(data,user,pswd):
    global awindow
    global connected
    if connected==True:
        r = tk.Tk()
        r.geometry()
        label = tk.Label(r, text="ENTER NAME", background="#fde871", font=fontStyle)
        label.pack()
        name = tk.Entry(r, font=fontStyle1, textvariable=User)
        name.pack()
        Enter = tk.Button(r, text="Add Name", height=1, font=fontStyle1, command=lambda:add_refresh(Name=str(name.get()),data=data,user=user,pswd=pswd))
        Enter.pack()
        awindow=r


    else:
        messagebox.showerror(title="ERROR",message="AUTHORISATION REQUIRED")
        Load()


# ================DEFAULT===============
password = None
User = None
studentrcd = " NONE "
connected = False
data = None
pwindow = None
awindow = None
cur = 1  # current roll no of student
# =======================================================================================
today = date.today()

rw = tk.Tk()
height = rw.winfo_height()
width = rw.winfo_width()
# fonts
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
fontStyle1 = tkFont.Font(family="Lucida Grande", size=15)
fontStyle2 = tkFont.Font(family="Lucida Grande", size=25)
fontStyle3 = tkFont.Font(family="Lucida Grande", size=30)

rw.configure(bg="#fde871", height="500", width="900")
label = tk.Label(rw, text="School Attendance System", background="#fde871", font=fontStyle1)
label.place(relx=0.01, rely=0.01, anchor='nw')

# ===============IMAGES==================
iconn = ImageTk.PhotoImage(file="conn.png")
iconnected = ImageTk.PhotoImage(file="connect.png")
icant = ImageTk.PhotoImage(file="name cant.png")
isearch = ImageTk.PhotoImage(file="search.png")
ipres = ImageTk.PhotoImage(file="present.png")
iabs = ImageTk.PhotoImage(file="Absent.png")
iprevious = ImageTk.PhotoImage(file="previous.png")
inext = ImageTk.PhotoImage(file="next.png")
irefresh = ImageTk.PhotoImage(file="refresh.png")

view()
# P_AbName.pack()


# creating new button for Data, present and absent
Pbtn = tk.Button(image=ipres, border=0, bg='#fde871', activebackground='#fde871', command=lambda: p_ab("p"))
Pbtn.place(relx=0.2, rely=0.7, anchor='ne')

Abtn = tk.Button(image=iabs, border=0, bg='#fde871', activebackground='#fde871', command=lambda: p_ab("ab"))
Abtn.place(relx=0.3, rely=0.7, anchor='ne')

Date = tk.Label(rw, text=str(today), background="#fde871", font=tkFont.Font(family="Lucida Grande", size=40))
Date.place(relx=0.01, rely=0.07, anchor='nw')

# NEXT AND PREVIOUS
Prv = tk.Button(image=iprevious, border=0, bg='#fde871', activebackground='#fde871', command=lambda: pvnxt("p"))
Prv.place(relx=0.4, rely=0.715, anchor='ne')

Nxt = tk.Button(image=inext, border=0, bg='#fde871', activebackground='#fde871', command=lambda: pvnxt("n"))
Nxt.place(relx=0.5, rely=0.715, anchor='ne')

#Refresh buttons
refresh= tk.Button(image=irefresh, border=0, bg='#fde871', activebackground='#fde871', command=lambda: p_ab("r"))
refresh.place(relx=0.55, rely=0.92, anchor='ne')

# NAME AND ROLL NO

DATA()
#new data cant find your name
ENT = tk.Button(image=icant, border=0, bg='#fde871', activebackground='#fde871',command=lambda :newdata(data,User,password))
ENT.place(relx=0, rely=1, anchor='sw')

LOAD = tk.Button(image=iconn, border=0, bg='#fde871', activebackground='#fde871', command=lambda: Load())
LOAD.place(relx=0.99, rely=0.92, anchor='ne')

# search
slbl = tk.Label(rw, text="ENTER ROLL", background="#fde871", font=fontStyle1)
slbl.place(relx=0.735, rely=0.03, anchor='ne')
srchen = tk.Entry(rw, font=fontStyle1)
srchen.place(relx=0.9, rely=0.03, anchor='ne')
Search = tk.Button(image=isearch, border=0, bg='#fde871', activebackground='#fde871',
                   command=lambda: DATA(int(srchen.get())))
Search = tk.Button(image=isearch, border=0, bg='#fde871', activebackground='#fde871',
                   command=lambda: DATA(int(srchen.get())))
Search.place(relx=0.92, rely=0.01, anchor='ne', )
rw.mainloop()
