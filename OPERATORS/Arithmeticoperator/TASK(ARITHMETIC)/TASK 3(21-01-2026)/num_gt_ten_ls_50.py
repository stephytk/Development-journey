"""
Read a number and print the result of number > 10 and number < 50.

"""
number=(int(input("Enter the number :"))) #Enter the number : 40
if(number>10 and number<50):#40>10 and 40<50 =>True
    print("number is greater than 10 and less than 50") #number is greater than 10 and less than 50
else:
    print("not greater than 10 and less than 50")