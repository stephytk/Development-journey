"""
Armstrong number
"""

number=int(input("Enter the number :"))

number_copy=number

result =0

number_len=len(str(number))

while(number!=0):

    last_digit=number%10 

    expo=last_digit**number_len

    result=result+expo

    number=number//10

if number_copy==result:
        
        print("Armstrong number")
else:
        print("Not an armstrong number")
