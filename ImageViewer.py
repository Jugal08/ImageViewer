from tkinter import*
from PIL import Image,ImageTk


root=Tk()
root.title('Image Viewer By Jugal')




#The images
my_image1=ImageTk.PhotoImage(Image.open('/home/jugal/PythonPrograms/Photos/RickSanchez1.jpg'))
my_image2=ImageTk.PhotoImage(Image.open('/home/jugal/PythonPrograms/Photos/RickSanchez2.jpg'))
my_image3=ImageTk.PhotoImage(Image.open('/home/jugal/PythonPrograms/Photos/RickSanchez3.jpg'))




#List of the images used 
image_list=[my_image1,my_image2,my_image3]
my_label=Label(image=my_image1)
my_label.grid(row=0,column=0,columnspan=3)


#Defining the functions of the button

def Next(image_number):
    global my_label
    global Next_button
    global Previous_button
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    my_label.grid(row=0,column=0,columnspan=3)
    
    
    #Updating the buttons 

    Next_button=Button(root,text='>>',command=lambda : Next(image_number+1))
    Previous_button=Button(root,text='<<',command=lambda : Previous(image_number-1))
    if image_number==3:
        Next_button=Button(root,text='>>',state=DISABLED)



    Next_button.grid(row=1,column=2)
    Previous_button.grid(row=1,column=0)
    Exit_button.grid(row=1,column=1)


def Previous(image_number):
    global my_label
    global Next_button
    global Previous_button
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    my_label.grid(row=0,column=0,columnspan=3)

    Next_button=Button(root,text='>>',command=lambda : Next(image_number+1))
    Previous_button=Button(root,text='<<',command=lambda : Previous(image_number-1))



    if image_number==1:
        Previous_button=Button(root,text='<<',state=DISABLED)
    


    Next_button.grid(row=1,column=2)
    Previous_button.grid(row=1,column=0)
    Exit_button.grid(row=1,column=1)
    

    





#Defining the Buttons 

Next_button=Button(root,text='>>',command=lambda : Next(2))
Exit_button=Button(root,text='Exit',command=root.quit)
Previous_button=Button(root,text='<<',command=Previous,state=DISABLED)


#Displaying the buttons of the image viewer  


Next_button.grid(row=1,column=2)
Previous_button.grid(row=1,column=0)
Exit_button.grid(row=1,column=1)


#Status 

Status=Label(root,text="Image 1 of "+ str(len(image_list)),bd=1,relief=SUNKEN)



Status.grid(row=2,column=2,columnspan=3)



root.mainloop()
