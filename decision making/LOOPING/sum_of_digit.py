"""
Sum of digits
number=1234
"""

number=1234 #1234
sum=0

while(number!=0):#1234!=0

    last_digit=number%10 #1234%10=>4

    sum=sum+last_digit

    number=number//10
print(sum)  

