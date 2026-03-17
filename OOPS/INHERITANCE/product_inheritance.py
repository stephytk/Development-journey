"""
Brand => name

product => title,price
"""

class Brand:

    def __init__(self,name):

        self.name= name

    def display(self):

        print(self.name)
 

class Product(Brand):

    def __init__(self, name,title,price):
        super().__init__(name)

        self.title = title

        self.price =price

    def display(self):
        super().display()

        print(self.title,self.price)

pro_instance1 = Product("Apple","Mobile",100000)

pro_instance1.display()

pro_instance2 = Product("HP","Laptop",75000)

pro_instance2.display()

pro_instance3 = Product("Rolex","Watch",60000)

pro_instance3.display()




        
