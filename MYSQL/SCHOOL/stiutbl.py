import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "school"
)

sql = conn.cursor()

sinsert = "insert into teacher values(%s, %s, %s, %s)"
n = int(input("How many insert data your teacher table -> "))

for i in range(n):
    id = input("Enter teacher id : ")
    name = input("Enter the teacher name : ")
    standard = input("Enter the teacher standard learn : ")
    dob = input("Enter the teacher birth date : ")
    data = (id,name,standard,dob)
    sql.execute(sinsert, data)
    print(sql.rowcount, "data insert sucessfully.")

conn.commit()
