from flask_app.config.mysqlconnection import connectToMySQL as conn
from flask_app import schema
from flask import flash
from flask_app.models.message import Message

class Exchange:
    
    def __init__(self, data):
        self.id          = data["id"]
        self.sender_id   = data["sender_id"]
        self.receiver_id = data["receiver_id"]
        self.message_id  = data["message_id"]
        self.created_at  = data["created_at"]
        self.updated_at  = data["updated_at"]                                     
                
    @classmethod    
    def message_sent(self, data):                
        
        data["message_id"] = Message.get_message_id(data)
        
        query = """
                INSERT INTO exchanges
                (sender_id, receiver_id)
                VALUES
                 (%(sender_id)s, %(receiver_id)s, %(message_id)s);
                """ 
        result = conn(schema).query_db(query, data)                          
        return result                                  