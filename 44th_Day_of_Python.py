import random, os, time

#Subroutine to get random numbers
def ran(used_no):
  while True:
    no=random.randint(0,91)
    if no not in used_no:
      used_no.add(no)
      return no

used_no=set()

no=[]

#Putting random number in a list (row) and sorting the rows
for i in range(9):
  no.append(ran(used_no))
no.sort()

#2D list
bingo=[[no[0],no[1],no[2]],
  [no[3],"BINGO",no[4]],
  [no[5],no[6],no[7]]]

#Creating the bingo card
def createCard():
  print("Bingo Card Generator")
  print()
  print(f"{bingo[0][0]:^5} | {bingo[0][1]:^5} | {bingo[0][2]:^5}")
  print("--------------------")
  print(f"{bingo[1][0]:^5} | BINGO | {bingo[1][2]:^5}")
  print("--------------------")
  print(f"{bingo[2][0]:^5} | {bingo[2][1]:^5} | {bingo[2][2]:^5}")
  print()

tries=0

#Main loop
while True:
  os.system("clear")
  createCard()
  print()
  
  #User input
  nextNumber=int(input("Next number > "))
  time.sleep(1)

  found=False
    
  for row in bingo:
    for item in range(len(row)):
      if row[item]==nextNumber:
        row[item]="X"
        found=True
        
  if found:
    x=sum(row.count("X") for row in bingo)
    tries=0
    if x==8:
      os.system("clear")
      createCard()
      print("You have won!")
      time.sleep(1)
      break
  else:
    tries+=1
    if tries>3:
      os.system("clear")
      print("You've lost!")
      time.sleep(1)
      break
    else:
      print("Wrong number.")
      time.sleep(1)
