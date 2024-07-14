import random
import time
import hashlib
import json

Login = {}

# Load login data from file
try:
    with open("Login.txt", "r") as f:
        Login = json.load(f)
except Exception:
    pass

def Autosave():
    with open("Login.txt", "w") as f:
        json.dump(Login, f)

def hash_with_salt(text, salt):
    return hashlib.sha256(f"{text}{salt}".encode()).hexdigest()

def AddUser():
    username = input("Username: ")
    password = input("Password: ")

    salt = str(random.randint(100, 9999999999))

    newUser = hash_with_salt(username, salt)
    newPass = hash_with_salt(password, salt)

    Login[newUser] = {"password": newPass, "salt": salt}

    Autosave()

def LoginUser():
    username = input("Username: ")

    for user in Login:
        salt = Login[user]["salt"]
        newUser = hash_with_salt(username, salt)

        if newUser in Login:
            password = input("Password: ")
            newPass = hash_with_salt(password, salt)

            if newPass == Login[newUser]["password"]:
                print("Login Successful")
                return
            else:
                print("Login Failed")
                return

    print("Username not found")
    time.sleep(1)

while True:
    menu = input("1: Add User\n2: Login\n> ")
    if menu == "1":
        AddUser()
    elif menu == "2":
        LoginUser()