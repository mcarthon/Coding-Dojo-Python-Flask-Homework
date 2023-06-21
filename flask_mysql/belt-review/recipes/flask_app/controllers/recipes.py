from flask_app import app
from flask import redirect, request, render_template, session
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route("/logged-in/<int:id>")
def logged_in(id: int):
    
    user = User.get_user({"id": session["id"]})
    
    session["first_name"] = user.first_name
    session["last_name"]  = user.last_name   
    
    recipes = Recipe.get_all()
    all_info  = Recipe.get_all_info()
    
    return render_template("dashboard.html", 
                            recipes = recipes,
                            all_info = all_info)
    
@app.route("/view-recipe/<int:id>")
def view_recipe(id: int):
    
    data = dict(
        
        id = id           
        
    )
    
    recipe = Recipe.get_one_info(data)
    
    return render_template("view_recipe.html", recipe = recipe) 
    
@app.route("/edit-page/<int:recipe_id>")    
def edit_page(recipe_id: int):
    
    recipe = Recipe.get_one_info({"id": recipe_id})
    
    if "id" in session:
        return render_template("edit-recipe.html", recipe = recipe)
        
    return redirect("/")        


    
@app.route("/update-recipe/<int:id>", methods=["POST"])
def update_recipe(id: int):
    
    data = dict(
        
        id = id,
        name = request.form["name"],
        description = request.form["description"],
        instructions = request.form["instructions"],
        under = request.form["under"],
        created_at = request.form["created_at"]
        
    ) 
    
    print(f"\n\nupdate request.form\n{request.form}\n\n")
        
    if Recipe.validate_recipe(data):
             
        Recipe.update_info(data)
        
        recipe = Recipe.get_one({"id": id})
                
        return redirect(f"/view-recipe/{id}")
        
    return redirect(f"/edit-page/{id}")
            
    
@app.route("/delete-recipe/<int:id>")
def delete_recipe(id: int):
    
    data = dict(
        
        id = id
        
    )      
    
    Recipe.delete_recipe(data)
    
    return redirect(f"/logged-in/{session['id']}")    
    
@app.route("/new-recipe-page")
def new_recipe_page():
    
    if "id" in session:
        return render_template("new_recipe.html")
        
    return redirect("/")        
    
@app.route("/create-new-recipe", methods = ["POST"])
def create_new_recipe():
    
    data = dict(
        
        user_id      = int(session["id"]),
        name         = request.form["name"],
        description  = request.form["description"],
        instructions = request.form["instructions"],
        created_at   = request.form["created_at"],
        under        = request.form["under"]
        
    )
    
    if Recipe.validate_recipe(data):
    
        id = Recipe.create_new(data)  
        
        return redirect(f"/view-recipe/{id}")
              
    return redirect("/new-recipe-page")     