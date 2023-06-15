from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import schema

class User:
    
    def __init__(self, data):
        self.id         = data["id"]
        self.name       = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod    
    def get_all(cls):
        
        query = """
                SELECT *
                FROM users;
                """
                
        query_results = connectToMySQL(schema).query_db(query)
        
        users = []
        
        for user in query_results:
            users.append(cls(user)) 
            
        return users
      
    @classmethod    
    def get_user(cls, data):
        
        query = """
                SELECT *
                FROM users
                WHERE id = %(id)s;
                """
        print(connectToMySQL(schema).query_db(query, data)[0])
        return connectToMySQL(schema).query_db(query, data)[0]
        
    @classmethod    
    def add_user(cls, data):
        
        query = """
                INSERT INTO users
                (name)
                VALUES
                (%(name)s);
                """
                
        return connectToMySQL(schema).query_db(query, data)
        
   