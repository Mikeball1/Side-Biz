def ensure():
 global yesorno
 yesorno=input(str("Are you sure.(Y/N)\n"))
 while yesorno!='y' and yesorno!='n':
  print("Incorrect Input")
  yesorno=input("Are you sure\n")

def question():
    global smth
    smth=input("are you a fed (y/n)\n")
    return smth
def question2():
    global suck
    suck=input("zaza or lean (y/n)\n")
    return suck

def sure(function):
 function()
 ensure()   
 while yesorno=='n':
  function()
  ensure()
  print("the thing enter here")
sure(question)
sure(question2)

