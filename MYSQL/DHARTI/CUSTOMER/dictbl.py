import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "dharti"
)

sql = conn.cursor()

# sql.execute("insert into customer values(1, 'ankita', 'varachha'),(2, 'payal', 'nana varachha'), (3, 'vrushti', 'jakatnaka'),(4, 'kanika','kamrej'),(5, 'nirali', 'velnja')")
# sql.execute("insert into customer values('', 'kinjal', 'parvat patiya')")

conn.commit()