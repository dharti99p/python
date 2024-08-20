import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "dharti"
)

sql = conn.cursor()

# sql.execute("insert into custo values('', 'dharti miroliya', 'surat'),('', 'ami miroliya', 'bharuch'),('', 'parth ghantala', 'haidrabad'),('', 'aniket miroliya','banglor')")
# sql.execute("delete from custo where name = 'dharti miroliya'")
sql.execute("insert into custo values('','alka kubhani','vadodra')")


conn.commit()