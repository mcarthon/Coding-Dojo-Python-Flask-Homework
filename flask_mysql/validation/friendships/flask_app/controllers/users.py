from flask_app import app
from flask import request, redirect, render_template
from flask_app.models.user import User

@app.route("/add-user", methods = ["POST"])
def add_user():
    
    data = dict(
        
        first_name = request.form["first_name"],
        last_name = request.form["last_name"]
        
    )
    
    User.add_user(data)
    
    return redirect("/")