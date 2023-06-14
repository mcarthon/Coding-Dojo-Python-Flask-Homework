from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
    
@app.route("/new-ninja")
def new_ninja_page():
    dojos = Dojo.get_all()
    return render_template("new-ninja.html", dojos = dojos)
    
@app.route("/add-ninja", methods = ["POST"])
def add_ninja():
    data = {
        "dojo_id"   : request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age"       : request.form["age"]
    }
    Ninja.create_ninja(data)
    return redirect(f"/show-dojo/{request.form['dojo_id']}")