import tkinter as tk
from tkinter import *
import cv2
import csv
import os
import numpy as np
from PIL import *
import pandas as pd
import datetime
import time
from threading import Thread
from PIL import Image, ImageTk




win = tk.Tk()
win.iconbitmap('VIKAS.ico')
win.title("Admin VIKAS PORTAL")
win.geometry('880x420')
win.configure(background='snow')

def log_in():
    username = un_entr.get()
    password = pw_entr.get()

    if username == 'VIKAS':
        if password == 'VIKAS':
            win.destroy()
            import csv
            import tkinter
            root = tkinter.Tk()
            root.title("Student Details")
            root.configure(background='snow')

            cs = 'D:/VIKAS/StudentDetails/StudentDetails.csv'
            with open(cs, newline="") as file:
                reader = csv.reader(file)
                r = 0

                for col in reader:
                    c = 0
                    for row in col:
                        label = tkinter.Label(root, width=8, height=1, fg="black",
                                                  font=('MS Sans Serif', 15, ' bold '),
                                                  bg="light pink", text=row, relief=tkinter.RIDGE)
                        label.grid(row=r, column=c)
                        c += 1
                    r += 1
            root.mainloop()
        else:
            valid = 'Incorrect ID or Password'
            Nt.configure(text=valid, bg="red", fg="black", width=38, font=('MS Sans Serif', 19, 'bold'))
            Nt.place(x=120, y=350)

    else:
        valid = 'Incorrect ID or Password'
        Nt.configure(text=valid, bg="red", fg="black", width=38, font=('MS Sans Serif', 19, 'bold'))
        Nt.place(x=120, y=350)

Nt = tk.Label(win, text="Attendance filled Successfully", bg="Green", fg="white", width=40, height=2,
                  font=('MS Sans Serif', 19, 'bold'))
    # Nt.place(x=120, y=350)

un = tk.Label(win, text="Enter username", width=15, height=2, fg="white", bg="blue2",
                  font=('MS Sans Serif', 15, ' bold '))
un.place(x=30, y=50)

pw = tk.Label(win, text="Enter password", width=15, height=2, fg="white", bg="blue2",
                  font=('MS Sans Serif', 15, ' bold '))
pw.place(x=30, y=150)

def c00():
    un_entr.delete(first=0, last=22)

un_entr = tk.Entry(win, width=20, bg="yellow", fg="red", font=('MS Sans Serif', 23, ' bold '))
un_entr.place(x=290, y=55)

def c11():
    pw_entr.delete(first=0, last=22)

pw_entr = tk.Entry(win, width=20, show="*", bg="yellow", fg="red", font=('MS Sans Serif', 23, ' bold '))
pw_entr.place(x=290, y=155)

c0 = tk.Button(win, text="Clear", command=c00, fg="black", bg="orange", width=10, height=1, activebackground="Red",
                   font=('MS Sans Serif', 15, ' bold '))
c0.place(x=690, y=55)

c1 = tk.Button(win, text="Clear", command=c11, fg="black", bg="orange", width=10, height=1, activebackground="Red",
                   font=('MS Sans Serif', 15, ' bold '))
c1.place(x=690, y=155)

Login = tk.Button(win, text="LogIn", fg="black", bg="lime green", width=20, height=2, activebackground="Red",
                      command=log_in, font=('MS Sans Serif', 15, ' bold '))
Login.place(x=290, y=250)
win.mainloop()

