from flask_app.config.mysqlconnection import connectToMySQL as conn
from flask_app import schema
from flask import flash
from flask_app.models import user, like

class Show:
    
    def __init__(self, data):
        self.id           = data["id"]
        self.posted_by_id = data["posted_by_id"]
        self.title        = data["title"]
        self.description  = data["description"]
        self.network      = data["network"]
        self.release_date = data["release_date"]
        self.created_at   = data["created_at"]
        self.updated_at   = data["updated_at"]
        
    @classmethod
    def get_all(cls):
        
        query = """
                SELECT *
                FROM shows
                """        
        return [cls(show) for show in conn(schema).query_db(query)]
        
    @classmethod
    def get_one(cls, data):
        
        query = """
                SELECT *
                FROM shows
                WHERE id = %(id)s;
                """        
        return cls(conn(schema).query_db(query, data)[0])          
        
         
    @classmethod
    def get_shows_info(cls):
        
        query = """
                SELECT *,
                DATE_FORMAT(release_date,'%M %d %Y') AS showdate
                FROM shows
                JOIN users
                ON users.id = shows.posted_by_id
                LEFT JOIN likes
                ON likes.show_id = shows.id;
                """       
                
        results = conn(schema).query_db(query)
        
        print(f"\n\nresults\n{results}\n\n")
        
        all_shows = []
        
        for result in results:
            
            show_data = dict(
                
                id           = result["id"],
                title        = result["title"],
                network      = result["network"],
                release_date = result["release_date"],
                description  = result["description"],
                posted_by_id = result["posted_by_id"],
                created_at   = result["created_at"],
                updated_at   = result["updated_at"]
                
            )             
            
            user_data = dict(
                
                id         = result["users.id"],
                first_name = result["first_name"],
                last_name  = result["last_name"],
                email      = result["email"],
                password   = result["password"],
                created_at = result["users.created_at"],
                updated_at = result["users.updated_at"]
                
            )
            
            likes_data = dict(
                
                id         = result["likes.id"],
                user_id    = result["user_id"],
                show_id    = result["show_id"],
                created_at = result["likes.created_at"],
                updated_at = result["likes.updated_at"]
                
            )
           
            show = cls(show_data)
            
            show.poster = user.User(user_data)   
            
            show.likes = like.Like(likes_data)
            
            if show.likes.id:
                show.likes.num_likes += 1
            
            show.showdate = result["showdate"]                     
            
            all_shows.append(show) 
            
        print(f"\n\nnum_likes\n{len([show.likes.num_likes for show in all_shows if show.likes.num_likes])}\n{sorted([show.id for show in all_shows if show.likes.id])}\n\n")                           
            
        return all_shows            
                        
                                                         
        
    @classmethod
    def get_one_info(cls, data):
        
        query = """
                SELECT *
                FROM shows
                JOIN users
                ON users.id = shows.posted_by_id
                LEFT JOIN likes
                ON likes.show_id = shows.id
                WHERE shows.id = %(id)s;
                """   
                
        query_results = conn(schema).query_db(query, data)
        
        print(f"\n\nGet One Info\n{query_results}\n\n")
        
        all_results = []
        
        for result in query_results:   
            
            show_data = dict(
                
                id           = result["id"],
                title        = result["title"],
                network      = result["network"],
                release_date = result["release_date"],
                description  = result["description"],
                posted_by_id = result["posted_by_id"],
                created_at   = result["created_at"],
                updated_at   = result["updated_at"]
                
            )             
            
            user_data = dict(
                
                id         = result["users.id"],
                first_name = result["first_name"],
                last_name  = result["last_name"],
                email      = result["email"],
                password   = result["password"],
                created_at = result["users.created_at"],
                updated_at = result["users.updated_at"]
                
            )
            
            likes_data = dict(
                
                id         = result["likes.id"],
                user_id    = result["user_id"],
                show_id    = result["show_id"],
                created_at = result["likes.created_at"],
                updated_at = result["likes.updated_at"]
                
            )
            
            show = cls(show_data) 
            
            show.poster = user.User(user_data) 
            
            show.likes = like.Like(likes_data)
            
            if show.likes.id:
                show.likes.num_likes += 1
            
            all_results.append(show)                                       
                
        print(f"\n\nnum_likes\n{len([show.likes.num_likes for show in all_results if show.likes.num_likes])}\n{sorted([show.id for show in all_results if show.likes.id])}\n\n")                           
        return all_results                                
                       
    @classmethod
    def create_new(cls, data):
        
        query = """
                INSERT INTO shows
                (title, description, release_date, network, posted_by_id)
                VALUES
                (%(title)s, %(description)s, %(release_date)s, %(network)s, %(posted_by_id)s)
                """                               
        result = conn(schema).query_db(query, data)                
        
        print(f"\n\nCreate New Show Result:\n{result}\n\n")
        
        return result
        
    @classmethod
    def update_info(cls, data):
        
        query = """
                UPDATE shows
                SET title = %(title)s,
                description = %(description)s,
                release_date = %(release_date)s,
                network = %(network)s
                WHERE id = %(id)s;
                """        
                
        conn(schema).query_db(query, data)       
        
    @classmethod
    def delete_show(cls, data):
        
        query1 = """     
                DELETE FROM likes
                WHERE show_id = %(id)s;
                """
        query = """     
                DELETE FROM shows
                WHERE id = %(id)s;
                """
        conn(schema).query_db(query1, data)   
        conn(schema).query_db(query, data)  
        
    @staticmethod
    def validate_show(data):     
        
        is_valid = True                       
        
        if len(data["title"]) < 3:  
            flash("You need to give the title for the show")
            is_valid = False
            
        if len(data["network"]) < 3:
            flash("You give the network for the show")            
            is_valid = False             
            
        if not data["release_date"]:
            flash("You give the release_date for the show")            
            is_valid = False            
            
        if len(data["description"]) < 3:
            flash("You need to give the description for the show")            
            is_valid = False                                                   
       
        return is_valid          