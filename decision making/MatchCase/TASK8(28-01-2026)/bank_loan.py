"""
 Bank Loan Eligibility
------------------------------------
Task:
- Ask for monthly income

If income ≥ 25,000:
    - Ask for credit score
    - If credit score ≥ 700:
        "Loan approved"
    - Else:
        "Low credit score"
Else:
    "Income not sufficient"
"""

month_income=int(input("Enter the monthly income :"))

if month_income>=25000:
    credit_score=int(input("Enter the Credit score :"))

    if credit_score>=700:
        print("Loan approved")
    else:
        print("Low Credit score")

else:
    print("Income not sufficient")