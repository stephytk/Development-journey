from mysql import connector

class BookListCreateRetrieveUpdateDelete:

    def __init__(self):

        try:

            self.connection = connector.connect(
            host = "localhost",
            user = "root",
            password = "Password@123",
            database = "book_db"

            )

            self.cursor = self.connection.cursor()

            print("database connection ok")
        
            
        except Exception as e:

            print(e)

    def list(self):


        query = "select * from book"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        if records:

            for row in records:

                print(row)
        else:

            print("no records found")
       
    def create(self,title=None,author=None,price=None,pulisher=None,genre=None,year=None):

        query = """
                insert into book(title,author,price,publisher,genre,year) values(%s, %s,%s,%s,%s,%s)

                """
        
        data =(title,author,price,pulisher,genre,year)

        self.cursor.execute(query,data)

        self.connection.commit()

        print("record inserted")

    def retrieve(self,id=None):

        query = "select * from book where id = %s"

        data = (id,)

        self.cursor.execute(query,data)

        record = self.cursor.fetchone()

        print(record)

    def delete(self,id=None):

        query =" delete from book where id =%s"

        data =(id,)

        self.cursor.execute(query,data)

        self.connection.commit()

        print("1 row deleted")

    # def update(self,price=None,year=None,id=None):

    #     query= " update  book set price=%s,year=%s where id=%s"

    #     data =(price,year,id)

    #     self.cursor.execute(query,data)

    #     self.connection.commit()

    #     print("record updated")




        
book_instance = BookListCreateRetrieveUpdateDelete()

# book_instance.create(title="randamoozham",author="MT",price=500,pulisher="xyz",genre="fiction",year=1984)
# book_instance.create(title=" Julius Caesar",author="William Shakespeare",price=700,pulisher="abc",genre="mystery",year=1980)

# book_instance.retrieve(id=1)

# book_instance.delete(id=1)

# book_instance.update(price=800,year=1978,id=7)

book_instance.list()



