from flask_app.config.mysqlconnection import connectToMySQL as conn
from flask_app import bcrypt, schema
from flask import flash

class Login:
    
    def __init__(self, data):
        self.email = data["email"]
        self.password = data["password"]
    
    @classmethod
    def get_all(cls):
        
        query = """
                SELECT * 
                FROM info
                """
        print(conn(schema).query_db(query))                
        return conn(schema).query_db(query)   
        
    @classmethod    
    def get_one(cls, data):
        
        query = """
                SELECT *
                FROM info
                WHERE email = %(email)s;
                """                 
    
        return cls(conn(schema).query_db(query, data)[0])
        
    @staticmethod
    def validate_login(data):
        
        print(f"\n\ndata for log in validation:\n{data}\n\n")
        
        if len(data["email"]) < 1:
            flash("You forgot to enter an email")
            return False
            
        users = Login.get_all()
        emails = [user["email"] for user in users]
        print(emails)
                        
        if data["email"] not in emails:
            flash("Email not found")
            return False                                 
        
        user = Login.get_one(data)
        print(f"\n\nuser password after Login.get_one(data):\n{user.password}\n\n")
        
        if not bcrypt.check_password_hash(user.password, data["password"]):
            print(f"\n\ndata['password']:\n{data['password']}\n")
            print(f"user.password:\n{user.password}\n")
            flash("Password is incorrect")
            return False        
            
        return True           