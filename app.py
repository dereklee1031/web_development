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

@app.route("/photography/")
def photography():
    images = [
        {"path": "images/IMG_1649.JPG", "name": "Silent Feast", "orientation": "vertical"},
        {"path": "images/IMG_1703.JPG", "name": "Lisbon Street", "orientation": "vertical"},
        {"path": "images/IMG_1615.JPG", "name": "Berlin Hotel", "orientation": "vertical"},
        {"path": "images/DSCF2926.JPG", "name": "Washington Park", "orientation": "horizontal"},
        {"path": "images/DSCF2930.JPG", "name": "Morning Walk", "orientation": "horizontal"},
        {"path": "images/IMG_1565.JPG", "name": "Cathedral", "orientation": "vertical"},
        {"path": "images/IMG_1458.JPG", "name": "Seine", "orientation": "vertical"},
        {"path": "images/IMG_1456.JPG", "name": "Paris Alley", "orientation": "vertical"},
        {"path": "images/IMG_1763.jpg", "name": "Call Box", "orientation": "horizontal"},
        {"path": "images/IMG_1392 2.JPG", "name": "Massachusetts", "orientation": "horizontal"},

    ]
    return render_template("photography.html", images=images)


if __name__ == "__main__":
    app.run(debug=True, port=8000)