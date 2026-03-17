"""
Find leap year
"""
year=int(input("Enter the year :"))

if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
    print(year,"  is a leap year")
    
else:
    print(year,"not a leap year")