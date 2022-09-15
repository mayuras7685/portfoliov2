from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html')

@app.route("/about")
def about():
  return render_template('home.html')

@app.route("/projects")
def projects():
  return render_template('home.html')

@app.route("/work")
def work():
  return render_template('home.html')

@app.route("/certi")
def certi():
  return render_template('home.html')


if __name__ == "__main__":
  app.run(debug=False ,port=3000)