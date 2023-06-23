from flask_app import app
from flask import redirect, request, render_template, session
from flask_app.models.user import User
from flask_app.models.painting import Painting
from flask_app.models.purchase import Purchase

@app.route("/logged-in")
def logged_in():
    
    if "id" in session:
        user = User.get_user({"id": session["id"]})
        
        session["first_name"] = user.first_name
        session["last_name"]  = user.last_name   
        
        paintings = Painting.get_all()
        all_info  = Painting.get_all_info()
        user_purchases = Purchase.get_user_purchases({"user_id": session["id"]})
        
        return render_template("dashboard.html", 
                                paintings = paintings,
                                all_info = all_info,
                                user_purchases = user_purchases)
                                
    return redirect("/")                                
    
@app.route("/view-painting/<int:id>")
def view_painting(id: int):
    
    if "id" in session:
        data = dict(
            
            id = id           
            
        )
        
        painting = Painting.get_one_info(data)
        purchases = Purchase.get_purchases(data) 
        num_purchases = len(purchases)           
                
        
        return render_template("view-painting.html", 
                                painting = painting,
                                purchases = purchases,
                                num_purchases = num_purchases) 
    return redirect("/")        
    
@app.route("/edit-page/<int:painting_id>")    
def edit_page(painting_id: int):
    
    painting = Painting.get_one_info({"id": painting_id})
    
    if "id" in session:
        return render_template("edit-painting.html", painting = painting)
        
    return redirect("/")        


    
@app.route("/update-painting/<int:id>", methods=["POST"])
def update_painting(id: int):
    
    if "id" in session:
        data = dict(
            
            id          = id,
            title       = request.form["title"],
            description = request.form["description"],
            price       = int(request.form["price"]) if request.form["price"] else 0,
            quantity    = int(request.form["quantity"]) if request.form["price"] else 0
            
        ) 
        
        print(f"\n\nupdate request.form\n{request.form}\n\n")
            
        if Painting.validate_painting(data):
                 
            Painting.update_info(data)
            
            painting = Painting.get_one({"id": id})
                    
            return redirect(f"/view-painting/{id}")
            
        return redirect(f"/edit-page/{id}")
        
    return redirect("/")        
            
    
@app.route("/delete-painting/<int:id>")
def delete_painting(id: int):
    
    if "id" in session:
        data = dict(
            
            id = id
            
        )      
        
        Painting.delete_painting(data)
        
        return redirect(f"/logged-in/{session['id']}")  
        
    return("/")          
    
@app.route("/new-painting-page")
def new_painting_page():
    
    if "id" in session:
        return render_template("new-painting.html")
        
    return redirect("/")        
    
@app.route("/create-new-painting", methods = ["POST"])
def create_new_painting():
    
    if "id" in session:
        data = dict(
            
            author_id   = int(session["id"]),
            title       = request.form["title"],
            description = request.form["description"],
            price       = int(request.form["price"]) if request.form["price"] else 0,
            quantity    = int(request.form["price"]) if request.form["price"] else 0
        )
        
        if Painting.validate_painting(data):
        
            id = Painting.create_new(data)  
            
            return redirect(f"/view-painting/{id}")
                  
        return redirect("/new-painting-page")     
    return redirect("/")        