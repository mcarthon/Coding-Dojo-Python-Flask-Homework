from flask_app.config.mysqlconnection import connectToMySQL as conn
from flask_app import schema

class Friendship:
    
    def __init__(self, data):
        
        self.id         = data["id"]
        self.user_id    = data["user_id"]
        self.friend_id  = data["friend_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def get_all(cls):
        
        query = """
                SELECT 
                       users_a.first_name AS user_first_name,
                	   users_a.last_name AS user_last_name,
                       users_b.first_name AS friend_first_name,
                       users_b.last_name AS friend_last_name
                FROM users AS users_a
                JOIN friendships
                ON users_a.id = friendships.user_id
                JOIN users AS users_b
                ON users_b.id = friendships.friend_id;
                """
                
        query_results = conn(schema).query_db(query)                
        
        friendships = []
        
        print(f"\n\nGet All Friendships:\n{query_results}\n\n")
        
        for friendship in query_results:
            friendships.append(friendship)
            
        return friendships    
        
    @classmethod
    def add_new(cls, data):
        
        query = """
                INSERT INTO friendships
                (user_id, friend_id)
                VALUES
                (%(user_id)s, %(friend_id)s);
                """                           
        conn(schema).query_db(query, data)                     
            
    @staticmethod
    def validate_friendship(data):
        
        query = """
                SELECT * 
                FROM friendships
                WHERE user_id = %(user_id)s
                AND friend_id = %(friend_id)s;
                """                           
                
        if conn(schema).query_db(query, data):
            return False
            
        return True            