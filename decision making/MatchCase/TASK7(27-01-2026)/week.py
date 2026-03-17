"""
Write a Python program using match–case to display the day of the week based on a number (1–7).
"""

day=int(input("Enter the day:"))

match day:

    case 1:
        print("Sun")
    case 2:
        print("Mon")
    case 3:
        print("Mon")
    case 4:
        print("Wed")
    case 5:
        print("Thur")
    case 6:
        print("Fri")
    case 7:
        print("Sat")
    case _:
        print("Invalid day")