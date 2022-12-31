from tkinter import *
root=Tk()
def newwind():
    top=Toplevel()
    wind=Label(top,text="You have opened a new window")
    wind.grid(row=0,column=0)
    match int(x):
     case 2 :
        window=Label(top,text="You have picked Input New Item To Inventory")
        window.grid(row=1,column=1)
     case "2":
      pass

def pushed():
    push=Label(root, text="You pushed")
    push.grid(row=15,column=15)
    newwind()
def push(inputs,x):
    chose=Button(root,text=inputs,command=pushed)
    chose.grid(row=x,column=0)
choices=[0,"1. Input New Item to Inventory","2. Payout","3. Enter Sale","4. Item sales Per Person",
"5. Sales Per Person","6. End Program","7. Add Shipment","8. Refund","9. Other Fees","10. Current Sales","11. Current Profits"]


myLabel= Label(root,text="Main Menu")
myLabel.grid(row=0,column=0) 
if type(root.winfo_exists())!=True:
 for option in choices: 
#     break 
  if option==0:
    pass
  else:
    x=choices.index(option)
    push(option,x)



root.mainloop()