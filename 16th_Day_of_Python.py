#First attempt of while loop
x=1
while True:
  song=input("My favourite song by the Strokes is called: ")
  if song=="Reptilia":
    print("You got it!")
    break
  else:
    print("Try again!")
    x=x+1
if x==1:
  print ("It took you only", x, "try.")
else:
  print("It took you only", x, "tries.")

#Second attempt, same result
x=1
song=""
while song!="Reptilia":
  song=input("My favourite song by the Strokes is called: ")
  if song!= "Reptilia":
    print("Incorrect, try again")
    x=x+1
if x==1:
  print("You guessed it! It took you",x,"attempt.")
else:
  print("You guessed it! It took you",x,"attempts.")
