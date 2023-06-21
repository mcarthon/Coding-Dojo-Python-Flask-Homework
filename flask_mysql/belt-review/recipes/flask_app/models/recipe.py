from flask_app.config.mysqlconnection import connectToMySQL as conn
from flask_app import schema
from flask import flash
from flask_app.models import user

class Recipe:
    
    def __init__(self, data):
        self.id           = data["id"]
        self.name         = data["name"]
        self.under        = data["under"]
        self.user_id      = data["user_id"]
        self.description  = data["description"]
        self.instructions = data["instructions"]
        self.created_at   = data["created_at"]
        self.updated_at   = data["updated_at"]
        
    @classmethod
    def get_all(cls):
        
        query = """
                SELECT *
                FROM recipes
                """        
        return [cls(recipe) for recipe in conn(schema).query_db(query)]
        
    @classmethod
    def get_one(cls, data):
        
        query = """
                SELECT *
                FROM recipes
                WHERE id = %(id)s;
                """        
        return cls(conn(schema).query_db(query, data)[0])          
        
         
    @classmethod
    def get_all_info(cls):
        
        query = """
                SELECT *
                FROM users
                JOIN recipes
                WHERE recipes.user_id = users.id;
                """        
                
        results = conn(schema).query_db(query)
        
        all_recipes = []
        
        for result in results:
            
            user_data = dict(
                
                id         = result["id"],
                first_name = result["first_name"],
                last_name  = result["last_name"],
                email      = result["email"],
                password   = result["password"]
                
            )
            
            recipe_data = dict(
                
                id           = result["recipes.id"],
                name         = result["name"],
                under        = result["under"],
                user_id      = result["user_id"],
                description  = result["description"],
                instructions = result["instructions"],
                created_at   = result["recipes.created_at"],
                updated_at   = result["recipes.updated_at"]
                
            )
            
            recipe = cls(recipe_data)
            
            recipe.author = user.User(user_data)
            
            all_recipes.append(recipe)
            
        return all_recipes            
                        
                                                         
        
    @classmethod
    def get_one_info(cls, data):
        
        query = """
                SELECT recipes.id,
        	    users.id,
                first_name,
                last_name,
                name, 
                email,
                password,
                under,
                user_id,                
                users.created_at,
                users.updated_at,
                DATE(recipes.created_at),
                DATE(recipes.updated_at),
                instructions,
                description
                FROM users
                JOIN recipes
                WHERE recipes.user_id = users.id
                AND recipes.id = %(id)s;
                """   
                
        result = conn(schema).query_db(query, data)[0] 
        
        user_data = dict(
            
            id         = result["users.id"],
            first_name = result["first_name"],
            last_name  = result["last_name"],
            email      = result["email"],
            password   = result["password"]
            
        )                                        
        
        recipe_data = dict(
            
            id           = result["id"],
            name         = result["name"],
            under        = result["under"],
            user_id      = result["user_id"],
            description  = result["description"],
            instructions = result["instructions"],
            created_at   = result["DATE(recipes.created_at)"],
            updated_at   = result["DATE(recipes.updated_at)"]                        
            
        )
        
        recipe = cls(recipe_data) 
        
        recipe.author = user.User(user_data) 
        
        return recipe     
               
        
    @classmethod
    def create_new(cls, data):
        
        query = """
                INSERT INTO recipes
                (name, description, instructions, created_at, under, user_id)
                VALUES
                (%(name)s, %(description)s, %(instructions)s, %(created_at)s, %(under)s, %(user_id)s)
                """                               
        result = conn(schema).query_db(query, data)                
        
        print(f"\n\nCreate New Recipe Result:\n{result}\n\n")
        
        return result
        
    @classmethod
    def update_info(cls, data):
        
        query = """
                UPDATE recipes
                SET name = %(name)s,
                description = %(description)s,
                instructions = %(instructions)s,
                under = %(under)s,
                created_at = %(created_at)s
                WHERE id = %(id)s;
                """        
                
        return conn(schema).query_db(query, data)       
        
    @classmethod
    def delete_recipe(cls, data):
        
        query = """
                DELETE FROM recipes
                WHERE id = %(id)s;
                """
        return conn(schema).query_db(query, data)    
        
    @staticmethod
    def validate_recipe(data):
        
        print(f"\n\nupdate data\n{data}\n\n")
        
        if len(data["name"]) < 1:  
            flash("You need to give the name for the recipe")
            return False
            
        if len(data["description"]) < 1:
            flash("You need to give the description for the recipe")            
            return False
            
        if len(data["instructions"]) < 1:
            flash("You give the instructions for the recipe")            
            return False
            
        if not data["created_at"]:
            flash("You need to give the date for the recipe")            
            return False
            
        if not data["under"]:
            flash("We need to know if the recipe is less then 30 minutes")                
            return False
            
        return True            
                              