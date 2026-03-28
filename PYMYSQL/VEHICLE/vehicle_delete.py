from mysql import connector

connection = connector.connect(

    host = "localhost",
    user = "root",
    password = "Password@123", 
    database = "vehicle_db"
)

cursor = connection.cursor()

query = "delete from vehicle where id=%s"

data = (4,)

cursor.execute(query,data)

connection.commit()

cursor.close()

connection.close()

print("1 row deleted")
