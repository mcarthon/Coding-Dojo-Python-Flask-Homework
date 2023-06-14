from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import schema

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = """
                SELECT *
                FROM dojos;
                """
        query_results = connectToMySQL( schema ).query_db( query )
        
        dojos = []
        
        for dojo in query_results:
            dojos.append( cls(dojo) )
        
        return dojos
        
    @classmethod
    def get_dojo(cls, data):
        query = """
                SELECT *
                FROM dojos
                WHERE id = %(id)s;
                """
        
        query_result = connectToMySQL( schema ).query_db( query, data )
        
        dojo = cls( query_result[0] )
        
        return dojo
        
    @classmethod
    def create_new_dojo(cls, data):
        query = """
                INSERT INTO dojos
                (name)
                VALUES
                (%(name)s);
                """
        return connectToMySQL( schema ).query_db( query, data )
        