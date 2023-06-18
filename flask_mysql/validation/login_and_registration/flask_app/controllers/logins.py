from flask_app import app, bcrypt
from flask import render_template, request, redirect
from flask_app.models.registration import Registration
from flask_app.models.login import Login

@app.route(f"/logged-in/<int:id>")
def logged_in(id: int):
    user = Registration.get_user_by_id({"id":id})
    return render_template("logged_in.html", user = user)
    
@app.route("/login-page")    
def login_page():
    return render_template("login.html")
    
@app.route("/login", methods = ["POST"])    
def login():
       
    data = dict(
        email = request.form["email"],
        password = request.form["password"]
    )    
    
    if Login.validate_login(data):
        user = Registration.get_user_by_email(data)
        return redirect(f"/logged-in/{user.id}")        
        
    return redirect("/login-page")    
        