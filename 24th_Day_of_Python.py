import random
def InfinityDice():
  while True:
    sides=int(input("How many sides? "))
    roll=random.randint(1, sides)
    print("You rolled", roll)
    again=input("Roll again? ")
    if again=="yes":
      InfinityDice()
    else:
     break

InfinityDice()
