"""
Leap year 
"""

i=1800

while(i<=2026):

    if(i%100==0 and i%400==0) or (i%100!=0 and i%4==0):
        print(i,"Leap year")

    i=i+1