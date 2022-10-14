import openpyxl
wb=openpyxl.load_workbook("C:\\Users\\Lopez\\OneDrive\\WIP\\Test Excel.xlsx")
sh1=wb['Sheet1']
rows=sh1.max_row
print(rows)
def which():
    global guide
    guide=input(str("Which action would you like to perform\n1. Input New Item to Inventory\n2. Add Cost\n3. Profit\n4.Payout Per Person\n5. Check Total Cost\n"))
def ensure():
 global yesorno
 yesorno=input(str("Are you sure.(Y/N)\n"))
 while yesorno!='y' and yesorno!='n':
  print("Incorrect Input")
  yesorno=input("Are you sure\n").lower

which()
ensure()
while yesorno=='n':
    which()
    ensure()

      
match guide:
 case "1": 
  newitem=input("Input New item\n")
  newcost=input("Input cost of Items\n")
  quantity=int(input('Input the quantity of Items\n'))
  #while sh1['D2'].value ==None: 
  for i in range (1,rows+2):
    if sh1.cell(i,1).value !=None and sh1.cell(i,1).value==newitem:
        yesorno=input("This item has already been inputted\n")

        upquan=int(sh1.cell(i,3).value)
        upquan+=quantity
        sh1.cell(i,3).value=upquan 
        break 
    elif sh1.cell(i,1).value ==None:
     print("This cell is empty",i)
     sh1.cell(i,1).value=newitem
     sh1.cell(i,2).value=newcost
     sh1.cell(i,3).value=quantity


wb.save("Test Excel.xlsx")



    


"""
 case '2':
  costname=input("Input Cost Name\n")
  cost= input("Input Cost\n")
 case '3':
  print("The total profit is")
 case '4':
  print("The Payout Per Person is")
 case '5':
  print("The total cost is ")
"""