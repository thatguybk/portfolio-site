from flask import Flask, render_template
import json
import os


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")

@app.route("/projects")
def projects():
    with open(os.path.join(app.root_path, 'projects.json')) as f:
        projects_data = json.load(f)
    return render_template("projects.html", projects=projects_data)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

