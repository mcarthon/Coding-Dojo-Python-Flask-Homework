from flask_app.config.mysqlconnection import connectToMySQL as conn
from flask_app import schema
from flask import flash
from flask_app.models import user

class Painting:
    
    def __init__(self, data):
        self.id          = data["id"]
        self.title       = data["title"]
        self.author_id   = data["author_id"]
        self.description = data["description"]
        self.price       = data["price"]
        self.quantity    = data["quantity"]
        self.created_at  = data["created_at"]
        self.updated_at  = data["updated_at"]
        
    @classmethod
    def get_all(cls):
        
        query = """
                SELECT *
                FROM paintings
                """        
        return [cls(painting) for painting in conn(schema).query_db(query)]
        
    @classmethod
    def get_one(cls, data):
        
        query = """
                SELECT *
                FROM paintings
                WHERE id = %(id)s;
                """        
        return cls(conn(schema).query_db(query, data)[0])          
        
         
    @classmethod
    def get_all_info(cls):
        
        query = """
                SELECT *
                FROM users
                JOIN paintings
                WHERE paintings.author_id = users.id;
                """        
                
        results = conn(schema).query_db(query)
        
        all_paintings = []
        
        for result in results:
            
            user_data = dict(
                
                id         = result["id"],
                first_name = result["first_name"],
                last_name  = result["last_name"],
                email      = result["email"],
                password   = result["password"],
                created_at = result["created_at"],
                updated_at = result["updated_at"]
                
            )
            
            painting_data = dict(
                
                id           = result["paintings.id"],
                title        = result["title"],
                author_id    = result["author_id"],
                description  = result["description"],
                price        = result["price"],
                quantity     = result["quantity"],
                created_at   = result["paintings.created_at"],
                updated_at   = result["paintings.updated_at"]
                
            )
            
            painting = cls(painting_data)
            
            painting.author = user.User(user_data)
            
            all_paintings.append(painting)
            
        return all_paintings            
                        
                                                         
        
    @classmethod
    def get_one_info(cls, data):
        
        query = """
                SELECT *
                FROM users
                JOIN paintings
                WHERE paintings.author_id = users.id
                AND paintings.id = %(id)s;
                """   
                
        result = conn(schema).query_db(query, data)[0] 
        
        user_data = dict(
            
            id         = result["id"],
            first_name = result["first_name"],
            last_name  = result["last_name"],
            email      = result["email"],
            password   = result["password"],
            created_at = result["created_at"],
            updated_at = result["updated_at"]
            
        )                                        
        
        painting_data = dict(
            
            id          = result["paintings.id"],
            title       = result["title"],
            author_id   = result["author_id"],
            description = result["description"],
            price       = result["price"],
            quantity    = result["quantity"],
            created_at  = result["paintings.created_at"],
            updated_at  = result["paintings.updated_at"]                        
            
        )
        
        painting = cls(painting_data) 
        
        painting.author = user.User(user_data) 
        
        return painting     
               
        
    @classmethod
    def create_new(cls, data):
        
        query = """
                INSERT INTO paintings
                (title, description, price, quantity, author_id)
                VALUES
                (%(title)s, %(description)s, %(price)s, %(quantity)s, %(author_id)s)
                """                               
        result = conn(schema).query_db(query, data)                
        
        print(f"\n\nCreate New Painting Result:\n{result}\n\n")
        
        return result
        
    @classmethod
    def update_info(cls, data):
        
        query = """
                UPDATE paintings
                SET title = %(title)s,
                description = %(description)s,
                price = %(price)s,
                quantity = %(quantity)s
                WHERE id = %(id)s;
                """        
                
        return conn(schema).query_db(query, data)       
        
    @classmethod
    def delete_painting(cls, data):
        
        query = """
                DELETE FROM paintings
                WHERE id = %(id)s;
                """
        return conn(schema).query_db(query, data)    
        
    @staticmethod
    def validate_painting(data):     
        
        is_valid = True                       
        
        if len(data["title"]) < 2:  
            flash("You need to give the title for the painting")
            is_valid = False
            
        if len(data["description"]) < 10:
            flash("You need to give the description for the painting")            
            is_valid = False
            
        if data["price"] < 1:
            flash("You give the price for the painting")            
            is_valid = False
            
        if data["quantity"] < 1:
            flash("You give the quantity for the painting")            
            is_valid = False            
       
        return is_valid          