"""
Method Overriding => Child class redefines the method that is already defined in Parent class.

"""

class Parent:

    def vehicle(self):

        print("Passion pro")


class Child(Parent):


    def vehicle(self):

        print("pulsar")

child_instance = Child()

child_instance.vehicle()