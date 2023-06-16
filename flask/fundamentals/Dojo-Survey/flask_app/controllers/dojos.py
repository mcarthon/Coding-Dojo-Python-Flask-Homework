from flask_app import app
from flask import render_template, session, request, redirect
from flask_app.models.dojo import Dojo


@app.route("/")
def home_page():
    return render_template("survey.html")

@app.route("/form-submit", methods = ["POST"])
def form_submit():
    session["form-submit"] = request.form
    
    if not Dojo.validate_dojo(request.form):
        return redirect("/")
    
    return render_template("result.html")