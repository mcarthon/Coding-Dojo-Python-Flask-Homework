from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User
from flask_app.models.book import Book
 
@app.route("/")
def home_page():
    users = User.get_all()
    return render_template("home_page.html", users = users)
    
@app.route("/add-user", methods = ["POST"])
def add_user():
    data = {
        "name": request.form["name"]
    }
    User.add_user(data)
    return redirect("/")
    
@app.route("/user-info-page/<int:id>")
def user_page(id: int):
    data = {
        "id": id
    }
    books = Book.get_all()
    user = User.get_user(data)
    user_favs = Book.get_user_favs(data)
    return render_template("user-page.html", 
                            user = user, 
                            user_favs = user_favs,
                            books = books)
                            
@app.route("/add-fav-book/<int:user_id>", methods = ["POST"])                
def add_fav_book(user_id: int):
    data = {
        "user_id": int(user_id),
        "book_id": int(request.form["book-name"])
    }
    Book.add_to_favs(data)
    return redirect(f"/user-info-page/{user_id}")