"""
Factorial of a  number using for loop
"""

number=int(input("Enter the number :"))#6

fact=1 #1

for i in range(1,number+1):

    fact=fact*i#fact=1*1
    
print(f"factorial of {number} is {fact}")#