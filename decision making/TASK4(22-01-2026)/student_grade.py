"""
Read three marks m1,m2,m3 each out of 50
find the total
Display A if total >140
"""

m1=int(input("Enter the mark1:"))
m2=int(input("Enter the mark2 :"))
m3=int(input("Enter the mark3:"))
total=m1 + m2 + m3

if total>140:
    print("A")
elif total>130:
    print("B")
elif total>120:
    print("C")
else:
    print("Fail")