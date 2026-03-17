class Shape:

    def area(self,*args):

        if len(args)==1:

            r=args[0]

            print("Area of a circle",3.14*r**2)

        elif len(args)==2:

            l=args[0]

            b=args[1]

            print("Area of rectangle",l*b)

        elif len(args)==3:

            l=args[0]
            b=args[1]
            h=args[2]

            print("Area of cuboid",l*b*h)

sh =Shape()

sh.area(10)

sh.area(10,20)

sh.area(10,20,30)
   