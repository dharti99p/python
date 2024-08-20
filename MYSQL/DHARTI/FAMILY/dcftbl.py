import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "dharti"
)

sql = conn.cursor()

sql.execute("create table family(no int(2), f_nm varchar(30), dob date, mobile_no varchar(10))")