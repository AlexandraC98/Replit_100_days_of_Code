import random, time

Login={}

try:
  with open("Login.txt", "r") as f:
    Login = eval(f.read())
except Exception:
  pass

def Autosave():
  with open("Login.txt", "w") as f:
    f.write(str(Login))

def AddUser():
  username=input("Username: ")
  password=input("Password: ")

  salt=random.randint(100,9999999999)
  salt=str(salt)

  newUser=hash(f"{username} {salt}")
  newPass=hash(f"{password} {salt}")
  
  Login[newUser]={"password":newPass, "salt":salt}
  
  Autosave()

def LoginUser():
  username=input("Username: ")

  for user in Login:
    salt=Login[user]["salt"]
    newUser=hash(f"{username} {salt}")
    
    if newUser in Login:
      password=input("Password: ")
      newPass = hash(f"{password} {salt}")
        
      if newPass==Login[newUser]["password"]:
        print("Login Successful")
        return
      else:
        print("Login Failed")
        return

  print("Username not found")
  time.sleep(1)

while True:
  menu=input("1: Add User\n2: Login\n> ")
  if menu=="1":
    AddUser()
  elif menu=='2':
    LoginUser()
