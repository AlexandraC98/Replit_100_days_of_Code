MokeBeast={}

def prettyPrint():
  print()
  for key, value in MokeBeast.items():
    print(key, end="> ")
    for subKey, subValue in value.items():
      print(subKey, subValue, end=" | ")
    print()
    
def Quit():
  print("\033[0m")
  choice=input("Do you want to quit? (y/n) > ")
  if choice[0]=="y":
    exit()
    
while True:

  #User input
  name=input("Name your beast: > ")
  type=input("What type of a beast is this? > ")
  move=input("Name a special move for your beast: > ")
  hp=input("What is the starting HP of your beast? > ")
  mp=input("What is the starting MP of your beast? > ")

  #Add to dictionary
  MokeBeast[name]={
    "type":type,
    "move":move,
    "hp":hp,
    "mp":mp
  }

  print()

  prettyPrint()

  Quit()
