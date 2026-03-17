"""
 Screen Time Health Check

Input: screen_hours
Conditions:

If screen_hours < 2 → Healthy Usage

If screen_hours between 2 and 5 → Moderate Usage

If screen_hours > 5 → Excessive Usage
"""

screen_hours=int(input("Enter the screen hours :")) #4

if screen_hours<2: #4<2 False
    print("Healthy Usage")

elif screen_hours<5: #4<5 True
    print("Moderate Usage") #Moderate usage

else:
    print("Excessive Usage")