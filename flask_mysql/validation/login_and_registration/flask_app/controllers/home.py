from flask_app import app
from flask import render_template

@app.route("/")
def home_page():
    return render_template("home_page.html")