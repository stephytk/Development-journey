weight_in_kg=float(input("Enter the weight :"))
height_in_cm=float(input("Enter the height :"))
height_in_m=height_in_cm/100
bmi=weight_in_kg/(height_in_m**2) #60/(156**2)
bmi=round(bmi,2)
print(bmi)

if bmi<18.5:
    print("underweight")
elif bmi<25:
    print("Normal")

elif bmi<30:
    print("Overweight")
else:
    print("obese")
