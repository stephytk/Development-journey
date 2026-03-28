from mysql import connector

connection = connector.connect(

    host = "localhost",
    user = "root",
    password = "Password@123"
)

cursor = connection.cursor()

query ="create database vehicle_db"

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()

print("Database created")

