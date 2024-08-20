import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "school"
)

sql = conn.cursor()

sinsert = "insert into teacher values (%s, %s, %s, %s)"
val = [(1, 'ayushi', 10, '2001-02-10'),(2, 'kiran', 12, '2002-09-29'),(3, 'panthi', 3, '2004-11-23')]

sql.executemany(sinsert, val)

conn.commit()

print(sql.rowcount, "data inserted sucessfully")