from flask_app import app
from flask import redirect, request, render_template, session
from flask_app.models.user import User
from flask_app.models.show import Show
from flask_app.models.like import Like
from datetime import datetime

@app.route("/logged-in")
def logged_in():
    
    if "id" in session:
        user = User.get_user({"id": session["id"]})
        
        session["first_name"] = user.first_name
        session["last_name"]  = user.last_name   
        
        all_shows  = Show.get_shows_info()
        
        all_likes = Like.get_user_likes({"user_id": session["id"]})
        
        user_show_likes = [like.show_id for like in all_likes]
        
        return render_template("dashboard.html", 
                                all_shows = all_shows,
                                user_show_likes = user_show_likes)
                                
    return redirect("/")                                
    
@app.route("/view-show/<int:id>")
def view_show(id: int):
    
    if "id" in session:
    
        data = dict(
            
            id = id           
            
        )
        
        show = Show.get_one_info(data)[0]
        
        return render_template("view-show.html", show = show) 
        
    return redirect("/")        
    
@app.route("/edit-page/<int:show_id>")    
def edit_page(show_id: int):
    
    if "id" in session:
        
        show = Show.get_one_info({"id": show_id})[0]
               
        return render_template("edit-show.html", show = show)
        
    return redirect("/")        


    
@app.route("/update-show/<int:id>", methods=["POST"])
def update_show(id: int):
    
    if "id" in session:
        
        data = dict(
            
            id           = id,
            title        = request.form["title"],
            description  = request.form["description"],
            network      = request.form["network"],
            release_date = request.form["release_date"]
            
        ) 
        
        print(f"\n\nupdate request.form\n{request.form}\n\n")
            
        if Show.validate_show(data):
                 
            Show.update_info(data)
            
            show = Show.get_one({"id": id})
                    
            return redirect(f"/view-show/{id}")
            
        return redirect(f"/edit-page/{id}")
    
    return redirect("/")        
            
    
@app.route("/delete-show/<int:id>")
def delete_show(id: int):
    
    if "id" in session:
        print("ture")
    
        data = dict(
            
            id = id
            
        )      
        
        Show.delete_show(data)
        
        return redirect(f"/logged-in")    
    print("dddd")        
    return redirect("/")        
    
@app.route("/new-show-page")
def new_show_page():
    
    if "id" in session:
        return render_template("new-show-page.html")
        
    return redirect("/")        
    
@app.route("/create-new-show", methods = ["POST"])
def create_new_show():
    
    if "id" in session:
    
        data = dict(
            
            posted_by_id = int(session["id"]),
            title        = request.form["title"],
            description  = request.form["description"],
            network      = request.form["network"],
            release_date = request.form["release_date"]
            
        )                
        
        if Show.validate_show(data):
        
            id = Show.create_new(data)  
            
            return redirect(f"/view-show/{id}")
                  
        return redirect("/new-show-page")    
        
    return redirect("/")         