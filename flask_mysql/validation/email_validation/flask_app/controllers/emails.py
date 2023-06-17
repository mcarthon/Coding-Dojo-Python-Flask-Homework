from flask_app import app
from flask_app.models.email import Email
from flask import render_template, request, redirect, session

@app.route("/")
def home_page():
    return render_template("home_page.html")
    
@app.route("/submit-email", methods = ["POST"])
def submit_email():
    
    show_red_bar = False
    
    if not Email.validate_email(request.form["email"]):
        show_red_bar = True
        return render_template("home_page.html", show_red_bar = show_red_bar)
    
    else:
        session["email"] = request.form["email"]
        
        data = {
            "email": session["email"]
        }
        
        Email.add_valid_email(data)
        return redirect("/success")
    
@app.route("/success")
def success():
    
    emails = Email.get_all()
    
    print(f"\n\nemails from controller: {emails}\n\n")
    
    return render_template("success_page.html", 
                            emails = emails)
    
@app.route("/delete", methods = ["POST"])
def delete():
    
    data = dict(
        email = request.form["email_id"]
    )
    print(f"\n\ndelete data: {request.form['email_id']}\n\n")
    
    Email.delete(data)
    
    return redirect("/success")