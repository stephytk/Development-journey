"""
Sleep Duration Health Check
    Input: hours_of_sleep
    Conditions:
    If sleep < 6 → Sleep Deprived
    If sleep between 6 and 8 → Healthy Sleep
    If sleep > 8 → Oversleeping
"""

hours_of_sleep=int(input("Enter the hours:"))#10
if hours_of_sleep<6:#10<6 false
    print("Sleep Deprived")
elif hours_of_sleep<8:  #10<8 False
    print("Healthy Sleep")
else:
    print("Oversleeping")#Oversleeping