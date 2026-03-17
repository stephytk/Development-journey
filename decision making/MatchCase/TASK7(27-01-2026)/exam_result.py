"""
Write a program to determine exam result category.
* Marks ≥ 90 → Distinction
* Marks ≥ 60 → First class
* Marks ≥ 40 → Pass
* Below 40 → Fail


"""

mark=int(input("Enter the mark :"))


if mark>=90:

    print("Distinction")

elif mark>=60:

    print("First class")

elif mark>=40:

    print("Pass")

else:

    print("Fail")


