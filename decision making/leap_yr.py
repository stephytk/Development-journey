"""
check the year is leap year or not
"""

year=int(input("Enter year:"))
if year%4==0:
    print(year,"is a leap year")
else:
    print(year,"not a leap year")