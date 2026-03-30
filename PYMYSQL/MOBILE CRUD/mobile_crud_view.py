from mysql import connector

class MobileListCreateRetrieveUpdateDelete():

    def __init__(self):
        
        self.connection = connector.connect(

            host ="localhost",
            user = "root",
            password = "Password@123",
            database = "mobile_db"

        )

        self.cursor = self.connection.cursor()

        print("database connected")
    
    def list(self):


        query = "select * from mobile"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        if records:

            for row in records:

                print(row)

        else:

            print("record not found")

    def create(self,title=None,brand=None,specs=None,price=None):

        query= """
                insert into mobile (title,brand,specs,price) values(%s,%s,%s,%s)
            """
        

        data = (title,brand,specs,price)

        self.cursor.execute(query,data)

        self.connection.commit()

        print("value inserted")

    def retrieve(self,id=None):

        query ="select * from mobile where id =%s"

        data = (id,)

        self.cursor.execute(query,data)

        record = self.cursor.fetchone()

        print(record)

    def delete(self,id=None):

        query = "delete from mobile where id =%s"

        data =(id,)

        self.cursor.execute(query,data)

        self.connection.commit()

        print("Record deleted")

mobile_instance = MobileListCreateRetrieveUpdateDelete()

# mobile_instance.create(title= 'Galaxy S23',brand= 'Samsung', specs='Snapdragon Android 13, 8GB RAM, 128GB Storage', price=75000)
# mobile_instance.create(title= 'iPhone 14',brand= 'Apple',specs= 'A15 Bionic, iOS 16, 6GB RAM, 128GB Storage',price= 79900)
# mobile_instance.create(title='Redmi Note 12',brand= 'Xiaomi', specs='Snapdragon 4, Android 12, 6GB RAM, 128GB Storage', price=18000)
# mobile_instance.create(title='OnePlus 11',brand='OnePlus',specs= 'Snapdragon 8 , Android 13, 8GB RAM, 256GB Storage',price= 56000),
# mobile_instance.create(title='Vivo V27',brand= 'Vivo',specs= 'Dimensity 7200, Android 13, 8GB RAM, 128GB Storage',price= 32000)

# mobile_instance.retrieve(id=4)

mobile_instance.delete(id=2)

mobile_instance.list()