from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.book import Book
from flask_app.models.user import User
    
@app.route("/new-user")
def new_book():
    books = Book.get_all()
    return render_template("new-book.html", books = books)
    
@app.route("/add-book", methods = ["POST"])
def add_book():
    data = {
        "name": request.form["name"]
    }
    Book.add_book(data)
    return redirect("/new-user")
    
@app.route("/book-info-page/<int:id>")
def book_page(id: int):
    data = {
        "id": id
    }
    book = Book.get_book(data)
    favs = Book.get_favs(data)
    not_favs = Book.find_not_favs(data)
    return render_template("book-page.html", 
                            book = book, 
                            favs = favs, 
                            not_favs = not_favs)
   
@app.route("/add-to-favs/<int:id>", methods = ["POST"])
def add_to_favs(id: int):
    data = {
        "book_id": id,
        "user_id": int(request.form["new-fav-user"])
    }
    Book.add_to_favs(data)
    favs = Book.get_favs(data)
    return redirect(f"/book-info-page/{id}", favs = favs)
    

