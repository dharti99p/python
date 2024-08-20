import mysql.connector

conn  = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    # database = "dharti"
)

sql = conn.cursor()

sql.execute("create database dharti")

# sql.execute("show databases")
# for i in sql :
#     print(i)