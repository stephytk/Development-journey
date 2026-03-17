"""
"""

daily_calories={"sun":2300,"mon":1600,"tue":1800,"wed":1500,"thu":1900,"fri":1900,"sat":2000}

for k in daily_calories:

 print(k,daily_calories[k])

#total calories

total_calories=0

for k in daily_calories:
    cal=daily_calories[k]

    total_calories=total_calories+cal

print(total_calories)

#average calories

avg_calories=total_calories/len(daily_calories)
 
print(avg_calories)
