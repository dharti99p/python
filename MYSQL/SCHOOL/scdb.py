import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
)

sql = conn.cursor()

sql.execute("create database school ")