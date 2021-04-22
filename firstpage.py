from tkinter import *
from tkmacosx import *

import os

home=Tk()

home.configure(background="#80D8FF")
home.iconbitmap('VIKAS.ico')
def function1():
    
    os.system("python DB.py")    
def function2():
    
    os.system("python VIKAS.py")

def function3():
    
    os.system("python admin.py")
text1 = """Welcome to VIKAS :)    **when moving to other windows, do not close this main window!Welcome to VIKAS :)    **when moving to other windows, do not close this main window!Welcome to VIKAS :)    **when moving to other windows, do not close this main window!Welcome to VIKAS :)    **when moving to other windows, do not close this main window!Welcome to VIKAS :)    **when moving to other windows, do not close this main window!Welcome to VIKAS :)    **when moving to other windows, do not close this main window!Welcome to VIKAS :)    **when moving to other windows, do not close this main window!Welcome to VIKAS :)    **when moving to other windows, do not close this main window!Welcome to VIKAS :)    **when moving to other windows, do not close this main window!Welcome to VIKAS :)    **when moving to other windows, do not close this main window!Welcome to VIKAS :)    **when moving to other windows, do not close this main window!Welcome to VIKAS :)    **when moving to other windows, do not close this main window!"""

home.title("----VIKAS----")
#Label(home,text='---HOME PAGE---',font='Helvetica 20 bold',bg='#49A').grid(row=1,column=3)
#Version 11.1.21.DRAVID

Marquee(home, bg='#fe15b4', fg='#101820', text='Latest Version 11.1.21.DRAVID.',font=('MS Sans Serif', 20, 'bold ')).grid(row=3,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(home,text='Student Information',font=("times new roman",20),command=function1,bg='yellow').grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(home,text="VIKAS",font=("times new roman",20),bg='orange',fg='white',command=function2).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
Button(home,text="Admin",font=("times new roman",20),bg='green',fg='white',command=function3).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Marquee(home, bg='#15fed7', fg='#101820', text=text1).grid(row=7,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#home.resizable(True, True)

home.mainloop()
