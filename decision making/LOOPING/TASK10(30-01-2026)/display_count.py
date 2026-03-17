"""
number=1234
display count of digits
"""

number=1234 #1234



count=0 #0

while(number!=0):#1234!=0 

    last_digit=number%10 #1234%10 => 4 123%10=>3


      
    count=count+1 #count= 0+1 =>1 2 3 4

    number=number//10 #number=1234//10 =>123

print(count)#4
