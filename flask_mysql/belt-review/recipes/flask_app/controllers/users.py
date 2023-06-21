from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User

@app.route("/")
def home_page():
    return render_template("home_page.html")
    
@app.route("/register", methods=["POST"])    
def register():             
    
    if User.validate_registration(request.form):  
                      
        data = dict(
            
            first_name = request.form["first_name"],
            last_name  = request.form["last_name"],
            email      = request.form["email"],
            password   = request.form["password"]            
            
        )
             
        session["id"] = User.register(data)    
        
        return redirect(f"/logged-in/{session['id']}")
        
    return redirect("/")        
    
@app.route("/login", methods = ["POST"])
def login():
    
    if User.validate_login(request.form):
        
        data = dict(
            
            email = request.form["login-email"]
            
        )
        
        user = User.get_user_by_email(data)
        
        session["id"] = user.id
        
        return redirect(f"/logged-in/{user.id}")
        
    return redirect("/")        
    
    
@app.route("/logout")    
def logout():
    
    session.clear()

    return redirect("/")