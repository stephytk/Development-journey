"""
Input: oxygen_level
    Conditions:
    If oxygen_level >= 95 → Normal
    If oxygen_level between 90 and 94 → Mild Concern
    If oxygen_level < 90 → Critical

"""
oxygen_level=int(input("Enter oxygen level :"))
if oxygen_level>=95:
    print("normal")

elif oxygen_level<=90 and oxygen_level<94:
    print("Mild Concern")
else:
    print("Critical")