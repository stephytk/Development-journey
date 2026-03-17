"""
Input: systolic_bp
    Conditions:
    If bp < 120 → Normal
    If bp between 120 and 129 → Elevated
    If bp between 130 and 139 → High BP Stage 1
    If bp >= 140 → High BP Stage 2
"""

systolic_bp=int(input("Enter the blood pressure :"))#119

if systolic_bp<120: #119<120
    print("Normal")# Normal

elif systolic_bp<129:
    print("Elevated")

elif systolic_bp<139:
    print("High BP Stage 1")

else:
    print("High Bp Stage 2")
