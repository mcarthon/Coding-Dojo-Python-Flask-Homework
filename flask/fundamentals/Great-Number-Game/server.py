from flask import Flask, request, session, render_template, redirect
from random import randint

app = Flask(__name__)

app.secret_key = "yo mama"

@app.route("/")
def home_page():
    session["guess"] = None    
    session["num_guesses"] = 0
    session["correct_number"] = randint(1, 100)
    print(f"correct number: {session}")
    return render_template("number-game.html")

@app.route("/number-input", methods = ["POST"])
def guess():
    print(f"correct number: {session}")
    try:
        session["guess"] = int(request.form["guess"])
    except:
        session["guess"] += 0
    session["num_guesses"] += 1

    lose = False
    
    low_display = False
    high_display = False
    correct_display = False

    try:
        if session["guess"] > session["correct_number"]:
            high_display = True

        elif session["guess"] < session["correct_number"]:
            low_display = True

        else:
            correct_display = True
    except:
        pass
    print(f"correct number: {session}")
    if session["num_guesses"] > 4 and not correct_display:
        lose = True
    return render_template("number-game.html", 
                            high_display  = high_display,
                            low_display = low_display,
                            correct_display = correct_display,
                            lose = lose)

@app.route("/reset")
def reset_function():
    session.pop("correct_number")
    session.pop("num_guesses")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug = True, port = 5050)