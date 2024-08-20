import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "practice"
)

sql = conn.cursor()

# INNER JOIN -----------------------------------------
 
# sql.execute("SELECT \
#     order1.o_id AS id, \
#     product.p_nm AS name \
#     FROM order1 \
#     INNER JOIN product ON order1.p_id = product.p_id")


# LEFT JOIN------------------------------------

# sql.execute("select order1.o_status , product.p_nm from order1 left join product on order1.p_id = product.p_id")


# RIGHT JOIN---------------------------------------

sql.execute("select order1.o_id , product.p_nm from order1 right join product on order1.p_id = product.p_id ")
# OUTER JOIN -----------------------------------------

# sql.execute("SELECT \
#     order1.o_id,\
#     product.p_nm \
#     FROM order1 \
    # LEFT OUTER JOIN product ON order1.p_id = product.p_id")


res = sql.fetchall()

for i in res :
    print(i)