from flask import Flask, render_template

app = Flask(__name__)

myReflections={}

myReflections={
   "78": {
   'date': "23/07/2024",
   'reflection': "Complicated, but I'm very determined to understand this and do more complex projects."
   }
}

#First page loaded
@app.route("/")
def index():
  return render_template('index.html')

#Page for each day, day of writing code, link to the code, reflection on day
@app.route('/<pageNumber>')
def homepage(pageNumber):

    reflection_data = myReflections[pageNumber]
    return render_template('template.html', day=pageNumber, date=reflection_data["date"], reflection=reflection_data["reflection"])

if __name__ == '__main__':
    app.run(port=5001)