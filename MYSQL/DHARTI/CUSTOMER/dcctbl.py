import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "dharti"
)

sql = conn.cursor()

# sql.execute("CREATE TABLE customer(id INT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

sql.execute("CREATE TABLE custo(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")