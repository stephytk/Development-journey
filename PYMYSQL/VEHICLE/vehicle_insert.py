from mysql import connector

connection = connector.connect(

    host = "localhost",
    user = "root",
    password="Password@123",
    database = "vehicle_db"


)
cursor = connection.cursor()

query ="""

insert into vehicle(name,model,running_km,fuel_type,owner_type,place,owner) values (%s,%s,%s,%s,%s,%s,%s)

"""
data = ('Car D', 'BMW', 60000, 'Petrol', 'second_owner', 'Kochi', 'Rahul')

cursor.execute(query,data)

connection.commit()

cursor.close()

connection.close()

print("Data inserted")