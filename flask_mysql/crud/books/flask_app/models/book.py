from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import schema

class Book:
    
    def __init__(self, data):
        self.id         = data["id"]
        self.name       = data["name"]
        self.created    = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod    
    def get_all(cls):
        
        query = """
                SELECT *
                FROM books;
                """
        query_results = connectToMySQL(schema).query_db(query)
        
        books = []
        
        for book in query_results:
            books.append(cls(book))
            
        return books
    
    @classmethod
    def get_book(cls, data):
        
        query = """
                SELECT *
                FROM books
                WHERE id = %(id)s;
                """
        
        return cls(connectToMySQL(schema).query_db(query, data)[0])
        
    @classmethod
    def add_book(cls, data):
        
        query = """
                INSERT INTO books
                (name)
                VALUES
                (%(name)s);
                """
        return connectToMySQL(schema).query_db(query, data)
        
    @classmethod
    def get_favs(cls, data):
        
        query = """
                SELECT DISTINCT users.id,
                       users.name,
                       users.created_at,
                       users.updated_at
                FROM users
                JOIN orders
                ON users.id = orders.user_id
                JOIN books
                ON books.id = orders.book_id
                WHERE books.id = %(id)s;
                """
        
        query_results = connectToMySQL(schema).query_db(query, data)
        print(query_results)
        favs = []
        
        for fav in query_results:
            favs.append(fav)
        print(favs)
        return favs
        
    @classmethod
    def find_not_favs(cls, data):
        
        query = """
                SELECT DISTINCT users.id,
                       users.name,
                       users.created_at,
                       users.updated_at 
                FROM users
                WHERE id
                NOT IN (
                    SELECT user_id
                    FROM orders
                    WHERE book_id = %(id)s
                );
                """    
        query_results = connectToMySQL(schema).query_db(query, data)
        
        not_favs = []
        
        for not_fav in query_results:
            not_favs.append(cls(not_fav))
        print(not_favs)
        return not_favs
                
    @classmethod
    def add_to_favs(cls, data):
        
        query = """
                INSERT INTO orders
                (user_id, book_id)
                VALUES
                (%(user_id)s, %(book_id)s);
                """
        result = connectToMySQL(schema).query_db(query, data)
        print(result)
        return result
        
    @classmethod
    def get_user_favs(cls, data):
        
        query = """
                SELECT books.id, 
                       books.name,
                       books.created_at,
                       books.updated_at
                FROM books
                JOIN orders
                ON books.id = orders.book_id
                JOIN users
                ON users.id = orders.user_id
                WHERE users.id = %(id)s;
                """
                
        query_results = connectToMySQL(schema).query_db(query, data)
                
        user_favs = []
        
        for user_fav in query_results:
            user_favs.append(cls(user_fav))
            
        return user_favs