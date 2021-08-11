from logging import root
from subprocess import run
import time
import tkinter as tk
import tkinter as ttk
import threading
from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as st
from tkinter.constants import BOTH, BOTTOM
from PIL import ImageTk, Image
import os
import subprocess

splash =  tk.Tk()
splash.title('Wookie Force')
splash.geometry('800x500')

bg = PhotoImage(file="9thanniversary.png")

my_label = Label(splash,image=bg)
my_label.place(x=0,y=0,relheight=1,relwidth=1)


def menu():
    global callback_id
    splash.destroy()

    menu = tk.Tk()
    menu.title('Wookie Force')
    menu.geometry('1200x600')


    apps = []
    
    def addApp():
        filename = filedialog.askopenfilename(initialdir="/",title="Select file")
        apps.append(filename)
        for app in apps:
            label = tk.Label(frame,text=app,bg="#bbe8fd")
            label.pack()

    # Create a photoimage object of the image in the path
    image1 = Image.open("menu.png")
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    canvas = tk.Canvas(menu,width=1200,height=600)

    #Load the image
    menubg= ImageTk.PhotoImage(file="menu.png")
    #Create a canvas
    canvas= Canvas(menu,width= 400, height= 200)
    canvas.pack(expand=True, fill= BOTH)
    #Add the image in the canvas
    canvas.create_image(0,0,image=menubg, anchor="nw")

    #Position image
    label1.place(x=0, y=0,relheight=1,relwidth=1)

    canvas.pack()
    
    frame = Frame(menu,bg="white")
    frame.place(relwidth=0.6,relheight=0.6,relx=0.2,rely=0.2)

    files=[]

    def openProgram():
        filename = filedialog.askopenfilename(initialdir="/",title="Select file")
        result = subprocess.check_output(['python',filename])
        result = result.decode()
        print(result)
        label2 = tk.Label(frame,text=result,bg="#bbe8fd")
        label2.pack()

    openfile = tk.Button(canvas,text="Open file",padx=10,pady=5,command=addApp)
    openfile.pack(side=BOTTOM, padx=0, pady=10)

    runfile = tk.Button(canvas,text = "Run file",padx=10,pady=5,command=openProgram)
    runfile.pack(side=BOTTOM, padx=0, pady=10)
    
    callback_id = canvas.after(1000, menu)

button_img = PhotoImage(file="Start.png")

Start = tk.Button(splash,image =button_img,borderwidth=0,command = menu)
Start.pack(side=BOTTOM, padx=0, pady=230)

mainloop()
