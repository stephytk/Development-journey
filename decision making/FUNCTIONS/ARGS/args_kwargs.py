"""
combined args and kwargs
"""

def calculator(*args,**kwargs):

    #args =(10,20,30)

    #kwargs ={"key":"+"}

    if kwargs.get("key")=="+":

        return sum(args)
    
    if kwargs.get("key")=="*":

        p=1

        for num in args:

            p =p*num

        return p
    
print(calculator(10,20,30,key="+"))

print(calculator(10,20,10,key="*"))








