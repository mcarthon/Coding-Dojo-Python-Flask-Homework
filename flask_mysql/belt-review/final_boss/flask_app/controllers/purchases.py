from flask_app import app
from flask import redirect, session, render_template
from flask_app.models.purchase import Purchase

@app.route("/buy/<int:painting_id>/<int:quantity>/<int:user_id>", methods =["POST"])
def buy_painting(painting_id: int, quantity: int, user_id: int):
    
    if "id" in session:
        
        data = dict(
            
            painting_id = painting_id,
            quantity    = quantity - 1,
            user_id     = user_id
            
        )
        
        Purchase.purchase_painting(data)              
        
        return redirect(f"/view-painting/{painting_id}")
        
    return redirect("/")        
        
        
        