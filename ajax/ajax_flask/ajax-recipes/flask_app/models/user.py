from flask_app.config.mysqlconnection import connectToMySQL as conn
from flask_app import schema, bcrypt
from flask import flash

class User:      
    
    def __init__(self, data):
        self.id         = data["id"]
        self.first_name = data["first_name"]
        self.last_name  = data["last_name"]
        self.email      = data["email"]
        self.password   = data["password"]
        
    @classmethod
    def get_all_emails(cls):
        
        query = """
                SELECT email
                FROM users
                """       
        return [email["email"] for email in conn(schema).query_db(query)]                  
        
    @classmethod
    def get_user(cls, data):
        
        query = """
                SELECT *
                FROM users
                WHERE id = %(id)s;               
                """       
        return cls(conn(schema).query_db(query, data)[0])      
        
    @classmethod
    def get_user_by_email(cls, data):
        
        query = """
                SELECT * 
                FROM users
                WHERE email = %(email)s;
                """   
        
        return cls(conn(schema).query_db(query, data)[0])                  