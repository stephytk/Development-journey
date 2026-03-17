"""
Find Fastingbloodsugar
"""

fasting_blood_sugar=int(input("Enter the blood sugar :")) #90

if fasting_blood_sugar<100: #90<100
    print("Normal") #Normal

elif fasting_blood_sugar<125:
    print("Normal")

else:
    print("Diabetic")
