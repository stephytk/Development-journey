"""
Write a Python program to print each digit of a number separately using a while loop.
"""

number=1234 #1234

while(number!=0): #1234!=0 

    last_digit=number%10 #1234%1000 => 4 123%10 => 3 12%10=>2 1%10=>1

    number=number//10 #1234//10 =>123  123//10=>12 12//10=> 1

    print(last_digit) # 4 3 2 1
   

   