from tkinter import *
from PIL import Image,ImageTk


root=Tk()
root.geometry("200x200")
root.title("Learning radio Buttons")


def Clicked(value):
    label=Label(root,text=value)
    label.pack()




a=IntVar()
a.set(2)
Radiobutton(root,text="Option1",variable=a,value=1,command= lambda:Clicked(a.get())).pack()
Radiobutton(root,text="Option2",variable=a,value=2,command= lambda:Clicked(a.get())).pack()

label=Label(root,text=a.get())
label.pack()

root.mainloop()
