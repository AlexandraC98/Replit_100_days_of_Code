x=1
nmb=float(input("Enter a number: "))
if nmb<0 or nmb>1000000:
  print ("You weren't supposed to do that")
  exit()
while True:
  guess=float(input("Guess the number: "))
  if x==3:
    print("You have run out of guesses")
    exit()
  if guess<0 or guess>1000000:
    print("Wrong choice")
    exit()
  elif guess<nmb:
    print("Too low")
    x+=1
    continue
  elif guess>nmb and guess<=1000000:
    print("Too high")
    x+=1
    continue
  elif guess==nmb:
    print("Correct!")
    break
if x==1:
  print("It took you",x,"attempt to guess the number")
else:
  print("It took you",x,"attempts to guess the number")