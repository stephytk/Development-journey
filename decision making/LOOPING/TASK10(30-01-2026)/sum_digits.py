"""
10.Write a program to find the sum of digits of a given number using a while loop.
"""

number=5678


sum=0

while(number!=0):#1!=5678

    last_digit=number%10 #5678%10 =>8 7 6 5



    sum=sum+last_digit# 0+5 5+6 11+ 7

    number=number//10 #5678//10 =>567
print(sum)





    

 

