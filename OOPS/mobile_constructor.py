

class Mobile:


        #constructor (intializing attributes)
    def __init__(self,image,name,price,rating):

        self.image=image

        self.name=name

        self.price=price

        self.rating=rating


    def display(self):

        print(self.name,self.price,self.rating)

mobile_instance1=Mobile("iphone.png","iphone 16",130000,5)

mobile_instance1.display()

        