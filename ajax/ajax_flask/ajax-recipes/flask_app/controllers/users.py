from flask_app import app
from flask import render_template, redirect, session, request

@app.route("/")
def home_page():    
    return render_template("home-page.html")

@app.route("/")
def get_emails():
	 
	