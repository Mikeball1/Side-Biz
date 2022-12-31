from tkinter import *
root=Tk()
#Creates entry box
#Width changes box width
enter=Entry(root,width=10) 
enter.grid(row=2,column=5)
#Put text in the box
enter.insert(0,"Enter your name")
#function that allows text to be displayed after button is pressed
#enter.get
def ifclick():
    myLabels=Label(root,text="Hello " +enter.get())
    myLabels.grid(row=1,column=1)

#Creates button, padx and pady determines the size of the button, command allows text to be displayed after button is pressed
butt=Button(root, text="Enter Name",padx=30,pady=90,command=ifclick)
butt.grid(row=1,column=12)
#Determines where the text will be placed within the tab. Text position is relative to other text
#Places text within a tab 
myLabel= Label(root,text="Hello World!")
myLabel2= Label(root,text="Wagwan")
myLabel.grid(row=0,column=0)
myLabel2.grid(row=0,column=2)
#Creates a New window
top=Toplevel()
lbl=Label(top,text="New Window").pack()
root.mainloop()