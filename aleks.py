def ensure():
 global yesorno
 yesorno=input(str("Are you sure.(Y/N)\n"))
 while yesorno!='y' and yesorno!='n':
  print("Incorrect Input")
  yesorno=input("Are you sure\n")

def question():
    global smth
    smth=input("nazi or soldier\n")
    return smth
def question2():
    global suck
    suck=input("candy or ice cream\n")
    return suck

question()
ensure()
while yesorno=='n':
  question()
  ensure()
  print("the thing enter here")

question2()
ensure()
while yesorno=='n':
  question2()
  ensure()
  print("the thing enter here")
