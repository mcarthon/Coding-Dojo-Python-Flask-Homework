from flask import Flask, request, render_template, redirect
from users import User

app = Flask(__name__)

app.secret_key = "java world"

@app.route("/")
def home_page():
    
    users = User.get_all()
    print(users)
    
    return render_template("users-r.html", users = users)
    
@app.route("/add_user")
def add_user():
    return render_template("users-c.html")
    
@app.route("/create", methods = ["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email"     : request.form["email"]
    }
    
    User.create(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)