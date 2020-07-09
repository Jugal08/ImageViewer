from tkinter import *
from PIL import Image,ImageTk


root=Tk()
root.title("Krishna Narzary")
frame=LabelFrame(root,text="This is my frame",padx=50,pady=50)
frame.pack(padx=50,pady=50)

a=Button(frame,text="I Love you",padx=20,pady=20)
a.pack()
root.mainloop()