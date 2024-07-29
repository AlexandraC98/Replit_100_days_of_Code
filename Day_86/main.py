from flask import Flask, request, render_template, session, redirect # type: ignore
from dotenv import load_dotenv # type: ignore
import os

app = Flask(__name__, static_url_path="/static")

#Used python dotenv to store password in a secret in VSCode
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
myUser = "AC98"

#Entries will be saved in this dictionary
blog = {}


#Create a subroutine to display all the entries of the list
def getBlogs():
  content = "" #variable content will display each entry added
  entry = ""

  f = open ("templates/entry.html", "r") #used template to store entries
  entry = f.read()
  f.close()

  keys = blog.keys()
  keys = list(keys) #created a list to reverse the order of entries, in order to display the last entry added at the top

  for key in reversed(keys):
    newEntry = entry #made a copy of entry
    if key != "user":
      newEntry = newEntry.replace("{date}", blog[key]["date"])
      newEntry = newEntry.replace("{title}", blog[key]["title"])
      newEntry = newEntry.replace("{body}", blog[key]["body"])
      content+=newEntry

  return content


#Home page
@app.route('/')
def home():

  if session.get('user'):
    return redirect ('/dashboard') #if I'm logged in, don't make me login again
    
  return render_template('home.html')


#Login page
@app.route('/login', methods=['GET', 'POST'])
def login():

  if session.get('user'):
    return redirect ('/dashboard')
  
  if request.method == 'POST':
    username=request.form['userName']
    password=request.form['userPassword']

    if username == myUser and password == os.getenv('SECRET_KEY'): #check username and secret password
      session ['user'] = {"username": username} #store user in session
      return redirect('/dashboard')
      
    else:
      return render_template('login.html', error='Invalid username or password')
      
  return render_template('login.html')


#Dashboard page
@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():

  if session['user']['username'] != myUser:
    return redirect('/')

  page = ""

  f = open ("templates/dashboard.html", "r")
  page = f.read()
  f.close()

  page = page.replace("{content}", getBlogs()) #display all the entries which were added in this session

  if session['user']['username'] == myUser:
    page = page.replace("{user}", myUser)
  else:
    page = page.replace("{user}", "")

  return page


#Add new entry to the dictionary blog
@app.route('/add', methods = ["POST"])
def add():
  form = request.form

  entry = {
    "date": form["date"],
    "title": form["title"],
    "body": form["body"]
  }

  blog[form["date"]] = entry

  return redirect ('/dashboard')


#Logout page
@app.route('/logout')
def logout():
  session.clear()
  return redirect("/")


if __name__ == '__main__':
  app.run(debug=True)