

class Biriyani():   

    name:str

    category:str

    price:int

        #initilaize attribute,instance variable
    def __iniit__(self,name,category,price):


        self.name=name

        self.category=category

        self.price=price

    def display(self):

        print(self.name,self.category,self.price)

biriyani_instance1=Biriyani("Chicken Biriyani","Nonveg",250)

biriyani_instance2=Biriyani("Paneer","Veg",200)

biriyani_instance1.display()

biriyani_instance2.display()

        



