from mysql import connector

connection = connector.connect(

    host ="localhost",
    user ="root",
    password = "Password@123",
    database = "vehicle_db"


)

cursor = connection.cursor()

query = """

create table vehicle(
id int auto_increment Primary key,
name varchar(200) not null,
model varchar(200) not null,
running_km int null,
fuel_type enum('petrol','diesel','electric') default 'petrol',
owner_type enum('first_owner','second_owner','third_owner','other') default 'first_owner',
place varchar(50) not null,
owner varchar(200) not null
)
 
"""

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()

print("Table created")
