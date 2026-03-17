"""
Write a program using match–case to check whether a given number is positive, negative, or zero.
"""

number=int(input("Enter the number :"))

match number:
    case 0:

        print("number is equal to zero")


    case _ if number > 0: 
        
        print("Number is positive")

    case _ if number<0:
        
        print("Number is negative")

    case _:

        print("Inavlid")
