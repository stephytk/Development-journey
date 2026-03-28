from mysql import connector

connection = connector.connect(

    host = "localhost",
    user = "root",
    password = "Password@123", 
    database = "vehicle_db"
)

cursor = connection.cursor()

query = "update vehicle set model=%s,owner_type=%s  where id =%s" 

data = ("KIA","second_owner",1)

cursor.execute(query,data)

connection.commit()

cursor.close()

connection.close()

print("Data Updated")