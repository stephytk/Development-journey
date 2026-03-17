

class Shape:

    def area(self):

        print("calculating the area of shape")

class Square(Shape):

    def __init__(self,side):

        self.side = side

    def area(self):

        print("Area of a square",self.side **2)

class Rectangle(Shape):

    def __init__(self,l,b):

        self.l = l

        self.b = b
        
    def area(self):

        print("Area of rectangle",self.l * self.b)
        

square_instance= Square(4)

square_instance.area()

rect_instance = Rectangle(4,10)

rect_instance.area()
       

   