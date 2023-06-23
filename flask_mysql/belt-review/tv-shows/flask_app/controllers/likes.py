from flask_app import app
from flask_app.models.like import Like
from flask import redirect, session

@app.route("/unlike/<int:user_id>/<int:show_id>")
def unlike_show(user_id: int, show_id: int):
    
    if "id" in session:
    
        data = dict(
            
            user_id = user_id,
            show_id = show_id
            
        )
        
        Like.unlike_show(data)
    
        return redirect("/logged-in")
    
    return redirect("/")

@app.route("/like/<int:user_id>/<int:show_id>")
def like_show(user_id: int, show_id: int):
    
    if "id" in session:
    
        data = dict(
            
            user_id = user_id,
            show_id = show_id
            
        )
        
        Like.like_show(data)
    
        return redirect("/logged-in")
    
    return redirect("/")