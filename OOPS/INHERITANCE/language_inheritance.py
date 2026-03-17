"""
"""

class Language:

    def __init__(self,name):

        self.name = name

    def display(self):

        print(self.name)

class Framework(Language):

    def __init__(self,name,fname):

        super().__init__(name)

        self.fname =fname

    def display(self):

        super().display()

        print(self.fname)


frame_instance = Framework("Python","django")

frame_instance.display()




    
        