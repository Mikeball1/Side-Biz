
from tkinter import *
# Define the functions that open new windows
tk = Tk()
tk.title("Inventory Management System")
newwind=Toplevel()
# def clicked():
#   displayed=Label(input_window)

def input_new_item():
    # input_window = Toplevel()
    # input_window.title("Input New Item")
    inputs=Label(newwind,text="Input the name of the new item")
    inputs.pack()
    Newitem=Entry(newwind,width=50)
    Newitem.pack()

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
# Create the main window

# Create the buttons
input_button = Button(tk, text="Input New Item", command=input_new_item)
payout_button = Button(tk, text="Payout", command=payout)
sale_button = Button(tk, text="Enter Sale", command=enter_sale)
item_sales_button = Button(tk, text="Item Sales Per Person", command=item_sales_per_person)
sales_button = Button(tk, text="Sales Per Person", command=sales_per_person)
end_button = Button(tk, text="End Program", command=end_program)
shipment_button = Button(tk, text="Add Shipment", command=add_shipment)
refund_button = Button(tk, text="Refund", command=refund)
fees_button = Button(tk, text="Other Fees", command=other_fees)
sales_button = Button(tk, text="Current Sales", command=current_sales)
profits_button = Button(tk, text="Current Profits", command=current_profits)

# Place the buttons on the window
input_button.pack()
payout_button.pack()
sale_button.pack()
item_sales_button.pack()
sales_button.pack()
end_button.pack()
shipment_button.pack()
refund_button.pack()
fees_button.pack()
sales_button.pack()
profits_button.pack()

# Run the main loop
tk.mainloop()
