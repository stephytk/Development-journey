"""
Hydration Status (Urine Color Scale)

Input: urine_color (1–8 scale)
Conditions:

If color between 1 and 3 → Well Hydrated

If color between 4 and 6 → Mild Dehydration

If color between 7 and 8 → Severe Dehydration

"""


urine_color =int(input("Enter the Urine Color :"))#8

if urine_color<3: #8<3 False
    print("Well Hydrated") 

elif urine_color<6: #8<6 False
    print("Mild Dehydration")

else:
    print("Severe Dehydration") #Dehydration
