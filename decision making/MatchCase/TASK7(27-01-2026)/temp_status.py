"""
Write a program to check temperature status.
* Below 20 → Cold
* 20–30 → Normal
* Above 30 → Hot
"""

temperature =int(input("enter the temperature :"))

if temperature<20:

    print("Cold")

elif temperature<=30 :

    print("Normal")

elif temperature>30:

    print("Hot")

else:

    print("Invalid")
