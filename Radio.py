from tkinter import *
from PIL import Image,ImageTk


root=Tk()
root.geometry("200x200")
root.title("Learning radio Buttons")

Fruits=StringVar()
Fruits.set("Apple")


MODES=[("Apple","Apple"),
       ("Banana","Banana"),
       ("Mango","Mango"),
       ("Watermelon","Watermelon"),
       ("Grapes","Grapes")  
  ]



for text,modes in MODES:
    Radiobutton(root,text=text,variable=Fruits,value=modes).pack(anchor=W)

def Clicked(value):
    label=Label(root,text=value)
    label.pack()



#a=IntVar()
#a.set(2)

#Radiobutton(root,text="Option1",variable=a,value=1,command= lambda:Clicked(a.get())).pack()


#Radiobutton(root,text="Option2",variable=a,value=2,command= lambda:Clicked(a.get())).pack()

button1=Button(root,text="Click me",command=lambda : Clicked(Fruits.get())).pack()



#label=Label(root,text=Fruits.get())
#label.pack()

root.mainloop()
