#write a  program to find the bmi(bodymassindex)
#Equation=(bmi=weight_in_kg/(height_in_meter)^2)

height_in_cm=186 #height in cm=186
weight_in_kg=77 #weight in kg=77
height_in_m=height_in_cm/100 #height_in_m=186/100
bmi=weight_in_kg/(height_in_m**2)#bmi=77/186/100**2
print(bmi)