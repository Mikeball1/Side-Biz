from tkinter import *
class NewItem():
 def __init__(self,Name,Cost,Quantity):
    self.Name=Name
    self.Cost=Cost
    self.Quantity=Quantity

def input_new_item():
    input_window = Toplevel()
    input_window.title("Input New Item")
    inputs=Label(input_window,text="Input the name of the new item")
    inputs.pack()
    NewitemName=Entry(input_window,width=50)
    NewitemName.pack()
    NewitemAmount=Entry(input_window,width=50)
    NewitemAmount.pack()
    NewitemCost=Entry(input_window,width=50)
    NewitemCost.pack()
    def show_input():
     global Item
     Item=NewItem(NewitemName.get(),NewitemCost.get(),NewitemAmount.get())
     itemDes=Label(input_window,text="The name of your inputted item is "+Item.Name+"\nThe cost of your inputted item is "+Item.Cost+"\nThe quantity of the item is "+Item.Quantity)
     itemDes.pack()
    Characteristics=Button(input_window,text="Press to lock in values",command=show_input)
    Characteristics.pack()

def payout():
    payout_window = Toplevel()
    payout_window.title("Payout")
    # Add space for the coder to input their code here
    pass
def enter_sale():
    payout_window = Toplevel()
    payout_window.title("enter_sale")
    # Add space for the coder to input their code here
    pass
def item_sales_per_person():
    payout_window = Toplevel()
    payout_window.title("item_sales_per_person")
    # Add space for the coder to input their code here
    pass
def sales_per_person():
    payout_window = Toplevel()
    payout_window.title("sales_per_person")
    # Add space for the coder to input their code here
    pass
def end_program():
    payout_window = Toplevel()
    payout_window.title("end_program")
    # Add space for the coder to input their code here
    pass
def add_shipment():
    payout_window = Toplevel()
    payout_window.title("add_shipment")
    # Add space for the coder to input their code here
    pass
def refund():
    payout_window = Toplevel()
    payout_window.title("refund")
    # Add space for the coder to input their code here
    pass
def other_fees():
    payout_window = Toplevel()
    payout_window.title("other_fees")
    # Add space for the coder to input their code here
    pass
def current_sales():
    payout_window = Toplevel()
    payout_window.title("current_sales")
    # Add space for the coder to input their code here
    pass
def current_profits():
    payout_window = Toplevel()
    payout_window.title("current_profits")
    # Add space for the coder to input their code here
    pass
#sure function is used for running other functions with the yes or no prompt

# def ensure():
#  global yesorno
#  yesorno=input(str("Are you sure.(Y/N)\n"))
#  while yesorno!='y' and yesorno!='n':
#   print("Incorrect Input")
#   yesorno=input("Are you sure\n")
# #sure function is used for running input with the yes or no prompt
# def sure(function):
#  function()
#  ensure()   
#  while yesorno=='n':
#   function()
#   ensure()
def case1():
    pass