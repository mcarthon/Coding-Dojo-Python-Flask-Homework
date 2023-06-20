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
    
    messages = Message.get_loser_messages(data)
    
    senders = Loser.get_sender_data(data)
    
    return render_template("dashboard.html", 
                            loser = loser,
                            messages = messages,
                            senders = senders,
                            other_losers = other_losers)

@app.route("/send-message/<int:id>", methods=["POST"])
def send_message(id: int):
    
    data = dict(
        receiver_id = int(request.form["receiver_id"]),
        sender_id   = id,
        message     = request.form["message"]
    )      
    
    Message.send_message(data)
    Exchange.message_sent(data)
                 
    return redirect(f"/wall/{id}")