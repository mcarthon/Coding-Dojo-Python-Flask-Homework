from flask_app.config.mysqlconnection import connectToMySQL as conn
from flask_app import schema
from flask_app.models import user, painting

class Purchase:
    
    def __init__(self, data):
        
        self.id          = data["id"]
        self.user_id     = data["user_id"]
        self.painting_id = data["painting_id"]
        self.created_at  = data["created_at"]
        self.updated_at  = data["updated_at"]
        
        
    @classmethod
    def get_purchases(cls, data):
        
        query = """
                SELECT *
                FROM purchases
                WHERE painting_id = %(id)s
                GROUP BY painting_id;
                """
                
        purchases = [cls(result) for result in conn(schema).query_db(query, data)]                                                              
        
        return purchases
        
        
    @classmethod
    def get_user_purchases(cls, data):
        
        query = """
                SELECT *
                FROM users AS buyer
                JOIN purchases
                ON buyer.id = purchases.user_id
                JOIN paintings
                ON purchases.painting_id = paintings.id
                JOIN users AS seller
                ON seller.id = paintings.author_id
                WHERE buyer.id = %(user_id)s; 
                """        
        query_results = conn(schema).query_db(query, data)
        
        
        
        print(f"\n\nquery_results:\n{query_results}\n\n")

        all_user_purchases = []   
        
        for result in query_results:
        
            buyer_data = dict(
                
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
            
            purchases_data = dict(
                
                id          = result["purchases.id"],
                user_id     = result["user_id"],
                painting_id = result["painting_id"],
                created_at  = result["purchases.created_at"],
                updated_at  = result["purchases.updated_at"]
                
            )    
            
            seller_data = dict(
                
                id         = result["seller.id"],
                first_name = result["seller.first_name"],
                last_name  = result["seller.last_name"],
                email      = result["seller.email"],
                password   = result["seller.password"],
                created_at = result["seller.created_at"],
                updated_at = result["seller.updated_at"]
                
            )
            
            purchase = cls(purchases_data)
            
            purchase.painting = painting.Painting(painting_data)
            
            purchase.buyer = user.User(buyer_data)
            
            purchase.seller = user.User(seller_data)
            
            all_user_purchases.append(purchase)                        
                                                
        return all_user_purchases
            
    @classmethod            
    def purchase_painting(cls, data):
        
        buy_query = """
                INSERT INTO purchases
                (user_id, painting_id)
                VALUES
                (%(user_id)s, %(painting_id)s);
                """
        conn(schema).query_db(buy_query, data)
        
        quantity_query = """
                         UPDATE paintings
                         SET quantity = %(quantity)s                       
                         WHERE id = %(painting_id)s; 
                         """  
                         
        conn(schema).query_db(quantity_query, data)  
        
        print("Item has been bought")                                     
                     