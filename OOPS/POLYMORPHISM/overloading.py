

class Calculator:

    def add(self,n1,n2):

        return n1+n2
    
    def add(self,n1,n2,n3):

        return n1+n2+n3
    
    def add(self,n1,n2,n3,n4):

        return n1+n2+n3+n4
    
cal_instance= Calculator()

print(cal_instance.add(10,20,30,40)) #only last value will access

print(cal_instance.add(10,20,30)) #error


    
    
    

