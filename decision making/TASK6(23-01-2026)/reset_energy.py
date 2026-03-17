"""
Resting Energy Level

Input: energy_score (1–10)
Conditions:

If score between 1 and 3 → Low Energy

If score between 4 and 7 → Moderate Energy

If score between 8 and 10 → High Energy

"""
energy_score=int(input("Enter the energy score :"))

if energy_score<3:
    print("Low energy")

elif  energy_score<7:
    print("Moderate energy")

else:
    print("High energy")