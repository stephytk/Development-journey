""""
read rating
display unstatisfied if rating<4.0
display neutral if rating >=4.0 and <4.5
display statisfied if rating >=4.5

"""
rating=float(input("enter rating:"))#5
if rating<4.0: #5<4.0 False
    print("Unstatisfied")
elif rating>=4.0 and rating<4.5:#5<=4.0  and 5<4.5 False
    print("Neutral")
else:
    print("Satisfied")# Satisfied
