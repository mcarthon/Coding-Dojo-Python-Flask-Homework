from flask_app import app
from flask import render_template, request, redirect
from flask_app.controllers import losers
from flask_app.models.loser import Loser
from flask_app.models.message import Message
from flask_app.models.exchange import Exchange

@app.route("/wall/<int:id>")
def wall(id: int):
    
    data = dict(
        id = id
    )
    
    other_losers = Loser.get_other_losers(data)    
    
    loser = Loser.get_loser_by_id(data)
    
    all_things = Message.dashboard_messages(data)
    
    sent_messages_count = Message.count_sent_messages(data)   
    
    return render_template("dashboard.html", 
                            loser = loser,
                            all_things = all_things,
                            other_losers = other_losers,
                            sent_messages_count = sent_messages_count)

@app.route("/send-message/<int:id>", methods=["POST"])
def send_message(id: int):
    
    data = dict(
        receiver_id = int(request.form["receiver_id"]),
        sender_id   = id,
        message     = request.form["message"]
    ) 
    
    print()     
    
    message_id = Message.send_message(data)
    
    data["message_id"] = message_id
    
    Exchange.message_sent(data)
                 
    return redirect(f"/wall/{id}")
    
@app.route("/delete/<int:receiver_id>/<int:message_id>")    
def delete_message(receiver_id: int, message_id: int):
    
    data = dict(
        message_id = message_id
    )
    
    Message.delete_message(data)
    
    return redirect(f"/wall/{receiver_id}")