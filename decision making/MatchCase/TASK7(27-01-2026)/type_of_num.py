"""
Write a program to determine the type of number based on its value.
* Less than 0 → Negative
* Equal to 0 → Zero
* Greater than 0 → Positive
"""

number=int(input("Enter the number :"))

if number<0:

    print("Number is negative")

elif number==0:

    print("Number is equal to zero")

else:

    print("Number is positive")