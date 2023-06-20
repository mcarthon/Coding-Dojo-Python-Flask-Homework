from flask_app.config.mysqlconnection import connectToMySQL as conn
from flask_app import schema

class User:
    
    def __init__(self, data):
        self.id         = data["id"]      
        self.first_name = data["first_name"] 
        self.last_name  = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        
        query = """
                SELECT *
                FROM users;
                """
        query_results = conn(schema).query_db(query)
        
        users = []
        
        for user in query_results:
            users.append(cls(user))
            
        return users            
        
    
    @classmethod        
    def add_user(cls, data):
        
        query = """
                INSERT INTO users
                (first_name, last_name)
                VALUES
                (%(first_name)s, %(last_name)s);                    
                """
        
        return conn(schema).query_db(query, data)                