from flask_app.config.mysqlconnection import connectToMySQL as conn
from flask_app import schema
from flask import flash

class Message:
    
    def __init__(self, data):
        self.id          = data["id"]
        self.message     = data["message"]
        self.created_at  = data["created_at"]
        self.updated_at  = data["updated_at"]
    
    @classmethod    
    def get_loser_messages(cls, data):
        
        query = """
                SELECT *
                FROM exchanges
                JOIN messages
                ON exchanges.message_id = messages.id
                WHERE exchanges.receiver_id = %(id)s;
                """        
        query_results = conn(schema).query_db(query, data)
        
        messages = []
        
        for message in query_results:
            messages.append(cls(message))
            
        return messages         
        
                 
        
    @classmethod
    def send_message(cls, data):
        
        query = """
                          INSERT INTO messages
                          (message)
                          VALUES
                          (%(message)s);
                          """                          
        result = conn(schema).query_db(query, data)                
        return result               
        
    @classmethod
    def get_message_id(cls, data):     
        
        query = """
                SELECT id
                FROM messages
                WHERE message LIKE %(message)s;
                """                
        result = conn(schema).query_db(query, data)                
        return result                 