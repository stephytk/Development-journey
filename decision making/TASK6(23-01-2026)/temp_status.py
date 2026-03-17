"""
1. Body Temperature Status

Input: body_temperature (°C)
Conditions:

If temperature < 36 → Low Body Temperature

If temperature between 36 and 37.5 → Normal

If temperature > 37.5 → Fever

"""

body_temperature=float(input("Enter the body temperature :")) #36.5

if body_temperature<36:#36.5<36 False
    print("Low Body Temperature")

elif body_temperature<37.5:#36.5<37.5 True
    print("Normal") # Normal

else:
    print("Fever")