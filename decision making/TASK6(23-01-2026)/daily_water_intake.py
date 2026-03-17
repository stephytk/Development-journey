"""
Daily Water Intake

Input: liters
Conditions:

If intake < 2 → Dehydrated

If intake between 2 and 3 → Adequate Intake

If intake > 3 → Excess Intake
"""

litre=int(input("Enter the litre :")) #2

if litre<2: #2<2  False
    ("Dehydrated")

elif litre<3: #2<3 True
    print("Adequate Intake") #Adequate intake

else:
    print("Excess Intake")