from flask_app import app
from flask import render_template
from flask_app.controllers import losers
from flask_app.models.loser import Loser
from flask_app.models.message import Message

@app.route("/wall/<int:id>")
def wall(id: int):
    
    data = dict(
        id = id
    )
    
    loser = Loser.get_loser_by_id(data)
    
    messages = Message.get_loser_messages(data)
    
    senders = Message.get_sender_data(data)
    
    return render_template("messages.html", 
                            loser = loser,
                            messages = messages,
                            senders = senders)