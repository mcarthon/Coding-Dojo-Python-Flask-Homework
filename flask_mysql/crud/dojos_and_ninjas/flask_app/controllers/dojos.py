from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def home_page():
    dojos = Dojo.get_all()
    return render_template("home_page.html", dojos = dojos)

@app.route("/show-dojo/<int:id>")    
def show_dojo(id: int):
    data   = {"id": id}
    dojo   = Dojo.get_dojo(data)
    data = {"id": id}
    ninjas = Ninja.get_all(data)
    return render_template("show-dojo.html", dojo = dojo, ninjas = ninjas)
    
@app.route("/new-dojo", methods = ["POST"])
def new_dojo():
    data = {
        "name": request.form["new_dojo_name"]
    }
    Dojo.create_new_dojo(data)
    return redirect("/")
    
