#2 through the power of 0 to 10
#define both the root and the power
counter = 1
x=1
while counter <= 2024:
  print(counter)
  counter=2**x
  x=x+1

#Animal game for kids
exit=""
while exit != "yes":
  animal=input("What animal do you want?: ")
  if animal=="Cow":
    print("A cow goes moo.")
  elif animal=="Cat":
    print("A cat goes meow.")
  elif animal=="Duck":
    print("A duck goes quack.")
  else:
    print("Go ahead and do the sound yourself.")
  exit=input("Do you want to exit? ")
