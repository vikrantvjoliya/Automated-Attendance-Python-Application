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
from tkmacosx import *


###########Window is our Main frame of system
window = tk.Tk()
window.title("VIKAS™ \U0001f600")

window.geometry('1368x1240')
window.configure(background='snow')


def clear():
    txt.delete(first=0, last=22)


def clear1():
    txt2.delete(first=0, last=22)


def del_sc1():
    sc1.destroy()


def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry('300x100')
    sc1.iconbitmap('VIKAS.ico')
    sc1.title('Warning!!')
    sc1.configure(background='snow')
    Label(sc1, text='Enrollment & Name required!!!', fg='red', bg='white', font=('MS Sans Serif', 16, ' bold ')).pack()
    Button(sc1, text='OK', command=del_sc1, fg="black", bg="light pink", width=9, height=1, activebackground="Red",
           font=('MS Sans Serif', 15, ' bold ')).place(x=90, y=50)


##Error screen2
def del_sc2():
    sc2.destroy()


def err_screen1():
    global sc2
    sc2 = tk.Tk()
    sc2.geometry('300x100')
    sc2.iconbitmap('VIKAS.ico')
    sc2.title('Warning!!')
    sc2.configure(background='snow')
    Label(sc2, text='Please enter your subject name!!!', fg='red', bg='white',
          font=('MS Sans Serif', 16, ' bold ')).pack()
    Button(sc2, text='OK', command=del_sc2, fg="black", bg="light pink", width=9, height=1, activebackground="Red",
           font=('MS Sans Serif', 15, ' bold ')).place(x=90, y=50)

