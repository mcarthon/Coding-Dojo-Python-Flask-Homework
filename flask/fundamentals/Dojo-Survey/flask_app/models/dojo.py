from flask_app.config.mysqlconnection import connectToMySQL as connect
from flask import flash

class Dojo:
    
    def __init__(self, data):
        self.id         = data["id"]
        self.name       = data["name"]
        self.location   = data["location"]
        self.comment    = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @staticmethod
    def validate_dojo(dojo):
        
        is_valid = True
        
        if not all([dojo[str(key)] for key in dojo.keys()]):
            flash("All fields must be completed.")
            is_valid = False
        
        return is_valid
        
        