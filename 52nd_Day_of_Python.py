Pizza=[]

try:
  with open("Pizzalist.txt", "r") as f:
    Pizza = eval(f.read())
except Exception:
  pass

def AutoSave():
  with open("Pizzalist.txt", "w") as f:
    f.write(str(Pizza))

def PrettyPrint():
  print()
  for index, row in enumerate(Pizza, start=1):
    print(f"\033[36m {index:>2} \033[0m", end=" | ")
    for item in row:
      print(f"\033[36m {item:^10} \033[0m", end=" | ")
    print()
  print()

def Add():
  name=input("Your name > ").capitalize()
  try:
    quantity=int(input("How many pizzas? > "))
  except ValueError:
    print("Please enter a number")
    quantity=int(input("How many pizzas? > "))
  size=input("What size? (S/M/L) > ")
  
  if size.strip().lower()=="s":
    cost=5
    price=quantity*cost
    Pizza.append([name, quantity, price])
  elif size.strip().lower()=="m":
    cost=10
    price=quantity*cost
    Pizza.append([name, quantity, price])
  elif size.strip().lower()=="l":
    cost=15
    price=quantity*cost
    Pizza.append([name, quantity, price])
  
def Quit():
  done=input("Do you wish to purchase anything else? (Y/N) > ").strip().lower()
  if done[0]=="n":
    AutoSave()
    exit()

while True:
  Add()
  PrettyPrint()
  Quit()
