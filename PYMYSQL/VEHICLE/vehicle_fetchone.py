from mysql import connector

connection = connector.connect(

    host = "localhost",
    user = "root",
    password = "Password@123", 
    database = "vehicle_db"
)

cursor = connection.cursor()

query = "select * from vehicle where id =%s"

data =(4,)

cursor.execute(query,data)

record = cursor.fetchone()

print(record)

cursor.close()

connection.close()


