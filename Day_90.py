import requests # import the required library
import json
from builtins import range


for i in range(10):
  result = requests.get("https://randomuser.me/api/") # ask the site for data and store it in a variable
  
  if result.status_code != 200:
    print ("Error, couldn't get API")
    
  else:
    user = result.json() # convert result into a dictionary
  
  
    for person in user['results']:
      
        
      img = person["picture"]["medium"] #assigning user's profile picture to a variable
      picture = requests.get(img) #download the image
  
      
      first_name = person["name"]["first"].lower() #assigning user's first name to a variable
      last_name = person["name"]["last"].lower() #assigning user's last name to a variable
      complete_name = f"""{first_name}_{last_name}.jpg"""
    
      with open(complete_name, "wb") as f: #open the file
        f.write(picture.content)
        
      print (f"Saved {complete_name}")
