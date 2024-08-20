import mysql.connector

__cnx = None

def get_sql_connection() :
    global __cnx
    
    if __cnx is None :
        cnx = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "gs"
            )
    return cnx