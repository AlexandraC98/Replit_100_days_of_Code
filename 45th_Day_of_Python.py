import os, time

toDoList = []
row = []

def prettyPrint():
  print()
  for index, row in enumerate(toDoList, start=1):
    print(f"\033[36m {index:>2} \033[0m", end=" | ")
    for item in row:
      print(f"\033[36m {item:^10} \033[0m", end=" | ")
    print()
  print()

def Add():
  time.sleep(1)
  os.system("clear")
  name = input("What is the task? > ").strip().capitalize()
  date = input("When is it due by? > ").strip().capitalize()
  priority = input("What is the priority? (High/Medium/Low) > ").strip().capitalize()
  if name in [items[0] for items in toDoList]:
    print ("Task already added.")
    time.sleep(1)
    prettyPrint()
  else:
    row = [name, date, priority]
    toDoList.append(row)
    print("Added.")
    time.sleep(1)
    prettyPrint()

def View():
  time.sleep(1)
  os.system("clear")
  prettyPrint()

def Remove():
  time.sleep(1)
  os.system("clear")
  verify=input("Are you sure you wish to remove something? (y/n) > ")
  if verify[0]=="y":
    prettyPrint()
    remove=int(input("Which task do you wish to remove? > "))
    if 0<remove<=len(toDoList):
      del toDoList[remove-1]
      print("Removed.")
      time.sleep(1)
      prettyPrint()
    else:
      print("Task already removed.\n")
      time.sleep(1)
  else:
    prettyPrint()

def Edit():
  time.sleep(1)
  os.system("clear")
  prettyPrint()
  edit=int(input("Which item do you wish to edit? > "))
  if 0<edit<=len(toDoList):
    toDoList.pop(edit-1)
    Add()
  else:
    print("There is no such task in your to do list.")
    time.sleep(1)
    prettyPrint()

def Sort():
  def_priority = {"High":1, "Medium":2, "Low":3}
  toDoList.sort(key=lambda x: def_priority.get(x[2], 4))
  time.sleep(1)
  prettyPrint()
      
def Quit():
  quit=input("Do you want to see the menu again? > ").strip().lower()
  if quit[0] == "n":
    exit()
  
while True:
  menu=input("Do you want to:\n1. Add\n2. View\n3. Remove\n4. Edit\n5. Sort\n> ").strip().lower()
  if menu=="1" or menu[0]=="a":
    Add()
    Quit()
  elif menu=="2" or menu[0]=="v":
    View()
    Quit()
  elif menu=="3" or menu[0]=="r":
    Remove()
    Quit()
  elif menu=="4" or menu[0]=="e":
    Edit()
    Quit()
  elif menu=="5" or menu[0]=="s":
    Sort()
    Quit()
