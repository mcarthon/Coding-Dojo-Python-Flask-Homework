from flask_app.config.mysqlconnection import connectToMySQL as conn
from flask import flash
import re
from flask_app import schema, bcrypt

EMAIL_REGEX  = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Registration:
    
    def __init__(self, data):
        self.id         = data["id"]
        self.first_name = data["first_name"]
        self.last_name  = data["last_name"]
        self.email      = data["email"]
        self.password   = data["password"]
    
    @classmethod
    def get_all(cls):
        
        query = """
                SELECT *
                FROM info
                """
                
        query_results = conn(schema).query_db(query)
        
        print(query_results)
        
        users = []
        
        for user in query_results:
            users.append(cls(user))
            
        return users
        
    
    @staticmethod        
    def validate_registration(data):
        
        #validate first and last name       
        
        if len(data["first_name"]) < 2 or len(data["last_name"]) < 2:
            flash("First Name and Last Name must be at least 2 characters long")
            return False
        
        #validate email                 
          
        if not EMAIL_REGEX.match(data["email"]):
            flash("You did not enter a valid email")
            return False
            
        if data["email"] != data["confirm_email"]:
            flash("Your emails did not match")
            return False
        
        emails = [user.email for user in Registration.get_all()]            
        if data["email"] in emails:
            flash("This email has already been registered")
            return False    
            
        if len(data["password"]) < 8:
            flash("Password must be at least 8 characters long")
            return False
            
        if data["password"] != data["confirm_password"]:
            flash("Your passwords did not match")
            return False
            
        return True
        
    @classmethod
    def add_user(cls, data):
        
        query = """
                INSERT INTO info
                (first_name, last_name, email, password)
                VALUES
                (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
                """        
        return conn(schema).query_db(query, data)
        
    @classmethod
    def get_user_by_email(cls, data):
        
        query = """
                SELECT *
                FROM info
                WHERE email = %(email)s;
                """
                
        return cls(conn(schema).query_db(query, data)[0])        
        
    @classmethod
    def get_user_by_id(cls, id):
        
        query = """
                SELECT *
                FROM info
                WHERE id = %(id)s;
                """
                
        return cls(conn(schema).query_db(query, id)[0])