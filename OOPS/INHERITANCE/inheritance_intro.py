"""
"""

class Parent:

    def house(self):

        print("parent class house method")

class Child(Parent): #child inherits parent method

    def  mobile(self):

        print("child class mobile method")

child_instance =Child()

child_instance.mobile()

child_instance.house()



