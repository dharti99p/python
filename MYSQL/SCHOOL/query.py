import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "school"
)

sql = conn.cursor()

# sql.execute("select t_id, dob from teacher where 9 < t_id")

sql.execute("select * from teacher where t_nm like '%y%'")

# sql.execute("select * from teacher where t_nm like '%n'") # last character n

# sql.execute("select * from teacher where t_nm like 'n%'")# first character n

# sql.execute("select * from teacher order by t_nm")

# sql.execute("select * from teacher order by t_nm desc")

# sql.execute("delete from teacher where t_nm = 'panthi'")
# conn.commit()



# fetch = sql.fetchone()

# for i in fetch :
#     print(i, type(i))


# user fetch data--------------------------

# squery = "select * from teacher where t_nm = %s"

# item = input("Enter the name : ")
# itemfinal = (item, )
# sql.execute(squery, itemfinal)
# fetch = sql.fetchall()

# for i in fetch :
#     print(i, type(i))
    #   print(sql.rowcount, "Data inserted successfully.")



# user how many data fetch -----------------

# squery = "select * from teacher where t_nm = %s"

# n = int(input("How many Data fetch : "))

# for i in range(n) :
#     item = input("Enter the Name : ")
#     itemfinal = (item, )
#     sql.execute(squery, itemfinal)
#     fetch = sql.fetchall()

#     for i in fetch :
#         print(i, type(i))
#         print(sql.rowcount,"Data inserted successfully.")



# user delete ---------------------

# squery = "delete from teacher where t_nm = %s"
# item = input("enter the name : ")
# itemfinal = (item, )
# sql.execute(squery, itemfinal)

# conn.commit()



# user how many delete data ------------------------

# squery = "delete from teacher where t_nm = %s"
# n = int(input("How many data delete : "))

# for i in range(n) :
#     item = input("Enter the name : ")
#     itemfinal = (item, )
#     sql.execute(squery,itemfinal)
#     print(sql.rowcount, "Data Deleted Successfully.")

# conn.commit()



# update data--------------------------

# sql.execute("update teacher set t_id = 3 where t_nm = 'nayan sir'")
# conn.commit()
# print(sql.rowcount, "Data updated successfully.")



# update user-----------------------------

# squery = "update teacher set t_id = %s where t_nm = %s"
# id = input("Enter the new id number : ")
# name = input("Enter the name : ")
# final = (id, name, )

# sql.execute(squery, final)
# conn.commit()



# update how many data user update --------------------

# squery = "update teacher set t_id = %s where t_nm = %s"
# n = int(input("How many data updated : "))

# for i in range(n) : 
#     id = input("Enter the new id number : ")
#     name = input("Enter the change id for name : ")
#     final = (id, name)

#     sql.execute(squery, final)
#     print(sql.rowcount, "Data Updated Successfully.")

conn.commit()