from flask_app.config.mysqlconnection import connectToMySQL as conn
from flask_app import schema

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
                       
        return conn(schema).query_db(query, data)      
        
    @classmethod
    def dashboard_messages(cls, data):
        
        query = """
                SELECT *,
                TIMESTAMPDIFF(MINUTE, messages.updated_at, NOW()) AS minutes_passed 
                FROM exchanges
                JOIN losers
                ON losers.id = exchanges.sender_id
                JOIN messages
                ON messages.id = exchanges.message_id
                WHERE exchanges.receiver_id = %(id)s;
                """  
                
        query_results = conn(schema).query_db(query, data)
        
        stuffs = []
        
        for stuff in query_results:
            stuffs.append(stuff)

        return stuffs 
        
    @classmethod
    def count_sent_messages(cls, data):
        
        query = """
                SELECT COUNT(exchanges.id) AS num_messages_sent
                FROM  exchanges
                WHERE exchanges.sender_id = %(id)s;
                """                             
                
        return conn(schema).query_db(query, data)[0]["num_messages_sent"]
        
    @classmethod
    def delete_message(cls, data):
        
        query = """
                DELETE FROM exchanges
                WHERE message_id = %(message_id)s;
                """        
                
        conn(schema).query_db(query, data)