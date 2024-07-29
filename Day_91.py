import requests, json, time, os

saved_jokes = {}

def autoSave():
  with open ("DadJokes.txt", "w") as f:
    # Write the dictionary to the file
    json.dump(saved_jokes, f)

def autoLoad():
  global saved_jokes
  try:
    with open ("DadJokes.txt", "r") as f:
      saved_jokes = json.load(f)
      
    if not isinstance(saved_jokes, dict):
      raise ValueError("Data loaded from file is not a dictionary.")
      
  except FileNotFoundError:
    saved_jokes = {}
  except (ValueError, json.JSONDecodeError) as e:
    print(f"Error loading data: {e}")
    saved_jokes = {}

def Quit():
  print("Thank you for using the Joke Generator")
  time.sleep(1)
  autoSave()
  exit()
  

#Main loop
autoLoad()

while True:
  os.system("clear")
  
  random_joke = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) #get random joke

  if random_joke.status_code != 200:
    print("Error, couldn't get the joke (we are too serious).")

  else:
    joke = random_joke.json() #convert joke into a dictionary

    jk = joke["joke"] #get joke from dictionary
    id = joke["id"] #get id from dictionary
    
    print(jk) #print joke
    
    menu = input ("Save joke (1), Load old jokes (2), New joke (3), Exit (4): ")

    if menu == "3":
      continue
    
    elif menu == "1":
      saved_jokes[id] = jk
      autoSave()
      print("Joke saved!")
      time.sleep(1)
      continue
      
    elif menu =="2":
      autoLoad()
      if saved_jokes:
        for key in saved_jokes:
          print(saved_jokes[key])
          time.sleep(1)
      else:
        print ("No saved jokes")
        time.sleep(1)
      
    else:
      Quit()
