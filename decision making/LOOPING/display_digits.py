"""
Display digits
floor
"""

number=int(input("Enter the number:")) #123

while(number!=0):#123!=0

    last_digit=number%10  #123%10 =>3  12%10 =>2

    print(last_digit) #3 2

    number=number//10 #number=123//10 =>12 , 12//10 => 1

