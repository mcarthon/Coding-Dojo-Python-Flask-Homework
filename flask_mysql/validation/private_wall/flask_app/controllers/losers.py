from flask_app import app, bcrypt
from flask import render_template, request, redirect
from flask_app.models.loser import Loser

@app.route("/")
def home_page():
    return render_template("home_page.html")
    
@app.route("/register", methods=["POST"])  
def register():
    
    data = dict(
        first_name       = request.form["first_name"],
        last_name        = request.form["last_name"],
        email            = request.form["email"],
        confirm_email    = request.form["confirm_email"],
        password         = request.form["password"],
        confirm_password = request.form["confirm_password"]
    )
    
    if Loser.validate_registration(data):
        
        data["password"] = bcrypt.generate_password_hash(
            data["password"]
                ).decode("utf-8")
            
        Loser.add_loser(data)    
        
        loser = Loser.get_loser_by_email(data)     
        
        return redirect(f"/wall/{loser.id}")
        
    return redirect("/")
        
@app.route("/login", methods = ["POST"])
def login():
    
    data = dict(
        email    = request.form["login-email"],
        password = request.form["login-password"]
    )                               
   
    if Loser.validate_login(data):
        
        loser = Loser.get_loser_by_email({"email": request.form["login-email"]})              
        
        return redirect(f"/wall/{loser.id}")

    return redirect("/")       