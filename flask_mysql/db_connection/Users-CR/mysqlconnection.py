# The cursor is the object we use to interact with the database
import pymysql.cursors
import credentials

# This class will give us an instance of a connection to our database
class MySQLConnection:

    def __init__(self, db):
        
        # Change the user and password as needed 
        connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = credentials.password,
            db = db,
            charset = "utf8mb4",
            cursorclass = pymysql.cursors.DictCursor,
            autocommit = False
        )
        
        # establish the connection to the database
        self.connection = connection
        
    # Create a method that queries the database
    def query_db(self, query:str, data:dict = None):
        with self.connection.cursor() as cursor:
            try:
                # Mogrify - Returns the exact 
                # string that would be sent to the 
                # database by calling the execute() method.
                # It preps the query for execution
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                
                cursor.execute(query)
                
                # str.find returns the lowest index in
                # the string where the substring is found
                # if it is not found it returns -1
                if query.lower().find("insert") > -1:
                # INSERT queries return the ID number of 
                # the row that was inserted into the table
                    self.connection.commit()
                    return cursor.lastrowid
                    
                elif query.lower().find("select") > -1:
                # SELECT queries will return the data in
                # a list of dictionaries
                    return cursor.fetchall()
                    
                else:
                    # UPDATE and DELETE queries return None
                    self.connection.commit()
                    
            except Exception as e:
                print("Query failed", e)
                return False
                
            finally:
                # close the connection
                self.connection.close()
                
# connecttoMySQL receives the database we're using and uises it to create an
# instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)                   