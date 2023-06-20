from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.friendship import Friendship
from flask_app.models.user import User

@app.route("/")
def home_page():
    
    users = User.get_all()        
    
    friendships = Friendship.get_all()
    
    return render_template("home_page.html", 
                            friendships = friendships,
                            users = users)
                            
@app.route("/create-friendship", methods=["POST"])                            
def create_friendship():
    
    data = dict(
        
        user_id   = int(request.form["user"]),
        friend_id = int(request.form["friend"])
        
    )
    
    if Friendship.validate_friendship(data):
        Friendship.add_new(data)
    
    return redirect("/")