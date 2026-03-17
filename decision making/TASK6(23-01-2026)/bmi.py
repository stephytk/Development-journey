"""
 Body Mass Index (BMI) Category

Input: bmi
Conditions:

If bmi < 18.5 → Underweight

If bmi between 18.5 and 24.9 → Normal Weight

If bmi between 25 and 29.9 → Overweight

If bmi ≥ 30 → Obese
"""


weight_in_kg=float(input("Enter the weight :"))

height_in_cm=float(input("Enter the height :"))

height_in_m= height_in_cm/100 
print(height_in_m)

bmi=weight_in_kg/(height_in_m**2)
bmi=round(bmi)
print(bmi)

if bmi<18.5:
    print("Underweight")
elif bmi<25:
    print("Normal weight")

elif bmi<30:
    print("Overweight")
else:
    print("Obese")