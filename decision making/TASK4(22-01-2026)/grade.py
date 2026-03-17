"""
Write a Python program to display the grade of a student using the following rules:

Marks ≥ 90 → Grade A
Marks ≥ 75 → Grade B
Marks ≥ 50 → Grade C
Otherwise → Fail
"""
mark=int(input("Enter mark:"))# 80
if mark>=90:#80>=90 False
    print("Grade A")
elif mark>=75:#80>=75  true
    print("Grade B") # Grade B
elif mark>=50:
    print("Grade C")
else:
    print("Fail")