"""
BMI calculation
"""
weight_in_kg=int(input("Enter the weight:"))

height_in_cm=int(input("Enter the height:"))

height_in_m=height_in_cm/100

bmi=weight_in_kg/(height_in_m**2)

bmi=round(bmi)
print(bmi)
if bmi<20:
    print("Underweight")
elif bmi<25:
    print("Normal")
elif bmi<30:
    print("Overweight")
else:
    print("Obese")