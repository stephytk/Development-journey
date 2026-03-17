"""
Palindrome or not
"""

number=int(input("enter the number:"))#121

number_copy=number

result=0#0

while(number!=0):#121!=0

    l_digit = number%10 #121%10 =>1

    result = result * 10 + l_digit #0*10+1=>1pa

    number = number//10 #121//10 =>12

if number_copy==result:#121==121 True

    print("number is a palindrome")

else:
    print("Not a palindrome")