default="\033[0m"
red="\033[31m"
green="\033[32m"
blue="\033[34m"
cyan="\033[36m"
purple="\033[35m"
yellow="\033[33m"

print("Exam Grade Calculator")
print()
nationality=input("Are you American or Romanian? ")
print()
name_of_exam = input("Name of exam: ")
maxscore=float(input("Max. Possible Score: "))
yourscore=float(input("Your score: "))
print()
percentage=round(float(yourscore*100/maxscore),2)
print(percentage,"%")
print()
if nationality=="American" or nationality=="american":
  if percentage>=90:
    print("Awesome, you got an", red, "A+",default)
  elif percentage>=80 and percentage<90:
    print("Bravo, you got an", purple, "A-",default)
  elif percentage>=70 and percentage<80:
    print("That's good, you got an", blue, "B",default)
  elif percentage>=60 and percentage<70:
    print("It's ok, you got an", cyan, "C", default)
  elif percentage>=50 and percentage<60:
    print("Meh, you got an", yellow, "D", default)
  else:
    print("You got an", yellow, "U", default)

if nationality=="Romanian" or nationality=="romanian":
  if percentage>=95:
    print("10")
  elif percentage>=85 and percentage<94:
    print("9")
  elif percentage>=75 and percentage<84:
    print("8")
  elif percentage>=65 and percentage<74:
    print("7")
  elif percentage>=55 and percentage<64:
    print("6")
  elif percentage>=50 and percentage<54:
    print("5")
  else:
    print("Loser!")
