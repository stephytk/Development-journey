

class GrandParent:

    def properties(self):

        print("Grandparent property method")

class Parent(GrandParent):

    def house(self):

        print("parent house method")

class Child(Parent):

    pass

child_instance = Child()

child_instance.house()
child_instance.properties()

