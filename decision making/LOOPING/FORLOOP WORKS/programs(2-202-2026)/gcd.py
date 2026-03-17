
"""
To display the GCD
"""

num1=int(input("Enter the number :"))

num2=int(input("Enter the number2 :"))

if num1<num2:

    smallest=num1
else:
    smallest=num2

gcd=1

for i in range(1,smallest+1):

        if num1%i==0 and num2%i==0: #10%1==0
                 
            gcd=i

print(gcd)



