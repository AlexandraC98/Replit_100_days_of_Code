import datetime, os, time, pytz

bucharest_tz = pytz.timezone('Europe/Bucharest')

Tweets={}

try:
  with open("Tweets.txt", "r") as f:
    Tweets=eval(f.read())
except Exception:
  pass

def prettyPrint():
  print()
  sorted_keys=sorted(Tweets.keys(), reverse=True)
  for key in sorted_keys:
    local_time=key.astimezone(bucharest_tz)
    print(f"{local_time.strftime('%Y-%m-%d %H:%M:%S')}: {Tweets[key]}", end="\n")
  print()

def Add():
  os.system("clear")
  tweet=input("Enter your tweet: ")
  key=datetime.datetime.now()
  Tweets[key]=tweet
  time.sleep(1)
  prettyPrint()

def View():
  sorted_keys=sorted(Tweets.keys(), reverse=True)
  for key in sorted_keys[:10]:
    local_time=key.astimezone(bucharest_tz)
    print(f"{local_time.strftime('%Y-%m-%d %H:%M:%S')}: {Tweets[key]}", end="\n")

  if len(sorted_keys)>10:
    if input("Do you want to see more? (y/n) > ")[0].lower()=="y":
      os.system("clear")
      prettyPrint()

def AutoSave():
  with open("Tweets.txt", "w") as f:
    f.write(str(Tweets))

def Quit():
  choice=input("Do you want to quit? (y/n): ")
  if choice.lower().startswith("y"):
    AutoSave()
    exit()

while True:
  os.system("clear")
  menu=input("1: Add Tweet\n2: View Tweets\n")
  if menu=="1":
    Add()
    Quit()
  else:
    View()
    Quit()
