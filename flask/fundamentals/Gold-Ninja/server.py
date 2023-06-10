from flask import Flask, request, session, redirect, render_template
from random import randint

app = Flask(__name__)

app.secret_key = "java world"

@app.route("/")
def home_page():
    if "farm_increase" in session:
        session["farm_increase"] += 0
    else:
        session["farm_increase"] = 0
    
    if "cave_increase" in session:
        session["cave_increase"] += 0
    else:
        session["cave_increase"] = 0

    if "house_increase" in session:
        session["house_increase"] += 0
    else:
        session["house_increase"] = 0
    
    if "casino_increase" in session:
        session["casino_increase"] += 0
    else:
        session["casino_increase"] = 0

    return render_template("ninja.html") 

@app.route("/process_money", methods = ["POST"])
def process_money():
    if request.form["which_form"] == "farm":
        session["farm_increase"] += randint(10, 20)

    elif request.form["which_form"] == "cave":
        session["cave_increase"] += randint(5, 10)
        
    elif request.form["which_form"] == "house":
        session["house_increase"] += randint(2, 5)

    elif request.form["which_form"] == "casino":
        session["casino_increase"] += randint(-50, 50)

    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)