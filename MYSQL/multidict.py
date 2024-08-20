import mysql.connector
import json

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "uprofile"
)

sql = conn.cursor()

sql.execute("SELECT * FROM datafamily")
results = sql.fetchall()
data=results[0][1].decode()
data_dict = json.loads(data)

lat = data_dict['state']

print(lat)
