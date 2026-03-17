"""
Display perfect number or not
"""

number=int(input("Enter the number :"))

sum=0

for i in range(1,number):

    if number%i==0:

        sum=sum+i

print("perfect number" if number==sum else "not a perfect number")