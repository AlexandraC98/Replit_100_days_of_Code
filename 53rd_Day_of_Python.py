import os, time

Game=[]

try:
  with open("Inventory.txt", "r") as f:
    Game = eval(f.read())
except Exception:
  pass

def prettyPrint():
  for index, item in enumerate(Game, start=1):
    print(f"\033[36m {index:>2}\033[0m  |  \033[36m{item} \033[0m")
  print()

def Add():
  add=input("What kind of a weapon do you wanna add? > ").capitalize().strip()
  Game.append(add)
  print(f"{add} added.")
  time.sleep(1)
  prettyPrint()

def Remove():
  prettyPrint()
  time.sleep(1)
  try:
    remove=int(input("Which weapon do you wanna remove? (index) > "))
    choice=input("Are you sure you want to remove this? (y/n) > ").strip().lower()
    if choice[0]=="y" and 0<remove<=len(Game):
      del Game[remove-1]
      print(f"{remove} removed")
      prettyPrint()
    else:
      print("There is no such weapon in your list.")
      time.sleep(1)
      prettyPrint()
  except (ValueError, IndexError):
    print("Ivalid index; please try again.")
    time.sleep(1)
    prettyPrint()

def View():
  prettyPrint()
  time.sleep(1)
  try:
    view=int(input("Which weapon do you want to view? (index) > "))
    if 0<view<=len(Game):
      item=Game[view-1]
      counter=Game.count(item)
      print(f"You have {counter} {item}.")
      time.sleep(1)
  except (ValueError, IndexError):
    print("Ivalid index; please try again.")
    time.sleep(1)
    prettyPrint()

def Autosave():
  with open("Inventory.txt", "w") as f:
    f.write(str(Game))

def Quit():
  choice=input("Do you wish to quit (y/n)? > ").strip().lower()
  if choice=="y":
    Autosave()
    exit()

while True:
  os.system("clear")
  menu=input("1. Add\n2. Remove\n3. View\n> ").strip().lower()
  if menu=="1" or menu[0]=="a":
    Add()
    time.sleep(1)
    os.system("clear")
    Quit()
  elif menu=="2" or menu[0]=="r":
    Remove()
    time.sleep(1)
    os.system("clear")
    Quit()
  elif menu=="3" or menu[0]=="v":
    View()
    time.sleep(1)
    os.system("clear")
    Quit()
