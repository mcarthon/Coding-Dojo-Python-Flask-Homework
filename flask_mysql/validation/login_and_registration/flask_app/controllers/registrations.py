from flask_app import app, bcrypt
from flask import render_template, redirect, session, request
from flask_app.models.registration import Registration


@app.route("/registration")
def registration_link():
    return render_template("registration.html")

@app.route("/submit-registration", methods = ["POST"])    
def submit_registration():
    
    data = dict(
        first_name = request.form["first_name"],
        last_name  = request.form["last_name"],
        email      = request.form["email"],
        confirm_email = request.form["confirm_email"],
        password   = request.form["password"],
        confirm_password = request.form["confirm_password"]
    )
    
    if Registration.validate_registration(data):
        data["password"] = bcrypt.generate_password_hash(request.form["password"]).decode("utf-8")
        Registration.add_user(data)
        user = Registration.get_user_by_email(data)
        return redirect(f"/logged-in/{user.id}")
    
    return redirect("/registration")
    
    