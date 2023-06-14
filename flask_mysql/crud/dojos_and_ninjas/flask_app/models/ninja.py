from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import schema

class Ninja:
    def __init__(self, data):
        self.id         = data["id"]
        self.first_name = data["first_name"]
        self.last_name  = data["last_name"]
        self.age        = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def get_all(cls, data):
        query = """
                SELECT *
                FROM ninjas
                WHERE dojo_id = %(id)s;
                """
                
        query_results = connectToMySQL( schema ).query_db(query, data)
        
        ninjas = []
        
        for ninja in query_results:
            ninjas.append( cls(ninja) )
            
        return ninjas
        
    @classmethod
    def create_ninja(cls, data):
        query = """
                INSERT INTO ninjas
                (first_name, last_name, age, dojo_id)
                VALUES
                (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
                """
        return connectToMySQL( schema ).query_db( query, data ) 