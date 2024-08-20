import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "school"
)

# print(conn)

sql = conn.cursor()
s = sql.execute("insert into student values (2, 'mitesh', 1, 'B'),(3, 'aniket', 2, 'C')")
conn.commit()
# for i in sql : 
#     print(i)