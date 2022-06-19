from os import access
import tkinter as tkinter
from tkinter import *
import login_db
import psycopg2



connector=psycopg2.connect(database="shopclassy",user='shopclassy',host="127.0.0.1",password="classyclothes",port="5432")
cursor=connector.cursor()
print(connector)
    
window = tkinter.Tk()
window.geometry("400x400")
window.title("shopclassy login")
box=tkinter.Label(window,text="\n\nwelcome to classy clothes! \n lets Begin your shopping!!\n",font=('Dingbat',20),fg='green')
box.pack()

username = tkinter.Label(window, text="username:", font=("consolas", 20))
entry1 = tkinter.Entry(window)


def show():
    p = password.get() #get password from entry
    print(p)


def access():
    user=entry1.get()
    passcode=passEntry.get()
    data=(user,passcode)
    sql_q= 'SELECT isadmin FROM Authentication where username like %s and passcode like %s'
    data=(user,passcode)
    cursor.execute(sql_q,data)
    isadmin=cursor.fetchall()
    # print(isadmin[0][0])
    variable1= isadmin[0][0]
    # print(variable1)
    if variable1 == 0:
        print('user')
        return 0
    elif variable1 == 1:
        print('admin')
        return 1

        
def log_page():
    log=access()      
    if log == 1:
        outbox=tkinter.Label(window,text="\n\nwelcome back admin!",font=("consolas", 20))
        outbox.place(x=20,y=100)
        outbox.pack()
    elif log == 0:
        outbox=tkinter.Label(window,text="\n\nwelcome back hearty user!",font=("consolas", 20))
        outbox.place(x=20,y=100)
        outbox.pack()
    elif log == 2:
        outbox=tkinter.Label(window,text="\nNot a valid user! try gain..",font=("consolas", 20))
        outbox.place(x=20,y=100)
        outbox.pack()
        
    
passw = tkinter.Label(window, text="password:", font=("consolas", 20))
password = StringVar() #Password variable
passEntry = Entry(window, textvariable=password, show='*')
submit = Button(window, text='Show Console',fg='green',bg='red',padx=10,pady=10,command=show)
btn = tkinter.Button(window, text="Login",fg='green',bg='red',padx=30,pady=30,command=log_page)

btn.place(x=100,y=100)

username.pack()
entry1.pack()
passw.pack()
passEntry.pack() 
submit.pack()  
btn.pack(side=tkinter.BOTTOM)

window.mainloop()

