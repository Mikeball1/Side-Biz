from tkinter import *
root=Tk()
#function that allows text to be displayed after button is pressed
def ifclick():
    myLabels=Label(root,text="Button is clicked")
    myLabels.grid(row=1,column=1)
#Places text within a tab 
myLabel= Label(root,text="Hello World!")
myLabel2= Label(root,text="Wagwan")
#Determines where the text will be placed within the tab. Text position is relative to other text
myLabel.grid(row=0,column=0)
myLabel2.grid(row=0,column=2)
#Creates button, padx and pady determines the size of the button
#command allows text to be displayed after button is pressed. command means: once pressed do this
butt=Button(root, text="click Me!",padx=30,pady=90,command=ifclick)
butt.grid(row=1,column=12)


root.mainloop()