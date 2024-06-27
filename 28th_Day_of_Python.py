import os, time, pyfiglet
  
#subroutine to define a dice with a random no. of sides
def rollDice(sides):
  import random
  return random.randint(1,sides)

#subroutine to define a health stat based on Replit's formula
def health():
  health=(rollDice(6)*rollDice(12)*0.5)+10
  return health

#subroutine to define a strength stat based on Replit's formula
def strength():
  strength=(rollDice(6)*rollDice(12)*0.5)+12
  return strength

#definition of character
def character():
  name=input("Epic Character Name: ")
  type=input("Epic Character Type: ")
  character= {
    "name":name,
    "type":type,
    "health":health(),
    "strength":strength()
  }
  return character

#presenting the data in a menu
while True:
  os.system("clear")
  title=pyfiglet.figlet_format("Character Builder", font="slant")
  print(title)
  print("\033[33m")
  
  #first character
  character1=character()
  print()
  print(f"{character1['name']}")
  print(f"HEALTH: {character1['health']}")
  print(f"STRENGTH: {character1['strength']}","\n")
  time.sleep(1)
  
  print("\n","\033[0m", "Who are they battling?")
  time.sleep(1)
  print("\033[36m")
  
  #second character
  character2=character()
  print()
  print(f"{character2['name']}")
  print(f"HEALTH: {character2['health']}")
  print(f"STRENGTH: {character2['strength']}","\n")
  time.sleep(1)
  os.system("clear")
  print("\033[0m")
  
  #Begin of battle
  subtitle=pyfiglet.figlet_format("⚔️ BATTLE TIME ⚔️")
  print(subtitle)
  time.sleep(1)

  round=1
  while True:
    if round>5:
      print("\033[0m","The battle is over!","\n")
      if character1['health']>character2['health']:
        print(f"{character1['name']} wins the battle!","\n")
      else:
        print(f"The winner is {character2['name']}!","\n")
      break
    print(f"Round {round}! Now roll the dice!","\033[0m","\n")
    time.sleep(2)
    roll1=rollDice(6)
    roll2=rollDice(6)
    #subroutine to calculate the damage
    def damage():
      damage=abs(character1['strength']-character2['strength']+1)
      return damage
    #start of rounds
    if roll1==roll2:
      round+=1
      print ("\033[32m","Score tied, roll again!","\033[0m","\n")
      continue
    elif roll1>roll2:
      round+=1
      print("\033[31m",f"{character1['name']} wins the round","\033[0m")
      print("\033[34m",f"{character2['name']} takes a hit, with", roll1, "damage", "\033[0m","\n")
      character2["health"]=character2["health"]-damage()
      if character2["health"]<=0:
        print("\033[30m",f"Oh no,", character2["name"], "has died!","\033[0m")
        print("\033[31m",f"The winner is {character1['name']}!","\n")
        time.sleep(1)
        break
      else:
        continue
    elif roll2>roll1:
      round+=1
      print("\033[31m",f"{character2['name']} wins the round","\033[0m")
      print("\033[34m",f"{character1['name']} takes a hit, with", roll2, "damage","\033[0m", "\n")
      character1["health"]=character1["health"]-damage()
      if character1["health"]<=0:
        print("\033[30m",f"Oh no,", character1["name"], "has died!","\033[0m")
        print("\033[31m",f"The winner is {character2['name']}!","\n")
        time.sleep(1)
        break
      else:
        continue
    else:
      print("\033[36m","Something went wrong","\033[0m","\n")
      break
  print("\n","\033[0m","The battle has ended!")
  time.sleep(1)
  if input("Do you wish to create other characters? ") != "yes":
    break
  else:
    time.sleep(1)
    continue
