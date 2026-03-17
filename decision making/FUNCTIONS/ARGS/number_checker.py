

def number_checker(*args,**kwargs):

    if kwargs.get("type")=="odd": #type=kwargs.get("type"), if type=="odd"

        odds =[num for num in args if num%2!=0]

        return len(odds)
    
    if kwargs.get("type")=="even":

        even =[num for num in args if num%2==0]

        return len(even)
    
    if kwargs.get("type")=="positive":

        positive =[num for num in args if num>0]

        return len(positive)
    
    if kwargs.get("type")=="negative":

        negative =[num for num in args if num<0]

        return len(negative)


print(number_checker(10,12,13,type="odd"))

print(number_checker(10,12,13,type="even"))

print(number_checker(10,12,13,type="positive"))

print(number_checker(10,12,13,-14,-20,type="negative"))







    