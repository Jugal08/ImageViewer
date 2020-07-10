from tkinter import *
from PIL import Image,ImageTk


root=Tk()
root.title("Creating a frame")
frame=LabelFrame(root,padx=50,pady=50)
frame.pack(padx=50,pady=50)

a=Button(frame,text="This is the first frame",padx=20,pady=20)
b=Button(frame,text="This is the first frame",padx=20,pady=20)
b.grid(row=0,column=0)
a.grid(row=1,column=0)
root.mainloop()