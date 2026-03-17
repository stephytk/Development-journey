"""
Write a program to calculate discount eligibility based on purchase amount.
* Above 5000 → 20% discount
* 2000–5000 → 10% discount
* Below 2000 → No discount
"""

p_amnt=int(input("Enter the discount :"))

if p_amnt>5000:

    print("20% of discount")

elif p_amnt>2000 and p_amnt<5000 :

    print("10% of discount")

else:
    print("No discount")