#########For take images for datasets
def take_img():
    l1 = txt.get()
    l2 = txt2.get()
    if l1 == '':
        err_screen()
    elif l2 == '':
        err_screen()
    else:
        try:
            cam = cv2.VideoCapture(0)
            detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            Enrollment = txt.get()
            Name = txt2.get()
            sampleNum = 0
            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # incrementing sample number
                    sampleNum = sampleNum + 1
                    # saving the captured face in the dataset folder
                    cv2.imwrite("TrainingImage/ " + Name + "." + Enrollment + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])
                    cv2.imshow('Frame', img)
                # wait for 100 miliseconds
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum > 70:
                    break
            cam.release()
            cv2.destroyAllWindows()
            ts = time.time()
            Date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            Time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            row = [Enrollment, Name, Date, Time]
            with open('D:\\VIKAS\\StudentDetails\\StudentDetails.csv', 'a', newline='') as csvFile:
                writer = csv.writer(csvFile, delimiter=',')
                writer.writerow(row)
                csvFile.close()
            res = "Images Saved for Enrollment : " + Enrollment + " Name : " + Name
            Notification.configure(text=res, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
            Notification.place(x=250, y=400)
        except FileExistsError as F:
            f = 'Student Data already exists'
            Notification.configure(text=f, bg="Red", width=21)
            Notification.place(x=450, y=400)


#########for choose subject and fill attendance
def subjectchoose():
    def Fillattendances():
        sub=tx.get()
        now = time.time()  
        future = now + 20
        if time.time() < future:
            if sub == '':
                err_screen1()
            else:
                recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
                try:
                    recognizer.read("TrainingImageLabel\Trainner.yml")
                except:
                    e = 'Model not found,Please train model'
                    Notifica.configure(text=e, bg="red", fg="black", width=33, font=('times', 15, 'bold'))
                    Notifica.place(x=20, y=250)

                harcascadePath = "haarcascade_frontalface_default.xml"
                faceCascade = cv2.CascadeClassifier(harcascadePath)
                df = pd.read_csv("StudentDetails\StudentDetails.csv")
                cam = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                col_names = ['Enrollment', 'Name', 'Date', 'Time']
                attendance = pd.DataFrame(columns=col_names)
                while True:
                    ret, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        global Id

                        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                        if (conf <70):
                            print(conf)
                            global Subject
                            global aa
                            global date
                            global timeStamp
                            Subject = tx.get()
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                            aa = df.loc[df['Enrollment'] == Id]['Name'].values
                            global tt
                            tt = str(Id) + "-" + aa
                            En = '15624031' + str(Id)
                            attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                            cv2.putText(im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4)

                        else:
                            Id = 'Unknown'
                            tt = str(Id)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                            cv2.putText(im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4)
                    if time.time() > future:
                        break

                    attendance = attendance.drop_duplicates(['Enrollment'], keep='first')
                    cv2.imshow('Filling attedance..', im)
                    key = cv2.waitKey(30) & 0xff
                    if key == 27:
                        break

                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                Hour, Minute, Second = timeStamp.split(":")
                fileName = "Attendance/" + Subject + "_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
                attendance = attendance.drop_duplicates(['Enrollment'], keep='first')
                print(attendance)
                attendance.to_csv(fileName, index=False)


                M = 'Attendance filled Successfully'
                Notifica.configure(text=M, bg="Green", fg="white", width=33, font=('times', 15, 'bold'))
                Notifica.place(x=20, y=250)

                cam.release()
                cv2.destroyAllWindows()

                import csv
                import tkinter
                root = tkinter.Tk()
                root.title("Attendance of " + Subject)
                root.configure(background='snow')
                cs = 'D:/VIKAS/' + fileName
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
                print(attendance)

    #########windo is frame for subject chooser
    windo = tk.Tk()
    windo.iconbitmap('VIKAS.ico')
    windo.title("Enter subject name...")
    windo.geometry('680x400')
    windo.configure(background='snow')
    Notifica = tk.Label(windo, text="Attendance filled Successfully", bg="Green", fg="white", width=33,
                        height=2, font=('MS Sans Serif', 15, 'bold'))

    def Attf():
        import subprocess
        subprocess.Popen('explorer "D:\\VIKAS\\Attendance"')

    attf = tk.Button(windo, text="Check Sheets", command=Attf, fg="black", bg="light pink", width=12, height=1,
                     activebackground="Red", font=('MS Sans Serif', 14, ' bold '))
    attf.place(x=430, y=255)

    sub = tk.Label(windo, text="Enter Subject", width=15, height=2, fg="white", bg="blue2",
                   font=('MS Sans Serif', 15, ' bold '))
    sub.place(x=30, y=100)

    tx = tk.Entry(windo, width=20, bg="yellow", fg="red", font=('MS Sans Serif', 23, ' bold '))
    tx.place(x=250, y=105)

    fill_a = tk.Button(windo, text="Fill Attendance", fg="white", command=Fillattendances, bg="orange", width=20,
                       height=2,
                       activebackground="Red", font=('MS Sans Serif', 15, ' bold '))
    fill_a.place(x=250, y=160)
    windo.mainloop()



#########For train the model
def trainimg():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Dataset Trained Successfully"
    res = "Model Trained"  # +",".join(str(f) for f in Id)
    Notification.configure(text=res, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
    Notification.place(x=250, y=400)

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.iconbitmap('VIKAS.ico')

def on_closing():
    #from tkinter import messagebox
    #if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)

#message = tk.Label(window, text="Welcome to VIKAS :) ", bg="light pink", fg="black", width=50, height=3,font=('MS Sans Serif', 30, 'italic bold '))

#message.place(x=80, y=20)

text1="Welcome to VIKAS :)    **when moving to other windows, do not close this main window!" 
Marquee(window, bg='#15fe76', fg='#101820', text=text1,font=('MS Sans Serif', 35, 'italic bold '),width=1000).place(x=180,y=20)

text2="""Follow The Instructions Carefully 1.Enroll Your DETAILS BELOW ROLLNO and NAME.  2.Next, Capture your Dataset with A Smile 😎  3.Now, Train your Dataset  4.Press AUTOMATIC ATTEND.....  5.In NEXT GUI Enroll your Subject. AND Capture a Smile 🤐 """
Marquee(window, bg='#aa00ff', fg='#101820', text=text2,font=('MS Sans Serif', 35, 'bold '),width=1000).place(x=180,y=90)

Notification = tk.Label(window, text="All things good", bg="Green", fg="white", width=15, height=3,
                        font=('MS Sans Serif', 17, 'bold'))

lbl = tk.Label(window, text="Enter Enrollment", width=20, height=2, fg="black", bg="cyan",
               font=('MS Sans Serif', 15, ' bold '))
lbl.place(x=200, y=200)


def testVal(inStr, acttyp):
    if acttyp == '1':  # insert
        if not inStr.isdigit():
            return False
    return True


txt = tk.Entry(window, validate="key", width=20, bg="yellow", fg="red", font=('MS Sans Serif', 25, ' bold '))
txt['validatecommand'] = (txt.register(testVal), '%P', '%d')
txt.place(x=550, y=210)

lbl2 = tk.Label(window, text="Enter Name", width=20, fg="black", bg="cyan", height=2,
                font=('MS Sans Serif', 15, ' bold '))
lbl2.place(x=200, y=300)

txt2 = tk.Entry(window, width=20, bg="yellow", fg="red", font=('MS Sans Serif', 25, ' bold '))
txt2.place(x=550, y=310)

clearButton = tk.Button(window, text="Clear", command=clear, fg="black", bg="orange", width=10, height=1,
                        activebackground="Red", font=('MS Sans Serif', 15, ' bold '))
clearButton.place(x=950, y=210)

clearButton1 = tk.Button(window, text="Clear", command=clear1, fg="black", bg="orange", width=10, height=1,
                         activebackground="Red", font=('MS Sans Serif', 15, ' bold '))
clearButton1.place(x=950, y=310)



takeImg = tk.Button(window, text="Take Images", command=take_img, fg="white", bg="blue2", width=20, height=3,
                    activebackground="Red", font=('MS Sans Serif', 15, ' bold '))
takeImg.place(x=90, y=500)

trainImg = tk.Button(window, text="Train Images", fg="white", command=trainimg, bg="deep pink", width=20, height=3,
                     activebackground="Red", font=('MS Sans Serif', 15, ' bold '))
trainImg.place(x=390, y=500)

FA = tk.Button(window, text="Automatic Attendance", fg="white", command=subjectchoose, bg="red", width=20, height=3,
               activebackground="Red", font=('MS Sans Serif', 15, ' bold '))
FA.place(x=690, y=500)


def DevelopersHTML():
    os.startfile(os.getcwd() + "/developers/MAIN.html");


DP = tk.Button(window, text="Developers", command=DevelopersHTML, fg="black", bg="gold", width=20, height=3,
               activebackground="Red", font=('MS Sans Serif', 15, ' bold '))
DP.place(x=990, y=500)

window.mainloop()