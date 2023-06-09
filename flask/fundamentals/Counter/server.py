from flask import Flask, request, redirect, session, render_template

app = Flask(__name__)

app.secret_key = "secret key"

@app.route("/")
def home_page():
    if "click_count" in session:
        session["click_count"] += 0
    else:
        session["click_count"] = 1
    if "times_visited" in session:
        session["times_visited"] += 1
    else:
        session["times_visited"] = 1
    return render_template("counter.html")

@app.route("/click")
def click_function():
    session["click_count"] += 1
    return redirect("/")

@app.route("/bytwo")
def bytwo():
    session["click_count"] += 2
    return redirect("/")

@app.route("/custom_increment", methods = ["POST"])
def custom_increment():
    try:
        session["click_count"] += int(request.form["increment"])
    except:
        session["click_count"] += 0
    return redirect("/") 

@app.route("/reset")
def reset_function():
    # session.clear()
    session.pop("click_count")
    session["click_count"] = 1
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True, port = 5001)