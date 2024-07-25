from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')


@app.route('/one', methods=['GET'])
def one():

  # Get page arguments and change the template to the one encoded in the URL
  data=request.args
  
  template="default"
  if data != {}:
    template=data['template']
  
  page=""

  #Arguments filled on day one, current date and text
  day="one"
  date=str(datetime.date.today())
  text="""Today was a beautiful day at a skiing resort."""
  
  f = open("templates/template.html", "r")
  page = f.read()
  f.close()

  #Replace the arguments in the template
  page=page.replace("{day}", day)
  page=page.replace("{date}", date)
  page=page.replace("{text}", text)
  page=page.replace("{template}", template)

  #Return the page with the arguments given on day one
  return page


@app.route('/two', methods=['GET'])
def two():
  
  # Get page arguments and change the template to the one encoded in the URL
  data=request.args

  template="default"
  if data != {}:
    template=data['template']
    
  page=""

  #Arguments on day 2
  day="two"
  date=str(datetime.date.today())
  text="""I drank some coffee and ate some pancakes."""
  
  f = open("templates/template.html", "r")
  page = f.read()
  f.close()

  #Replace the arguments in the template
  page=page.replace("{day}", day)
  page=page.replace("{date}", date)
  page=page.replace("{text}", text)
  page=page.replace("{template}", template)

  #Return the page with the arguments given on day two
  return page
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
