"""
check SIBL score
"""
sibl_score=int(input("Enter the Sibl Score:")) #450

if sibl_score>=300 and sibl_score<550: #450>=300 and 450<550
    print("Poor") #Poor

elif sibl_score>=550 and sibl_score<650:
    print("Average")

elif sibl_score>=650 and sibl_score<750:
    print("Good")
    
else:
    print("Excellent")