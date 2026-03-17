"""
Prime number or not
"""

number=int(input("Enter the number :"))#7

is_prime=True# true

for i in range(2,number):#[2,6]

    if number%i==0:#7%2==0

        is_prime=False

        break
print(is_prime)


#with function

def prime(num):

    is_prime = True

    for i in range(2,num):

        if num %i==0:

            is_prime =False

            break

    return is_prime

num = int(input("enter the number :"))

result = prime(num)

print(result)


#with class

class Prime:

    def prime(self,num):

        is_prime= True

        for i in range(2,num):

            if num %i ==0:

                is_prime =False

        print(is_prime)


p = Prime()

num = int(input ("Enter the number :"))

p.prime(num)
        


   











