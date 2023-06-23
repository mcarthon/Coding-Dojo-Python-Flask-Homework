from flask_app.config.mysqlconnection import connectToMySQL as conn
from flask_app import schema
from flask_app.models import user, show

class Like:
    
    def __init__(self, data):
        
        self.id         = data["id"]
        self.user_id    = data["user_id"]
        self.show_id    = data["show_id"]
        self.num_likes  = 0
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def unlike_show(cls, data):
        
        query = """
                DELETE FROM likes
                WHERE user_id = %(user_id)s
                AND show_id = %(show_id)s;
                """        
                
        conn(schema).query_db(query, data)
        
    @classmethod
    def like_show(cls, data):
        
        query = """
                INSERT INTO likes
                (user_id, show_id)
                VALUES
                (%(user_id)s, %(show_id)s);
                """                                 
        return conn(schema).query_db(query, data)           
        
    @classmethod
    def get_user_likes(cls, data):
        
        query = """
                SELECT *
                FROM likes
                WHERE user_id = %(user_id)s;                
                """       
                
        query_results = conn(schema).query_db(query, data)                      
        
        all_user_likes = []
        
        for like in query_results:
            
            all_user_likes.append(cls(like))
            
        return all_user_likes           
        
    @classmethod
    def get_all_show_likes(cls, data):
        
        query = """
                SELECT *
                FROM likes
                WHERE show_id = %(id)s;
                """        
                
        query_results = conn(schema).query_db(query, data)                
        
        all_show_likes = []
        
        for like in query_results:
            
            all_show_likes.append(cls(like))
            
        return all_show_likes            
        
                              