import mysql.connector

conn = mysql.connector.connect(
    host = "localhost" ,
    user = "root", 
    password = "",
    database = "dharti"
)

sql = conn.cursor()

sql.execute("insert into family values(2, 'Sangitaben', '1978-10-10', '9979014656'),(3, 'Ami', '1999-01-24', '9512270896'),(4, 'Dharti', '2001-01-31', '9712527697'),(5, 'Aniket', '2004-11-23', '9104120896'),(6, 'Mit', '2005-11-23', '9023855171'),(7, 'Parth', '1999-10-10', '8140416981')")

conn.commit()