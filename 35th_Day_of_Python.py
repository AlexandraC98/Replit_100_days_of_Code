import time, os

List=[]

def printList():
  os.system("clear")
  print("Your To Do List so far:\n")
  for i in range(len(List)):
    print(f"{i+1}: {List[i]}")
  time.sleep(1)

while True:
  os.system("clear")
  print("My To Do List\n")
  menu=input("What do you want to do?\n1. Add\n2. View\n3. Edit\n4. Remove\n5. Exit\n> ")
  if menu=="1":
    add=input("What do you want to add?\n> ")
    if add in List:
      print("Item already added in the list.")
      time.sleep(1)
    else:
      List.append(add)
    printList()
    time.sleep(1)
  elif menu=="2":
    printList()
    time.sleep(1)
  elif menu=="3":
    printList()
    edit=int(input("Which item do you want to edit?\n> "))
    if 1<=edit<=len(List):
      List[edit-1]=input("What do you want to change it to?\n> ")
      time.sleep(1)
      printList()
    else:
      print("Invalid input.")
      time.sleep(1)
  elif menu=="4":
    printList()
    if input("Are you sure you want to remove an item? yes/no\n> ")=="yes":
      item=int(input("Which item do you want to remove?\n> "))
      if 1<=item<=len(List):
        List.remove(List[item-1])
      else:
        print("Invalid input.")
        time.sleep(1)
  elif menu=="4":
    break
