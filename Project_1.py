from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects/")
def projects():
    return render_template("projects.html")

@app.route("/experience/")
def experience():
    return render_template("experience.html")


    
if __name__ == "__main__":
    app.run(debug=True, port=8000)