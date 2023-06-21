from flask_app.config.mysqlconnection import connectToMySQL as conn
from flask_app import schema, bcrypt
from flask import flash
import re

EMAIL_REGEX  = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

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
        
    @staticmethod
    def validate_login(data):
        
        if len(data["login-email"]) < 1:
            flash("You forgot to enter an email")
            return False
        
        emails = User.get_all_emails()
        
        if data["login-email"] not in emails:
            flash("This email has not yet been registered")                               
            return False
            
        user = User.get_user_by_email({"email": data["login-email"]})            
            
        if not bcrypt.check_password_hash(user.password, data["login-password"]):
            flash("The password you entered is not the correct password for this email")                    
            return False
            
        return True            
                         
        
    @staticmethod
    def validate_registration(data):
        
        if len(data["first_name"]) < 2:
            flash("First Name must be at least 2 characters long")
            return False
            
        if len(data["last_name"]) < 2:
            flash("Last Name must be at least 2 characters long")
            return False                                         
            
        if not EMAIL_REGEX.match(data["email"]):
            flash("You have entered an invalid email address")
            return False
            
        if data["email"] != data["confirm-email"]:
            flash("The two emails you entered did not match")
            return False
            
        emails = User.get_all_emails()            
        
        if data["email"] in emails:
            flash("This email address has already been registered foo!")
            return False
        
        return True                                         
            
    @classmethod        
    def register(cls, data):
        
        data["password"] = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
        
        query = """
                INSERT INTO users
                (first_name, last_name, email, password)
                VALUES
                (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
                """         
        return conn(schema).query_db(query, data)                