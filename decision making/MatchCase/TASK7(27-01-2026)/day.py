"""
Write a program to display day type based on day number.
* 1–5 → Working day
* 6–7 → Weekend
"""
day=int(input("Enter the day :"))

if day>=1 and day<=5 :

    print ("Working day")

elif day==6 or day==7:

    print("Weekend")

else:

    print("Invalid day")





