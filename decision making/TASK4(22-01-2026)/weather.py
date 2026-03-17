"""
Write a Python program to display weather conditions based on temperature:

Above 30 → Hot
20 to 30 → Warm
Below 20 → Cold
"""

temperature=int(input("Enter the temperature :"))#28
if temperature>30:#28>30 False
    print("Hot")
elif (temperature >20) and (temperature<30):#28>20 (True) and 28<30 (True)
    print("Warm")
elif temperature<2:
    print("Cold")