"""
5. Exam Result System
------------------------------------
Task:
- Ask for roll number

If roll number exists:
    - Ask for marks
    - If marks ≥ 40:
        "Pass"
    - Else:
        "Fail"
Else:
    "Invalid roll number"
"""
student_roll=12
roll_no=int(input("Enter the roll number :"))

if roll_no==student_roll:
    marks=int(input("Enter the marks :"))

    if marks>=40:
        print("pass")
    else:
        print("Fail")

else:
    print("Inavalid roll number")

