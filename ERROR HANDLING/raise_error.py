

"""
Raise => for creating custom error
"""

age=int(input("Enter age"))


if age>18:

    raise Exception("invalid age")
else:
    print("access granted")