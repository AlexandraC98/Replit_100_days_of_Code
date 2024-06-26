x=0
variable=int(input("Number from 1-10: "))
for i in range (1,11):
  result=int(input(f"How much is {i} x {variable}?: "))
  if result==variable*i:
    print("Correct")
    x=x+1
  else:
    print("Wrong")
    x=x-1
if x==10:
  print("\033[35m","Sehr gut, your score is", x)
else:
  print ("\033[36m","Your score is", x)
