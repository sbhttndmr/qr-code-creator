import pyqrcode
import png
from pyqrcode import QRCode
from tkinter import *
import tkinter 
from tkinter.ttk import *
from tkinter import ttk
from tkinter.filedialog import askopenfile 
from tkinter import filedialog
import os
from PIL import Image

root = Tk() 
root.geometry('300x200')
root.title("QR Code Creator")
root.resizable(0,0)

label1=tkinter.Label(root, text="Link: ")
label1.pack()
entry1=tkinter.Entry(root, width= 40)
entry1.pack()
label2=tkinter.Label(root, text="Save Name: ")
label2.pack()
entry2=tkinter.Entry(root, width= 20)
entry2.pack()

def save_file():
    file_path = filedialog.askdirectory()
    #print(file_path)
    s = entry1.get()
    a = entry2.get()
    url = pyqrcode.create(s)

    url.png( file_path + "/" + a + ".png", scale = 3)
    url.show()

ttk.Button(root, text= "Create",width= 20, command= save_file).pack(pady=10)
ttk.Button(root, text= "Quit", width= 20,command= root.quit).pack(pady=10)

mainloop() 