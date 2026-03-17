"""
Exercise Duration

Input: exercise_minutes
Conditions:

If minutes < 30 → Insufficient Exercise

If minutes between 30 and 60 → Good Exercise

If minutes > 60 → Intense Exercise

"""

exercise_minutes=int(input("Enter the minutes:")) #26

if exercise_minutes<30: #26<30 True
    print("Insufficient Exercise") #Insufficient exercise

elif exercise_minutes<60:
    print("Good Exercise")

else:
    print("Intense Exercise")



