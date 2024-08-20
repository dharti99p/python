import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "school"
)

sql = conn.cursor()

sql.execute("create table teacher(t_id int(3), t_nm varchar(60), std int(2), dob date)")