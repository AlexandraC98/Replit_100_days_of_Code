import os, pyfiglet, pwinput

Dictionary={}

#Printing options
def prettyPrinting():
  for index, (key, value) in enumerate(Dictionary.items()):
    print(f"{index+1}: {key} \n")
  print()

#Create characters
def createCharacter():
  name=input("Name your character > ").capitalize().strip()
  intelligence=pwinput.pwinput(f"What is {name}'s intelligence? (1-99) > ")
  baldness=pwinput.pwinput(f"What is {name}'s baldness level? (1-99) > ")
  handsomeness=pwinput.pwinput(f"What is {name}'s handsomeness level? (1-99) > ")

  #Define dictionary
  Dictionary[name]={
    "intelligence":intelligence,
    "baldness":baldness,
    "handsomeness":handsomeness
  }
  
#Comparing stats
def compareStats(card1_index, card2_index, stat):
  os.system("clear")
  
  prettyPrinting()

  card1_name=list(Dictionary.keys())[card1_index]
  card2_name=list(Dictionary.keys())[card2_index]

  if stat in Dictionary[card1_name] and stat in Dictionary[card2_name]:
    card1_stat=int(Dictionary[card1_name][stat])
    card2_stat=int(Dictionary[card2_name][stat])

    if card1_stat>card2_stat:
      print(f"Character {card1_name} has a {stat} stat of {card1_stat} and wins!")
    elif card2_stat>card1_stat:
      print(f"Character {card2_name} has a {stat} stat of {card2_stat} and wins")
    else:
      print(f"Both characters have the same {stat}")
      
  else:
    print("One of both characters do not exist.")

#Quitting the game option
def Quit():
  choice=input("Do you want to quit? (y/n) > ")
  if choice.startswith("y"):
    print("Thanks for playing.")
    exit()
  else:
    os.system("clear")
#Main loop
while True:
  title=pyfiglet.figlet_format("Best Book Character")
  print(title)
  print()

  createCharacter()

  while True:
    add=input("Do you want to add another character? (y/n) > ")
    if add[0].lower()=="y":
      os.system("clear")
      createCharacter()
    else:
      os.system("clear")
      break
  
  os.system("clear")
  print("🌟Top Trumps🌟")
  print()
  prettyPrinting()

  #User input
  card1=int(input("Choose the index of your first character > ")) - 1
  card2=int(input("Choose the index of your second character > ")) - 1
  stat=input(f"Choose your stat (intelligence, baldness, handsomeness) > ").strip().lower()

  compareStats(card1, card2, stat)
  
  Quit()
