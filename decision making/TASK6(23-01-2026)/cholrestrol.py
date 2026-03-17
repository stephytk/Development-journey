"""
 Cholesterol Level Check

Input: cholesterol
Conditions:

If cholesterol < 200 → Desirable

If cholesterol between 200 and 239 → Borderline High

If cholesterol ≥ 240 → High Cholesterol

"""
cholesterol=int(input("Enter the cholestrol :")) #250

if cholesterol<200: #250<200 False
    print("Desirable")

elif cholesterol<239: #250<239 false
    print("Borderline High")

else:
    print("High cholestrol") #High Cholestrol