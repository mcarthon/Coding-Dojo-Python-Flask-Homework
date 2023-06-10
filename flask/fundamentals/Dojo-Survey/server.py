from flask import Flask, request, session, redirect, render_template

app = Flask(__name__)

app.secret_key = "rgbfrdgtb"

@app.route("/")
def home_page():
    return render_template("survey.html")

@app.route("/form-submit", methods = ["POST"])
def form_submit():
    session["form-submit"] = request.form

    print()
    print("-" * 150)
    print(session["form-submit"])
    print("-" * 150)
    print()

    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug = True, port = 5050)