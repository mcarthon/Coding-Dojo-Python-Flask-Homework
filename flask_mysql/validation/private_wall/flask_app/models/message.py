from flask_app.config.mysqlconnection import connectToMySQL as conn
from flask_app import schema
from flask import flash

class Message:
    
    def __init__(self, data):
        self.id          = data["id"]
        self.sender_id   = data["sender_id"]
        self.receiver_id = data["receiver_id"]
        self.message     = data["message"]
        self.created_at  = data["created_at"]
        self.updated_at  = data["updated_at"]
    
    @classmethod    
    def get_loser_messages(cls, data):
        
        query = """
                SELECT *
                FROM messages
                WHERE receiver_id = %(id)s;
                """        
        query_results = conn(schema).query_db(query, data)
        
        messages = []
        
        for message in query_results:
            messages.append(cls(message))
            
        return messages         
        
    @classmethod
    def get_sender_data(cls, data):
        
        query = """
                SELECT * 
                FROM messages
                JOIN losers
                ON losers.id = messages.sender_id
                WHERE messages.receiver_id = %(id)s;               
                """           
        query_results = conn(schema).query_db(query, data)
        
        senders = []
        
        for sender in query_results:
            senders.append(cls(sender))
        
        return senders
        
            
        
                                