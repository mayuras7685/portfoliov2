from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
  return render_template('index.html')

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/contact")
def contact():
  return render_template('contact.html')

@app.route("/projects")
def projects():
  return render_template('projects.html')

@app.route("/experience")
def experience():
  return render_template('experience.html')

@app.route("/certi")
def certi():
  return render_template('certificates.html')


if __name__ == "__main__":
  app.run(debug=True ,port=3000)