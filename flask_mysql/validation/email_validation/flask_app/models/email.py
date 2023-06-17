from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app import schema

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    
    def __init__(self, data):
        self.id = data["email"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod    
    def get_all(cls):
        
        query = """
                SELECT * 
                FROM emails
                """
                
        query_results = connectToMySQL(schema).query_db(query)
        
        emails = []
        
        for email in query_results:
            emails.append(cls(email))
            
        print(f"\n\nemails from query: {emails}\n\n")
            
        return emails
            
    @staticmethod    
    def validate_email(email):
               
        if not EMAIL_REGEX.match(email):
            flash("Email Address is invalid")
            return bool(EMAIL_REGEX.match(email))
            
        emails = Email.get_all()
        email_names = [email.email for email in emails]
        print(email_names)
        
        if email in email_names:
            print("\n\nhere\n\n")
            flash("That email is already in use")
            return False
        return bool(EMAIL_REGEX.match(email))
        
    
    @classmethod    
    def add_valid_email(cls, data):
        
        query = """
                INSERT INTO emails
                (email)
                VALUES
                (%(email)s);
                """
        return connectToMySQL(schema).query_db(query, data)
        
    @classmethod
    def delete(cls, data):
        
        query = """
                DELETE FROM emails
                WHERE email = %(email)s;
                """
        
                
        return connectToMySQL(schema).query_db(query, data)
        