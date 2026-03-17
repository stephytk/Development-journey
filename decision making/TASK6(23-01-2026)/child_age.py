"""
Age Group Classification

Input: age
Conditions:

If age < 13 → Child

If age between 13 and 19 → Teenager

If age between 20 and 59 → Adult

If age ≥ 60 → Senior Citizen

"""

age=int(input("Enter the age :")) #12

if age<13: #12<13 True
    print("Child") #Child

elif age<19:
    print("Teenager")

elif age<59:
    print("Adult")

else:
    print("Senior Citizen")