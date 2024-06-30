import os, time
import pyfiglet

ToDoList=[]

def printList():
  print()
  for item in ToDoList:
    print(item)
  print()

while True:
  os.system("clear")
  title=pyfiglet.figlet_format("To Do List Manager")
  print(title)
  print()
  menu=input("Do you want to view, add, edit or remove an item on your list? " )
  if menu=="add":
    item=input("What to you want to add? ")
    ToDoList.append(item)
  elif menu=="remove":
    item=("What do you want to remove? ")
    ToDoList.remove(item)
  elif menu=="edit":
    item=input("What do you want to edit? ")
    new=input("What do you want to change it to? ")
    for i in range(0,len(ToDoList)):
      if ToDoList[i]==item:
        ToDoList[i]=new
  elif menu=="view":
    time.sleep(1)
  printList()
  time.sleep(1)
  if input("Do you want to finish? ")=="yes":
    break
