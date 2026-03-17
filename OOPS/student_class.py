


class Student:

    name:str

    course:str

    rollno:int


    def __init__(self,name,course,rollno):

        self.name=name

        self.course=course

        self.rollno=rollno

    def display(self):

        print(self.name,self.course,self.rollno)

student_instance1=Student("Rahul","BCA",12)

student_instance1.display()


student_instance2=Student("Ram","MCA",14)

student_instance2.display()




