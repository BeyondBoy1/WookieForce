import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import threading
from PIL import ImageTk, Image, PyAccess
from tkinter import filedialog
import os

splash =  tk.Tk()
splash.title('Coc Analyzer')
splash.geometry('800x500')

bg = PhotoImage(file="D:\GUI Python\9thanniversary.png")

my_label = Label(splash,image=bg)
my_label.place(x=0,y=0,relheight=1,relwidth=1)

def load():
    #my_progress.start(10)
    for x in range (7):
        my_progress['value'] += 15
        splash.update_idletasks()
        time.sleep(1)

s = ttk.Style()
s.theme_use('clam')
s.configure("pink.Horizontal.TProgressbar", troughcolor ='white', background='#ff00fe')
my_progress= ttk.Progressbar(splash, style="pink.Horizontal.TProgressbar", orient="horizontal", length=200, mode="determinate")

my_progress.pack(pady=210) 
threading.Thread(target=load).start()

   

def menu():
    splash.destroy()
    global filebutton
    menu = Tk()
    menu.title('Wookie Force')
    menu.geometry('800x600')

    menu.filename = filedialog.askopenfilename(initialdir="D:\WookieForce",title="Select a file")
    
    
#Splash Timer
splash.after(3000,menu)

mainloop()
