
#step1:import connector

from mysql import connector

# step2: Establish  a connection connector >connect()

connection = connector.connect(

    host = "localhost",
    user="root",
    password="Password@123"

)

print(connection)


cursor = connection.cursor()

query = "create database py_db"

cursor.execute(query)

connection.commit()

print("completed")




