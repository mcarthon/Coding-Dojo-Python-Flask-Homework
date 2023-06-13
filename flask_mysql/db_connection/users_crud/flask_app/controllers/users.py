from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User


@app.route("/")
def home_page():
    users = User.get_all()
    return render_template("users-r.html", users = users)
    
@app.route("/add_user")
def add_user():    
    return render_template("users-c.html")
    
@app.route("/show_user/<int:id>")
def show_user(id: int):
    user = User.get_one(id)
    return render_template("users-show.html", user = user)
    
@app.route("/edit_user/<int:id>")
def edit_user(id: int):
    user = User.get_one(id)
    return render_template("user-edit.html", user = user)  
                            
@app.route("/update", methods = ["POST"])
def update_user():
    data = {
        "id": request.form["id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.update(data)
    return redirect(f"/show_user/{request.form['id']}")
    
@app.route("/create", methods = ["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email"     : request.form["email"]
    }
    User.create(data)
    return redirect("/")

@app.route("/delete/<int:id>")    
def delete_user(id):
    User.delete(id)
    return redirect("/")